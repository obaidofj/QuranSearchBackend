from flask import Blueprint, request, jsonify
from app.models import Words
from app import db

word_root_bp = Blueprint('word_root', __name__)

@word_root_bp.route('/word-root', methods=['POST'])
def word_root_search():
    root = request.json.get('root')
    if not root:
        return jsonify({'error': 'A root word must be provided'}), 400
    results = Words.query.filter(Words.جذر_الكلمة.ilike(f'%{root}%')).all()
    results_data = [{'word': word.الكلمة, 'root_word': word.جذر_الكلمة} for word in results]
    return jsonify(results_data), 200
