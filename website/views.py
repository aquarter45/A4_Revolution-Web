from flask import Blueprint,render_template,abort,url_for,redirect
import os

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return redirect(url_for('views.getpage', page="home"))

@views.route('/page/<page>')
def getpage(page):
    if os.path.isfile(f"website/Markdown/{page}.md"):
        
        with open(f"website/Markdown/{page}.md",encoding="UTF-8") as f:
            lines = f.read()
            
        return render_template("home.html",post=lines)
    
    return abort(404)