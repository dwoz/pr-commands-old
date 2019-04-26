import logging
import json
import requests
import re
import os
from prcommands import *

log = logging.getLogger()
log.setLevel(logging.INFO)

def handler(event, context):
    log.error(event.keys())
    data = json.loads(event['body'])
    if data['action'] != 'created':
        log.error('Skipping action: %s', data['action'])
        return {
            'statusCode': 201,
            'body': ''
        }
    for cmd in parse_body(data['comment']['body']):
        run_cmd(cmd, data['issue']['number'])
    return {
        'statusCode': 201,
        'body': ''
    }