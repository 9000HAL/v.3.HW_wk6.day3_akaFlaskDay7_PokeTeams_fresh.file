from flask import Blueprint

auth = Blueprint('auth', __name__)

#from app.blueprints.auth import routes        #---cp commented out

from . import routes