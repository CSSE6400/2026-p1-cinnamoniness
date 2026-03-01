from flask import Blueprint, jsonify
api = Blueprint('api', __name__,url_prefix='/api/v1')

@api.route('/health')
def health():
    return jsonify({'status': 'ok'}),200

@api.route('todos', methods=['GET'])
def get_todos():
    return jsonify([{
        "id": 1,
        "title": "Watch CSSE6400 lectures",
        "description": "Watch all the lectures for CSSE6400 for week 1",
        "completed": True,
        "deadline": "2026-02-27T18:00:00",
        "created_at": "2026-02-20T14:00:00",
        "updated_at": "2026-02-21T144:30:00"

    }])