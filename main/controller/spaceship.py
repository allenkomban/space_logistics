from flask import request
from flask_restplus import Resource, marshal
from ..util.dto import SpaceshipDto
from ..service.spaceship import *
import json
from ..util.http_status import *

api = SpaceshipDto.api
add_spaceship_model = SpaceshipDto.add_spaceship
view_spaceship_model =  SpaceshipDto.view_spaceship
view_spaceships_model = SpaceshipDto.view_spaceships
update_spaceship_model = SpaceshipDto.update_spaceship

"""
controller to trigger spaceship related operations

    End point '/spaceships'
    GET Method -- this method is to view details of all spaceship
    
    End point '/spaceships/<spaceship_id>'
    POST  -- this triggers methods to add a new spaceship to an existing location
    GET -- this is a method to view details of a spaceship along with its location
    PUT -- this is a method to update the status
    DELETE -- this trigger methods to delete a spaceship   
"""

@api.route('')
class Spaceships(Resource):

    @api.doc('view all spaceships ')
    @api.response(200, 'success', model = view_spaceships_model)
    @api.response(400, 'Bad request')
    def get(self):
        """
                   interface to view details of all spaceships and their current location.
        """
        response = view_all_spaceships()
        return marshal(response, view_spaceships_model), SUCCESS

@api.route('/<int:id>')
@api.doc(params = {'id': 'spaceship id'})
class Spaceship(Resource):

    @api.doc('add a new spaceship ')
    @api.expect(add_spaceship_model, validate = True )
    @api.response(201, 'created')
    @api.response(400, 'Bad request')
    def post(self, id):
        """
            interface to add new spaceship .
        """
        spaceship_data = json.loads(request.get_data())
        response = add_spaceship(spaceship_data, id)

        return response

    @api.doc('view a spaceship ')
    @api.response(200, 'success', model = view_spaceship_model)
    @api.response(404, 'Not found')
    def get(self, id):
        """
                   interface to view details of a spaceship and its current location.
        """
        response = view_spaceship(id)
        if type(response) == dict:
            return marshal(response, view_spaceship_model), SUCCESS
        else:
            return response

    @api.doc('update spaceship status')
    @api.response(200, 'success')
    @api.expect(update_spaceship_model, validate = True)
    @api.response(400, 'Bad request')
    @api.response(404, 'not found')
    def put(self, id):
        """
            interface to update status of spaceship.
        """

        updated_info = json.loads(request.get_data())
        response = update_spaceship(updated_info, id)
        return response

    @api.doc('update spaceship status')
    @api.response(200, 'success')
    @api.response(404, 'not found')
    def delete(self,id):
        """
                    interface to remove a spaceship .
        """

        response = remove_spaceship(id)
        return response

