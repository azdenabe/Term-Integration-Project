from urllib.request import urlopen
from werkzeug.security import generate_password_hash,check_password_hash
import requests
import json
from templates.home.chart import *
from flask import render_template, request,session,redirect, url_for
from jinja2 import TemplateNotFound
import numpy
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] ="password"
@app.route('/')
def hello():
    return render_template("accounts/login.html")

@app.route('/index.html')
def index():
    if "username" in session:
        return redirect("/april.html")

    else:
        return redirect('/login.html')

@app.route('/january.html')
def january():
    data = sla_total(1)
    number1 = week_closed()
    number1_op = week_opened()
    mtbr_me = mtbr_met(1)
    mtbr_not_me = mtbr_not_met(1)
    num_closed = closed(1)
    num_op = opened(1)
    num_bl = backlog(1)
    perc = average_met(1)
    perc_not = average_not_met(1)
    wcr = week_critic_raised()
    inc_mon = incident_mont(1)
    cls_prio = closed_prio(1)
    opn_prio = open_prio(1)
    return render_template('home/january.html', segment='index',inc_mon = inc_mon,perc_not=perc_not,mtbr_not_me = mtbr_not_me,mtbr_me=mtbr_me,wcr = wcr,perc =perc ,num_bl=num_bl,num_op=num_op,num_closed=num_closed, data=data,
                            number1=number1,cls_prio=cls_prio,opn_prio=opn_prio, number1_op=number1_op)

@app.route('/february.html')
def february():
    if "username" in session:
        data = sla_total(2)
        number1 = week_closed()
        number1_op = week_opened()
        mtbr_me = mtbr_met(2)
        mtbr_not_me = mtbr_not_met(2)
        num_closed = closed(2)
        num_op = opened(2)
        num_bl = backlog(2)
        perc = average_met(2)
        perc_not = average_not_met(2)
        wcr = week_critic_raised()
        inc_mon = incident_mont(2)
        cls_prio = closed_prio(2)
        opn_prio = open_prio(2)
        return render_template('home/february.html', segment='index', inc_mon=inc_mon, perc_not=perc_not,
                               mtbr_not_me=mtbr_not_me, mtbr_me=mtbr_me, wcr=wcr, perc=perc, num_bl=num_bl,
                               num_op=num_op,cls_prio=cls_prio,opn_prio=opn_prio, num_closed=num_closed, data=data,
                               number1=number1, number1_op=number1_op)
@app.route('/march.html')
def march():
    if "username" in session:
        data = sla_total(3)
        number1 = week_closed()
        number1_op = week_opened()
        mtbr_me = mtbr_met(3)
        mtbr_not_me = mtbr_not_met(3)
        num_closed = closed(3)
        num_op = opened(3)
        num_bl = backlog(3)
        perc = average_met(3)
        perc_not = average_not_met(3)
        wcr = week_critic_raised()
        inc_mon = incident_mont(3)
        cls_prio = closed_prio(3)
        opn_prio = open_prio(3)
        return render_template('home/march.html', segment='index', inc_mon=inc_mon, perc_not=perc_not,
                               mtbr_not_me=mtbr_not_me, mtbr_me=mtbr_me, wcr=wcr, perc=perc, num_bl=num_bl,
                               num_op=num_op,cls_prio=cls_prio,opn_prio=opn_prio, num_closed=num_closed, data=data,
                               number1=number1, number1_op=number1_op)


@app.route('/april.html')
def april():
    if "username" in session:
        data = sla_total(4)
        number1 = week_closed()
        number1_op = week_opened()
        mtbr_me = mtbr_met(4)
        mtbr_not_me = mtbr_not_met(4)
        num_closed = closed(4)
        num_op = opened(4)
        num_bl = backlog(4)
        perc = average_met(4)
        perc_not = average_not_met(4)
        wcr = week_critic_raised()
        inc_mon = incident_mont(4)
        cls_prio = closed_prio(4)
        opn_prio = open_prio(4)
        return render_template('home/april.html', segment='index', inc_mon=inc_mon, perc_not=perc_not,
                               mtbr_not_me=mtbr_not_me, mtbr_me=mtbr_me, wcr=wcr, perc=perc, num_bl=num_bl,
                               num_op=num_op,cls_prio=cls_prio,opn_prio=opn_prio, num_closed=num_closed, data=data,
                               number1=number1, number1_op=number1_op)
# ---------------------------------------- Login ---------------------------------------- #
@app.route("/login.html")
def login_page():
    return render_template("accounts/login.html")

@app.route("/log_in", methods=["POST"])
def login():
    # 1. get the form from the request
    username = request.form["username"]
    password = request.form["password"]
    if username == "" or password =="":
        return render_template("accounts/login.html",  msg="Please Enter Data.")

    # 2. Fetch Data from DB
    r = requests.get(f"https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/user/users/{username}")
    j = r.json()
    user_data = j['items']

    # 3. Validate user and password combination
    # 3.1 Return Empty --> User unknown
    if user_data == []:
        return render_template("accounts/login.html", msg="Unknown user.")
    # 3.2 Password correct
    elif check_password_hash(user_data[0]['password'], password):
        session["username"] = username
        return redirect('/index.html')
    # 3.3 Password incorrect
    else:
        return render_template("accounts/login.html", msg="Wrong Password.")


# ---------------------------------------- Registration ---------------------------------------- #
@app.route("/register.html")
def register():
    return render_template("/accounts/register.html", text_register='Register:')


@app.route("/create_new_user", methods=["POST"])
def create_new_user():
    # 1. Collect the data from the form
    username = request.form["username"]
    password = request.form["password"]
    password_confirmed = request.form["password_confirmed"]

    # 2. Make Sure Email is from iberia or ie
    if 'iberia' in username or 'ie' in username:
        # 2.1 Confirm that password matches
        # 2.1.1 If match, create user in db and log user in
        if password == password_confirmed:
            hashed_password = generate_password_hash(password)
            url = "https://gede70d2b4abe6a-db202203211039.adb.eu-milan-1.oraclecloudapps.com/ords/admin/createuser/users/"
            requests.post(url, data={"username": username, "password": hashed_password})
            session["username"] = username
            return redirect('index.html')
        # 2.1.2 When password don't match, re-render and inform
        else:
            return render_template("accounts/register.html", text_register='Error: Passwords did not match')
    # 3. If Iberia or IE not in username
    else:
        return render_template("accounts/register.html", text_register='Unauthorised user')




@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
        return render_template("accounts/login.html",  msg="Bye")





if __name__ == "__main__":
    app.run("0.0.0.0", port =5000)


