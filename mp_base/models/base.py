from odoo import models, fields

class common_code(models.Model):
    _name = 'mp.common_code'
    _description = 'common code table'

    name = fields.Char()
    code = fields.Char()
    code_type = fields.Char()

class cities_municipalities(models.Model):
    _name = 'mp.cities_municipalities'
    _description = 'Country cities and municipalities'

    name = fields.Char(size=60, string="City or municipality")
    class_type = fields.Selection([
        ('Municipality','Municipality'),
        ('CC','Component cities'),
        ('HUC','Highly urbanized cities'),
        ('ICC','Independent Component cities')
    ],string="Class")
    psgc_no = fields.Char(size=20, string="PSGC no")
    province_id = fields.Many2one(comodel_name="mp.province", string="Province", ondelete="restrict")

class province(models.Model):
    _name = 'mp.province'
    _description = 'Country provinces'

    iso = fields.Char(size=20, string="ISO")
    name = fields.Char(size=60, string="Province")
    division_type = fields.Selection([
        ('Luzon','Luzon'),
        ('Visayas','Visayas'),
        ('Mindanao','Mindanao')
    ],string="Division")
    country_id = fields.Many2one(comodel_name="res.country", string="Country")
    cities_municipalities_ids = fields.One2many(comodel_name="mp.cities_municipalities", inverse_name="province_id", string="City or municipality")


