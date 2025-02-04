# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Producto(models.Model):
    _name = 'pcs_tienda_animal.producto'
    _description = 'Descripcion'
    
    precio = fields.Float(string="Precio", required=True)
    stock = fields.Integer(string="Stock Disponible", default=0)
    fecha_ingreso = fields.Date(string="Fecha de Ingreso", default=fields.Date.today)
    imagen = fields.Image(string="Imagen del Producto")
    en_oferta = fields.Boolean(string="En Oferta", default=False)
    
    categoria_id = fields.Many2one('pcs_tienda_animal.categoria', string="Categoría")
    cliente_ids = fields.Many2many('pcs_tienda_animal.cliente', string="Clientes que han comprado")
    
    # Un producto pertenece a una categoría, pero una categoría puede tener muchos productos.
    # Cada producto tiene una única categoría.