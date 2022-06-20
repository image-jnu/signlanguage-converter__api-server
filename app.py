from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from example_data import ANIMATION_DATA

app = Flask(__name__)
api = Api(app)

def abort_if_anim_data_doesnt_exist(anim_id: str):
    if anim_id not in ANIMATION_DATA:
        abort(404, message="Animation ID: {} doesn't exist".format(anim_id))

parser = reqparse.RequestParser()

class AnimationData(Resource):
    def get(self):
        return ANIMATION_DATA

class EachAnimationData(Resource):
    def get(self, anim_id: str):
        abort_if_anim_data_doesnt_exist(anim_id)
        return ANIMATION_DATA[anim_id]


##
## Actually setup the Api resource routing here
##
api.add_resource(AnimationData, '/animation')
api.add_resource(EachAnimationData, '/animation/<anim_id>')

if __name__ == '__main__':
    app.run(debug=True)