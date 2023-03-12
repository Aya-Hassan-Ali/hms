# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'hms',
    'version' : '1.0',
    'author':'aya',
    'data': [
        'security/hms_groups.xml',
        'security/ir.model.access.csv',

        'views/hms_patients_views.xml',
        'views/hms_departments_views.xml',
        'views/hms_doctors.xml',
        'reports/hms_patient_template.xml',
        'reports/reports.xml',

    ],
    'installable': True,
    'application': False,
}
