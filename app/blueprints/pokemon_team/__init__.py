from flask import Blueprint

pokemon_team = Blueprint('pokemon_team', __name__)

from . import routes