# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class asy_mrp_custom(models.Model):
#     _name = 'asy_mrp_custom.asy_mrp_custom'
#     _description = 'asy_mrp_custom.asy_mrp_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
