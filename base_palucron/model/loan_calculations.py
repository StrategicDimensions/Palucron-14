# Copyright 2021 Strategic Dimensions <info@strategicdimensions.co.za> 
# License LGPL-3 -

from odoo import api, fields, models
import numpy

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    def calc_function_ipmt(self, rate, insta_num,terms,principal):
        return (0 - numpy.ipmt(rate/12,insta_num,terms,principal))
    
    def calc_function_ppmt(self, rate, insta_num,terms,principal):
        return (0 - numpy.ppmt(rate/12,insta_num,terms,principal))
    
    def calc_function_pmt(self, rate, insta_num,terms,principal):
        return (0 - numpy.pmt(rate/12,terms,principal))
    