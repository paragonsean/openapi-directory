from typing import List, Dict
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.tax import Tax
from openapi_server.models.tax_edit import TaxEdit
from openapi_server import util


async def taxes_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single Tax information.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Tax
    :type id: int

    """
    return web.Response(status=200)


async def taxes_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Retrieve all Taxes.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)


async def taxes_json_post(request: web.Request, login, authtoken, body) -> web.Response:
    """Create a new Tax.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: Tax parameters.
    :type body: dict | bytes

    """
    body = TaxEdit.from_dict(body)
    return web.Response(status=200)
