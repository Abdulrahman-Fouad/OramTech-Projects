from odoo import api, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _search_display_name(self, operator, value):

        domain = ['|', '|', '|', '|', '|', '|',
                  ('complete_name', operator, value),
                  ('email', operator, value), ('ref', operator, value),
                  ('vat', operator, value),
                  ('company_registry', operator, value),
                  ('phone', operator, value),
                  ('mobile', operator, value)]
        return domain
