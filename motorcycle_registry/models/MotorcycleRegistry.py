from odoo import api, models, fields
import re
from odoo.exceptions import UserError, ValidationError


class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = 'registry_number'


    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    license_plate = fields.Char(string="License Plate")
    date_registry = fields.Date(string="Registry Date")
    vin = fields.Char(string="Vehical Identity Number", )
    current_mileage = fields.Float(string="Current Milage")
    certificate_title = fields.Binary(attachment=True)
    vehicle_image = fields.Image("Vehicle Image", max_width=1920, max_height=1920)
    registry_number = fields.Char(string="Registry Number", required=True, default="MRN0001", copy=False, readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('registry_number', ('MRN0001')) == ('MRN0001'):
            vals['registry_number'] = self.env['ir.sequence'].next_by_code('motorcycle_registry.registry_number')
        return super().create(vals)

    @api.constrains('vin')
    def _check_vin(self):
        for record in self:
            if record.vin and not re.match(r'^[A-Z]{2}[A-Z0-9]{2}\d{2}[A-Z0-9]{2}\d{5}$', record.vin):
                raise ValidationError("Invalid VIN number format. Please use the format specified.")
    
    @api.constrains('license_plate')
    def _check_license_plate_pattern(self):
        for record in self:
            if record.license_plate:
                pattern = r'^[A-Z]{4}\d{3}(?:[A-Z]{2})?$'
                
                if not re.match(pattern, record.license_plate):
                    raise ValidationError("Invalid license plate format. Please use the specified pattern: 4 capital letters, 3 digits, optional 2 capital letters.")
    
    @api.constrains('vin')
    def _check_unique_vin_number(self):
        for record in self:
            if record.vin:
                existing_records = self.env['motorcycle.registry'].search([('vin', '=', record.vin)])
                if len(existing_records) > 1:
                    raise ValidationError("A Motorcycle Registry with the same VIN already exists. Each VIN must be unique.")