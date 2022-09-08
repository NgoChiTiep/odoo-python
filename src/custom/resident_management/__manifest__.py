{
    'name' : 'GELEXIMCO RESIDENTIAL MANAGEMENT',
    'version' : '1.0.0',
    'category': 'Resident',
    'summary': 'GELEXIMCO RESIDENTIAL MANAGEMENT',
    'description': """GELEXIMCO RESIDENTIAL MANAGEMENT""",
    'depends': ['mail'],
    'sequence': -100,
    'data': [
        'security/resident_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/system_parameter_view.xml',
        'views/notification_view.xml',
        'views/building_view.xml',
        'views/resident_report_view.xml',
    ],
    'application': True,
    'license': 'AGPL-3',
    'assets': {}
}
