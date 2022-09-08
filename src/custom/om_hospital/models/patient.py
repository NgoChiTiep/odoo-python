from odoo import fields, models, api
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string="Name", required=True, tracking=True)
    ref = fields.Char(string="Reference", tracking=True)
    age = fields.Integer(string="Age", tracking=True, compute='_compute_age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    date_of_birth = fields.Date(string="Date Of Birth")
    active = fields.Boolean(default=True, string="Trạng thái", tracking=True)

    # note = fields.Text(string='Description')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            print("today", today)
            print("self.date_of_birth", rec.date_of_birth)
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1
