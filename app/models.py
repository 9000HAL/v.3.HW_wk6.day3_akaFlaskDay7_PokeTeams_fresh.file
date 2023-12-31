
from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class PokemonCatch(db.Model):
    """Adds the Pokemon to the User's team"""
    id = db.Column(db.Integer, primary_key=True)
    pokemon_name = db.Column(db.String)
    added_to_team_on = db.Column(db.DateTime, default=datetime.utcnow)


class PokemonTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon_catch.id'))
    name = db.Column(db.String(255))
    ability = db.Column(db.String)
    sprite = db.Column(db.String)
    base_exp = db.Column(db.Integer)



class User(UserMixin, db.Model):
    """ Adds the user data to the database"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def hash_password(self, signup_password):
        return generate_password_hash(signup_password)

    def from_dict(self, user_data):
        """Adds user data for the following fields to the database
         Also hashes the password they input"""
        self.username = user_data['username']
        self.email = user_data['email']
        self.password = self.hash_password(user_data['password'])




















































"""




from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash
#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()


# Association table between followers and followed
followers_followed = db.Table(
    'followers_followed',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

# Association table between User and Pokemon
user_pokemon = db.Table('user_pokemon',           ######TABLE###################################################
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True)
)

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    followed = db.relationship('User',
                               secondary=followers_followed,
                               primaryjoin=(followers_followed.c.follower_id == id),
                               secondaryjoin=(followers_followed.c.followed_id == id),
                               backref=db.backref('followers_followed', lazy='dynamic'),
                               lazy='dynamic')
    
    # Relation to Pokemon model
    pokemons = db.relationship('Pokemon', secondary=user_pokemon, back_populates='users')
    
    # Hashes our password when a user signs up
    def hash_password(self, signup_password):
        return generate_password_hash(signup_password)
    
    # This method will assign our columns with their respective values
    def from_dict(self, user_data):
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.email = user_data['email']
        self.password_hash = self.hash_password(user_data['password'])





# Pokemon model
class Pokemon(db.Model):
    __tablename__ = 'pokemon'                        ######TABLE###################################################
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False, unique=True)
    img_url = db.Column(db.String(500))
    
    # User relation through association table
    users = db.relationship('User', secondary=user_pokemon, back_populates='pokemons')

# CRUD utility functions
def add_pokemon(name, img_url):
    new_pokemon = Pokemon(name=name, img_url=img_url)
    db.session.add(new_pokemon)
    db.session.commit()
    return new_pokemon

def get_pokemon_by_name(name):
    return Pokemon.query.filter_by(name=name).first()

def add_pokemon_to_user(user_id, pokemon_name):
    user = User.query.get(user_id)
    pokemon = get_pokemon_by_name(pokemon_name)
    if user and pokemon:
        user.pokemons.append(pokemon)
        db.session.commit()

def remove_pokemon_from_user(user_id, pokemon_name):
    user = User.query.get(user_id)
    pokemon = get_pokemon_by_name(pokemon_name)
    if user and pokemon:
        user.pokemons.remove(pokemon)
        db.session.commit()

def list_user_pokemons(user_id):
    user = User.query.get(user_id)
    if user:
        return user.pokemons
    return []

def list_all_pokemon():
    return Pokemon.query.all()

# Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String(500))
    title = db.Column(db.String(30))
    caption = db.Column(db.String(30))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def from_dict(self, post_data):
        self.img_url = post_data['img_url']
        self.title = post_data['title']
        self.caption = post_data['caption']
        self.user_id = post_data['user_id']

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



"""













































































#v.1 pre documentation here below
"""
from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash #check_password_hash




# from documentation 1.1 ###########################################################VVVVVVVVVV


# New Pokémon model
class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the Pokemon
    name = db.Column(db.String(100), nullable=False)  # Pokemon name
    image_url = db.Column(db.String(500))  # URL of Pokemon image

    # User relation through association table
    users = db.relationship('User', secondary='user_pokemon', back_populates='pokemons')

    # from documentation 1.1 ###########################################################^^^^^^^^^^^^^



#from documentation 1.2 ###########################################################VVVVVVVVVV

# Association table between User and Pokemon
user_pokemon = db.Table('user_pokemon',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True)
)

# Assuming your User model looks something like this:
class User(db.Model):
    # ...[your existing user fields here]...
    
    # Add relation to Pokemon model
    pokemons = db.relationship('Pokemon', secondary=user_pokemon, back_populates='users')


#from documentation 1.2 ###########################################################^^^^^^^^^^^^







class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    #password_hash = db.Column(db.String) 
    password_hash = db.Column(db.String, nullable=False) # Save hashed password.
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    

    #this section from template below
    # hashes our password when user signs up
    def hash_password(self, signup_password):
        return generate_password_hash(signup_password)
    
    # This method will assign our columns with their respective values

    def from_dict(self, user_data):
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.email = user_data['email']
        self.password_hash = self.hash_password(user_data['password'])    #c4 suggested this change



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String)
    title = db.Column(db.String(30))
    caption = db.Column(db.String(30))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    #foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

      # This method will assign our columns with their respective values
    def from_dict(self, post_data):
        self.img_url = post_data['img_url']
        self.title = post_data['title']
        self.caption = post_data['caption']
        self.user_id = post_data['user_id']

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)













#<!--removed my v.1 set up here commented out below-->
def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)





"""












































############lecture version below#######################

"""   
from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String)  
    created_on = db.Column(db.DateTime, default=datetime.utcnow())


    # hashes our password when a user signs up
    def hash_password(new_user, signup_password):        
        return generate_password_hash(signup_password)





##############
    # this method will assign our columns with their respective values ---- WORK ??? --NO DO NOT USE SELF
def from_dict(self, user_data): 
    self.first_name = user_data['first_name']
    self.last_name = user_data['last_name']
    self.email = user_data['email']
    self.password = self.hash_password(user_data['password'])
    --- WORK ??? --NO DO NOT USE SELF
##############

# DUPLICATE MODEL TO FIX ERROR ------WORK ?????????? ---YES!!!!!!
def from_dict(new_user, user_data): 
    new_user.first_name = user_data['first_name']
    new_user.last_name = user_data['last_name']
    new_user.email = user_data['email']
    new_user.password = new_user.hash_password(user_data['password'])


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



    """