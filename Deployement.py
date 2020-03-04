#!/usr/bin/env python
# coding: utf-8

# In[5]:


from flask import *
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd
import os

chatbot = ChatBot(
    'Menaps',
    trainer='chatterbot.trainers.ListTrainer'
)

app = Flask(__name__)

@app.route('/')
def Hello():
    return "Hello World"

@app.route('/question')
def getResponse():
    question = request.args.get('q', None)
    if question is None:
        abort(404)
    else:
        return str(chatbot.get_response(question))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


# In[ ]:




