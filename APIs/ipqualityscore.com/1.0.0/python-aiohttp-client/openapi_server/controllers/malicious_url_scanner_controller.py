from typing import List, Dict
from aiohttp import web

from openapi_server.models.email_validation400_response import EmailValidation400Response
from openapi_server.models.malicious_url_scanner200_response import MaliciousUrlScanner200Response
from openapi_server import util


async def malicious_url_scanner(request: web.Request, your_api_key_here, url_here) -> web.Response:
    """Malicious URL Scanner

    Malicious URL Scanner

    :param your_api_key_here: (Required) YOUR_API_KEY_HERE
    :type your_api_key_here: str
    :param url_here: (Required) URL_HERE
    :type url_here: str

    """
    return web.Response(status=200)
