from flask_restplus import Namespace, fields


class SpaceshipDto:
    api = Namespace('spaceship', description='spaceship related operations:')

    add_spaceship = api.model('model to add spaceship', {
        'name': fields.String,
        'model': fields.String,
        'city': fields.String,
        'planet': fields.String,
        'status': fields.String
    })

    view_spaceship = api.model('model to view spaceship',{
        'id' :fields.String,
        'name': fields.String,
        'model': fields.String,
        'city': fields.String,
        'planet': fields.String,
        'status': fields.String

    })

    view_spaceships = api.model('model to view spaceships', {
        'spaceships': fields.List(fields.Nested(view_spaceship))
    })

    update_spaceship = api.model('model to update spaceship status', {
        'status': fields.String,
    })





class LocationDto:
    api = Namespace('location', description='location related operations:')

    add_location = api.model(' model for adding new location', {
        'city': fields.String,
        'planet': fields.String,
        'capacity': fields.Integer,
    })

    spaceship_in_location = api.model('model of spaceship in location',{
        'id' :fields.String,
        'name': fields.String,
        'model': fields.String,
        'status': fields.String
    })

    view_location = api.model('model for viewing a location',{
        'id':fields.Integer,
        'city': fields.String,
        'planet': fields.String,
        'capacity': fields.Integer,
        'availability': fields.Integer,
        'spaceships': fields.List(fields.Nested(spaceship_in_location))
    })

    view_locations = api.model('model to view locations', {
        'locations': fields.List(fields.Nested(view_location))
    })


class TravelDto:
    api = Namespace('travel', description='travel related operations:')

    travel = api.model('input model for travel functionality', {
        'name': fields.String,
        'model': fields.String,
        'destination_city':fields.String,
        'destination_planet':fields.String,
    })
