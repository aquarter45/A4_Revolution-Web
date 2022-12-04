from flask import Flask, render_template
from flaskext.markdown import Markdown

def page_not_found(e):
    return render_template('404.html'), 404

def create_app():
    app = Flask(__name__)

    Markdown(app)

    from .views import views
    from .support_us import support_us
    from .about_us import about_us

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(support_us,url_prefix='/support-us')
    app.register_blueprint(about_us,url_prefix='/about-us')
    app.register_error_handler(404, page_not_found)

    return app