from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_group_create_or_update200_response import ProductGroupCreateOrUpdate200Response
from openapi_server.models.product_group_list_by_product200_response import ProductGroupListByProduct200Response
from openapi_server.models.product_list_default_response import ProductListDefaultResponse
from openapi_server import util


async def product_group_create_or_update(request: web.Request, product_id, group_id, api_version) -> web.Response:
    """product_group_create_or_update

    Adds the association between the specified developer group with the specified product.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def product_group_delete(request: web.Request, product_id, group_id, api_version) -> web.Response:
    """product_group_delete

    Deletes the association between the specified group and product.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def product_group_list_by_product(request: web.Request, product_id, api_version, filter=None, top=None, skip=None) -> web.Response:
    """product_group_list_by_product

    Lists the collection of developer groups associated with the specified product.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | type        | eq, ne                 | N/A                                         |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
