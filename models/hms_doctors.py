from odoo import models,fields


class HmsDoctors(models.Model):
    _name = "hms.doctors"
    patients = fields.One2many(comodel_name="hms.patients", inverse_name="doctors")
    fName = fields.Char(required=True)
    lName = fields.Char(required=True)
    image = fields.Image()

