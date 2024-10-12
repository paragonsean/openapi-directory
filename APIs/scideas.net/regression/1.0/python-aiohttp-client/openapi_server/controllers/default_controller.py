from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_response200 import InlineResponse200
from openapi_server.models.regression_api_body import RegressionApiBody
from openapi_server import util


async def regression_api_post(request: web.Request, body) -> web.Response:
    """Returns regression analysis.

    

    :param body: 
    :type body: dict | bytes

    """
    body = RegressionApiBody.from_dict(body)
    return web.Response(status=200)
