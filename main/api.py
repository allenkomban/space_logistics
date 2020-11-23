from flask_restplus import Api
from flask import Blueprint
from .controller.location import api as location


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Stomble spaceships Restplus API',
          version='1.0',
          description='This api is a system to manage the logistics of Stomble’s fleet of spaceships'
                      '\r\n\r\n\r\n'
                      'By Allen Kombasseril',

          )


api.add_namespace(location, path='/location')