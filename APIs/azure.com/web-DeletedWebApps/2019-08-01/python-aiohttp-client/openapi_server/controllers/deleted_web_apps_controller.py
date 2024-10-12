from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted_web_app_collection import DeletedWebAppCollection
from openapi_server.models.deleted_web_apps_get_deleted_web_app_by_location200_response import DeletedWebAppsGetDeletedWebAppByLocation200Response
from openapi_server.models.deleted_web_apps_list_default_response import DeletedWebAppsListDefaultResponse
from openapi_server import util


async def deleted_web_apps_get_deleted_web_app_by_location(request: web.Request, location, deleted_site_id, subscription_id, api_version) -> web.Response:
    """Get deleted app for a subscription at location.

    Description for Get deleted app for a subscription at location.

    :param location: 
    :type location: str
    :param deleted_site_id: The numeric ID of the deleted app, e.g. 12345
    :type deleted_site_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def deleted_web_apps_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get all deleted apps for a subscription.

    Description for Get all deleted apps for a subscription.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def deleted_web_apps_list_by_location(request: web.Request, location, subscription_id, api_version) -> web.Response:
    """Get all deleted apps for a subscription at location

    Description for Get all deleted apps for a subscription at location

    :param location: 
    :type location: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
