from flask import request
from flask_restplus import Resource, marshal
from ..util.dto import LocationDto
from ..service.location import *
import json
from ..util.http_status import *

api = LocationDto.api
add_location_model = LocationDto.add_location
view_location_model= LocationDto.view_location
view_locations_model=LocationDto.view_locations


@api.route('')
class Locations(Resource):
	@api.doc('view all locations ')
	@api.response(200, 'success', model=view_locations_model)
	@api.response(400, 'Bad request')
	def get(self):
		"""
            interface to view all location details.
        """
		response = view_locations()

		return marshal(response, view_locations_model), SUCCESS



@api.route('/<int:id>')
class Location(Resource):

	@api.doc('view a location ')
	@api.response(200, 'success', model=view_location_model)
	@api.param('id', description='location id')
	@api.response(400, 'Bad request')
	def get(self, id):
		"""
            interface to view location details, given id.
        """
		response = view_location(id)
		if type(response) == dict:
			return marshal(response, view_location_model), SUCCESS
		else:
			return response

	@api.doc('add a new location')
	@api.response(200, 'Success')
	@api.expect(add_location_model)
	@api.param('id', description='location id')
	@api.response(400, 'bad request')
	def post(self, id):
		"""
			interface to add new location
		"""
		data = json.loads(request.get_data())
		response = add_location(data, id)
		return response

	@api.doc('delete a location')
	@api.response(200, 'success')
	@api.param('id', description='location id')
	@api.response(404, 'bad request')
	def delete(self, id):
		"""
			interface to delete a location
		"""
		response = remove_location(id)
		return response

