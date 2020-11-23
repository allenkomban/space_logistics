from flask import request
from flask_restplus import Resource, marshal
from ..util.dto import LocationDto
from ..service.location import *
import json
from ..util.http_status import *

api = LocationDto.api
location_model = LocationDto.location

@api.route('/<id>')
class Location(Resource):

	@api.doc('add a new location')
	@api.response(200, 'Success')
	@api.expect(location_model)
	@api.response(400, 'bad request')
	def put(self, id):
		"""
			This is a functionality to add new location to the database
		"""
		data = json.loads(request.get_data())
		response = add_location(data, id)
		return response

	@api.doc('delete a location')
	@api.response(200, 'success')
	@api.response(404, 'bad request')
	def delete(self, id):
		"""
			This is the functionality to to delete a location from the database
		"""
		response = remove_location(id)
		return response

