from typing import List, Dict
from aiohttp import web

from openapi_server.models.time_rule import TimeRule
from openapi_server import util


async def time_rule_delete(request: web.Request, web_id) -> web.Response:
    """Delete a Time Rule.

    

    :param web_id: The ID of the Time Rule.
    :type web_id: str

    """
    return web.Response(status=200)


async def time_rule_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a Time Rule.

    

    :param web_id: The ID of the Time Rule.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def time_rule_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a Time Rule by path.

    This method returns a Time Rule based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the Time Rule.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def time_rule_update(request: web.Request, web_id, time_rule) -> web.Response:
    """Update a Time Rule by replacing items in its definition.

    

    :param web_id: The ID of the Time Rule.
    :type web_id: str
    :param time_rule: A partial Time Rule containing the desired changes.
    :type time_rule: dict | bytes

    """
    time_rule = TimeRule.from_dict(time_rule)
    return web.Response(status=200)
