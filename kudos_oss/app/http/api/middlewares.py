from functools import wraps
from flask import request, g, abort
from jwt import decode, exceptions
import json

def login_required(f):
    @wraps(f) # Q: What is this "@" symbol for?
    def wrap(*args, **kwargs):
        authorization = request.headers.get("authorization", None)
        if not authorization:
            return json.dumps({'error': 'no authorization token provided'}), 403, {'Content-type': 'application/json'}

        try:
            token = authorization.split(' ')[1]
            resp = decode(token, None, verify=False, algorithms=['HS256']) # Decodes authorization token
            g.user = resp['sub'] # Q: What is "g"? A: "g" is a global context shared across request life cycle; Q: What is 'sub'?
        except exceptions.DecodeError as identifier: # Q: Why "identifier"?
            return json.dumps({'error': 'invalid authorization token'}), 403, {'Content-type': 'application/json'}

        return f(*args, **kwargs)

    return wrap
