from flask import Blueprint , render_template

about_us = Blueprint('about_us', __name__)

@about_us.route('/')
def abouts_us():
    return render_template("/about-us/about-us.html")