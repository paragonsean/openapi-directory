from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.event_category_collection import EventCategoryCollection
from openapi_server import util


async def event_categories_list(request: web.Request, api_version) -> web.Response:
    """event_categories_list

    Get the list of available event categories supported in the Activity Logs Service.&lt;br&gt;The current list includes the following: Administrative, Security, ServiceHealth, Alert, Recommendation, Policy.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
