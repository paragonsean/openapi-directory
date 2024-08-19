from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.gas_weekly_list_response import GasWeeklyListResponse
from openapi_server import util


async def gasweekly_get(request: web.Request, current_row=None, offset=None) -> web.Response:
    """Returns the weekly gasoline report. This resource pulls back the report with ProductLine &#x3D; \&quot;US Weekly Gasoline Demand Report\&quot;. Keep in mind that you must be subscribed to the gasoline weekly report to be able to receive data back from this resource.

    Returns the weekly gasoline report. This resource pulls back the report with ProductLine &#x3D; \&quot;US Weekly Gasoline Demand Report\&quot;. Keep in mind that you must be subscribed to the gasoline weekly report to be able to receive data back from this resource. 

    :param current_row: Starting record number to return.
    :type current_row: str
    :param offset: Used to restrict the number of records returned if needed to be less than max.
    :type offset: str

    """
    return web.Response(status=200)
