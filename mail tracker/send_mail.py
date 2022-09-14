from time import sleep
from json import dumps
from kafka import KafkaProducer
import win32com.client as client
import os
userid=['saurav','saurav1','saurav2']
emailid=['saurav.baliga@convergytics.com']
outlook=client.Dispatch('Outlook.Application')
j=0
for i in userid:
    msg=outlook.CreateItem(0)
    msg.BCC='saurav.baliga@convergytics.com'
    msg.Subject='you are in topic '+str(j)
    j=j+1
    msg.HTMLBODY="<html><h1>welcome</h1><body><img src=""http://localhost:5000/static/images/"+i+"></body></html>"
    msg.Send()