# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Producto(models.Model):
    _name = 'pcs_tienda_animal.producto'
    _description = 'Descripcion'
    
    precio = fields.Integer('precio', required=True)
    