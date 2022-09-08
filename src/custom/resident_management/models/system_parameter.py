from odoo import models, fields


class SystemParameter(models.Model):
    _name = 'resident.system.parameter'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Tham số hệ thống'

    name = fields.Char(string='Tên', required=True, copy=False,)
    description = fields.Char(string='Mô tả',  copy=False,)
    p_value = fields.Char(string='Giá trị', copy=False,)
    p_status = fields.Selection([
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ], required=True, default='ACTIVE', tracking=True, string="Trạng thái")



