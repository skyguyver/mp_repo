from openerp import models, fields

class mp_common_code(models.Model):
    _name = 'mp.common_code'
    _description = 'common code table'

    name = fields.Char()
    code = fields.Char()
    code_type = fields.Char()