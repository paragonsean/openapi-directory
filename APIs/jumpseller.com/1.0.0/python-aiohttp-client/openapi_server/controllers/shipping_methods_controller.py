from typing import List, Dict
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.shipping_method import ShippingMethod
from openapi_server.models.shipping_method_edit import ShippingMethodEdit
from openapi_server import util


async def shipping_methods_id_json_delete(request: web.Request, login, authtoken, id) -> web.Response:
    """Delete an existing Shipping Method.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Shipping Method
    :type id: int

    """
    return web.Response(status=200)


async def shipping_methods_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single Shipping Method.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Shipping Method
    :type id: int

    """
    return web.Response(status=200)


async def shipping_methods_id_json_put(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Update a Shipping Method.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Shipping Method
    :type id: int
    :param body: Shipping Method parameters.
    :type body: dict | bytes

    """
    body = ShippingMethodEdit.from_dict(body)
    return web.Response(status=200)


async def shipping_methods_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Retrieve all Store&#39;s Shipping Methods.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)


async def shipping_methods_json_post(request: web.Request, login, authtoken, body) -> web.Response:
    """Creates a Shipping Method.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: Shipping Method parameters.
    :type body: dict | bytes

    """
    body = ShippingMethodEdit.from_dict(body)
    return web.Response(status=200)
