# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class Purchase(models.Model):
    _inherit = ['purchase.order']
    
    end_user_retails = fields.Char()
    delivery_location = fields.Char()
