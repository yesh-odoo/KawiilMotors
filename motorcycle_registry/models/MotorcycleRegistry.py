from odoo import models, fields

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = 'registry_number'


    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    license_plate = fields.Char(string="License Plate")
    date_registry = fields.Date(string="Registry Date")
    vin = fields.Char(string="Vehical Identity Number")
    current_mileage = fields.Float(string="Current Milage")
    certificate_title = fields.Binary(attachment=True)
    vehicle_image = fields.Image("Vehicle Image", max_width=1920, max_height=1920)
    registry_number = fields.Char(string="Registry Number", required=True)