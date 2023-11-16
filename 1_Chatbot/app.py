from flask import Flask, render_template, request
import numpy as np
import os
from time import sleep
from config import Config
from model import  get_response




app = Flask(__name__)
app.config.from_object((Config))
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'static'



start=['Chatbot:How can I help you?']
thread=[]
@app.route('/')
def index():  # put application's code here
    thread=[]
    return render_template('index.html',  thread=start)

@app.route('/', methods=['POST','GET'])
def upload():
    sleep(2)
    if request.method=='POST':
        question1= request.form['question']
    thread.append('You:'+question1)

    prompt=f'User: {question1=}\nChatbox:'
    chat_response=get_response(prompt)
    thread.append('Chatbot:'+chat_response)

    return render_template('index.html', thread=thread)



if __name__ == '__main__':
    app.run(DEBUG=True)
