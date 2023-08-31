from flask import Blueprint

pokemon_release = Blueprint('pokemon_release', __name__)

from . import routes