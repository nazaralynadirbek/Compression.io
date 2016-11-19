# -*- coding: utf-8 -*-

import os

from app import app
from flask import request
from flask import render_template

from werkzeug import secure_filename

@app.route('/')
@app.route('/index')
def index():
    return render_template('default/pages/index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        filename = secure_filename(file.filename)

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        file.save(os.path.abspath(app.config['UPLOAD_FOLDER'] + filename))

        return file.filename