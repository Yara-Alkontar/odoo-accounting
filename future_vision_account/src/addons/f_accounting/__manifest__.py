{
    'name': 'account_future',
    'version': '16',
    'category': '',
    'depends': [
        'base',
        'account',
    ],
     'data': [
        'security/ir.model.access.csv',
        'views/menuitem.xml',
        'wizard/asset_modify_views.xml',
        'wizard/batch_error_views.xml',
        'report/account_batch_payment_reports.xml',
        'report/account_batch_payment_report_templates.xml',
        'views/batch_payment_views.xml',
        'views/journal.xml',
        'views/asset.xml',
        
     ],


     'installable': True,
     'application': True,
     'auto_install': False,
     'license': 'LGPL-3',
}

