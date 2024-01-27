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
    # results_data = [{'word': word.الكلمة, 'root_word': word.جذر_الكلمة} for word in results]
    # results_data = {key: getattr(Words, key) for key in Words.__dict__ if not key.startswith("_")}

    results_data = []
    for myword in results:
     myword_dict = {key: getattr(myword, key) for key in myword.__dict__ if not key.startswith("_")}
     results_data.append(myword_dict)

    return jsonify(results_data), 200
