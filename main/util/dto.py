from flask_restplus import Namespace, fields


class SpaceshipDto:
    api = Namespace('spaceship', description='spaceship related operations:')
    spaceship = api.model('spaceship', {
        'name': fields.String,
        'model': fields.String,
        'city': fields.String,
        'planet': fields.String,
        'status': fields.String
    })

    update_spaceship = api.model('update spaceship status', {
        'status': fields.String,
    })

class LocationDto:
    api = Namespace('location', description='location related operations:')
    location = api.model('location', {
        'city': fields.String,
        'planet': fields.String,
        'capacity': fields.String,
    })


