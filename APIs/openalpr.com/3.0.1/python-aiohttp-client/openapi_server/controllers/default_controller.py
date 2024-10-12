from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_config200_response import GetConfig200Response
from openapi_server.models.recognize_file200_response import RecognizeFile200Response
from openapi_server.models.recognize_file400_response import RecognizeFile400Response
from openapi_server import util


async def get_config(request: web.Request, ) -> web.Response:
    """get_config

    Get a list of available results for plate and vehicle recognition 


    """
    return web.Response(status=200)


async def recognize_bytes(request: web.Request, secret_key, country, image_bytes, recognize_vehicle=None, return_image=None, topn=None) -> web.Response:
    """recognize_bytes

    Send an image for OpenALPR to analyze and provide metadata back The image is sent as base64 encoded bytes. 

    :param secret_key: The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/ 
    :type secret_key: str
    :param country: Defines the training data used by OpenALPR.  \&quot;us\&quot; analyzes  North-American style plates.  \&quot;eu\&quot; analyzes European-style plates.  This field is required if using the \&quot;plate\&quot; task 
    :type country: str
    :param image_bytes: The image file that you wish to analyze encoded in base64 
    :type image_bytes: str
    :param recognize_vehicle: If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request 
    :type recognize_vehicle: int
    :param return_image: If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response 
    :type return_image: int
    :param topn: The number of results you would like to be returned for plate  candidates and vehicle classifications 
    :type topn: int

    """
    return web.Response(status=200)


async def recognize_file(request: web.Request, secret_key, country, image, recognize_vehicle=None, return_image=None, topn=None, is_cropped=None) -> web.Response:
    """recognize_file

    Send an image for OpenALPR to analyze and provide metadata back The image is sent as a file using a form data POST 

    :param secret_key: The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/ 
    :type secret_key: str
    :param country: Defines the training data used by OpenALPR.  \&quot;us\&quot; analyzes  North-American style plates.  \&quot;eu\&quot; analyzes European-style plates.  This field is required if using the \&quot;plate\&quot; task 
    :type country: str
    :param image: The image file that you wish to analyze 
    :type image: str
    :param recognize_vehicle: If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request 
    :type recognize_vehicle: int
    :param return_image: If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response 
    :type return_image: int
    :param topn: The number of results you would like to be returned for plate  candidates and vehicle classifications 
    :type topn: int
    :param is_cropped: When providing a plate or vehicle that is already cropped,   this performs a recognition against the full crop and does not  attempt to localize the plate/vehicle 
    :type is_cropped: int

    """
    return web.Response(status=200)


async def recognize_url(request: web.Request, image_url, secret_key, country, recognize_vehicle=None, return_image=None, topn=None) -> web.Response:
    """recognize_url

    Send an image for OpenALPR to analyze and provide metadata back The image is sent as a URL.  The OpenALPR service will download the image  and process it 

    :param image_url: A URL to an image that you wish to analyze 
    :type image_url: str
    :param secret_key: The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/ 
    :type secret_key: str
    :param country: Defines the training data used by OpenALPR.  \&quot;us\&quot; analyzes  North-American style plates.  \&quot;eu\&quot; analyzes European-style plates.  This field is required if using the \&quot;plate\&quot; task 
    :type country: str
    :param recognize_vehicle: If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request 
    :type recognize_vehicle: int
    :param return_image: If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response 
    :type return_image: int
    :param topn: The number of results you would like to be returned for plate  candidates and vehicle classifications 
    :type topn: int

    """
    return web.Response(status=200)
