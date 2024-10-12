from typing import List, Dict
from aiohttp import web

from openapi_server.models.unit import Unit
from openapi_server.models.unit_class import UnitClass
from openapi_server import util


async def unit_class_create_unit(request: web.Request, web_id, unit_dto, web_id_type=None) -> web.Response:
    """Create a unit in the specified Unit Class.

    

    :param web_id: The ID of the server.
    :type web_id: str
    :param unit_dto: The new unit definition.
    :type unit_dto: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    unit_dto = Unit.from_dict(unit_dto)
    return web.Response(status=200)


async def unit_class_delete(request: web.Request, web_id) -> web.Response:
    """Delete a unit class.

    

    :param web_id: The ID of the unit class.
    :type web_id: str

    """
    return web.Response(status=200)


async def unit_class_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a unit class.

    

    :param web_id: The ID of the unit class.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def unit_class_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a unit class by path.

    

    :param path: The path to the unit class.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def unit_class_get_canonical_unit(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get the canonical unit of a unit class.

    

    :param web_id: The ID of unit class.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def unit_class_get_units(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get a list of all units belonging to the unit class.

    

    :param web_id: The ID of unit class.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def unit_class_update(request: web.Request, web_id, unit_class_dto) -> web.Response:
    """Update a unit class.

    

    :param web_id: The ID of the unit class.
    :type web_id: str
    :param unit_class_dto: A partial unit class containing the desired changes.
    :type unit_class_dto: dict | bytes

    """
    unit_class_dto = UnitClass.from_dict(unit_class_dto)
    return web.Response(status=200)
