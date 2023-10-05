from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(
        selection_add=[('motorcycle', 'Motorcycle')],
        ondelete={'motorcycle': 'set product'}
    )

    location_id = fields.Many2one(
        'stock.location',
        string='Default Location',
        domain="[('usage', '=', 'internal')]",
        help="The default location for motorcycle products."
    )

    horsepower = fields.Float(string='Horsepower')
    top_speed = fields.Float(string='Top Speed')
    torque = fields.Float(string='Torque')
    battery_capacity = fields.Selection(
        [('xs', 'Small'), ('0m', 'Medium'), ('0l', 'Long'), ('xl', 'Extra Large')],
        string='Battery Capacity'
    )
    charge_time = fields.Float(string='Charge Time')
    range = fields.Float(string='Range')
    curb_weight = fields.Float(string='Weight')
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
    year = fields.Char(string='Year')