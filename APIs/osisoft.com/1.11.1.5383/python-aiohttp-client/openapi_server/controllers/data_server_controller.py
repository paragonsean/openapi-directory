from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_server import DataServer
from openapi_server.models.data_server_license import DataServerLicense
from openapi_server.models.enumeration_set import EnumerationSet
from openapi_server.models.errors import Errors
from openapi_server.models.items_data_server import ItemsDataServer
from openapi_server.models.items_enumeration_set import ItemsEnumerationSet
from openapi_server.models.items_point import ItemsPoint
from openapi_server.models.point import Point
from openapi_server import util


async def data_server_create_enumeration_set(request: web.Request, web_id, enumeration_set, web_id_type=None) -> web.Response:
    """Create an enumeration set on the Data Server.

    

    :param web_id: The ID of the server on which to create the enumeration set.
    :type web_id: str
    :param enumeration_set: The new enumeration set definition.
    :type enumeration_set: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    enumeration_set = EnumerationSet.from_dict(enumeration_set)
    return web.Response(status=200)


async def data_server_create_point(request: web.Request, web_id, point_dto, web_id_type=None) -> web.Response:
    """Create a point in the specified Data Server.

    

    :param web_id: The ID of the server.
    :type web_id: str
    :param point_dto: The new point definition.
    :type point_dto: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    point_dto = Point.from_dict(point_dto)
    return web.Response(status=200)


async def data_server_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a Data Server.

    

    :param web_id: The ID of the server.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def data_server_get_by_name(request: web.Request, name, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a Data Server by name.

    This method returns a data server based on the name. Users should primarily search with the WebID when available.

    :param name: The name of the server.
    :type name: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def data_server_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a Data Server by path.

    This method returns a data server based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the server. Note that the path supplied to this method must be of the form &#39;\\\\servername&#39;.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def data_server_get_enumeration_sets(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve enumeration sets for given Data Server.

    

    :param web_id: The ID of the server.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def data_server_get_license(request: web.Request, web_id, module, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieves the specified license for the given Data Server. The fields of the response object are string representations of the numerical values reported by the Data Server, with \&quot;Infinity\&quot; representing a license field with no limit.

    

    :param web_id: The ID of the server.
    :type web_id: str
    :param module: The case-sensitive name of the module.
    :type module: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def data_server_get_points(request: web.Request, web_id, max_count=None, name_filter=None, selected_fields=None, start_index=None, web_id_type=None) -> web.Response:
    """Retrieve a list of points on a specified Data Server.

    Users can search for the data servers based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the data servers that match the default search.

    :param web_id: The ID of the server.
    :type web_id: str
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
    :param name_filter: A query string for filtering by point name. The default is no filter.
    :type name_filter: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_index: The starting index (zero based) of the items to be returned. The default is &#39;0&#39;.
    :type start_index: int
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def data_server_list(request: web.Request, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a list of Data Servers known to this service.

    This method returns a list of all available known Data Servers that the user can connect to. Even though a server may be returned in the list, the user may not have permission to access it.

    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)
