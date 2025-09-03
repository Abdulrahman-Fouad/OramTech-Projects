from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_street = fields.Char(related="partner_id.street", readonly=False)
    partner_street2 = fields.Char(related="partner_id.street2", readonly=False)
    partner_city = fields.Char(related="partner_id.city", readonly=False)
    partner_state_id = fields.Many2one(related="partner_id.state_id", readonly=False)
    partner_country_id = fields.Many2one(related="partner_id.country_id", readonly=False)
    partner_phone = fields.Char(related="partner_id.phone", readonly=False)
    partner_mobile = fields.Char(related="partner_id.mobile", readonly=False)
    partner_email = fields.Char(related="partner_id.email", readonly=False)
