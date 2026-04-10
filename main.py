"""
Flask web server for rpcats portfolio.
Serves the static frontend files and provides API endpoints.
"""

from flask import Flask, render_template, send_from_directory, jsonify
import os
from trips import trips_bp

# Create Flask application
app = Flask(__name__)

# Register blueprints
app.register_blueprint(trips_bp)

# Get the directory containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    """Serve the main HTML page."""
    return render_template('index.html')


@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (CSS, JS, images, etc.)."""
    return send_from_directory(BASE_DIR, filename)


@app.route('/api/health')
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'rpcats',
        'version': '0.1.0'
    })


@app.route('/api/info')
def info():
    """Return server information."""
    return jsonify({
        'name': 'Alex Chen | Python Developer',
        'description': 'Portfolio webserver',
        'endpoints': {
            '/': 'Home page',
            '/styles.css': 'Stylesheet',
            '/script.js': 'JavaScript',
            '/api/health': 'Health check',
            '/api/info': 'Server information'
        }
    })

if __name__ == '__main__':
    # Run the development server
    port = int(os.environ.get('PORT', 8000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"Starting Flask server on http://localhost:{port}")
    print("Press CTRL+C to stop the server")
    print(f"Base Directory:{__file__}")

    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
