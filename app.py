# coding: utf-8
from flask import Flask, request, send_file
from export import export_pdf
app = Flask(__name__)
@app.route('/')
def hello():
    return '<h1>USAGE</h1><p>https://chatgpt-export.cloudmatica.com/pdf?url=<strong>https://chatgpt.com/share/YOUR_CHATGPT_SHARE_CODE</strong></p>'

@app.route('/pdf')
def export_to_pdf():
    url = request.args.get('url')
    print(url)
    export_pdf(url)
    return send_file('page.pdf', as_attachment=True)
