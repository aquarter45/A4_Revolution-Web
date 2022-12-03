from flask import Blueprint , render_template

support_us = Blueprint('support_us', __name__)

@support_us.route('/')
def supportus_Home():
    return render_template("/support-us/support-us.html")