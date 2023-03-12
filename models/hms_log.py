from odoo import models, fields, api
from datetime import datetime


class HMSLogs(models.Model):
    _name = 'hms.logs'
    created_by = fields.Char(string='patients')
    description = fields.Text('Description')
    date = fields.Date('Date',default=datetime.today())

