# -*- coding: utf-8 -*-
# from odoo import http


# class AsyMrpCustom(http.Controller):
#     @http.route('/asy_mrp_custom/asy_mrp_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asy_mrp_custom/asy_mrp_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asy_mrp_custom.listing', {
#             'root': '/asy_mrp_custom/asy_mrp_custom',
#             'objects': http.request.env['asy_mrp_custom.asy_mrp_custom'].search([]),
#         })

#     @http.route('/asy_mrp_custom/asy_mrp_custom/objects/<model("asy_mrp_custom.asy_mrp_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asy_mrp_custom.object', {
#             'object': obj
#         })
