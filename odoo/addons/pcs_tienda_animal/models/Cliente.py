# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cliente(models.Model):
    _name = 'pcs_tienda_animal.cliente'
    _description = 'cliente'
    
    name  = fields.Char('Nombre', required=True, help="Introduzca el nombre del cliente")
    description = fields.Char('Descripcion')
    fecha_nacimiento = fields.Date('fecha_nacimiento')