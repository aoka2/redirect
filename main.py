from flask import Flask, request, render_template
import os
import pyttsx3
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('id1.html')

@app.route('/talk', methods=["POST"])
def talkGround():
    data = request.form.get('background')
    print(data)
    return render_template('talk.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)
