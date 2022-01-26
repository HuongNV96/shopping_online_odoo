# -*- coding: utf-8 -*-
import requests

from odoo import http
import logging

_logger = logging.getLogger(__name__)


class ShoppingOnline(http.Controller):
    @http.route('/shopping_online/products/', auth='public')
    def view_products(self, **arg):
        products = http.request.env['products.shopping_online']
        filter = arg.get('search_products')
        if filter is None:
            list_products = products.search([])
        else :
            list_products = products.search([('name','ilike',filter)])
        return http.request.render('shopping_online.view_products', {
            'products': list_products,
        })
