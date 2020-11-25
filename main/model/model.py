from .. import db
import enum


class Status(enum.Enum):
    OPERATIONAL = 'operational'
    MAINTENANCE = 'maintenance'
    DECOMMISSIONED = 'decommissioned'

class Planet(enum.Enum):
    EARTH = "Earth"
    JUPITER = 'Jupiter'
    MARS = 'Mars'
    NEPTUNE = 'Neptune'
    SATURN = 'Saturn'
    VENUS = 'Venus'
    MERCURY = 'Mercury'
    URANUS = 'Uranus'

class Spaceship(db.Model):
    __tablename__ = 'spaceship'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    model = db.Column(db.String(100))
    status = db.Column(db.Enum(Status), default=Status.OPERATIONAL, nullable=False)
    location = db.Column(db.Integer, db.ForeignKey('location.id'))

class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(200))
    planet = db.Column(db.String(100))
    capacity = db.Column(db.Integer)
    availability = db.Column(db.Integer)

