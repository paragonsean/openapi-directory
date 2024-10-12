from typing import List, Dict
from aiohttp import web

from openapi_server.models.enumeration_value import EnumerationValue
from openapi_server import util


async def enumeration_value_delete_enumeration_value(request: web.Request, web_id) -> web.Response:
    """Delete an enumeration value from an enumeration set.

    Deleting a value will remove it from the enumeration set along with any value references within the PI Web API system.

    :param web_id: The ID of the enumeration value.
    :type web_id: str

    """
    return web.Response(status=200)


async def enumeration_value_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an enumeration value mapping

    

    :param web_id: The ID of the enumeration value.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def enumeration_value_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an enumeration value by path.

    This method returns a enumeration value based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the target enumeration value.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def enumeration_value_update_enumeration_value(request: web.Request, web_id, enumeration_value) -> web.Response:
    """Update an enumeration value by replacing items in its definition.

    

    :param web_id: The ID of the enumeration value to update.
    :type web_id: str
    :param enumeration_value: A partial enumeration value containing the desired changes.
    :type enumeration_value: dict | bytes

    """
    enumeration_value = EnumerationValue.from_dict(enumeration_value)
    return web.Response(status=200)
