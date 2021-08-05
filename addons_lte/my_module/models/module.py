# -*- coding: utf-8 *-*

from odoo import api, fields, models, _


class TestModel(models.Model):
    _name = 'test.model'
    _description = 'Test Model'

    name = fields.Char()
    info = fields.Char()
    calc = fields.Char(compute='_record_size')
    size = fields.Char(compute='_record_size')

    @api.depends('calc', 'size')
    def _record_size(self):
        for record in self:
            record.calc = len(record.name)
            record['size'] = len(record.name)

    # For this to work you need to have fields 'size','calc' declared in
    # class with form: size = fields.Char(compute='_method_name'),
    # calc = fields.Char(compute='_method_name'),

    # def my_module(self):
    #     data = {
    #         'form': self.read()[0]
    #     }
    #     return data

