from odoo import models, fields, api

class customer(models.Model):
    _name = 'mp.customer'
    _description = 'Customer'

    # Perform a soft delete
    @api.multi
    def unlink(self):
        for rec in self:
            rec.active = False

    name = fields.Char(size=60, string="Customer name", index=True)
    mobile_no = fields.Char(size=20, string="Mobile no")
    date_of_birth = fields.Date(string="Date of Birth")
    active = fields.Boolean(string="Active", default="True")

class customer_address(models.Model):
    _name = 'mp.customer_address'
    _description = 'Customer Address'

    customer_id = fields.Many2one(comodel_name="mp.customer", string="Customer", ondelete="cascade", index=True)
    address1 = fields.Char(size=100)
    city = fields.Char(size=40)
    postcode = fields.Char(size=20)
