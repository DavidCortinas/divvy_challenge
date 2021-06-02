from datetime import datetime as dt
from app.api import db

class Trip(db.Model):
    trip_id = db.Column(db.Integer, index=True, primary_key=True)
    starttime = db.Column(db.DateTime, index=True)
    stoptime = db.Column(db.DateTime, index=True)
    bikeid = db.Column(db.Integer, index=True)
    from_station_id = db.Column(db.Integer, index=True)
    from_station_name = db.Column(db.String, index=True)
    to_station_id = db.Column(db.Integer, index=True)
    to_station_name = db.Column(db.String, index=True)
    usertype = db.Column(db.String, index=True)
    gender = db.Column(db.String, index=True)
    birthday = db.Column(db.String, index=True)
    trip_duration = db.Column(db.Integer, index=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

