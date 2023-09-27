from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .algorithms.key_generation import generate_rsa_keys
import json
import requests


# Create your views here.
@api_view(["POST"])
def elector_keygen(request):
    # converting request body to dict
    clear_dict = JSONParser().parse(request)

    # generating rsa keys
    clear_dict["private_key"], clear_dict["public_key"] = generate_rsa_keys()

    # creating json body without private key for elector commission service
    post_data = json.dumps({i: clear_dict[i] for i in clear_dict if i != 'private_key'})

    # sending post request to elector commission service
    requests.post("http://0.0.0.0:8000/elector_commission/", post_data)

    # returning private and public key attached to passport id back to election portal
    return Response(json.dumps(clear_dict))
