from flask import Blueprint, redirect, url_for, flash,render_template
from flask_login import login_required
from app.models import PokemonTeam
from app import db
from . import pokemon_release

@pokemon_release.route('/pokemon_release/<int:pokemon_id>', methods=['POST', 'GET'])

@login_required
def pokemon_release(pokemon_id):
    pokemon = PokemonTeam.query.get(pokemon_id)
    if "POST":
        db.session.delete(pokemon)
        db.session.commit()

        flash(f"You have released {pokemon.name} from your Team!")
    else:
        flash(f"You can't release a Pokemon you haven't caught yet!")
        render_template('pokemon_team.html')

    return redirect(url_for('pokemon_team.pokemon_team'))
