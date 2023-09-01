from flask import request, render_template, url_for, flash, redirect
from flask_login import login_required, current_user
from .import pokemon_catch
import requests
from app.blueprints.auth.forms import PokemonSelect
from app.models import PokemonTeam
from app import db


@pokemon_catch.route('/catch_pokemon', methods=['POST'])
@login_required
def catch_pokemon():
    if request.method == 'POST' and request.form.get('pokemon_name'):
        pokemon_name = request.form.get('pokemon_name')
        pokemon_ability = request.form.get('pokemon_ability')
        pokemon_base_exp = request.form.get('pokemon_base_exp')
        pokemon_sprite = request.form.get('pokemon_sprite')

        
        team_count = PokemonTeam.query.filter_by(user_id=current_user.id).count()
        if team_count >= 5:
            flash('Your Pokemon Team is full! You cannot catch more Pokémon until you reduce your current team.')
            return redirect(url_for('pokemon_team.pokemon_team'))

        existing_pokemon = PokemonTeam.query.filter_by(name=pokemon_name).first()

        if existing_pokemon:
            existing_pokemon.ability = pokemon_ability
            existing_pokemon.base_exp = pokemon_base_exp
            existing_pokemon.sprite = pokemon_sprite
            db.session.commit()
            flash('Pokemon team updated')
        else:
            pokemon_data = PokemonTeam(
                name=pokemon_name,
                ability=pokemon_ability,
                base_exp=pokemon_base_exp,
                sprite=pokemon_sprite,
                user_id=current_user.id
            )
            db.session.add(pokemon_data)
            db.session.commit()
            flash('Pokemon has been added to your Team')

    return redirect(url_for('pokemon_team.pokemon_team'))
