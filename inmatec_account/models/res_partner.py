from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    axx_invoice_report_id = fields.Many2one('ir.actions.report', string="Invoice Layout")


