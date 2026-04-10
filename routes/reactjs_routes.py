from flask import Blueprint, render_template

reactjs_bp = Blueprint('/reactjs', __name__, template_folder='../templates')

@reactjs_bp.route('/')
def reactjs_home():
    return render_template('reactjs/index.html', name="Geek")

