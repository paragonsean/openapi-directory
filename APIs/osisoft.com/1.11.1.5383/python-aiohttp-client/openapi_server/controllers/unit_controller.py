from typing import List, Dict
from aiohttp import web

from openapi_server.models.unit import Unit
from openapi_server import util


async def unit_delete(request: web.Request, web_id) -> web.Response:
    """Delete a unit.

    

    :param web_id: The ID of the unit.
    :type web_id: str

    """
    return web.Response(status=200)


async def unit_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a unit.

    

    :param web_id: The ID of the unit.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def unit_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a unit by path.

    

    :param path: The path to the unit.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def unit_update(request: web.Request, web_id, unit_dto) -> web.Response:
    """Update a unit.

    

    :param web_id: The ID of the unit.
    :type web_id: str
    :param unit_dto: A partial unit containing the desired changes.
    :type unit_dto: dict | bytes

    """
    unit_dto = Unit.from_dict(unit_dto)
    return web.Response(status=200)
