from server import app
from flask import request, render_template, redirect, url_for
from ciphers.caesar import Caesar


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/caesar_cipher', methods = ['POST', 'GET'])
def caesar():
    if request.method == 'POST':
        key = int(request.form['key'])
        message = request.form['message']
        caesar = Caesar(message, key)
        if request.form['option'] == "Encrypt":
            print ('hi')
        new_message = caesar.encrypt()
        return render_template("caesar.html", new_message=new_message)
    return render_template("caesar.html")


@app.route('/reverse_cipher')
def reverse():
    return render_template("reverse.html")


@app.route('/caesar_cipher_no_key')
def caesar_no_key():
    return render_template("caesar_no_key.html")