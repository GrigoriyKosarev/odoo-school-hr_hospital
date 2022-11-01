
from odoo import models, fields

class Diagnosis(models.Model):
    _name = 'hr.hos.diagnosis'
    _description = 'Diagnosis description'
    name = fields.Char()