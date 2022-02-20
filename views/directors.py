from flask_restx import Resource, Namespace
from models import Director, DirectorSchema
from setup_db import db

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        result = db.session.query(Director).all()
        res = DirectorSchema(many=True).dump(result)
        return res, 200


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        result_director = db.session.query(Director).get(rid)
        ready_director = DirectorSchema().dump(result_director)
        return ready_director, 200