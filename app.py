import os
from flask import Flask,redirect
from routes import blueprints  # Import the list of blueprints

def create_app():
    app = Flask(__name__)

    # Register all blueprints
    for blueprint in blueprints:
        print(blueprint.name)
        app.register_blueprint(blueprint, url_prefix=blueprint.name)

    return app

app = create_app()
@app.route('/')
def index():
    """Serve the main HTML page."""
    return redirect("/app")

@app.route('/assets/<path:filename>')
def assets(filename):
    """Serve the main HTML page."""
    return redirect("/app/assets/{}".format(filename))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    # app = create_app()
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
