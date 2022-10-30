
from odoo import models, fields

class Patient(models.Model):
    _name = 'hr.hos.patient'
    _description = 'Patient description'

    name = fields.Char()
    full_name = fields.Char()

    active = fields.Boolean(
        default=True, )