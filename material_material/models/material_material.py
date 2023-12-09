# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MaterialMaterial(models.Model):
    _name = 'material.material'
    _description = 'material material'

    material_code = fields.Char('Material Code', copy=False)
    material_name = fields.Char('Material Name')
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Material Type')
    material_buy_price = fields.Integer('Material Buy Price')
    supplier_partner_id = fields.Many2one('res.partner', string='Supplier')

    _sql_constraints = [
        ('unique_material_code', 'unique(material_code)', 'Material code must be unique!')
    ]


    @api.constrains('material_buy_price')
    def action_material(self):
        for x in self:
            if x.material_buy_price < 100:
                raise ValidationError('Buy price cannot be less than 100')