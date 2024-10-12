from typing import List, Dict
from aiohttp import web

from openapi_server.models.work_type_create_api_model import WorkTypeCreateApiModel
from openapi_server.models.work_type_delete_api_model import WorkTypeDeleteApiModel
from openapi_server.models.work_type_details_api_model import WorkTypeDetailsApiModel
from openapi_server.models.work_type_update_api_model import WorkTypeUpdateApiModel
from openapi_server import util


async def work_type_api_all(request: web.Request, x_auth_key, x_auth_secret) -> web.Response:
    """Return all work types for the account

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def work_type_api_delete(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Delete an existing work type

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = WorkTypeDeleteApiModel.from_dict(body)
    return web.Response(status=200)


async def work_type_api_details(request: web.Request, work_type_id, x_auth_key, x_auth_secret) -> web.Response:
    """Return work type details

    

    :param work_type_id: 
    :type work_type_id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def work_type_api_new(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Create a work type

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = WorkTypeCreateApiModel.from_dict(body)
    return web.Response(status=200)


async def work_type_api_search(request: web.Request, x_auth_key, x_auth_secret, query_options_query=None, query_options_order_by=None, query_options_order=None, query_options_page=None, query_options_page_size=None) -> web.Response:
    """Return all work types for the account that match the query param

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param query_options_query: 
    :type query_options_query: str
    :param query_options_order_by: 
    :type query_options_order_by: str
    :param query_options_order: 
    :type query_options_order: str
    :param query_options_page: 
    :type query_options_page: int
    :param query_options_page_size: 
    :type query_options_page_size: int

    """
    return web.Response(status=200)


async def work_type_api_update(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Update an existing work type

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = WorkTypeUpdateApiModel.from_dict(body)
    return web.Response(status=200)
