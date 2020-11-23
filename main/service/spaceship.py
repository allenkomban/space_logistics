from .. import db
from ..model.model import *
from flask import jsonify, make_response
from ..util.http_status import *

"""
	service.spaceship provides supported functions for controll.spaceship
	add_spaceship() -- support create api
	update_spaceship() -- support update api
"""

def add_spaceship(data,id):
    """ Function to add spaceship
    param: spaceship_data,id
            - data is a dictionary containing the details of the spaceship to be added
            - id is the id of the spaceship to be added

            1. checks for validity of data
            2. make a new spaceship with data
            3. add it to database
            return: resp
        """
    spaceship = Spaceship.query.filter_by(id=id).first()

    if spaceship:
        resp=make_response(jsonify({'message': 'spaceship with id already exists in database '}))
        resp.status_code = BAD_REQUEST
        return resp

    location = Location.query.filter_by( city = data['city'] , planet = data['planet'] ).first()
    if not location:
        resp = make_response(jsonify({'message': 'please enter a valid city and planet '}))
        resp.status_code = BAD_REQUEST
        return resp
    if location.availability==0:
        resp = make_response(jsonify({'message': 'this location is at its maximum capacity'}))
        resp.status_code = BAD_REQUEST
        return resp

    try:
        if 'status' in data.keys():
            status = Status[data['status']]
    except KeyError:
        resp = make_response(jsonify({'error': 'Invalid status'}))
        resp.status_code = BAD_REQUEST
        return resp

    location.availability=location.availability-1
    spaceship = Spaceship(id=id, name=data['name'], model=data['model'], location=location.id,status=status)
    db.session.add(spaceship,location)
    db.session.commit()
    resp=make_response(jsonify({'message': 'spaceship added succesfully '}))
    resp.status_code= SUCCESS
    return resp


def update_spaceship(data,id):
    """ Function to update status of spaceship
       		param: updated_info, iD
       		- updated_info contains updated status for
       		- id is the id of spaceship to be updated

       		1. check for validity of data
       		2. lookup the spaceship according to id
       		3. update the status
       		return: resp
       	"""
    spaceship = Spaceship.query.filter_by(id=id).first()

    if spaceship:
        if 'status' in data.keys():
            try:
                spaceship.status = Status[data['status']]
            except KeyError:
                resp = make_response(jsonify({'error': 'Invalid status provided '}))
                resp.status_code = BAD_REQUEST
                return resp

            db.session.add(spaceship)
            db.session.commit()
            resp = make_response(jsonify({'message': 'status of spaceship updated succesfully'}))
            resp.status_code = SUCCESS
            return resp
        else:
            resp = make_response(jsonify({'message': 'please provide status'}))
            resp.status_code = BAD_REQUEST
            return resp
    else:
        resp = make_response(jsonify({'message': 'spaceship with id do not exist in database'}))
        resp.status_code = NOT_FOUND
        return resp

    
    
def remove_spaceship(id):
    spaceship = Spaceship.query.filter_by(id=id).first()
    location = Location.query.filter_by(id=spaceship.location).first()
    if spaceship:
        location.availability=location.availability+1
        db.session.delete(spaceship)
        db.session.add(location)
        db.session.commit()
        resp = make_response(jsonify({'message': 'spaceship removed succesfully '}))
        resp.status_code = SUCCESS
        return resp

    else:
        resp = make_response(jsonify({'error': 'spaceship with id do not exist in database '}))
        resp.status_code = NOT_FOUND
        return resp


    
