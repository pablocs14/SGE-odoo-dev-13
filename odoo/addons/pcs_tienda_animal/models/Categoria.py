# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'pcs_tienda_animal.categoria'
    _description = 'Categoria'
    
    name = fields.Char('Nombre', required=True, help="Introduzca el nombre de la categoria")
    description = fields.Char('Descripcion')
    codigo = fields.Char(string="Código", help="Código único de la categoría")
    fecha_creacion = fields.Date(string="Fecha de Creación", default=fields.Date.today)
    activo = fields.Boolean(string="Activo", default=True)
    
    producto_ids = fields.One2many('pcs_tienda_animal.producto', 'categoria_id', string="Productos")