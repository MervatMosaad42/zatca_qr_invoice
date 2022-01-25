import base64

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import datetime



class InheritAccountMove(models.Model):
    _inherit = 'account.move'

    l10n_sa_qr_code_str = fields.Char(string='Zatka QR Code', compute='_compute_qr_code_str')

    @api.depends('amount_total', 'amount_untaxed', 'invoice_date', 'company_id', 'company_id.vat')
    def _compute_qr_code_str(self):
        print('calling compute qr code method')
        """ Generate the qr code for Saudi e-invoicing. Specs are available at the following link at page 23
        https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20210528_ZATCA_Electronic_Invoice_Security_Features_Implementation_Standards_vShared.pdf
        """

        def get_qr_encoding(tag, field):
            company_name_byte_array = field.encode('UTF-8')
            company_name_tag_encoding = tag.to_bytes(length=1, byteorder='big')
            company_name_length_encoding = len(company_name_byte_array).to_bytes(length=1, byteorder='big')
            return company_name_tag_encoding + company_name_length_encoding + company_name_byte_array

        for record in self:
            time_sa = ''
            qr_code_str = ''
            if record.company_id.vat:
                seller_name_enc = get_qr_encoding(1, record.company_id.display_name)
                company_vat_enc = get_qr_encoding(2, record.company_id.vat)
                if record.l10n_sa_confirmation_datetime:
                    time_sa = fields.Datetime.context_timestamp(self.with_context(tz='Asia/Riyadh'),
                                                            record.l10n_sa_confirmation_datetime)
                elif record.l10n_sa_delivery_date:
                    print('l10n_sa_delivery_date')
                    time_sa = record.l10n_sa_delivery_date
                timestamp_enc = get_qr_encoding(3, time_sa.isoformat())
                invoice_total_enc = get_qr_encoding(4, str(record.amount_total))
                total_vat_enc = get_qr_encoding(5, str(record.currency_id.round(
                    record.amount_total - record.amount_untaxed)))

                str_to_encode = seller_name_enc + company_vat_enc + timestamp_enc + invoice_total_enc + total_vat_enc
                qr_code_str = base64.b64encode(str_to_encode).decode('UTF-8')
            record.l10n_sa_qr_code_str = qr_code_str
