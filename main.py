"""
    @Author => Aman Raj
    @Encoding => UTF-8
    @File Created => 02/02/2023
"""

from modules import SentenceCheck, PreProcessor, Log
from modules import sprint, Filter, log_clear
from modules import DataBaseCreatorCleaner
from modules import path
from modules import encode, decode
from reader import Links
from flask import Response, send_file
from flask import redirect, url_for
from flask import Flask
from flask import render_template
from flask import request
from flask import flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlite3 import connect
import pandas as pd
import warnings
import json
import sys
import time
import os

# Setting up Module Handler

sys.path.append("modules/__init__.py")
sys.path.append("./reader.py")
warnings.filterwarnings('ignore')

#####################################

# Global Variables / Independent Variables

app = Flask(__name__)
app.config["SECRET_KEY"] = 'amanr@j_bose9077'
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, "database", "database.db")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

MAX_VALUE_RATE = 5
json_files = Links(directory='meta', file=['links.json', 'today.agenda.json'])
log = []

######################################################################

# Log Cleaner

log_path = os.path.join(path(os.path.abspath(os.path.dirname(__file__))), 'Data_Collecter', 'log')
# log_clear(path=log_path) # , 'system.log'

###########################################################

# DataBase Handler


class DataBase(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    text_data = db.Column(db.Text)

    def __repr__(self) -> str:
        return "<Advisor {}>".format(self.text_data[:5])

##############################################################

# Main App


@app.route('/')
def home():
    log.append(
        f"[Info] [{request.remote_addr}] [{time.asctime()}] User Visited on your Website\n")
    return render_template(r'index.html',
                           api=json_files.API,
                           github=json_files.GITHUB,
                           module=json_files.MODULE,
                           os=json_files.OS,
                           kaggle=json_files.KAGGLE,
                           Hugging_Face=json_files.HUGGING_FACE,
                           twitter=json_files.TWITTER,
                           collector="/collector",
                           home="/",
                           module_name=json_files.MODULE_NAME,
                           data="/07397d633f25a7101990a75864ae03d5a3b9ac07c4ed6accbc52cbfd7d7c13b4", about="/a4262e1c9bcbc1721eb3fe13558154460a2b2a2d307daa32532478526ce6ccb1")


@app.route('/collector', methods=['GET', 'POST'])
def collector():
    logger = Log(os.path.join(log_path, "system.log"))
    submited = ""
    if request.method == "POST":
        filters = Filter()
        verifier = SentenceCheck()
        value = request.form.get("input_text", type=str)
        for_predictor = filters.clear(value)
        verify = verifier(text=for_predictor, news=False,
                          return_dict=True)
        if int(len(value)) > int(MAX_VALUE_RATE):
            if verify['sentiment'] == True and verify['spam'] == False and verify['language'] == 'english':
                for_database = filters(value)
                if len(str(for_database)) > MAX_VALUE_RATE:
                    data = DataBase()
                    data.text_data = for_database
                    db.session.add(data)
                    db.session.commit()
                    log.append(
                        f"[Info] [{request.remote_addr}] [{time.asctime()}] DataBase OverWrited\n")
                    logger.log(log)
                else:
                    flash("Length Error")
                    log.append(
                        f"[Error] [{request.remote_addr}] [{time.asctime()}] Length Of the sentence is Too short\n")
                    logger.log(log)
            else:
                flash("Sentiment Error")
                log.append(
                    f"[Error] [{request.remote_addr}] [{time.asctime()}] Error Text Type\n")
                logger.log(log)
            return render_template(r'collector.html',
                               twitter=json_files.TWITTER,
                               github=json_files.GITHUB,
                               home="/", collector="/collector",
                               agenda=str(json_files.AGENDA_CONTENT + ".").capitalize(), Identity=submited, data="/07397d633f25a7101990a75864ae03d5a3b9ac07c4ed6accbc52cbfd7d7c13b4", time_cool_down=json_files.COOL_DOWN_TIME, about="/a4262e1c9bcbc1721eb3fe13558154460a2b2a2d307daa32532478526ce6ccb1")
        else:
            flash("It is a Result Panel More info Click `Form` navlink.")
            log.append(
                f"[Error] [{request.remote_addr}] [{time.asctime()}] First Layer Stop the Input\n")
            logger.log(log)

            redirect(url_for('collector'))

        log.append(
            f"[Info] [{request.remote_addr}] [{time.asctime()}] User Visited on your Website '/collector' \n")
        logger.close()


    elif request.method == "GET":
        log.append(
            f"[Info] [{request.remote_addr}] [{time.asctime()}] User Visited on your Website '\colledctor' \n")
        return render_template(r'collector.html', twitter=json_files.TWITTER, github=json_files.GITHUB, home="/", collector="/collector", agenda=str(json_files.AGENDA_CONTENT + ".").capitalize(), Identity=submited, data="/07397d633f25a7101990a75864ae03d5a3b9ac07c4ed6accbc52cbfd7d7c13b4", time_cool_down=json_files.COOL_DOWN_TIME, about="/a4262e1c9bcbc1721eb3fe13558154460a2b2a2d307daa32532478526ce6ccb1")


@app.route("/07397d633f25a7101990a75864ae03d5a3b9ac07c4ed6accbc52cbfd7d7c13b4")
def data():
    return render_template(r'form.html', data="/07397d633f25a7101990a75864ae03d5a3b9ac07c4ed6accbc52cbfd7d7c13b4", home="/", collector="/collector",
                           twitter=json_files.TWITTER, github=json_files.GITHUB, about="/a4262e1c9bcbc1721eb3fe13558154460a2b2a2d307daa32532478526ce6ccb1")


@app.route("/data_download", methods=['GET', 'POST'])
def data_download():
    log.append(f"[Info] [{request.remote_addr}] [{time.asctime()}] Data Download By any User")
    if request.method == "POST":
        try:
            os.mkdir(os.path.join(path(os.path.abspath(os.path.dirname(__file__))), "app", "data"))
        except Exception:
            pass

        to_csv_file = os.path.join(path(os.path.abspath(os.path.dirname(__file__))), "app", "data", "database.csv")

        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "meta", "login.secret.json"), "r") as f:
            login = json.load(f)['login']

        username = request.form.get("userPass", type=str)
        password = request.form.get("passval", type=str)
        if (username == login['username'] and password == login['password']):
            log.append(f"[Warning] UserName >> {encode(username)}, Password >> {encode(password)}".format(
            username=username, password=password))

            conn = connect(os.path.join(basedir, "database", "database.db"))
            service = pd.read_sql("SELECT * FROM data_base", conn)
            service.to_csv(to_csv_file, index=False)
            return send_file(
                to_csv_file,
                mimetype='text/csv',
                download_name='advice.csv',
                as_attachment=True
            )

        else:
            print("Response is Zero.")

        return render_template(r'data.html')
    else:
        return render_template(r'data.html')


@app.route("/a4262e1c9bcbc1721eb3fe13558154460a2b2a2d307daa32532478526ce6ccb1")
def about():
    return render_template(r'about.html', about="/a4262e1c9bcbc1721eb3fe13558154460a2b2a2d307daa32532478526ce6ccb1", data="/07397d633f25a7101990a75864ae03d5a3b9ac07c4ed6accbc52cbfd7d7c13b4", home="/", collector="/collector", twitter=json_files.TWITTER, github=json_files.GITHUB, author="Aman Raj",
    github_author_1="", twitter_author_1="")

# if __name__ == '__main__':
#     app.app_context().push()
#     db.drop_all()
#     db.create_all()
#     app.run(host="0.0.0.0", port=4000)
