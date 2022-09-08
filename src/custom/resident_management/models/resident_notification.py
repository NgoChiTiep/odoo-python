from odoo import models, fields


class ResidentNotification(models.Model):
    _name = 'resident.notification'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Thông báo'

    name = fields.Char(string='Tiêu đề', required=True, copy=False,)
    content = fields.Html(string='Nội dung',  copy=False,)



