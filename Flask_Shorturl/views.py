from flask import Flask,render_template,flash,redirect,request,session,url_for
from app import app
from model import *
from forms import foorms


@app.route('/home/',methods=['GET','POST'])
def home():
    s=0
    fo=foorms()
    con=models()
    if request.method=='POST':
        if request.form['add']=='convert':
            ur=str(fo.logi.data)
            s=con.gen(ur)
    return render_template('home.html',fo=fo,s=s)        
@app.route('/<username>')
def newu(username):
    con=models()
    c=con.ret(username)
    return redirect(c)
        

