# coding: utf-8
from flask import Flask, request, send_file, render_template
from export import export_pdf
app = Flask(__name__, static_folder='media')
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/pdf')
def export_to_pdf():
    url = request.args.get('url')
    print(url)
    export_pdf(url)
    return send_file('page.pdf', as_attachment=True)
