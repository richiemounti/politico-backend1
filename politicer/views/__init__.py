from flask import request, make_response, jsonify, abort

from politicer.models.party_models import parties
from politicer.models.office_models import offices

class Views(object):
        
    @staticmethod
    def get_data():
        data = request.get_json()
        return data
    

    @staticmethod
    def destroy_lists():
        parties.clear()
        offices.clear()
        return make_response(jsonify({"message":"Done", "status" : 200}))
    
    
    
    
    