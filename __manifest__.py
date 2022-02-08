{
    'name': 'My Sale Module',
    'summary': """ 
       My Sale Module addons
    """,
    'depends': ['sale'],
    'description': 'Sale module',
    'author': 'zakariya',
    'data': [
        'views/my_order_sale_view.xml',
        'views/account_move_form_view.xml',
        'views/stock_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'licence': 'LGPL-3'
}
