from flask import Flask 
from flask_restful import Api , Resource
app = Flask(__name__)
api = Api(app)


class test(Resource):  
    def get(self):
        return "testing pipeline"

class test1(Resource):
    def get(self):
        return "testing python"


api.add_resource(test, '/test')
api.add_resource(test1, '/test1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)
