# -*- coding: utf-8 -*-

from odoo import models


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    def _render_qweb_pdf(self, res_ids=None, data=None):
        if self.model == 'account.move':
            invoice_ids = self.env['account.move'].browse(res_ids)
            self = invoice_ids.mapped('partner_id').mapped('axx_invoice_report_id') or self
        return super(IrActionsReport, self)._render_qweb_pdf(res_ids, data)
