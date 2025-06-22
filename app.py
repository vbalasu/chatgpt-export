# coding: utf-8
from flask import Flask, request, send_file
from export import export_pdf
app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello world'

@app.route('/pdf')
def export_to_pdf():
    url = request.args.get('url')
    export_pdf(url)
    return send_file('page.pdf', as_attachment=True)
