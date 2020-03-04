#!/usr/bin/env python
# coding: utf-8




from flask import *
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd


chatbot = ChatBot('Menaps')


trainer = ListTrainer(chatbot)

df=pd.read_table("countries.txt",error_bad_lines=False,sep=";")



tr=[]

for idx,row in df.iterrows():
    tr.append("What is the capital of "+str(row["name"]).lower()+" ?")
    tr.append("the capital of "+str(row["name"]).lower()+" is "+str(row["capital"]))


# Train the chatbot based on the english corpus
trainer.train(tr)



app = Flask(__name__)

@app.route('/question')
def get_hybrid_banners_recommendation():
    question = request.args.get('q', None)
    if question is None:
        abort(404)
    else:
        return str(chatbot.get_response(question))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)





