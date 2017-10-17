from odoo import models, fields, api
from odoo.exceptions import ValidationError

class customer(models.Model):
    _name = 'mp.customer'
    _description = 'Customer'

    # Perform a soft delete
    @api.multi
    def unlink(self):
        for rec in self:
            rec.active = False

            # this function for checking on repeated default or primary rec

    @api.constrains('address_ids')
    def get_default_address(self):
        if self.address_ids:
            default_count = 0
            for rec in self.env['mp.customer_address'].search([('customer_id', '=', self.id)]):
                if rec.default_rec == True:
                    default_count += 1
            if default_count >= 2:
                raise ValidationError('Sorry there is more than one default address in Addresses')

    name = fields.Char(size=60, string="Customer name", index=True)
    mobile_no = fields.Char(size=20, string="Mobile no")
    date_of_birth = fields.Date(string="Date of Birth")
    acct_ids = fields.One2many(comodel_name="mp.customer_acct", inverse_name="customer_id", string="Accounts")
    picture = fields.Binary(string='Picture', help='Attached picture will automatically be re-sized to 128x128px')
    address_ids = fields.One2many(comodel_name="mp.customer_address", inverse_name="customer_id", string="Customer address")
    active = fields.Boolean(string="Active", default="True")

class customer_address(models.Model):
    _name = 'mp.customer_address'
    _description = 'Customer Address'

    customer_id = fields.Many2one(comodel_name="mp.customer", string="Customer", ondelete="cascade", index=True)
    address1 = fields.Char(size=100)
    address2 = fields.Char(size=100)
    address3 = fields.Char(size=100)
    city = fields.Char(size=40)
    postcode = fields.Char(size=20)
    state_id = fields.Many2one(comodel_name="res.country.state", string="State", ondelete="restrict")
    state_name = fields.Char(size=100, string="State name")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", ondelete="restrict")
    province_id = fields.Many2one(comodel_name="mp.province", string="Province", ondelete="restrict")
    cities_municipalities_id = fields.Many2one(comodel_name="mp.cities_municipalities", string="Cities or municipality", ondelete="restrict")
    comments = fields.Text()
    address_type = fields.Selection([
        ('Permanent', 'Permanent'),
        ('Residential', 'Residential'),
        ('Work', 'Work'),
        ('Mailing', 'Mailing'),
        ('Other', 'Other'),
    ], string='Address type', default='Permanent')
    display_address = fields.Char(string='Display address', compute='_get_branch_address', store=True)
    default_rec = fields.Boolean(string="Default Address", default="True")
    active = fields.Boolean(string="Active", default="False")

class customer_acct(models.Model):
    _name = "mp.customer_acct"
    _description = "Customer Account"

    name = fields.Char(size=60, string="Account name")
    account_no = fields.Char(size=20, string="Account number", index=True)
    customer_id = fields.Many2one(comodel_name="mp.customer", string="Customer", ondelete="restrict")