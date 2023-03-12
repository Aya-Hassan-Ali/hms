from datetime import date

from odoo import models, fields, api,_
from odoo.fields import Text


class HmsPatient(models.Model):
    _name = "hms.patients"
    fName = fields.Char(required=True)
    lName = fields.Char(required=True)
    birth_date = fields.Date()
    blood_type = fields.Selection([('1', 'A+'), ('2', 'B+')], default='1')
    pcr = fields.Boolean(default=False)
    image = fields.Image()
    address = fields.Char()
    age = fields.Integer(readonly=True, compute='compute_age', store=True)
    history = fields.Html()
    cr_rate = fields.Float(required=True)
    logs = fields.Many2many('hms.logs', string="Patients Logs")
    states = fields.Selection([('1', 'Undetermined'), ('2', 'Good'), ('3', 'Fair'), ('4', 'Serious')], string="Student Level", required=True)
    dep_id = fields.Many2one('hms.departments')
    doctors = fields.Many2many('hms.doctors', string="doctors")
    dep_capacity= fields.Integer(related='dep_id.capacity')
    email=fields.Char(required=True,default="")
    _sql_constraints = [('email',
                         'UNIQUE (email)',
                         'email  already exists'), ]
    @api.onchange('states')
    def log_creation(self):
        if self.states:
            vals = {
                'description': 'states Changed to %s ' % (self.states),
                'created_by': self.fName,
            }
            log = self.env['hms.logs'].create(vals)
            self.logs += log
    @api.depends('birth_date')
    def compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                            (today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
            else:
                rec.age = 0