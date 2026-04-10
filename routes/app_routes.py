from flask import Blueprint, render_template
from flask import Flask, render_template, send_from_directory, jsonify
import os

app_bp = Blueprint('/app', __name__, template_folder='../templates')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_public_dir():
    return os.path.join(BASE_DIR, '../public')
def get_public_js_dir():
    return os.path.join(get_public_dir(), 'js')
def get_public_css_dir():
    return os.path.join(get_public_dir(), 'css')
def get_public_image_dir():
    return os.path.join(get_public_dir(), 'image')
def get_public_assets_dir():
    return os.path.join(get_public_dir(), 'assets')

@app_bp.route('/app')
@app_bp.route('/')
def index():
    """Serve the main HTML page."""
    return render_template('index.html')


@app_bp.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (CSS, JS, images, etc.)."""
    print("serve_static::" + BASE_DIR)
    print("serve_static::" + filename)
    final_filename = os.path.basename(filename)
    print(final_filename)  # Output: report.pdf
    if final_filename.endswith('.css'):
        return send_from_directory(get_public_css_dir(), final_filename)
    elif final_filename.endswith('.js'):
        return send_from_directory(get_public_js_dir(), final_filename)
    elif final_filename.endswith('.png'):
        print("serve_static::sending from " + get_public_image_dir())
        return send_from_directory(get_public_image_dir(), final_filename)
        return send_from_directory(get_public_image_dir(), filename)

@app_bp.route('/assets/<path:filename>')
def assets_static(filename):
    """Serve static files (CSS, JS, images, etc.)."""
    return send_from_directory(get_public_assets_dir(), filename)

@app_bp.route('/api/health')
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'rpcats',
        'version': '0.1.0'
    })


@app_bp.route('/api/info')
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
