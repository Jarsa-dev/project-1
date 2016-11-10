# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from openerp import api, fields, models


class ProjectProject(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    total_project_expenses = fields.Float(
        'Billing Total', compute='_compute_total_project_expenses')

    @api.multi
    def _compute_total_project_expenses(self):
        for rec in self:
            wbs_elements = self.env['project.wbs_element'].search([
                ('project_id', '=', rec.id)])
            if wbs_elements:
                for wbs_element in wbs_elements:
                    rec.total_project_expenses += (
                        wbs_element.total_concept_expense)
            else:
                rec.total_project_expenses = 0.0