from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_collection import ProductCollection
from openapi_server.models.product_contract import ProductContract
from openapi_server.models.product_list_default_response import ProductListDefaultResponse
from openapi_server.models.product_update_parameters import ProductUpdateParameters
from openapi_server import util


async def product_create_or_update(request: web.Request, product_id, api_version, parameters) -> web.Response:
    """product_create_or_update

    Creates or Updates a product.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Create or update parameters.
    :type parameters: dict | bytes

    """
    parameters = ProductContract.from_dict(parameters)
    return web.Response(status=200)


async def product_delete(request: web.Request, product_id, if_match, api_version, delete_subscriptions=None) -> web.Response:
    """product_delete

    Delete product.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param if_match: ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param delete_subscriptions: Delete existing subscriptions to the product or not.
    :type delete_subscriptions: bool

    """
    return web.Response(status=200)


async def product_get(request: web.Request, product_id, api_version) -> web.Response:
    """product_get

    Gets the details of the product specified by its identifier.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def product_list(request: web.Request, api_version, filter=None, top=None, skip=None, expand_groups=None) -> web.Response:
    """product_list

    Lists a collection of products in the specified service instance.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | terms       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state       | eq                     |                                             |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param expand_groups: When set to true, the response contains an array of groups that have visibility to the product. The default is false.
    :type expand_groups: bool

    """
    return web.Response(status=200)


async def product_update(request: web.Request, product_id, if_match, api_version, parameters) -> web.Response:
    """product_update

    Update product.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param if_match: ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = ProductUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
