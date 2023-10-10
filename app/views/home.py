from flask import Blueprint, render_template, redirect, url_for
from app.components.base_title_text import base_title_text
from app.constants.home import ABOUT_TEXT

home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/home')
def home():
    return render_template('home.html', about_university=base_title_text(ABOUT_TEXT))


@home_blueprint.route('/')
def index():
    return redirect(url_for('home.home'))
