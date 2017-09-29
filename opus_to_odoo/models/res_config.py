# -*- coding: utf-8 -*-
# Copyright 2016 Jarsa Sistemas S.A. de C.V.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from openerp import api, fields, models


class ProjectConfigSettings(models.Model):
    _inherit = 'project.config.settings'

    company_id = fields.Many2one(
        comodel_name='res.company',
        default=lambda self: self.env.user.company_id,
        string="Company",)
    opus_server = fields.Char(
        related='company_id.opus_server',
        help="Host of the database server and the server port.",
        string="Opus Server",)
    opus_username = fields.Char(
        related='company_id.opus_username',
        help="Username of the database server.",
        string="Opus Username",)
    opus_password = fields.Char(
        related='company_id.opus_password',
        help="Password of the connection user.",
        string="Opus Password",)