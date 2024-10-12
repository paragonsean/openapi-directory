from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_api_create_or_update200_response import ProductApiCreateOrUpdate200Response
from openapi_server.models.product_api_list_by_product200_response import ProductApiListByProduct200Response
from openapi_server.models.product_list_default_response import ProductListDefaultResponse
from openapi_server import util


async def product_api_create_or_update(request: web.Request, product_id, api_id, api_version) -> web.Response:
    """product_api_create_or_update

    Adds an API to the specified product.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def product_api_delete(request: web.Request, product_id, api_id, api_version) -> web.Response:
    """product_api_delete

    Deletes the specified API from the specified product.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def product_api_list_by_product(request: web.Request, product_id, api_version, filter=None, top=None, skip=None) -> web.Response:
    """product_api_list_by_product

    Lists a collection of the APIs associated with a product.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | serviceUrl  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | path        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | 
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
