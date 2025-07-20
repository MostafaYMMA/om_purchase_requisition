# -*- coding: utf-8 -*-

{
    'name': 'Purchase Requisition',
    'version': '1.0.0',
    'category' : 'Purchases',
    'sequence' : 10,
    'summary' : 'Products Managing System',
    'description' : """ Manage purchase requisitions with approval workflows""",
    'author' : "Mostafa Yasser",
    'depends' : ['base' ,'hr','product'],
    'data' : [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/purchase_requisition_views.xml',
        'views/menus.xml',
    ],
    'demo' : [],
    'application' : True,
    'installable' : True,
    'auto_install' : False,
    'license' : 'LGPL-3'
}
