from typing import List, Dict
from aiohttp import web

from openapi_server.models.tax_create_api_model import TaxCreateApiModel
from openapi_server.models.tax_delete_api_model import TaxDeleteApiModel
from openapi_server.models.tax_details_api_model import TaxDetailsApiModel
from openapi_server.models.tax_update_api_model import TaxUpdateApiModel
from openapi_server import util


async def tax_api_all(request: web.Request, x_auth_key, x_auth_secret) -> web.Response:
    """Return all taxes for the account

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def tax_api_delete(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Delete an existing tax

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = TaxDeleteApiModel.from_dict(body)
    return web.Response(status=200)


async def tax_api_new(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Create a tax

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = TaxCreateApiModel.from_dict(body)
    return web.Response(status=200)


async def tax_api_update(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Update an existing tax

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = TaxUpdateApiModel.from_dict(body)
    return web.Response(status=200)
