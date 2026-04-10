from flask import Blueprint, render_template

trip_bp = Blueprint('/trip', __name__, template_folder='../templates')

@trip_bp.route('/')
def home():
    return render_template('trip/index.html', name="Geek")

@trip_bp.route('/australia')
def australia():
    return render_template('trip/australia.html', name="Geek")