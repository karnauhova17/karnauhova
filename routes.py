from flask import Blueprint, jsonify

from models import db, TrainingType, Visit

index = Blueprint('index', __name__,url_prefix='/')
api = Blueprint('api', __name__,url_prefix='/api')


@api.route('/trainingtypes')
def get_trainingtypes():
    return jsonify([(lambda men: men.json())(men) for men in TrainingType.query.all()])


@api.route('/visits')
def get_visits():
    return jsonify([(lambda visit: visit.json())(visit) for visit in Visit.query.all()])
