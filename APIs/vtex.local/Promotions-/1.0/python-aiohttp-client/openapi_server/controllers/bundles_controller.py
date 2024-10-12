from typing import List, Dict
from aiohttp import web

from openapi_server.models.calculatediscountsandtaxes_bundles_request import CalculatediscountsandtaxesBundlesRequest
from openapi_server import util


async def calculatediscountsandtaxes_bundles(request: web.Request, content_type, accept, body) -> web.Response:
    """Calculate discounts and taxes (Bundles)

    Calculate discounts and taxes

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = CalculatediscountsandtaxesBundlesRequest.from_dict(body)
    return web.Response(status=200)
