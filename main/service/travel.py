from ..model.model import *
from flask import jsonify, make_response
from ..util.http_status import *

"""
	service.spaceship provides supported functions for controll.spaceship
	travel() -- support post api
	travel_with_payload() -- post api


"""


def travel(spaceship_id, location_id):
    """ Function for spaceships to travel to new location
       		param: spaceship_id, location_id
       		- spaceship_id contains id of spaceship
       		- location_id contains id of location

       		1. check for criterias of data
       		2. update the capacity of locations
       		3. update location of spaceship
       		return: resp
       	"""
    spaceship = Spaceship.query.filter_by(id = spaceship_id).first()
    current_location = Location.query.filter_by(id = spaceship.location).first()
    final_location = Location.query.filter_by(id = location_id).first()

    if spaceship:

        if Status[spaceship.status.name] != Status.OPERATIONAL:
            resp = make_response(jsonify({'error': 'spaceship is not operational '}))
            resp.status_code = BAD_REQUEST
            return resp

        if final_location:

            if final_location == current_location:
                resp = make_response(jsonify({'message': 'spaceship already at destination location'}))
                resp.status_code = SUCCESS
                return resp

            if final_location.availability > 0:

                current_location.availability = current_location.availability + 1
                final_location.availability = final_location.availability - 1
                spaceship.location = location_id
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


def travel_with_payload(data):
    """ Function for spaceships to travel to new location
           		param: data
           		- data contains spaceship name and model , as well as destination name and planet.

           		1. check for criterias of data
           		2. update the capacity of locations
           		3. update location of spaceship
           		return: resp
           	"""

    spaceship = Spaceship.query.filter_by(name = data['name'], model = data['model']).first()

    destination = Location.query.filter_by(city = data['destination_city'], planet = data['destination_planet']).first()

    if spaceship and destination:

        current_location = Location.query.filter_by(id = spaceship.location).first()

        if Status[spaceship.status.name] != Status.OPERATIONAL:
            resp = make_response(jsonify({'error': 'spaceship is not operational '}))
            resp.status_code = BAD_REQUEST
            return resp

        if destination == current_location:
            resp = make_response(jsonify({'message': 'spaceship already at destination location'}))
            resp.status_code = SUCCESS
            return resp

        if destination.availability > 0:

            current_location.availability = current_location.availability + 1
            destination.availability = destination.availability - 1
            spaceship.location = destination.id
            db.session.add(spaceship, current_location)
            db.session.add(destination)
            db.session.commit()
            resp = make_response(jsonify({'message': 'travel is successful'}))
            resp.status_code = SUCCESS
            return resp

        else:

            resp = make_response(jsonify({'error': 'location is at maximum capacity, travel unsuccessful'}))
            resp.status_code = BAD_REQUEST
            return resp

    elif spaceship and not destination:

        resp = make_response(jsonify({'error': 'location not found , check city name and planet name '}))
        resp.status_code = NOT_FOUND
        return resp

    elif not spaceship and destination:

        resp = make_response(jsonify({'error': 'spaceship not found, check name and model of spaceship'}))
        resp.status_code = NOT_FOUND

    elif not spaceship and not destination:

        resp = make_response(jsonify({'error': 'location and spaceship not found '}))
        resp.status_code = NOT_FOUND
