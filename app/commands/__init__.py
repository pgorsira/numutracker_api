from flask import Blueprint

app = Blueprint('commands', __name__)

from . import import_artists