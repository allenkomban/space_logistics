from ..model.model import *
from flask import jsonify, make_response
from ..util.http_status import *

def travel(spaceship_id,location_id):
    """ Function for spaceships to travel to new location
       		param: spaceship_id, location_id
       		- spaceship_id contains id of spaceship
       		- location_id contains id of location

       		1. check for criterias of data
       		2. update the capacity of locations
       		3. update location of spaceship
       		return: resp
       	"""
    spaceship = Spaceship.query.filter_by(id=spaceship_id).first()
    current_location = Location.query.filter_by(id=spaceship.location).first()
    final_location = Location.query.filter_by(id=location_id).first()

    if spaceship:

        if Status[spaceship.status.name]!=Status.OPERATIONAL:
            resp = make_response(jsonify({'error': 'spaceship is not operational '}))
            resp.status_code = BAD_REQUEST
            return resp

        if final_location:

            if final_location==current_location:
                resp = make_response(jsonify({'message': 'travel is successful'}))
                resp.status_code = SUCCESS
                return resp


            if final_location.availability > 0:

                current_location.availability = current_location.availability+1
                final_location.availability = final_location.availability-1
                spaceship.location=location_id
                db.session.add(spaceship, current_location)
                db.session.add(final_location)
                db.session.commit()
                resp = make_response(jsonify({'message': 'travel is successful'}))
                resp.status_code = SUCCESS
                return resp

            else:

                resp = make_response(jsonify({'error': 'location is at maximum capacity, travel unsuccessful'}))
                resp.status_code = BAD_REQUEST
                return resp

        else:

            resp = make_response(jsonify({'error': 'location with id do not exist in database'}))
            resp.status_code = NOT_FOUND
            return resp


    else:
        resp = make_response(jsonify({'message': 'spaceship with id do not exist in database'}))
        resp.status_code = NOT_FOUND
        return resp