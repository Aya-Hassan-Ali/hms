from odoo import models, fields


class HmsDepartment(models.Model):
    _name = "hms.departments"
    name = fields.Char(required=True)
    is_opened = fields.Boolean(default=False)
    capacity = fields.Integer(required=True,default=0)
    patients = fields.One2many(comodel_name="hms.patients", inverse_name="dep_id")
