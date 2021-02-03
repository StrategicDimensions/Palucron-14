# Copyright 2018 ForgeFlow, S.L. (https://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"


    account_internal_type = fields.Selection(related='account_id.user_type_id.type', store=True,
        string="Internal Type", readonly=True)
