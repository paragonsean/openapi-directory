from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_error import BadRequestError
from openapi_server.models.json_payload import JsonPayload
from openapi_server.models.receipt_result import ReceiptResult
from openapi_server.models.receipt_verbose_result import ReceiptVerboseResult
from openapi_server.models.url_payload import UrlPayload
from openapi_server import util


async def post_api_receipt_v1_simple_encoded(request: web.Request, apikey, body=None) -> web.Response:
    """transcribe a receipt using base64 encoded image in json payload

    

    :param apikey: API authentication key.
    :type apikey: str
    :param body: 
    :type body: dict | bytes

    """
    body = JsonPayload.from_dict(body)
    return web.Response(status=200)


async def post_api_receipt_v1_simple_url(request: web.Request, apikey, body=None) -> web.Response:
    """transcribe a receipt from URL

    

    :param apikey: API authentication key.
    :type apikey: str
    :param body: 
    :type body: dict | bytes

    """
    body = UrlPayload.from_dict(body)
    return web.Response(status=200)


async def post_api_receipt_v1_verbose_encoded(request: web.Request, apikey, body=None) -> web.Response:
    """transcribe a receipt using base64 encoded image in json payload and return detailed result

    

    :param apikey: API authentication key.
    :type apikey: str
    :param body: 
    :type body: dict | bytes

    """
    body = JsonPayload.from_dict(body)
    return web.Response(status=200)


async def post_api_receipt_v1_verbose_url(request: web.Request, apikey, body=None) -> web.Response:
    """transcribe a receipt from URL and return detailed result

    

    :param apikey: API authentication key.
    :type apikey: str
    :param body: 
    :type body: dict | bytes

    """
    body = UrlPayload.from_dict(body)
    return web.Response(status=200)
