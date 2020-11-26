from flask import jsonify, make_response
from ..model.model import *
from ..util.http_status import *

"""
	service.location provides supported functions for controll.location
	add_location() -- support post api
	remove_location() -- support delete api
	view_location() -- support get api 
	view_locations() -- support get api
"""

def add_location(data, id):
    """ Function to add location
    params: data, id
        1.check for vality of data
        2 check if location with same city and planet is already added .
        3.create new location with data
        4.add it to data base
        return:resp
    """
    location = Location.query.filter_by(id = id).first()

    if location:
        resp = make_response(jsonify({'message': 'location with id already exist in database'}))
        resp.status_code = BAD_REQUEST
        return resp
    else:

        duplicate_location = Location.query.filter_by(city = data['city'],planet = data['planet']).first()

        if duplicate_location:
            resp = make_response(jsonify({'message': 'location with city and planet already found in the database'}))
            resp.status_code = BAD_REQUEST
            return resp

        location = Location(**data)
        location.availability=location.capacity
        db.session.add(location)
        db.session.commit()
        resp = make_response(jsonify({'message': 'location added successfully'}))
        resp.status_code = CREATED
        return resp

def remove_location(id):
    """ Function to remove location
        params: id
        1.check criteria and validity
        2.modify database
    """
    location = Location.query.filter_by(id=id).first()

    if location:

        if location.availability==0:

            db.session.delete(location)
            db.session.commit()
            resp = make_response(jsonify({'message': 'location  removed successfully, '}))
            resp.status_code = SUCCESS
            return resp

        else:

            resp = make_response(jsonify({'message': 'location cannot be removed, please move spaceships at location'}))
            resp.status_code = BAD_REQUEST
            return resp

    else:
        resp = make_response(jsonify({'message': 'location with id do not exist in our database'}))
        resp.status_code = NOT_FOUND
        return resp


def view_location(id):
    """ Function to view location
           params: id

           1.return location info

           return:resp
       """
    location = Location.query.filter_by(id = id).first()


    if location:

        """
            This is the functionality to add new wishlist for the logged in user.
        """
        response = {'spaceships': []}
        spaceships = Spaceship.query.filter_by(location = id).all()
        for x in spaceships:
            resp = {}
            resp['id'] = x.id
            resp['name'] = x.name
            resp['model'] = x.model
            resp['status'] = x.status.name
            response['spaceships'].append(resp)

        half = location.__dict__
        del half['_sa_instance_state']
        half2 = response.copy()
        for key, value in half.items():
            half2[key] = value

        return half2
    else:
        resp = make_response(jsonify({'error': 'spaceship with id do not exist in database '}))
        resp.status_code = NOT_FOUND
        return resp

def view_locations():
    """ Function to view all locations
               params: id

               1.return info of all locations

               return:resp
           """
    total_response = {'locations': []}
    locations = Location.query.all()

    for x in locations:

        resp = view_location(x.id)
        total_response['locations'].append(resp)

    return total_response
