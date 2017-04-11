# -*- coding: utf-8 -*-
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    invoice_line_id = fields.Many2one(
        comodel_name='account.invoice.line', string="Origin line invoice",
    )
    asset_ids = fields.Many2many(
        comodel_name="account.asset.asset", string="Assets",
    )
    equipment_scrap_template_id = fields.Many2one(
        'mail.template',
        string='Equipment Scrap Email Template',
        default=(lambda self:
                 self.env.user.company_id.equipment_scrap_template_id)
    )

    @api.multi
    def action_perform_scrap(self):
        self.ensure_one()
        action = self.env.ref(
            'account_asset_maintenance.wizard_perform_equipment_scrap_action')
        result = action.read()[0]
        return result