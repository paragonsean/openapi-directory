from typing import List, Dict
from aiohttp import web

from openapi_server.models.analytics200_response import Analytics200Response
from openapi_server import util


async def analytics(request: web.Request, start=None, end=None, label=None, subaccounts=None, group_by=None) -> web.Response:
    """analytics

    

    :param start: Start date of the statistics in the format YYYY-MM-DD. By default, the date of 30 days ago is set.
    :type start: str
    :param end: End date of the statistics in the format YYYY-MM-DD. By default, the current day.
    :type end: str
    :param label: Shows only data of a specific label.
    :type label: str
    :param subaccounts: Receive the data only for the main account, all your (sub-)accounts or only for specific subaccounts.
    :type subaccounts: str
    :param group_by: Defines the grouping of the data.
    :type group_by: str

    """
    return web.Response(status=200)
