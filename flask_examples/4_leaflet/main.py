import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

BASECOORDS = [-13.9626, 33.7741]

districts = []
points = []

class Point():
    def __init__(self, id, district, lat, lng):
        self.id = id
        self.district = district
        self.latitude_off = lat
        self.longitude_off = lng

    def __repr__(self):
        return "<Point %d: Lat %s Lng %s>" % (self.id, self.latitude_off, self.longitude_off)

    @property
    def latitude(self):
        return self.latitude_off + self.district.latitude

    @property
    def longitude(self):
        return self.longitude_off + self.district.longitude


class District():
    def __init__(self, id, name, lat, lng):
        self.id = id
        self.name = name
        self.latitude = lat
        self.longitude = lng

@app.route('/')
def index():
    global districts
    return render_template('index.html', districts=districts)


@app.route('/district/<int:district_id>')
def district(district_id):
    global points
    dist_points = [x for x in points if x.district.id == district_id]
    coords = [[point.latitude, point.longitude] for point in dist_points]
    return jsonify({"data": coords})

def make_random_data():
    global points
    global districts

    NDISTRICTS = 5
    NPOINTS = 10
    for did in range(NDISTRICTS):
        district = District(did, "District %d" % did, BASECOORDS[0], BASECOORDS[1])
        districts.append(district)
        for pid in range(NPOINTS):
            lat = random.random() - 0.5
            lng = random.random() - 0.5
            row = Point(pid + NPOINTS * did, district, lat, lng)
            points.append(row)


if __name__ == '__main__':
    make_random_data()
    app.run(debug=True)