#!/usr/bin/env python
import util
import constants
from orvibo import Orvibo
bed_room_light = Orvibo('192.168.0.3')
living_room_light = Orvibo('192.168.0.4')
logger = util.get_logger()
devices_map = { "bed_room_light" : bed_room_light,
"living_room_light" : living_room_light
}

def toogle_lights(request_json):

    originalRequest = request_json.get("originalRequest")
    """ 
    To validate sender info.   
    data = originalRequest.get("data")
    sender = data.get("sender").get("id")
    if sender != "106193908059867":
      res = { 'speech' : 'You don't have access to control lights!!!' , 'displayText' : 'You don't have access to control lights!!!' }
      return res
    """
    result = request_json.get("result")
    parameters = result.get("parameters")
    actionToDo = parameters.get("lights")
    device = get_device()
    logger.info("Turning lights : "+actionToDo)
    if actionToDo == "on":
       device.on = True
    elif actionToDo == "off":
       device.on = False
    
    result = device.on
    
    if result:
       speech = constants.LIGHTS_ON_MSG
    else:
       speech = constants.LIGHTS_OFF_MSG
    
    res = {'speech' : speech, 'displayText' : speech}
    return res

def get_device():
    device = devices_map.get("bed_room_light")
    return device

