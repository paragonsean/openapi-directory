from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection import Connection
from openapi_server.models.connection_collection import ConnectionCollection
from openapi_server.models.connection_test import ConnectionTest
from openapi_server.models.error import Error
from openapi_server import util


async def delete_connection(request: web.Request, connection_id) -> web.Response:
    """Delete a connection

    

    :param connection_id: The connection ID.
    :type connection_id: str

    """
    return web.Response(status=200)


async def get_connection(request: web.Request, connection_id) -> web.Response:
    """Get a connection

    

    :param connection_id: The connection ID.
    :type connection_id: str

    """
    return web.Response(status=200)


async def get_connections(request: web.Request, limit=None, offset=None, order_by=None) -> web.Response:
    """List connections

    

    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param order_by: The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0* 
    :type order_by: str

    """
    return web.Response(status=200)


async def patch_connection(request: web.Request, connection_id, body, update_mask=None) -> web.Response:
    """Update a connection

    

    :param connection_id: The connection ID.
    :type connection_id: str
    :param body: 
    :type body: dict | bytes
    :param update_mask: The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
    :type update_mask: List[str]

    """
    body = Connection.from_dict(body)
    return web.Response(status=200)


async def post_connection(request: web.Request, body) -> web.Response:
    """Create a connection

    

    :param body: 
    :type body: dict | bytes

    """
    body = Connection.from_dict(body)
    return web.Response(status=200)


async def test_connection(request: web.Request, body) -> web.Response:
    """Test a connection

    Test a connection.  *New in version 2.2.0* 

    :param body: 
    :type body: dict | bytes

    """
    body = Connection.from_dict(body)
    return web.Response(status=200)
