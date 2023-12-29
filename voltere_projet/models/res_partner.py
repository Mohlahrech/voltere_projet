from odoo import models, fields, api

class resPartnerDob(models.Model):
    _inherit = 'res.partner'
    _description = 'nouveaux champs'

    dob = fields.Date(string='Date de Naissance')
    lieu = fields.Char(string='Lieu de naissance')