from urllib import request
from flask import Flask, render_template,request,redirect
import os
import time
import pandas as pd

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route("/")
def home():
    return render_template('index.html')


#@app.route("/static/images/user/<filename1>",methods=['GET',"POST"])
#def Display_IMG(filename1):
#    start=time.time()
    #print(start)
#    a=time.gmtime(start)
#    print(time.strftime("%H:%M:%S", a))
#    print('filenmae',filename1)
#    return redirect('http://localhost:5000/static/bg_1.jpg')

@app.route("/static/images/<user>",methods=['GET',"POST"])
def Display_IMG1(user):
    start=time.time()
    mail=pd.read_csv('static/csv files/mail_track.csv')
    #print(start)
    a=time.gmtime(start)
    print(time.strftime("%H:%M:%S", a))
    print('mail opened by ',user)
    mail=mail.append({'UserName':user,'Time':time.strftime("%H:%M:%S", a)},ignore_index=True)
    mail.to_csv('static/csv files/mail_track.csv',mode='a',index=False,header=False)
    return redirect('https://www2.hm.com/hm-logo.png')

if __name__=='__main__':
    app.run(debug=True)