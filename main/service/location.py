from flask import jsonify, make_response
from ..model.model import *
from ..util.http_status import *

"""
	service.location provides supported functions for controll.location
	add_location() -- support create api
	remove_location() -- support delete api
"""

def add_location(data, id):
    """ Function to add location
    params: data, id
        1.check for vality of data
        2.create new location with data
        3.add it to data base
        return:resp
    """
    location = Location.query.filter_by(id=id).first()

    if location:
        resp = make_response(jsonify({'message': 'location with id already exist in database'}))
        resp.status_code = BAD_REQUEST
        return resp
    else:
        location=Location(id=id, city=data['city'], planet=data['planet'], capacity=data['capacity'], availability=data['capacity'] )
        db.session.add(location)
        db.session.commit()
        resp = make_response(jsonify({'message': 'location added successfully'}))
        resp.status_code = SUCCESS
        return resp


def remove_location(id):
    """ Function to remove location
        params: id
        1.check criteria and validity
        2.modify database


    """
    location = Location.query.filter_by(id=id).first()

    if location:

        if location.availability!=location.capacity:
            resp = make_response(jsonify({'message': 'This location cannot be deleted as their are spaceships in the location, you will have to move the spaceships to another location'}))
            resp.status_code = BAD_REQUEST
            return resp


        db.session.delete(location)
        db.session.commit()
        resp = make_response(jsonify({'message': 'location  deleted successfully '}))
        resp.status_code = SUCCESS
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
    location = Location.query.filter_by(id=id).first()
    print('location',location)

    response = {'spaceships':[]}

    if location:

        """
            This is the functionality to add new wishlist for the logged in user.
        """
        spaceships = Spaceship.query.filter_by(location=id).all()
        print(spaceships)

        for x in spaceships:
            print ('x',x)
            resp={}
            resp['id']= x.id
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
    total_response={'locations':[]}
    locations = Location.query.all()

    for x in locations:
        print('id',x.id)
        resp = view_location(x.id)
        total_response['locations'].append(resp)

    return total_response