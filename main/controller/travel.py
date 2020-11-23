from flask import request
from flask_restplus import Resource, marshal
from ..util.dto import TravelDto
from ..service.travel import *
import json
from ..util.http_status import *

api = TravelDto.api

"""
    travel api
    update  -- update a travel status
"""


@api.route('/<s_id>/<l_id>')
class Travel(Resource):
    @api.doc('travel functionality ')
    @api.response(200, 'success')
    @api.response(400, 'Bad request')
    @api.response(404, 'not found')
    def post(self, s_id,l_id):
        """
            interface to add spaceship to the database.
        """
        response = travel(s_id, l_id)

        return response