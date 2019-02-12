import os

from flask import Flask
from politicer.views import party, office
from politicer.models import party_models, office_models
from instance.config import configs

def create_app(test_config):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(
        
        configs['production']
    )

    if test_config:
        app.config.from_object(configs['testing'])
        
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(party.bp)
    app.register_blueprint(office.bp)
    return app

   
    