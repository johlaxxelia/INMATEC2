# -*- coding: utf-8 -*-
{
    'name': 'INMATEC Account Module',

    'summary': 'This module contains the customised accounting features',
    'description': """
INMATEC Account Module
====================
This module contains the customised accounting features
    """,

    'category': 'Customer Add-On',
    'version': '15.0.0.1',
    'author': 'axxelia GmbH',
    'license': 'LGPL-3',
    'website': 'http://www.axxelia.com',

    'depends': [
        'base', 'account'
    ],

    'data': [
        # Data

        # Security
        # Views
        'views/res_partner_view.xml',


        # Menus
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',

}