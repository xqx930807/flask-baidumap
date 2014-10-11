
import simplejson as json
from flask import Flask, render_template, flash, redirect
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

import config

appx = Flask(__name__)
appx.config.from_object('config')

marker_num = 2
markers = [
  {'uid':'m1', 'lng':121.481912, 'lat':31.240308},
  {'uid':'m2', 'lng':121.484700, 'lat':31.240308},
]

def db_get_markers():
    global marker_num, markers
    return markers

def db_add_markers(lng, lat):
    global marker_num, markers
    marker_num += 1
    markers.append({'uid':"m"+str(marker_num), 'lng':lng, 'lat':lat})
    print markers

@appx.route('/')
def home():
    return render_template('home.html')

@appx.route('/getmarkers', methods=['POST'])
def getmarkers():
    res = db_get_markers()
    return json.dumps(res)

@appx.route('/addmarkers', methods=['POST'])
def addmarkers():
    class MarkPos(Form):
        lng = TextField('lng', validators=[Required()])
        lat = TextField('lat', validators=[Required()])
    form = MarkPos()
    lng = float(form.lng.data)
    lat = float(form.lat.data)
    db_add_markers(lng, lat)
    return json.dumps('ok')


if __name__ == "__main__":
    appx.run(debug=True)
