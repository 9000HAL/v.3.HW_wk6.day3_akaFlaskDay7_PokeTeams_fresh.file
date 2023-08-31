from flask import Blueprint

pokemon_select = Blueprint('pokemon_select',__name__)

from . import routes

