#!/usr/bin/env python

from appkit.api.v0_2_8 import App
from flask import render_template, request
import os
import sys
from docutils.core import publish_parts


app = App(__name__)

try:
    file_name = sys.argv[1]
    if not os.path.exists(file_name):
        open(file_name, 'w').close()
except:
    file_name = None

app.file_name = file_name


@app.route('/')
def index():
    text = None
    if app.file_name is not None:
        text = open(file_name).read()
    return render_template('/ui.html', file_name=app.file_name, text=text)


@app.route('/rst2html/', methods=['POST', ])
def rst2html():
    html = request.form.get('text', None)
    html = publish_parts(html, writer_name='html')['html_body']
    return html


@app.route('/save/', methods=['POST', ])
def save():
    """save rest content to the file"""

    file_name = request.form.get('file', None)
    text = request.form.get('text', None)
    f = open(file_name, 'w')
    f.write(text)
    f.close()
    return 'Saved'

if __name__ == '__main__':
    app.run()
