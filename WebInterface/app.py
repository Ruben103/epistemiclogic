from flask import Flask
from flask_restful import Resource, Api
import time

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'DateTime': time.time()}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
