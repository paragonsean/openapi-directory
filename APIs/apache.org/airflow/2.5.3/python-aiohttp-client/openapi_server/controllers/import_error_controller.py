from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.import_error import ImportError
from openapi_server.models.import_error_collection import ImportErrorCollection
from openapi_server import util


async def get_import_error(request: web.Request, import_error_id) -> web.Response:
    """Get an import error

    

    :param import_error_id: The import error ID.
    :type import_error_id: int

    """
    return web.Response(status=200)


async def get_import_errors(request: web.Request, limit=None, offset=None, order_by=None) -> web.Response:
    """List import errors

    

    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param order_by: The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0* 
    :type order_by: str

    """
    return web.Response(status=200)
