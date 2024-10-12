from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_failed import AuthFailed
from openapi_server.models.rate_limit import RateLimit
from openapi_server.models.remove_bg_json import RemoveBgJson
from openapi_server.models.remove_bg_json_response import RemoveBgJsonResponse
from openapi_server.models.remove_bg_multipart import RemoveBgMultipart
from openapi_server.models.removebg_post400_response import RemovebgPost400Response
from openapi_server.models.removebg_post402_response import RemovebgPost402Response
from openapi_server import util


async def removebg_post(request: web.Request, body) -> web.Response:
    """Remove the background of an image

    Removes the background of a JPG/PNG image.  * File size: up to 12 MB * Image source: File upload (binary or as base64 encoded string) or download from URL * Image Content: Any photo with a foreground [(e.g. people, products, animals, cars, etc.)](/supported-images) * Output resolutions available: Preview (up to 0.25 megapixels), Full (up to 25 megapixels)  Requires either an API Key to be provided in the &#x60;X-API-Key&#x60; request header or an OAuth 2.0 access token to be provided in the &#x60;Authorization&#x60; request header. 

    :param body: 
    :type body: dict | bytes

    """
    body = RemoveBgJson.from_dict(body)
    return web.Response(status=200)
