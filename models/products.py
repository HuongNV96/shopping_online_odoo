# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Products(models.Model):
    _name = 'products.shopping_online'
    _description = 'products.shopping_online'

    _sql_constraints = [
        ('barcode_uniq', 'unique(barcode)', 'product id is unique'),
    ]

    name = fields.Char()
    number = fields.Integer()
    remaining = fields.Integer(compute="_init_", store=True)
    sales = fields.Integer(compute="_init_", store=True)
    price = fields.Integer()
    description = fields.Text()
    picture = fields.Image('Picture')
    barcode = fields.Char()

    @api.depends('number')
    def _init_(self):
        for record in self:
            self.sales = 0
            self.remaining = self.number



