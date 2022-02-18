# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class relaciones(models.Model):
#     _name = 'relaciones.relaciones'
#     _description = 'relaciones.relaciones'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

#1
class alumno(models.Model):
	_name = 'relaciones.alumno'
	_description = 'model alumno'

	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)

	#relaciones
	tutor_id=fields.Many2one('relaciones.tutor',string='tutor')
#2
class asignatura(models.Model):
	_name = 'relaciones.asignatura'
	_description = 'model asignatura'

	name = fields.Char('Código',required=True)
	nombre = fields.Char(string='Asignatura',required=True)
	
    # relaciones
	tutor_ids=fields.Many2many('relaciones.tutor',string='Profesor')
	#libro_rel=fields.One2many('relaciones.libro',string='Editorial')
#3
class tutor(models.Model):
	_name = 'relaciones.tutor'
	_description = 'model tutor'

	name = fields.Char('Nombre',required=True)
	dni = fields.Char(string='DNI',required=True)
	
    # relaciones
	alumnos_ids = fields.One2many('relaciones.alumno','tutor_id',string='Alumno tutoria')
	asignatura_ids=fields.Many2many('relaciones.asignatura','tutor_ids',string='Asignatura')
#4
class aula(models.Model):
	_name = 'relaciones.aula'
	_description = 'model aula'

	name = fields.Char('Nombre',required=True)
	aula = fields.Char(string='Nº Aula',required=True)
#5

class colegio(models.Model):
	_name = 'relaciones.colegio'
	_description = 'model colegio'

	name = fields.Char('Nombre',required=True)
	codigo = fields.Char(string='codigo',required=True)
#6
class director(models.Model):
	_name = 'relaciones.director'
	_description = 'model director'

	name = fields.Char('Nombre',required=True)
	tiempo = fields.Char(string='Tiempo',required=True)

#7
class proveedores(models.Model):
	_name = 'relaciones.proveedores'
	_description = 'model proveedores'

	name = fields.Char('Nombre',required=True)
	producto = fields.Char(string='Producto',required=True)
#8
class libro(models.Model):
	_name = 'relaciones.libro'
	_description = 'model libro'

	name = fields.Char('Nombre',required=True)
	editorial = fields.Char(string='Editorial',required=True)

	#asignatura_rel=fields.Many2one('relaciones.asignatura','libro_rel',string='Asignatura')
    #9
class curso(models.Model):
	_name = 'relaciones.curso'
	_description = 'model curso'

	name = fields.Char('Curso',required=True)
	curso = fields.Char(string='Letra',required=True)



