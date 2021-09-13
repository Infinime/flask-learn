from flask import Flask  # , flash
# from markupsafe import escape

app = Flask(__name__)

from app import routes
