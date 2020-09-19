from flask import Flask,redirect
from flask import render_template,request
import csv

app=Flask(__name__)

@app.route('/')
def my():
    return render_template('index.html')

@app.route('/<string:page_name>')
def my_work(page_name):
    return render_template(page_name)

def write_in_text_file(data):
    a=data['name']
    b=data['email']
    c=data['subject']
    d=data['message']
    fp=open('database.txt',mode='a')
    fp.write(f'Name: {a}, Email: {b}, Subject: {c}, Message: {d}\n')
    fp.close()

def write_in_csv(data):
    dt=open('database.csv',mode='a',newline="")
    a=data['name']
    b=data['email']
    c=data['subject']
    d=data['message']
    writer=csv.writer(dt,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    writer.writerow([a,b,c,d])
    dt.close()

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        print(data)
        write_in_text_file(data)
        write_in_csv(data)
        return render_template('thank_you.html',name=data['name'])
    else:
        return 'Something went wrong.'
