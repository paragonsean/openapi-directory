from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def map_version_number_copyrights_caption_format_get(request: web.Request, version_number, format, param_callback=None) -> web.Response:
    """Captions

    This API returns copyright captions for the map service.

    :param version_number: Version of the service to call. The current version is 1.
    :type version_number: int
    :param format: Format of the response
    :type format: str
    :param param_callback: Specifies the jsonp callback method. Only used when format is jsonp
    :type param_callback: str

    """
    return web.Response(status=200)


async def map_version_number_copyrights_format_get(request: web.Request, version_number, format, param_callback=None) -> web.Response:
    """Copyrights whole world

    The Copyrights API returns copyright information for the Maps API Raster Tile Service in JSON, JSONP, or XML format. This call returns copyright information for the whole world.

    :param version_number: Version of the service to call. The current version is 1
    :type version_number: int
    :param format: Format of the response
    :type format: str
    :param param_callback: Specifies the jsonp callback method. Only used when format is jsonp
    :type param_callback: str

    """
    return web.Response(status=200)


async def map_version_number_copyrights_min_lon_min_lat_max_lon_max_lat_format_get(request: web.Request, version_number, format, min_lon, min_lat, max_lon, max_lat, param_callback=None) -> web.Response:
    """Copyrights bounding box

    The Copyrights API returns copyright information for the Maps API Raster Tile Service in JSON, JSONP, or XML format. This call returns copyright information for a specific bounding box.

    :param version_number: Version of the service to call. The current version is 1
    :type version_number: int
    :param format: Format of the response
    :type format: str
    :param min_lon: Minimum longitude coordinate of bounding box defined in terms of latitude/longitude.
    :type min_lon: 
    :param min_lat: Minimum latitude coordinate of bounding box defined in terms of latitude/longitude.
    :type min_lat: 
    :param max_lon: Maximum longitude coordinate of bounding box defined in terms of latitude/longitude.
    :type max_lon: 
    :param max_lat: Maximum latitude coordinate of bounding box defined in terms of latitude/longitude.
    :type max_lat: 
    :param param_callback: Specifies the jsonp callback method. Only used when format is jsonp.
    :type param_callback: str

    """
    return web.Response(status=200)


async def map_version_number_copyrights_zoom_xy_format_get(request: web.Request, version_number, format, zoom, x, y, param_callback=None) -> web.Response:
    """Copyrights tile

    The Copyrights API returns copyright information for the Maps API Raster Tile Service in JSON, JSONP, or XML format. This call returns copyright information for the a specific map tile.

    :param version_number: Version of the service to call. The current version is 1
    :type version_number: int
    :param format: Format of the response
    :type format: str
    :param zoom: Zoom level of tile to be rendered. Only used for tile-level copyright calls.
    :type zoom: int
    :param x: X coordinate of the tile on zoom grid. Only used for tile-level copyright calls.
    :type x: int
    :param y: Y coordinate of the tile on zoom grid. Only used for tile-level copyright calls.
    :type y: int
    :param param_callback: Specifies the jsonp callback method. Only used when format is jsonp.
    :type param_callback: str

    """
    return web.Response(status=200)
