from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.variable import Variable
from openapi_server.models.variable_collection import VariableCollection
from openapi_server import util


async def delete_variable(request: web.Request, variable_key) -> web.Response:
    """Delete a variable

    

    :param variable_key: The variable Key.
    :type variable_key: str

    """
    return web.Response(status=200)


async def get_variable(request: web.Request, variable_key) -> web.Response:
    """Get a variable

    Get a variable by key.

    :param variable_key: The variable Key.
    :type variable_key: str

    """
    return web.Response(status=200)


async def get_variables(request: web.Request, limit=None, offset=None, order_by=None) -> web.Response:
    """List variables

    The collection does not contain data. To get data, you must get a single entity.

    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param order_by: The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0* 
    :type order_by: str

    """
    return web.Response(status=200)


async def patch_variable(request: web.Request, variable_key, body, update_mask=None) -> web.Response:
    """Update a variable

    Update a variable by key.

    :param variable_key: The variable Key.
    :type variable_key: str
    :param body: 
    :type body: dict | bytes
    :param update_mask: The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
    :type update_mask: List[str]

    """
    body = Variable.from_dict(body)
    return web.Response(status=200)


async def post_variables(request: web.Request, body) -> web.Response:
    """Create a variable

    

    :param body: 
    :type body: dict | bytes

    """
    body = Variable.from_dict(body)
    return web.Response(status=200)
