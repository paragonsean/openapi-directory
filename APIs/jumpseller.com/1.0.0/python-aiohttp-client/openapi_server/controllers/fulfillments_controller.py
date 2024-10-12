from typing import List, Dict
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.fulfillment import Fulfillment
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def fulfillments_count_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Count all Fulfillments.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)


async def fulfillments_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single Fulfillment.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Fulfillment
    :type id: int

    """
    return web.Response(status=200)


async def fulfillments_json_get(request: web.Request, login, authtoken, limit=None, page=None) -> web.Response:
    """Retrieve all Fulfillments.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param limit: List restriction
    :type limit: int
    :param page: List page
    :type page: int

    """
    return web.Response(status=200)


async def order_id_fulfillments_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve the Fulfillments associated with the Order.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Order
    :type id: int

    """
    return web.Response(status=200)
