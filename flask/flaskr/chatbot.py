import functools
import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

#Creating a blueprint for the chatbot module
bp = Blueprint('chatbot', __name__)

#Function to send bot response according to the request message
@bp.route('/response/<msg>', methods=['GET'])
def get_bot_response(msg):
    while True:
        inp = msg.split(" ")
        if 'hi' in inp:
            response = "What can i do for you?"
        elif 'flask' in inp:
            response = "Flask is one of python's web framework that uses Jinja templating to help you develop web applications. It provides you with tools, libraries and technologies that allow you to build a web application. "
        elif 'django' in inp:
            response = "Django is a python web framework that follows the MVT architectural pattern allowing for easy and rapid developemtn of web application"
        elif 'web framework' in inp:
            response = "A web framework is a set of tools and other resources like libraries, APIs that supports the development of web applications"
        elif 'api' in inp:
            response = "Application Program Interface(API) is a set of rules that defines the connection between applications."
        else:
            response = "Hope I helped you out!"
            return response
            quit()
        return response
        
