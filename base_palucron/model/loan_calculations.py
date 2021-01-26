# Copyright 2021 Strategic Dimensions <info@strategicdimensions.co.za> 
# License LGPL-3 -

from odoo import api, fields, models


class CRM(models.Model):
    _inherit = 'crm.lead'

    def some_function(self, rate, insta_num,terms,principle):
        return (0 - numpy.ipmt(rate/12,insta_num,terms,principle))
    
    def some_function_ppmt(self, rate, insta_num,terms,principle):
        return (0 - numpy.ppmt(rate/12,insta_num,terms,principle))
    


    