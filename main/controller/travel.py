from flask import request
from flask_restplus import Resource
from ..util.dto import *
from ..service.travel import *
import json

api = TravelDto.api
travel_model=TravelDto.travel

"""
implemented 2 endpoints to travel, both does the same functionality

    End point '/travel/<spaceship_id>/<location_id>'
    POST Method -- this method executes travel functionality 
    
    End point '/travel'
    POST Method -- this method executes travel functionality with payload
    
    NOTE: both the methods do the same thing.
"""

@api.route('')
class Travel(Resource):
    @api.doc('travel functionality ')
    @api.response(200, 'success')
    @api.expect(travel_model)
    @api.response(400, 'Bad request')
    @api.response(404, 'not found')
    def post(self,):
        """
            interface for spaceship travel.
        """
        data = json.loads(request.get_data())
        response = travel_with_payload(data)

        return response

@api.route('/<spaceship_id>/<location_id>')
class Travel(Resource):
    @api.doc('travel functionality ')
    @api.response(200, 'success')
    @api.response(400, 'Bad request')
    @api.response(404, 'not found')
    def post(self, spaceship_id,location_id):
        """
            interface for spaceship travel.
        """
        response = travel(spaceship_id, location_id)

        return response