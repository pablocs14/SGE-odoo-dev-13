# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cliente(models.Model):
    _name = 'pcs_tienda_animal.cliente'
    _description = 'cliente'
    
    name  = fields.Char('Nombre', required=True, help="Introduzca el nombre del cliente")
    description = fields.Char('Descripcion')
    fecha_nacimiento = fields.Date('fecha_nacimiento')
    email = fields.Char(string="Correo Electrónico", required=True)
    telefono = fields.Char(string="Teléfono")
    direccion = fields.Text(string="Dirección")
    fecha_registro = fields.Date(string="Fecha de Registro", default=fields.Date.today)
    puntos_fidelidad = fields.Integer(string="Puntos de Fidelidad", default=0)
    es_vip = fields.Boolean(string="Es Cliente VIP", default=False)
    
    producto_ids = fields.Many2many('pcs_tienda_animal.producto', string="Productos comprados")
    
    # Un cliente puede comprar varios productos y un producto puede ser comprado por varios clientes.