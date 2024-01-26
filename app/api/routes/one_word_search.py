from flask import Blueprint, request, jsonify
from app.models import Words
from app import db

one_word_bp = Blueprint('one_word', __name__)

@one_word_bp.route('/one-word', methods=['POST'])
def one_word_search():
    word = request.json.get('الكلمة')
    if not word:
        return jsonify({'error': 'A word must be provided'}), 400
    results = Words.query.filter(Words.الكلمة.ilike(f'%{word}%')).all()
    results_data = [{'word': word.الكلمة, 'root_word': word.جذر_الكلمة ,'sura_no':   word.رقم_السورة} for word in results]
    return jsonify(results_data), 200
