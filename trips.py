"""
Trip-related routes and functionality.
Provides blueprint for trip pages and API endpoints.
"""

from flask import Blueprint, render_template, jsonify

# Create blueprint for trips
trips_bp = Blueprint('trips', __name__, template_folder='templates')


# Sample trip data (would typically come from database)
TRIPS_DATA = [
    {
        'id': 1,
        'destination': 'Australia',
        'description': 'Explore the land down under',
        'duration': '14 days',
        'highlights': ['Sydney Opera House', 'Great Barrier Reef', 'Outback']
    },
    {
        'id': 2,
        'destination': 'Japan',
        'description': 'Experience ancient culture and modern technology',
        'duration': '10 days',
        'highlights': ['Tokyo', 'Kyoto', 'Mount Fuji']
    },
    {
        'id': 3,
        'destination': 'Europe',
        'description': 'Multi-country European adventure',
        'duration': '21 days',
        'highlights': ['Paris', 'Rome', 'Barcelona']
    }
]


@trips_bp.route('/trips')
def trips_index():
    """Serve the trips listing page."""
    return render_template('trip/index.html')


@trips_bp.route('/trips/<int:trip_id>')
def trip_detail(trip_id):
    """Serve individual trip detail page."""
    trip = next((t for t in TRIPS_DATA if t['id'] == trip_id), None)
    if trip is None:
        return jsonify({'error': 'Trip not found'}), 404
    return render_template('trip/detail.html', trip=trip)


@trips_bp.route('/api/trips')
def api_trips_list():
    """Return list of all trips."""
    return jsonify({
        'trips': TRIPS_DATA,
        'count': len(TRIPS_DATA)
    })


@trips_bp.route('/api/trips/<int:trip_id>')
def api_trip_detail(trip_id):
    """Return single trip details."""
    trip = next((t for t in TRIPS_DATA if t['id'] == trip_id), None)
    if trip is None:
        return jsonify({'error': 'Trip not found'}), 404
    return jsonify(trip)


# Legacy route - keep for backward compatibility with existing templates
@trips_bp.route('/trip')
def trip():
    """Serve the main trip page (legacy route)."""
    return render_template('trip/index.html')