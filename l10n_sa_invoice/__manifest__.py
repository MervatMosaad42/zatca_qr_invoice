# -*- encoding: utf-8 -*-
{
    'name': 'K.S.A - Invoice Community Edition',
    'version': '1.0.0',
    'author': 'Mervat Mosaad',
    'category': 'Accounting/Localizations',
    'description': """
    Invoices for the Kingdom of Saudi Arabia Community Edition
""",
    'depends': ['l10n_sa', 'l10n_gcc_invoice'],
    'data': [
        'views/view_move_form.xml',
        'views/report_invoice.xml',
    ],
}