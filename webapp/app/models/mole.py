from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from geopy.geocoders import OpenMapQuest
from enum import Enum
from datetime import datetime

from config import Config
from .user import User
from .. import db

geolocator = OpenMapQuest(api_key=Config.OPENMAP_KEY)

def get_suburb_state(latitude, longitude):
    try:
        location = geolocator.reverse("{}, {}".format(latitude, longitude))
        return (location.raw['address']['suburb'], location.raw['address']['state'])
    except:
        return ("NA", "NA")

class Sex(Enum):
    FEMALE = 1
    MALE = 2
    OTHER = 3
    NA = 4

class Ancestry:
  values = []

class BodyLocation():
    defaults = ["We're going to use Leaflet.JS", "With a custom map of avatar bodies", "I promise we're working on it!"]

class Mole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sex = db.Column(db.Integer)
    age = db.Column(db.Integer)
    body_location = db.Column(db.String(32))
    geo_long = db.Column(db.String(32))
    geo_lat = db.Column(db.String(32))
    geo_suburb = db.Column(db.String(32))
    geo_state = db.Column(db.String(16))
    image_path = db.Column(db.String(64))
    pathology = db.Column(db.String(2048))
    date_submitted = db.Column(db.String(16))

    def __init__(self, **kwargs):
        super(Mole, self).__init__(**kwargs)
        if self.geo_suburb is None and self.geo_lat and self.geo_long:
            location = get_suburb_state(self.geo_lat, self.geo_long)
            self.geo_suburb, self.geo_state = location
        if self.date_submitted is None:
            self.date_submitted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def generate_fake(count=100, **kwargs):
        """Generate a number of fake moles for testing."""
        from sqlalchemy.exc import IntegrityError
        from faker import Faker
        import geopandas as gpd
        from shapely.geometry import Point
        import random, glob, os
        from datetime import timedelta

        random.seed()
        fake = Faker()
        users = User.query.all()

        example_pics= []
        for example in glob.glob("app/static/uploads/examples/*.jpg"):
            example_pics.append(example.replace("app/static/", ""))

        path_word_list = [
        'skin','lesion','cancer',
        'mole','melanome','malignant',
        'upper','lower','back',
        'arm','leg','irregular','face' ]

        def random_date(start, end):
            delta = end - start
            int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
            random_second = random.randrange(int_delta)
            return start + timedelta(seconds=random_second)

        d1 = datetime.strptime('20/9/2019 6:30 PM', '%d/%m/%Y %I:%M %p')
        d2 = datetime.strptime('22/9/2019 4:50 PM', '%d/%m/%Y %I:%M %p')

        aus = gpd.read_file("geojson/australian-states.json")

        def random_points_in_geodf(number, geodf):
            points = []
            i= 0
            while i < number:
                polygon = geodf.iloc[random.randint(0, len(geodf)-1)].geometry
                min_x, min_y, max_x, max_y = polygon.bounds
                point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
                if polygon.contains(point) and get_suburb_state(point.y, point.x) != ("NA", "NA"):
                    points.append(point)
                    i += 1
            return points

        points = random_points_in_geodf(count, aus)

        for i in range(count):
            m = Mole(
                user_id=random.choice(users).id,
                sex=random.randint(1, len(Sex)),
                age=random.randint(18, 100),
                body_location=random.choice(BodyLocation.defaults),
                geo_lat=str(points[i].y),
                geo_long=str(points[i].x),
                image_path=random.choice(example_pics),
                pathology=fake.sentence(ext_word_list=path_word_list),
                date_submitted=str(random_date(d1, d2)),
                **kwargs)
            db.session.add(m)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

    def update_pathology(self, token):
        """Update pathology information for this mole."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except (BadSignature, SignatureExpired):
            return False
        if data.get('update_pathology') != self.id:
            return False
        new_pathology = data.get('new_pathology')
        if new_pathology is None:
            new_pathology = ""
        self.pathology = new_pathology
        db.session.add(self)
        db.session.commit()
        return True