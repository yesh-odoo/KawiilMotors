{
    'name': "K'awiil Motors Motorcycle Registry",
    'summary': """Manage Registration of Motorcycles.""",
    'description': """Motorcycle Registry
    ====================
    This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycle of the brand.
    """,
    'license': 'OPL-1',
    'author': 'yesh-odoo',
    'version': '0.0.1',
    'category':  'Kawaiil/',
    'website': 'www.odoo.com',
    'depends': ['base'],
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'data/motorcycle_registry_data.xml',
        'views/motorcycle_registry_menuitems.xml',
        'views/motorcycle_registry_views.xml',
    ],
    'demo': [
        'demo/motorcycle_registry_demo.xml',
    ],
    'application': True,
}