# -*- coding: utf-8 -*-
# from odoo import http


# class VoltereProjet(http.Controller):
#     @http.route('/voltere_projet/voltere_projet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/voltere_projet/voltere_projet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('voltere_projet.listing', {
#             'root': '/voltere_projet/voltere_projet',
#             'objects': http.request.env['voltere_projet.voltere_projet'].search([]),
#         })

#     @http.route('/voltere_projet/voltere_projet/objects/<model("voltere_projet.voltere_projet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('voltere_projet.object', {
#             'object': obj
#         })
