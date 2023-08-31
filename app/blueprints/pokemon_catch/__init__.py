from flask import Blueprint

pokemon_catch = Blueprint('pokemon_catch', __name__)

from . import routes