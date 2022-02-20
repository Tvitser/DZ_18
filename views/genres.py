from flask_restx import Resource, Namespace

from models import Genre, GenreSchema
from setup_db import db

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        result = db.session.query(Genre).all()
        res = GenreSchema(many=True).dump(result)
        return res, 200


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        Genre_result = db.session.query(Genre).get(rid)
        Genre_ready = GenreSchema().dump(Genre_result)
        return Genre_ready, 200