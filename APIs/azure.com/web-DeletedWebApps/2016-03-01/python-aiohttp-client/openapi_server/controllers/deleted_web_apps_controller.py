from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted_web_app_collection import DeletedWebAppCollection
from openapi_server import util


async def deleted_web_apps_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get all deleted apps for a subscription.

    Get all deleted apps for a subscription.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
