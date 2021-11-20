from flask import Flask, request, jsonify

app = Flask(__name__)


import random
import time

@app.route('/api',methods = ["GET"])
def recognize():
    

    c = random.randint(1,100)
     
    d={}
    d['Query'] = str("Harsh")+str(c)
    return jsonify(d)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5758)
