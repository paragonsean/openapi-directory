from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification_plug_in import NotificationPlugIn
from openapi_server import util


async def notification_plug_in_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a notification plugin.

    

    :param web_id: The ID of the notification plugin.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def notification_plug_in_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a notification plugin by path.

    This method returns a notification plugin based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the notification plugin.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)
