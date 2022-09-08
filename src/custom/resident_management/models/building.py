from odoo import models, fields


class Building(models.Model):
    _name = 'resident.building'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Chung cư/Toà nhà'

    name = fields.Char(string='Tên toà nhà', required=True, copy=False,)
    address = fields.Char(string='Địa chỉ',  copy=False,)
    floor = fields.Char(string='Số tầng', copy=False,)




