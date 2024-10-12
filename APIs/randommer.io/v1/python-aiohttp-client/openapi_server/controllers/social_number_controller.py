from typing import List, Dict
from aiohttp import web

from openapi_server.models.id_type import IdType
from openapi_server.models.number_validation import NumberValidation
from openapi_server import util


async def api_social_number_get(request: web.Request, x_api_key=None) -> web.Response:
    """Generate a social security number

    

    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_social_number_post(request: web.Request, id_type, body, x_api_key=None) -> web.Response:
    """Validate VAT/identity numbers

    

    :param id_type: 
    :type id_type: dict | bytes
    :param body: 
    :type body: dict | bytes
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    id_type = .from_dict(id_type)
    body = NumberValidation.from_dict(body)
    return web.Response(status=200)
