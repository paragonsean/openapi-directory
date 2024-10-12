from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_list_default_response import ProductListDefaultResponse
from openapi_server.models.product_subscriptions_list200_response import ProductSubscriptionsList200Response
from openapi_server import util


async def product_subscriptions_list(request: web.Request, product_id, api_version, filter=None, top=None, skip=None) -> web.Response:
    """product_subscriptions_list

    Lists the collection of subscriptions to the specified product.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: | Field        | Supported operators    | Supported functions                         | |--------------|------------------------|---------------------------------------------| | id           | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | stateComment | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | userId       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | productId    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state        | eq                     |                                             |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
