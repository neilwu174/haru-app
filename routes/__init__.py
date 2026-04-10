from flask import Blueprint

# Import all route blueprints
from routes.trip_routes import trip_bp
from routes.app_routes import app_bp
from routes.reactjs_routes import reactjs_bp

# Create a list of blueprints to register in the app
blueprints = [trip_bp,app_bp,reactjs_bp]