from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.subscription_list_response import SubscriptionListResponse
from openapi_server import util


async def subscription_get(request: web.Request, current_row=None, offset=None) -> web.Response:
    """Returns a list of all reports one is currently subscribed to.

    Returns a list of all reports one is currently subscribed to. 

    :param current_row: Starting record number to return.
    :type current_row: str
    :param offset: Used to restrict the number of records returned if needed to be less than max.
    :type offset: str

    """
    return web.Response(status=200)
