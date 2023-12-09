# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class material_material(models.Model):
#     _name = 'material_material.material_material'
#     _description = 'material_material.material_material'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
