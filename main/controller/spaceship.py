from flask import request
from flask_restplus import Resource, marshal
from ..util.dto import SpaceshipDto
from ..service.spaceship import *
import json
from ..util.http_status import *

api = SpaceshipDto.api
spaceship_model = SpaceshipDto.spaceship
update_spaceship_model=SpaceshipDto.update_spaceship

"""
    spaceship api
    add   -- add a new spaceship to the database
    update  -- update a spaceship status
"""


@api.route('/<id>')
class Spaceship(Resource):
    @api.doc('add a new spaceship ')
    @api.response(200, 'success')
    @api.expect(spaceship_model)
    @api.response(400, 'Bad request')
    def post(self, id):
        """
            interface to add spaceship to the database.
        """
        spaceship_data = json.loads(request.get_data())
        response = add_spaceship(spaceship_data, id)

        return response


    @api.doc('update spaceship status')
    @api.response(200, 'success')
    @api.expect(update_spaceship_model)
    @api.response(400, 'Bad request')
    def put(self, id):
        """
            interface to modify/update the spaceship status.
        """

        updated_info = json.loads(request.get_data())
        response = update_spaceship(updated_info, id)
        return response


