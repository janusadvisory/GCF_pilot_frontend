from flask import Flask, request, jsonify
from flask_cors import CORS
# import pandas as pd
import sys
# from score_prop import score_proposal
from score_section import score_section

#Set up Flask:
app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

#Set up Flask to bypass CORS at the front end:
cors = CORS(app,resources={
    r"/*":{
        "origins" : "*"
    }
})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/scoreSection',methods=['POST','GET'])
def score_p():
    if request.method == 'POST':
        data = request.get_json()
        response = score_section(data['text'])
        re = jsonify(response)
        return re

if __name__ == "__main__":
 app.run(port=5000,host='0.0.0.0')
