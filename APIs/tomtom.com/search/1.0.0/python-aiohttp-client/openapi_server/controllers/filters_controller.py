from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_version_number_geometry_filter_ext_post_request import SearchVersionNumberGeometryFilterExtPostRequest
from openapi_server.models.search_version_number_routed_filter_position_heading_ext_post_request import SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest
from openapi_server import util


async def search_version_number_geometry_filter_ext_get(request: web.Request, version_number, ext, geometry_list, poi_list) -> web.Response:
    """Geometry Filter

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param ext: Expected response format.
    :type ext: str
    :param geometry_list: List of geometries to filter by. Available types are CIRCLE (with the radius expressed in meters) and POLYGON.
    :type geometry_list: str
    :param poi_list: List of POIs to filter. The only required attribute of a POI is position, everything else is optional and will be echoed back when passed in.
    :type poi_list: str

    """
    return web.Response(status=200)


async def search_version_number_geometry_filter_ext_post(request: web.Request, version_number, ext, body=None) -> web.Response:
    """Geometry Filter

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param ext: Expected response format.
    :type ext: str
    :param body: 
    :type body: dict | bytes

    """
    body = SearchVersionNumberGeometryFilterExtPostRequest.from_dict(body)
    return web.Response(status=200)


async def search_version_number_routed_filter_position_heading_ext_get(request: web.Request, version_number, position, heading, ext, poi_list, routing_timeout=None) -> web.Response:
    """Routed Filter

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param position: This is specified as a comma separated string composed of lat., lon.
    :type position: str
    :param heading: The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
    :type heading: float
    :param ext: Expected response format.
    :type ext: str
    :param poi_list: List of POIs to filter. The only required attribute of a POI is position, everything else is optional and will be echoed back when passed in.
    :type poi_list: str
    :param routing_timeout: Only return results that arrive from routing engine within this time limit.
    :type routing_timeout: int

    """
    return web.Response(status=200)


async def search_version_number_routed_filter_position_heading_ext_post(request: web.Request, version_number, position, heading, ext, routing_timeout=None, body=None) -> web.Response:
    """Routed Filter

    

    :param version_number: Service version number. The current value is 2.
    :type version_number: int
    :param position: This is specified as a comma separated string composed of lat., lon.
    :type position: str
    :param heading: The directional heading in degrees, usually similar to the course along a road segment. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.)
    :type heading: float
    :param ext: Expected response format.
    :type ext: str
    :param routing_timeout: Only return results that arrive from routing engine within this time limit.
    :type routing_timeout: int
    :param body: 
    :type body: dict | bytes

    """
    body = SearchVersionNumberRoutedFilterPositionHeadingExtPostRequest.from_dict(body)
    return web.Response(status=200)
