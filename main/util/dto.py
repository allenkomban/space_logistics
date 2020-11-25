from flask_restplus import Namespace, fields


class SpaceshipDto:
    api = Namespace('spaceship', description = 'spaceship related operations:')

    add_spaceship = api.model('model to add spaceship', {
        'name': fields.String(description = 'name of spaceship', required=True),
        'model': fields.String(description = 'model of spaceship', required=True),
        'city': fields.String(description = 'city to add spaceship', required=True),
        'planet': fields.String(description = 'planet to spaceship', enum = ['EARTH','JUPITER','MARS','NEPTUNE','SATURN','VENUS','MERCURY','URANUS']),
        'status': fields.String(description = 'status of spaceship', enum = ['OPERATIONAL', 'MAINTENANCE','DECOMMISSIONED'])
    })

    view_spaceship = api.model('model to view spaceship',{
        'id' :fields.String(description = 'id of spaceship'),
        'name': fields.String(description = 'name of spaceship'),
        'model': fields.String(description = 'model of spaceship'),
        'city': fields.String(description = 'city of spaceship'),
        'planet': fields.String(description = 'planet of spaceship'),
        'status': fields.String(description = 'status of spaceship')

    })

    view_spaceships = api.model('model to view spaceships', {
        'spaceships': fields.List(fields.Nested(view_spaceship), description='list of spaceship details')
    })

    update_spaceship = api.model('model to update spaceship status', {
        'status': fields.String(description = 'status of spaceship', enum = ['OPERATIONAL', 'MAINTENANCE','DECOMMISSIONED']),
    })


class LocationDto:
    api = Namespace('location', description = 'location related operations:')

    add_location = api.model('model for adding new location', {
        'city': fields.String(description = 'city name'),
        'planet': fields.String(description = 'planet name', enum = ['EARTH','JUPITER','MARS','NEPTUNE','SATURN','VENUS','MERCURY','URANUS']),
        'capacity': fields.Integer(description = 'capacity of location', min=0),
    })

    spaceship_in_location = api.model('model of spaceship in location',{
        'id' :fields.String(description = 'spaceship id'),
        'name': fields.String(description = 'name of spaceship'),
        'model': fields.String(description = 'model of spaceship'),
        'status': fields.String(description = 'spaceship status')
    })

    view_location = api.model('model for viewing a location',{
        'id':fields.Integer(description = 'location id'),
        'city': fields.String(description = 'name of city'),
        'planet': fields.String(description = 'name of planet'),
        'capacity': fields.Integer(description = 'capacity of location'),
        'availability': fields.Integer(description = 'availalibity in location'),
        'spaceships': fields.List(fields.Nested(spaceship_in_location),description = 'list of spaceship in location ')
    })

    view_locations = api.model('model to view locations', {
        'locations': fields.List(fields.Nested(view_location),description = 'list of all locaitons ')
    })


class TravelDto:
    api = Namespace('travel', description = 'travel related operations:')

    travel = api.model('input model for travel functionality', {
        'name': fields.String(description = 'name of spaceship'),
        'model': fields.String(description = 'model of spaceship'),
        'destination_city':fields.String(description = 'city to travel'),
        'destination_planet':fields.String(description = 'planet to travel', enum = ['EARTH','JUPITER','MARS','NEPTUNE','SATURN','VENUS','MERCURY','URANUS'])
    })
