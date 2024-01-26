from flask import Blueprint, request, jsonify
from app.models import Ayas
from app import db

aya_bp = Blueprint('aya', __name__)

@aya_bp.route('/aya-search', methods=['POST'])
def aya_search():
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'A text must be provided'}), 400
    results = Ayas.query.filter(Ayas.الآية_بالرسم_المعاصر.ilike(f'%{text}%')).all()
    # results_data = [{ 'sura no': aya.رقم_السورة, 'text': aya.الآية_بالرسم_المعاصر} for aya in results]
    # results_data = [{key: getattr(aya, key) for key in aya.__dict__} for aya in results]
    results_data = []
    for aya in results:
     aya_dict = {key: getattr(aya, key) for key in aya.__dict__ if not key.startswith("_")}
     results_data.append(aya_dict)

    return jsonify(results_data), 200

