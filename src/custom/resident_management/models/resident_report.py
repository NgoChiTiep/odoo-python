from odoo import models, fields


class ResidentReport(models.Model):
    _name = 'resident.report'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Phản ánh của cư dân'

    name = fields.Char(string='Tiêu đề', required=True, copy=False,)
    content = fields.Html(string='Nội dung',  copy=False,)
    # report_status = fields.Selection([
    #     ('NEW', 'Mới'),
    #     ('PENDING', 'Đăng xử lý'),
    #     ('DONE', 'Hoàn Thành'),
    #     ('CLOSE', 'Đã đóng'),
    # ], required=True, default='NEW', tracking=True, string="Trạng thái",)
    state = fields.Selection([
        ('NEW', 'Mới'),
        ('PENDING', 'Đang xử lý'),
        ('DONE', 'Hoàn Thành'),
        ('CLOSE', 'Đã đóng'),
    ], required=True, default='NEW', tracking=True, string="Trạng thái",)