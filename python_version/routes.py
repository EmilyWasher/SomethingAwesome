from server import app
from flask import request, render_template, redirect, url_for
from caesar import Caesar


@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/caesar_cipher', methods = ['POST', 'GET'])
def caesar():
    if request.method == 'POST':
        key = int(request.form['key'])
        message = request.form['message']
        caesar = Caesar(message, key)
        new_mess = caesar.encrypt()
    return render_template("caesar.html")
