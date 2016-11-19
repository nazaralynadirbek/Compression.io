# -*- coding: utf-8 -*-

from flask import Flask

# App
app = Flask(__name__)
app.config.from_object('config')

# Modules
from app import views