{
    'name': 'Oram Purchase Vendor Creation Control',
    'version': '18.0.1.0.0',
    "license": "LGPL-3",
    'depends': ['purchase'],
    'author': 'Oram - Abdulrahman Fouad',
    'category': 'Oram',
    'summary': "Control Vendor Creation in Purchase module.",
    'description': "Prevent Creation or edit of vendor from Purchase module.",
    'data':
        [
            'views/purchase_order_view.xml'
        ],
    "installable": True,
    'application': False,
}

