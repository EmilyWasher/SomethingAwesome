from server import app
from flask import request, render_template, redirect, url_for
from ciphers.caesar import Caesar
from ciphers.caesar_no_key import Caesar_no_key
from ciphers.reverse import Reverse
from ciphers.atbash import Atbash
from ciphers.rail_fence import Rail_fence
from ciphers. scramble import Scramble

import re
import enchant
import string
import random
d = enchant.Dict("en_AU")


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/caesar_cipher', methods=['POST', 'GET'])
def caesar():
    if request.method == 'POST':
        key = int(request.form['key'])
        message = request.form['message']
        caesar = Caesar(message, key)
        user_option = request.form['option']

        if user_option == 'encrypt':
            new_message = caesar.encrypt()
        elif user_option == 'decrypt':
            new_message = caesar.decrypt()
        return render_template("caesar.html", new_message=new_message)

    return render_template("caesar.html")


@app.route('/caesar_cipher_no_key', methods=['POST', 'GET'])
def caesar_no_key():
    if request.method == 'POST':
        message = request.form['message']
        print(message)
        caesar = Caesar_no_key(message)
        new_message = caesar.crack_caesar()
        return render_template('caesar_no_key.html', new_message=new_message)
    return render_template("caesar_no_key.html")


@app.route('/reverse_alpha_cipher', methods=['POST', 'GET'])
def reverse_alpha():
    if request.method == 'POST':
        message = request.form['message']
        reverse = Atbash(message)
        new_message = reverse.encode()

        return render_template('atbash.html', new_message=new_message)

    return render_template("atbash.html")


@app.route('/scramble_cipher', methods=['POST', 'GET'])
def scramble():
    if request.method == 'POST':
        key = request.form.get("key")
        message = request.form['message']
        user_option = request.form['option']

        if not key:
            scramble = Scramble(message, None) 
        else:
            scramble = Scramble(message, key)  
            
        if user_option == 'encrypt':
            new_message = scramble.encrypt()
        elif user_option == 'decrypt':
            new_message = scramble.decrypt()
           
        return render_template("scramble.html", new_message=new_message, new_key=scramble.get_key())

    return render_template("scramble.html")


@app.route('/reverse_cipher', methods=['POST', 'GET'])
def reverse():
    if request.method == 'POST':
        message = request.form['message']
        user_option = request.form['option']
        reverse = Reverse(message)

        if user_option == 'by_word':
            new_message = reverse.rev_by_word(message)
        elif user_option == 'by_letter':
            new_message = reverse.rev_by_letter(message)
        return render_template('reverse.html', new_message=new_message)

    return render_template("reverse.html")


@app.route('/rail_fence_cipher', methods=['POST', 'GET'])
def rail_fence():
    if request.method == 'POST':
        rails = int(request.form['rails'])
        message = request.form['message']
        #message.strip()
        rail_fence = Rail_fence(message, rails)
        user_option = request.form['option']

        if user_option == 'encrypt':
            new_message = rail_fence.encrypt()
        elif user_option == 'decrypt':
            new_message = rail_fence.decrypt()
        return render_template("rail.html", new_message=new_message)

    return render_template("rail.html")
