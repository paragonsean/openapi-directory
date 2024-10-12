from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_get_application_api_usage200_response import AppGetApplicationApiUsage200Response
from openapi_server.models.app_get_bungie_applications200_response import AppGetBungieApplications200Response
from openapi_server import util


async def app_get_application_api_usage(request: web.Request, application_id, end=None, start=None) -> web.Response:
    """app_get_application_api_usage

    Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.

    :param application_id: ID of the application to get usage statistics.
    :type application_id: int
    :param end: End time for query. Goes to now if not specified.
    :type end: str
    :param start: Start time for query. Goes to 24 hours ago if not specified.
    :type start: str

    """
    end = util.deserialize_datetime(end)
    start = util.deserialize_datetime(start)
    return web.Response(status=200)


async def app_get_bungie_applications(request: web.Request, ) -> web.Response:
    """app_get_bungie_applications

    Get list of applications created by Bungie.


    """
    return web.Response(status=200)
