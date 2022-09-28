# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SalesOrder(models.Model):
    _inherit= 'sale.order' #nombre tecnico para nuestra orden de venta, se ha heredado el modelo de orden de venta  en la aplicacion de ventas
    #crearemso un campo mnay2one para irde desde la plaicacion a academy
    session_id=fields.Many2one(comodel_name='academy.session',
                             string='Related Session',
                             ondelete='set null')
    instructor_id=fields.Many2one(string='Session Instructor',
                                related='session_id.instructor_id')
    student_ids=fields.Many2many(string='Students',
                                related='session_id.student_ids')