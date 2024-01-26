from flask import Blueprint, request, jsonify
from app.models import QuranSearch
from app import db

two_word_bp = Blueprint('two_word', __name__)

@two_word_bp.route('/two-words', methods=['POST'])
def two_word_search():
    word1 = request.json.get('wrdq1')
    word2 = request.json.get('wrdq2')

    wrd1='رقم_الكلمة_1'
    wrd2='رقم_الكلمة_2'

    if not word1 or not word2:
        return jsonify({'error': 'Both words must be provided'}), 400

    results = QuranSearch.query.filter((QuranSearch.الكلمة_1.ilike(f'%{word1}%') | QuranSearch.الكلمة_2.ilike(f'%{word2}%'))).all()
    
    results_data = [{'word1': word.رقم_الكلمة_1, 'word2': word.رقم_الكلمة_2} for word in results]
    
    return jsonify(results_data), 200
 