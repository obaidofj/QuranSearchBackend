from flask import jsonify
from .ping import ping_bp
from .routes.natural_language_search import natural_language_bp
from .routes.two_word_search import two_word_bp
from .routes.one_word_search import one_word_bp
from .routes.word_root_search import word_root_bp
from .routes.aya_search import aya_bp



def configure_api(app):
    app.register_blueprint(ping_bp, url_prefix='/api/v1')
    app.register_blueprint(natural_language_bp, url_prefix='/api/v1/search')
    app.register_blueprint(two_word_bp, url_prefix='/api/v1/search')
    app.register_blueprint(one_word_bp, url_prefix='/api/v1/search')
    app.register_blueprint(word_root_bp, url_prefix='/api/v1/search')
    app.register_blueprint(aya_bp, url_prefix='/api/v1/search')

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify(error=404, text=str(e)), 404
    

    

