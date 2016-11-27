# -*- coding: utf-8 -*-

import os
import datetime

from app import app

from flask import abort
from flask import request
from flask import jsonify
from flask import render_template

from werkzeug.utils import secure_filename

@app.route('/')
@app.route('/index')
def index():
    # Check folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER'] + '/original'):
        os.makedirs(app.config['UPLOAD_FOLDER'] + '/original')

    if not os.path.exists(app.config['UPLOAD_FOLDER'] + '/compressed'):
        os.makedirs(app.config['UPLOAD_FOLDER'] + '/compressed')

    return render_template('default/pages/index.html', source_image=None)

@app.route('/upload', methods=['GET','POST'])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        file.filename = secure_filename(file.filename)

        # Rename
        file.filename = datetime.datetime.now().strftime('%Y-%m-%d') + '-' + file.filename
        filename = file.filename

        file.save(os.path.abspath(app.config['UPLOAD_FOLDER'] + '/original/' + filename))

        return jsonify({'status': 'success'})
    else:
        abort(404)