from flask import Flask ,request ,render_template
import pandas
import numpy as np 
import pickle

model=pickle.load(open('model.pkl','rb'))

#flask_app

app=Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predic():
    return

# pyhton main
if __name__=="__main__":
    app.run(debug=True)
