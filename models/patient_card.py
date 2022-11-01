
from odoo import models, fields

class PatientCard(models.Model):
    _name = 'hr.hos.patient_card'
    _description = 'Patient card description'

    note = fields.Char()

    diagnosis_ids = fields.Many2many(
        comodel_name='hr.hos.diagnosis', )
