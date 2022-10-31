
from odoo import models, fields

class Doctor(models.Model):
    _name = 'hr.hos.doctor'
    _description = 'Doctor description'

    name = fields.Char()
    full_name = fields.Char()

    is_worker = fields.Boolean(
        default=True, )