# -*- coding: utf-8 -*-
{
    'name': "TestModule",

    'summary': """
        123 Practice Odoo Module Developing""",

    'description': """
        Practice Odoo Module Developing ... New description ...
    """,

    'author': "Isis Jimenez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/test_module.xml',
        'views/partner.xml',
        'views/session_workflow.xml',
        'views/session_board.xml',
        'views/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    #'installable': True,
    #'application': True,
    #'auto_install': False,
}