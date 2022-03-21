# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import sys
import gc
import imp 
import json
from botbuilder.schema import Activity
from botbuilder.applicationinsights.django import retrieve_bot_body

class IntegrationPostData:
    """ 
    Retrieve the POST body from the underlying framework:
    - Flask
    - Django
    - (soon Tornado?)

    This class:
    - Detects framework (currently flask or django)
    - Pulls the current request body as a string
    
    Usage:
      botdata = BotTelemetryData()
      body = botdata.activity_json  # Get current request body as json object
      activity_id = body[id] # Get the ID from the POST body
    """
    def __init__(self):
        pass

    @property
    def activity_json(self) -> json:
        body_text = self.get_request_body()
        return json.loads(body_text) if body_text != None else None
    
    def get_request_body(self) -> str:
        if self.detect_flask():
            flask_app = self.get_flask_app()
            
            with flask_app.app_context():
                mod = __import__('flask', fromlist=['Flask'])
                request = getattr(mod, 'request')
                body = self.body_from_WSGI_environ(request.environ)
            return body
        else:
            if self.detect_django():
                # Retrieve from Middleware cache
                return retrieve_bot_body()

    def body_from_WSGI_environ(self, environ):
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        return environ['wsgi.input'].read(request_body_size)

    def detect_flask(self) -> bool:
        return "flask" in sys.modules

    def detect_django(self) -> bool:
        return "django" in sys.modules

    def resolve_flask_type(self) -> 'Flask':
        mod = __import__('flask', fromlist=['Flask'])
        return getattr(mod, 'Flask')

    def get_flask_app(self) -> 'Flask':
        flask = [o for o in gc.get_objects() if isinstance(o, self.resolve_flask_type())]
        flask_instances = len(flask)
        if flask_instances <= 0 or flask_instances > 1:
            raise Exception(f'Detected {flask_instances} instances of flask.  Expecting 1.')
        return flask[0]