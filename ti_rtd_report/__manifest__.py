# -*-coding: utf-8 -*-
{
    'name': "RTD Report (Annual Return of Trading Details)",
    'summary': "Generate and manage RTD Reports for Irish VAT compliance easily",
    'description': """
RTD Report Module for Irish Businesses
====================================

This module helps Irish businesses generate and manage their Annual Return of Trading Details (RTD) reports efficiently.

Key Features:
------------
* Automated RTD report generation
* Proper VAT classification for Irish tax reporting
* Detailed breakdown of supplies and deductions
* Export options for Revenue submission
* Historical report access and management

Perfect for:
-----------
* Irish registered businesses
* Accountants and tax professionals
* Companies dealing with Irish VAT compliance
    """,
    'author': "Target Integration",
    'website': "https://www.targetintegration.com",
    'version': "18.0.0.0",
    'category': 'Accounting/Accounting',
    'license': "Other proprietary",
    
    # App store specific
    'price': '250.00',
    'currency': 'EUR',
    'maintainer': 'Target Integration',
    'images': ['static/description/banner.png',],
    
    # Dependencies
    'depends': ["account_accountant", "account_asset"],
    
    # Data files
    'data': [
        "data/tax_data.xml",
        "data/rtd_data.xml",
        "data/vat_return.xml",
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
    'uninstall_hook': 'uninstall_hook',
    'post_init_hook': 'assign_tags_to_custom_taxes',

}