from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _clean_phone_number(self, phone):
        if not phone:
            return phone
        cleaned = re.sub(r'[^\d+]', '', phone)
        return '+' + cleaned.replace('+', '') if '+' in cleaned else cleaned

    def _extract_phone_without_country_code(self, phone):
        if not phone or not phone.startswith('+'):
            return phone

        digits_only = phone[1:]
        codes = sorted(
            [str(c.phone_code) for c in self.env['res.country'].search([('phone_code', '!=', False)]) if c.phone_code],
            key=len, reverse=True)

        for code in codes:
            if digits_only.startswith(code):
                return digits_only[len(code):]
        return digits_only

    def _format_phone_number(self, phone, country_code=None, force_reformat=False):
        if not phone:
            return phone

        cleaned_phone = self._clean_phone_number(phone)
        if not cleaned_phone:
            return phone

        # Handle existing international numbers
        if cleaned_phone.startswith('+'):
            if not force_reformat:
                if len(re.sub(r'\D', '', cleaned_phone)) < 7:
                    raise ValidationError(f"Invalid phone number format: {phone}")
                return cleaned_phone
            cleaned_phone = self._extract_phone_without_country_code(cleaned_phone)

        # Get country code and format
        country_code = country_code or (self.country_id.phone_code if self.country_id else None) or '20'
        formatted_phone = f"+{country_code}{cleaned_phone.lstrip('0')}"

        if len(re.sub(r'\D', '', formatted_phone)) < 7:
            raise ValidationError(f"Phone number too short: {phone}")

        return formatted_phone

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'phone' in vals:
                vals['phone'] = self._format_phone_number(vals['phone'])
            if 'mobile' in vals:
                vals['mobile'] = self._format_phone_number(vals['mobile'])
        return super().create(vals_list)

    def write(self, vals):
        if 'phone' in vals:
            vals['phone'] = self._format_phone_number(vals['phone'])
        if 'mobile' in vals:
            vals['mobile'] = self._format_phone_number(vals['mobile'])
        return super().write(vals)

    @api.onchange('phone')
    def _onchange_phone(self):
        if self.phone:
            self.phone = self._format_phone_number(self.phone)

    @api.onchange('mobile')
    def _onchange_mobile(self):
        if self.mobile:
            self.mobile = self._format_phone_number(self.mobile)

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            if self.phone:
                self.phone = self._format_phone_number(self.phone, force_reformat=True)
            if self.mobile:
                self.mobile = self._format_phone_number(self.mobile, force_reformat=True)
