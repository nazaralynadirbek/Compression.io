# -*- coding: utf-8 -*-

import os
import datetime

from app import app

from flask import abort
from flask import request
from flask import jsonify
from flask import render_template

from werkzeug.utils import secure_filename

from PIL import Image

@app.route('/')
@app.route('/index')
def index():
    return render_template('default/pages/index.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        file.filename = secure_filename(file.filename)

        # Rename
        file.filename = datetime.datetime.now().strftime('%Y-%m-%d') + '-' + file.filename
        filename = file.filename

        file.save(os.path.abspath(app.config['UPLOAD_FOLDER'] + '/original/' + filename))

        # Compress
        compressed = Image.open(file)
        compressed.save(os.path.abspath(app.config['UPLOAD_FOLDER'] + '/compressed/' + filename), quality=50)

        return jsonify({'status': 'success'})
    else:
        abort(404)