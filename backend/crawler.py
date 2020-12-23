from newspaper import Article
from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS, cross_origin
import os
import json
import requests
app = Flask(__name__)
api = Api(app)
CORS(app)
from sumnews import *



class receiveurl(Resource):
    
    @cross_origin()
    def post(self):
        res = json.loads(request.data.decode('utf-8'))
        data = self.crawl(res['url'])
        # print(res['request'],type(res))
        process = {}
        process['knn'] = knn_model(data)
        process['kmean'] = kmean_model(data)
        return jsonify(process)
    @cross_origin()
    def options(self):
        pass

    def crawl(self,url):
        url = url
        art = Article(url)
        art.download()
        art.parse()
        return art.text


api.add_resource(receiveurl, '/api', endpoint='api')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)
