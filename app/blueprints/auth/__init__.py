from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import routes




#from app.blueprints.auth import routes        #---cp commented out
