from flask import jsonify, make_response
from ..model.model import *
from ..util.http_status import *


def add_location(data, id):
    """
    params: data, id
    adds a location with the data provided
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
        resp = make_response(jsonify({'message': 'location added succesfully'}))
        resp.status_code = SUCCESS
        return resp


def remove_location(id):
    """
        params: id
        this is the functionality to delete a location from the database
    """
    location = Location.query.filter_by(id=id).first()

    if location:

        db.session.delete(location)
        db.session.commit()
        resp = make_response(jsonify({'message': 'location  deleted succesfully'}))
        resp.status_code = SUCCESS
        return resp

    else:
        resp = make_response(jsonify({'message': 'location with id do not exist in our database'}))
        resp.status_code = NOT_FOUND
        return resp
