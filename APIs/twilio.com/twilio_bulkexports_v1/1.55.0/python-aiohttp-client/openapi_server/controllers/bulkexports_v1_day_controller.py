from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulkexports_v1_export_day_instance import BulkexportsV1ExportDayInstance
from openapi_server.models.list_day_response import ListDayResponse
from openapi_server import util


async def fetch_day(request: web.Request, resource_type, day) -> web.Response:
    """fetch_day

    Fetch a specific Day.

    :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants
    :type resource_type: str
    :param day: The ISO 8601 format date of the resources in the file, for a UTC day
    :type day: str

    """
    return web.Response(status=200)


async def list_day(request: web.Request, resource_type, page_size=None, page=None, page_token=None) -> web.Response:
    """list_day

    Retrieve a list of all Days for a resource.

    :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants
    :type resource_type: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
