#!/usr/bin/env python

import logging

logger = logging.getLogger('chitti-webhook')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler = logging.FileHandler('chitti-webhook.log')
handler.setFormatter(formatter)
logger.addHandler(handler) 
logger.setLevel(logging.DEBUG)

def get_logger():
    return logger
