from flask import Flask, render_template, request, redirect, session
from bson.objectid import ObjectId
from pymodm.connection import connect
from pymongo.write_concern import WriteConcern
from pymodm import EmbeddedMongoModel, MongoModel, fields
import datetime
import uuid

from app_models import User, Equipment, Error, Failure, Repair

SECRET_KEY = str(uuid.uuid4())
app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/')
def index():
    User('worker', '1', 'worker').save()
    User('repair_manager', '1', 'repair_manager').save()
    User('site_manager', '1', 'site_manager').save()
    User('foreman', '1', 'foreman').save()
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        try:
            user = User.objects.get({'_id': request.form['loginIn'], 'password': request.form['passwordIn']})
        except User.DoesNotExist:
            return render_template('login.html', error='Bad email or password')
        else:
            session['user'] = user.login
        return redirect(user.role)

@app.route('/worker', methods=['GET', 'POST'])
def worker():
    if request.method == 'GET':
        for repair in Repair.objects.all(): #iterator?
            repair.delete()
        Repair(datetime.datetime.now(), 3, "rep_5", "Small repair", False, False).save()
        Repair(datetime.datetime.now(), 2, "rep_4", "Wonderful repair", False, False).save()
        Repair(datetime.datetime.now(), 1, "rep_777", "Cute repair", False, False).save()
        Repair(datetime.datetime.now(), 3, "rep_333", "I wanna live", False, False).save()
        Repair(datetime.datetime.now(), 2, "rep_222", "I am tired of writing descriptions", False, True).save()
        Repair(datetime.datetime.now(), 1, "rep_123", "Ok?", False, True).save()
        return render_template('worker.html', Repair=Repair)
    else:
        repID = request.form.get('ID')
        repair = Repair.objects.get({'_id':  ObjectId(repID)})
        if request.form[repID] == '0':
            repair.completed = False
            repair.in_progress = False
        elif request.form[repID] == '1':
            repair.in_progress = True
        else:
            repair.completed = True
        repair.save()
        return render_template('worker.html', Repair=Repair)


@app.route('/site')
def site():
    # Example of some data
    for eq in Equipment.objects.all(): # Deleting old data...
        eq.delete()
    eq1 = Equipment(machineID=1, model='MODEL1').save()
    eq2 = Equipment(machineID=2, model='MODEL5').save()
    eq1.errors.append(Error(time=datetime.datetime.now(), etype="WRONG_INPUT", description="ERROR1"))
    eq1.errors.append(Error(time=datetime.datetime.now(), etype="OUT_OF_TIME", description="ERROR4"))
    eq1.failures.append(Failure(time=datetime.datetime.now(), ftype="OVERPOWER", description="FAILURETYPE5"))
    eq1.failures.append(Failure(time=datetime.datetime.now(), ftype="POWER_LOSS", description="FAILURETYPE2"))
    eq2.errors.append(Error(time=datetime.datetime.now(), etype="unknown", description="MYSTERY"))
    eq1.save()
    eq2.save()
    Equipment(machineID=3, model='NOERR').save()
    Equipment(machineID=4, model='NOERR').save()
    # Created 2 Equipments with some errors and 2 Equipments without
    return render_template('site_manager.html', Equipment=Equipment)

@app.route('/repair')
def repair():
    return render_template('repair_manager.html')

@app.route('/foreman')
def foreman():
    return render_template('foreman.html') 

@app.route('/clear')
def clear():
    for eq in Equipment.objects.all(): # Deleting old data...
        eq.delete()
    for repair in Repair.objects.all(): #iterator?
        repair.delete()
    return 'Deleted!'