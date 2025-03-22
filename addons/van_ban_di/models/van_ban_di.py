from odoo import models, fields


class ChucVu(models.Model):
    _name = 'van_ban_di'
    _description = 'Bảng chứa thông tin văn bản điđi'
    _rec_name = "ten_van_ban_di"  # Tên hiển thị đại diện

    ma_van_ban_di = fields.Char("Mã van_ban_di", required=True)
    ten_van_ban_di = fields.Char("Tên van_ban_di", required=True)