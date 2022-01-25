# -*- coding: utf-8 -*-
# from odoo import http


# class ZatcaQrInvoice(http.Controller):
#     @http.route('/zatca_qr_invoice/zatca_qr_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zatca_qr_invoice/zatca_qr_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zatca_qr_invoice.listing', {
#             'root': '/zatca_qr_invoice/zatca_qr_invoice',
#             'objects': http.request.env['zatca_qr_invoice.zatca_qr_invoice'].search([]),
#         })

#     @http.route('/zatca_qr_invoice/zatca_qr_invoice/objects/<model("zatca_qr_invoice.zatca_qr_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zatca_qr_invoice.object', {
#             'object': obj
#         })
