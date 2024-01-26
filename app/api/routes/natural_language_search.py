from flask import Blueprint, request, jsonify
from app.langchain_helper import process_natural_language_query

natural_language_bp = Blueprint('natural_language', __name__)

@natural_language_bp.route('/natural-language', methods=['POST'])
def natural_language_search():
    content = request.json
    if not content or 'query' not in content:
        return jsonify({'error': 'No query provided'}), 400
    query = content['query']
    response_text = process_natural_language_query(query)
    return jsonify({'response': response_text}), 200


