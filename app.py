from urllib import request
from flask import Flask, render_template,request,redirect
import os
import time
import pandas as pd
import datetime
import psycopg2

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER
DATABASE_URL = os.environ['DATABASE_URL']
print(DATABASE_URL)
con = psycopg2.connect(DATABASE_URL)
@app.route("/",methods=['GET'])
@app.route("/home",methods=['GET'])
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
    start=datetime.datetime.now()
    #mail=pd.read_csv('static/csv files/mail_track.csv')
    print(start)
    #a=time.gmtime(start)
    #print(a)
    #print(time.strftime("%H:%M:%S", a))
    print('mail opened by ',user)
    #mail=mail.append({'UserName':user,'Time':time.strftime("%H:%M:%S", a)},ignore_index=True)
    #mail1=pd.DataFrame()
    #mail1['user_name']=user
    #mail1['time']=time.strftime("%H:%M:%S", a)
    #print(mail)
    #mail.to_csv('static/csv files/mail_track.csv',mode='a',index=False,header=False)
    #print(mail1)
    cursor = con.cursor()
    table_name='mail_data'
    columns='user_data,time'
    values=[user_name,start]
    statement=f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    print(statement)
    #cursor.execute(statement)
    #mail1.to_sql('mail_data', con = engine, if_exists='append')
    return redirect('https://lh3.googleusercontent.com/p/AF1QipMYpbypAsagW1iih-6hinCGdwiDfZIl7R5R3P8k=w1080-h608-p-no-v0')

if __name__=='__main__':
    app.run(debug=True)
