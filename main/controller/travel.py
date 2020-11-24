from flask import request
from flask_restplus import Resource, marshal
from ..util.dto import *
from ..service.travel import *
import json
from ..util.http_status import *

api = TravelDto.api
travel_model=TravelDto.travel
"""
implemented two types of travel endpoints which does the same functionality
    End point '/travel/<s_id>/<l_ic>'
    update  -- update tables according to travel details
    
    End point '/travel'
    update  -- update tables according to travel status
    
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



@api.route('/<s_id>/<l_id>')
class Travel(Resource):
    @api.doc('travel functionality ')
    @api.response(200, 'success')
    @api.response(400, 'Bad request')
    @api.response(404, 'not found')
    def post(self, s_id,l_id):
        """
            interface for spaceship travel.
        """
        response = travel(s_id, l_id)

        return response