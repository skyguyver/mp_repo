from openerp import models, fields

class customer(models.Model):
    _name = 'mp.customer'
    _description = 'Customer'

    name = fields.Char(size=60, string="Customer name", index=True)
    mobile_no = fields.Char(size=20, string="Mobile no")