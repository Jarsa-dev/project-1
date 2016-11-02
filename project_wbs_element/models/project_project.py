# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from openerp import fields, models, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    wbs_element_ids = fields.One2many(
        comodel_name='project.wbs_element',
        inverse_name='project_id',
        copy=True)
    nbr_wbs_elements = fields.Integer(
        'Number of WBS Elements',
        compute='_compute_count_wbs_elements')
    label_tasks = fields.Char(
        default='Concepts')
    indirects_account_id = fields.Many2one(
        'account.analytic.account',
        string='Analytic account')

    @api.depends('wbs_element_ids')
    def _compute_count_wbs_elements(self):
        for record in self:
            record.nbr_wbs_elements = len(record.wbs_element_ids)

    @api.model
    def create(self, values):
        project = super(ProjectProject, self).create(values)
        project.indirects_account_id = (
            project.analytic_account_id.create({
                'company_id': self.env.user.company_id.id,
                'name': '[' + project.name + ' / Indirects]',
                'account_type': 'normal'}))
        return project
