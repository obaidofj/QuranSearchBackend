from flask import Blueprint, request, jsonify
from app.models import Words
from app import db
from flask_cors import cross_origin


one_word_bp = Blueprint('one_word', __name__)

@one_word_bp.route('/one-word', methods=['POST'])
@cross_origin()
def one_word_search():
    response = jsonify({'message': 'Success'})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    word = request.json.get('wrdq')
    if not word:
        return jsonify({'error': 'A word must be provided'}), 400
    results = Words.query.filter(Words.الكلمة.ilike(f'%{word}%')).all()
    # results_data = [{'word': word.الكلمة, 'root_word': word.جذر_الكلمة ,'sura_no':   word.رقم_السورة} for word in results]

    results_data = []
    for myword in results:
     myword_dict = {key: getattr(myword, key) for key in myword.__dict__ if not key.startswith("_")}
     results_data.append(myword_dict)
    


    return jsonify(results_data), 200
 