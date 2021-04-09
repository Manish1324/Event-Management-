from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']='mysql://un:up@url/data_base_name';

app.config['SQLALCHEMY_DATABASE_URI']='mysql://manish1324:root123$%^@manish1324.mysql.pythonanywhere-services.com/manish1324$default';

db=SQLAlchemy(app)

class Contact_us(db.Model):
    FIRSTNAME=db.Column(db.String(20),primary_key=True)
    LASTNAME=db.Column(db.String(20),nullable=True)
    CONTACT=db.Column(db.Numeric,nullable=True)
    EMAIL=db.Column(db.String(40),nullable=False)
    SUBJECT=db.Column(db.String(40),nullable=False)
    MESSAGE=db.Column(db.String(100),nullable=False)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")

@app.route("/contact_us_1",methods=["GET","POST"])
def contact_us_1():
    if(request.method=='POST'):
        a=request.form.get('first_name')
        b=request.form.get('last_name')
        c=request.form.get('tel')
        d=request.form.get('email')
        e=request.form.get('subject')
        f=request.form.get('comments')
        entry=Contact_us(FIRSTNAME=a,LASTNAME=b,CONTACT=c,EMAIL=d,SUBJECT=e,MESSAGE=f)
        db.session.add(entry)
        db.session.commit()
    return render_template("contact_us.html")
    #return "value is inserted..."

@app.route("/past_event")
def past_event():
    return render_template("past_event.html")


@app.route("/all_services")
def all_services():
    return render_template("all_services.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")