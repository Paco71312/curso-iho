# -*- coding: utf-8 -*-

{
    
    'name': 'Odoo Academy',
    'summary': """Academy app to manage trainig""",
    'description': """
        Academy Module to manage Training:
        -Courses
        -Sessions
        -Attendees
    """,

    'author': 'Paco',
    'license': 'LGPL-3',
    'Website': 'https://iho.com.mx/home/',
    'category': 'Training',
    'version': '0.1',
    'depends': ['sale','website'],
    'data':['security/academy_security.xml','security/ir.model.access.csv','views/academy_menuitems.xml','views/course_views.xml','views/session_views.xml','views/sales_views_inherit.xml', 'reports/session_report_templates.xml','views/academy_web_templates.xml',

    ],
    'demo':['demo/academy_demo.xml',

    ],
}