from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.parameter_list_response import ParameterListResponse
from openapi_server import util


async def parameters_get(request: web.Request, current_row=None, offset=None) -> web.Response:
    """Returns a distinct list of all reports are available and that one is subscribed to.

    Returns a distinct list of all reports are available and that one is subscribed to. 

    :param current_row: Starting record number to return.
    :type current_row: str
    :param offset: Used to restrict the number of records returned if needed to be less than max.
    :type offset: str

    """
    return web.Response(status=200)
