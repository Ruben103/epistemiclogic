from flask import Flask, request
from flask_restful import Resource, Api
import time
from main import playGame

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'DateTime': time.time()}


api.add_resource(HelloWorld, '/')
api.add_resource(playGame, '/start')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
