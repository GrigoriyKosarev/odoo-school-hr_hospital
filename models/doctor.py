from odoo import models, fields

class Patient(models.Model):
    _name = 'hr.hos.doctor'
    _description = 'Doctor description'

    name = fields.Char()
    full_name = fields.Char()

    worker = fields.Boolean(
        default=True, )