from odoo import models, fields

class Patient(models.Model):
    _name = 'hr.hos.patient'
    _description = 'Patient'

    name = fields.Char()
    full_name = fields.Char()
    # sex = fields.
    birthday = fields.Date()
    years = fields.Integer()

    active = fields.Boolean(
        default=True, )

    patient_card_ids = fields.Many2many(comodel_name='hr.hos.patient_card', )