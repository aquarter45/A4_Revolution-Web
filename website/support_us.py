from flask import Blueprint,render_template,abort,url_for,redirect
import os

support_us = Blueprint('support_us', __name__)

@support_us.route('/')
def supportus_Home():
    return redirect(url_for("support_us.getpage", page='support-us'))

@support_us.route('/<page>')
def getpage(page):
    if os.path.isfile(f"website/Markdown/{page}/{page}.md"):
        with open(f"website/Markdown/{page}/{page}.md",encoding="UTF-8") as f:
            lines = f.read()
        return render_template("support-us/support-us.html",support_us=lines)

    return abort(404)
    