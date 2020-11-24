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
    spaceship api
    add   -- add a new spaceship to the database
    update  -- update a spaceship status
    remove -- removing a spaceship 
"""

@api.route('')
class Spaceships(Resource):

    @api.doc('view all spaceships ')
    @api.response(200, 'success', model=view_spaceships_model)
    @api.response(400, 'Bad request')
    def get(self):
        """
                   interface to view spaceship details.
        """
        response = view_all_spaceships()
        return marshal(response, view_spaceships_model), SUCCESS



@api.route('<int:id>')
class Spaceship(Resource):

    @api.doc('add a new spaceship ')
    @api.param('id', description='spaceship id')
    @api.expect(add_spaceship_model)
    @api.response(200, 'success')
    @api.response(400, 'Bad request')
    def post(self, id):
        """
            interface to add spaceship .
        """
        spaceship_data = json.loads(request.get_data())
        response = add_spaceship(spaceship_data, id)

        return response

    @api.doc('view a spaceship ')
    @api.response(200, 'success', model=view_spaceship_model)
    @api.param('id', description='spaceship id')
    @api.response(400, 'Bad request')
    def get(self, id):
        """
                   interface to view spaceship details.
        """
        response = view_spaceship(id)
        if type(response) == dict:
            return marshal(response, view_spaceship_model), SUCCESS
        else:
            return response


    @api.doc('update spaceship status')
    @api.response(200, 'success')
    @api.expect(update_spaceship_model)
    @api.param('id', description='spaceship id')

    @api.response(400, 'Bad request')
    @api.response(404, 'not found')
    def put(self, id):
        """
            interface to update the spaceship status.
        """

        updated_info = json.loads(request.get_data())
        response = update_spaceship(updated_info, id)
        return response

    @api.doc('update spaceship status')
    @api.response(200, 'success')
    @api.param('id', description='spaceship id')
    @api.response(404, 'not found')
    def delete(self,id):
        """
                    interface to remove a spaceship .
        """

        response = remove_spaceship(id)
        return response

