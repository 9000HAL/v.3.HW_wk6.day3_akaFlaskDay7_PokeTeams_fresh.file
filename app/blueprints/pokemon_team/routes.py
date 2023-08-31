from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import PokemonTeam
from . import pokemon_team
from app import db


@pokemon_team.route('/pokemon_team')
@login_required
def pokemon_team():
    pokemon_data = PokemonTeam.query.all()

    return render_template('pokemon_team.html', pokemon_data=pokemon_data)


