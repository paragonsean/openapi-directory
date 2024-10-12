from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.pool import Pool
from openapi_server.models.pool_collection import PoolCollection
from openapi_server import util


async def delete_pool(request: web.Request, pool_name) -> web.Response:
    """Delete a pool

    

    :param pool_name: The pool name.
    :type pool_name: str

    """
    return web.Response(status=200)


async def get_pool(request: web.Request, pool_name) -> web.Response:
    """Get a pool

    

    :param pool_name: The pool name.
    :type pool_name: str

    """
    return web.Response(status=200)


async def get_pools(request: web.Request, limit=None, offset=None, order_by=None) -> web.Response:
    """List pools

    

    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param order_by: The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0* 
    :type order_by: str

    """
    return web.Response(status=200)


async def patch_pool(request: web.Request, pool_name, body, update_mask=None) -> web.Response:
    """Update a pool

    

    :param pool_name: The pool name.
    :type pool_name: str
    :param body: 
    :type body: dict | bytes
    :param update_mask: The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
    :type update_mask: List[str]

    """
    body = Pool.from_dict(body)
    return web.Response(status=200)


async def post_pool(request: web.Request, body) -> web.Response:
    """Create a pool

    

    :param body: 
    :type body: dict | bytes

    """
    body = Pool.from_dict(body)
    return web.Response(status=200)
