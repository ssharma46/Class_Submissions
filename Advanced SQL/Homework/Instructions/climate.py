#!/usr/bin/python

# Import dependencies
import numpy as np
import pandas as pd
from datetime import datetime
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
Base = automap_base()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import inspect
from sqlalchemy import desc
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base

# Reflect the Tables
Base.prepare(engine, reflect=True)

# View classes
Base.classes.keys()

# Save references to both tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session (link) from Python to the DB
session = Session(engine)

# Setup Flask
app = Flask(__name__)

# Flask route setup
@app.route('/')
def welcome():
    return jsonify(f"Welcome to Hawaii Climate API<br/>"
                    f"------------------------------<br/>"
                    f"Available Routes:<br/>"
                    f"/api/v1.0/stations --------- List of weather observation stations<br/>"
                    f"/api/v1.0/precipitation ---------- Precipitation data from latest year<br/>"
                    f"/api/v1.0/tobs ---------- Temperature observations from latest year<br/>"
                    f"/api/v1.0/<start> ---------- Minimum temperature, Average temperature, and Maximum temperature for a given start date<br/>"
                    f"/api/v1.0/<start>/<end> ---------- Minimum temperature, Average temperature, and Maximum temperature for a given start to end range<br/>")

@app.route('/api/v1.0/stations')
def station_list():
    stations = session.query(Station.station).all()
    
    total_stations = list(np.ravel(stations))

    return jsonify(total_stations)

@app.route('/api/v1.0/precipitation')
def prcp():

    prcp_info = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= "2016-08-23", Measurement.date <= "2017-08-23").all()
    
# Create dictionary
    for _ in prcp_info:
        prcp_dict = {}
        prcp_dict["date"] = Measurement.date
        prcp_dict["precipitation"] = Measurement.prcp
    
    return jsonify(prcp_info)

@app.route('/api/v1.0/tobs')
def temp():

    temp_info = session.query(Station.name, Measurement.date, Measurement.tobs).filter(Measurement.date >= "2016-08-23", Measurement.date <= "2017-08-23").all()

    # Create dictionary
    for _ in temp_info:
        temp_dict = {}
        temp_dict["station"] = Measurement.station 
        temp_dict["temperature"] = Measurement.prcp
    return jsonify(temp_info)

@app.route('/v1.0/<start>')
def start_data(start):
    
    start_date = datetime.strptime(start, '%Y-%m-%d')

    max_t = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()
    min_t = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start_date).all()
    ave_t = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start_date).all()

    # Create dictionary
    start_dict = {}
    start_dict["Max Temp"] = max_t[0]
    start_dict["Min Temp"] = min_t[0]
    start_dict["Ave Temp"] = ave_t[0]
    
    return jsonify(start_dict)

@app.route('/v1.0/<start>/<end>')
def range_data(start, end):
    start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')

    max_rtemp = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    min_rtemp = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    ave_rtemp = session.query(func.ave(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    # Create dictionary
    range_dict = {}
    range_dict["Max Temp"] = max_rtemp[0]
    range_dict["Min Temp"] = min_rtemp[0]
    range_dict["Ave Temp"] = ave_rtemp[0]

    return jsonify(range_dict)

if __name__ == '__main__':
    app.run(debug=True)