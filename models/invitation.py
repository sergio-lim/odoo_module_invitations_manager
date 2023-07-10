from odoo import api, fields, models

class ManagementInvitation(models.Model):
    _name = "management.invitation"
    _description = "Invitation management"

    name = fields.Char(string='Name')
    plus_ones = fields.Integer(string='Plus Ones')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    is_vip = fields.Boolean(string="Is VIP?")
