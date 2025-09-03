{
    'name': 'Oram Customer Fields On Sales Order',
    'version': '18.0.1.0.0',
    "license": "LGPL-3",
    'depends': ['sale'],
    'author': 'Oram - Abdulrahman Fouad',
    'category': 'Oram',
    'summary': "Edit and update key customer details directly from the Sales Order form.",
    'description': """
Oram Customer Fields on Sales Order
===================================

This module enhances the Sales Order form by allowing users to view and update key customer 
information without leaving the page. All changes are automatically saved back to the 
customer record.

Features:
---------
- Edit customer address fields: Street, Street 2, City, State, Country.
- Edit contact fields: Phone, Mobile, Email.
- Updates are written directly to the linked customer (res.partner).
- Improves efficiency and reduces navigation between forms.
""",
    'data':
        [
            'views/sale_order_view.xml',
        ],
    "installable": True,
    'application': False,
}

