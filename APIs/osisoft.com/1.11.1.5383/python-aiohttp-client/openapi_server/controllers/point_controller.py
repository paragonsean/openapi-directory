from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_item_point import ItemsItemPoint
from openapi_server.models.items_point_attribute import ItemsPointAttribute
from openapi_server.models.point import Point
from openapi_server.models.point_attribute import PointAttribute
from openapi_server import util


async def point_delete(request: web.Request, web_id) -> web.Response:
    """Delete a point.

    

    :param web_id: The ID of the point.
    :type web_id: str

    """
    return web.Response(status=200)


async def point_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get a point.

    

    :param web_id: The ID of the point.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def point_get_attribute_by_name(request: web.Request, name, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get a point attribute by name.

    

    :param name: The name of the attribute.
    :type name: str
    :param web_id: The ID of the point.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def point_get_attributes(request: web.Request, web_id, name=None, name_filter=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Get point attributes.

    

    :param web_id: The ID of the point.
    :type web_id: str
    :param name: The name of a point attribute to be returned. Multiple attributes may be specified with multiple instances of the parameter.
    :type name: List[str]
    :param name_filter: The filter to the names of the list of point attributes to be returned. The default is no filter.
    :type name_filter: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def point_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Get a point by path.

    This method returns a PI Point based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the point.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def point_get_multiple(request: web.Request, as_parallel=None, include_mode=None, path=None, selected_fields=None, web_id=None, web_id_type=None) -> web.Response:
    """Retrieve multiple points by web id or path.

    

    :param as_parallel: Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested points. The default is &#39;false&#39;.
    :type as_parallel: bool
    :param include_mode: The include mode for the return list. The default is &#39;All&#39;.
    :type include_mode: str
    :param path: The path of a point. Multiple points may be specified with multiple instances of the parameter.
    :type path: List[str]
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id: The ID of a point. Multiple points may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def point_update(request: web.Request, web_id, point_dto) -> web.Response:
    """Update a point. The only PI Point attributes that can be updated include: Name, Descriptor, EngineeringUnits, Step, and DisplayDigits. Other PI Point attributes cannot be updated through PI Web API.

    

    :param web_id: The ID of the point.
    :type web_id: str
    :param point_dto: A partial point containing the desired changes.
    :type point_dto: dict | bytes

    """
    point_dto = Point.from_dict(point_dto)
    return web.Response(status=200)
