#!/usr/bin/env python

import json
import os
import util
import service
from flask import Flask
from flask import request
from flask import make_response


# Flask app should start in global layout
app = Flask(__name__)
logger = util.get_logger()

@app.route('/chitti-api-ai-webhook', methods=['POST'])
def handle_webhook_data():
    logger.debug("Handling POST request.")
    response = "{}"
    try:
  	  request_json = request.get_json(silent=True, force=True)

  	  action = request_json.get("result").get("action")
  	  if action == "toogleLights":
              logger.info("action is toogleLights")
  	      res = service.toogle_lights(request_json)
  	  else:
  	      return {}

  	  res = json.dumps(res, indent=4)

  	  response = make_response(res)
  	  response.headers['Content-Type'] = 'application/json'
    except Exception as e:
          logger.exception("Exception while processing POST request.")
    logger.info(response)
    return response

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting chitti-webhook on port %d ..." % port

    app.run(debug=False, port=port, host='0.0.0.0')
