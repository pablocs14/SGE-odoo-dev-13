# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'pcs_tienda_animal.Categoria'
    _description = 'Categoria'
    
    name = fields.Char('Nombre', required=True, help="Introduzca el nombre de la categoria")
    description = fields.Char('Descripcion')
    
    