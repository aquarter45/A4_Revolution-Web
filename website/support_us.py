from flask import Blueprint , render_template

supportus = Blueprint('supportus', __name__)

@supportus.route('/')
def supportus_Home():
    return render_template("/support-us/support-us.html")