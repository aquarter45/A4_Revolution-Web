from flask import Blueprint,render_template,abort,url_for,redirect
import os

about_us = Blueprint('about_us', __name__)

@about_us.route('/')
def abouts_us():
    return redirect(url_for('about_us.getPage', page="our_goals"))

@about_us.route('/<page>')
def getPage(page):
    if os.path.isfile(f"website/Markdown/{page}/{page}.md"):
        with open(f"website/Markdown/{page}/{page}.md",encoding="UTF-8") as f:
            lines = f.read()
        return render_template("about-us/our_goals.html",our_goals=lines)

    return abort(404)