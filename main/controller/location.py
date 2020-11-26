from flask import request
from flask_restplus import Resource, marshal
from ..util.dto import LocationDto
from ..service.location import *
import json
from ..util.http_status import *

api = LocationDto.api
add_location_model = LocationDto.add_location
view_location_model = LocationDto.view_location
view_locations_model = LocationDto.view_locations

"""
controller to trigger location related operations

    End point '/locations'
    GET Method -- this method executes a methods to view details of all locations along with spaceships stationed at those locations.

    End point '/locations/<location_id>'
    POST  -- this triggers method to add a new location .
    GET -- this is a method to view information of location along with information of spaceships stationed at that location.
    DELETE -- this trigger methods to remove a location
"""

@api.route('')
class Locations(Resource):
    @api.doc('view all locations ')
    @api.response(200, 'success', model=view_locations_model)
    @api.response(400, 'Bad request')
    def get(self):
        """
            interface to view details of all locations and spaceships at those locations.
        """
        response = view_locations()
        return marshal(response, view_locations_model), SUCCESS


@api.route('/<int:id>')
@api.doc(params={'id': 'location id'})
class Location(Resource):

    @api.doc('view a location ')
    @api.response(200, 'success', model=view_location_model)
    @api.response(400, 'Bad request')
    def get(self, id):
        """
            interface to view details of a location and the spaceships stationed at the location.
        """
        response = view_location(id)
        if type(response) == dict:
            return marshal(response, view_location_model), SUCCESS
        else:
            return response

    @api.doc('add a new location')
    @api.response(201, 'Created')
    @api.expect(add_location_model, validate=True)
    @api.response(400, 'bad request')
    def post(self, id):
        """
			interface to add new location.
		"""

        data = json.loads(request.get_data())
        response = add_location(data, id)
        return response

    @api.doc('delete a location')
    @api.response(200, 'success')
    @api.response(400, 'bad request')
    @api.response(404, 'not found')
    def delete(self, id):
        """
			interface to remove a location.
		"""
        response = remove_location(id)
        return response
