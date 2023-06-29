from __future__ import absolute_import
from flask import Flask, g, request, jsonify, json, Response
import traceback
#from cnvrg import Endpoint
from multiprocessing import Value
import subprocess
import time
from time import gmtime, strftime
import datetime
import sys
import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info('AFTER LOAD')

import os
import sys

app = Flask(__name__)

try:
    with app.app_context():
        #PREPROCESS_IMPORT#
        #PREPROCESS_IMPORT_PATH#
        import predict
        #IMPORT_PATH#
except Exception as e:
    print("ERROR " + str(e) + "\\n" + traceback.format_exc().replace("\n","\\n"))
    exit(1)
import io
import base64
import uuid

print("Server started")
sys.stdout.flush()
def verify_access(api_key):
    try:
        access_key = 'P7CTEuTNKSrhJ3D2cTyqxePW'
        if access_key == api_key:
            return True
        else:
            return False

    except Exception as e:
        return jsonify(status_code='500', msg='Internal server error: can not verify request'), 500

@app.route('/metrics', methods=['GET'])
def metrics():
    return Response("", mimetype='text/plain')

@app.errorhandler(401)
def unauthorized():
    return jsonify(error_code='401', msg='You are not Authorized'), 401

@app.route('/api', methods=['POST'])
def run():
    print("In run")
    try:
        start_time = time.time()
        ip = request.remote_addr
        auth = request.headers.get('Cnvrg-Api-Key', None)
        if verify_access(auth):
            #endpoint = Endpoint()
            #endpoint.log_error("Unauthorized", trace=True)
            return unauthorized()
        input_params = []
        original_input_params = []
        try:
            data = request.get_json(force=True)
            if "input_params" in data:
                original_input_params = request.get_json(force=True, cache=False)['input_params']
                input_params = data['input_params']
                if isinstance(input_params, list):

                    if not isinstance(input_params, list):
                        input_params = [input_params]
                    result =  predict.predict(*input_params)
                else:

                    result =  predict.predict(input_params)
#                 result = str(result)
            if "data" in data:
                input_data = data["data"]
                data_base = base64.b64decode(input_data)
                file_path = "/tmp/" + str(uuid.uuid4())
                f = open(file_path, 'wb')
                f.write(data_base)
                f.close()
                result =  predict.predict(file_path)
#                 result = str(result)
                os.remove(file_path)

        except Exception as e:
            #endpoint = Endpoint()
            #endpoint.log_error(e, trace=True)
            return jsonify({'error': str(e), 'stacktrace':traceback.format_exc()}), 500
        end_time = time.time()
        elapsed_time = int((end_time - start_time) * 1000)  # ms
        log = {
         "input": str(original_input_params),
         "model": "3",
         "job_id": "n5jzic1zrdznytozmfhx",
         "job_type": "Endpoint",
         "output": str(result),
         "elapsed_time": elapsed_time,
         "start_time": str(datetime.datetime.utcfromtimestamp(int(start_time)))
        }
        print("{}".format(json.dumps(log)))
        sys.stdout.flush()
      #  endpoint = Endpoint()
       # endpoint.log_request(input_params=original_input_params, result=result, start_time=start_time)
        return jsonify({'prediction': result})
    except Exception as e:
      #  endpoint.log_error(e, trace=True)
        return jsonify({'error': str(e), 'stacktrace':traceback.format_exc()}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
