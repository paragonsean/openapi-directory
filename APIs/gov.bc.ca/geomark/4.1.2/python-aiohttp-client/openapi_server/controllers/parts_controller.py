from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def geomarks_geomark_id_parts_file_format_extension_get(request: web.Request, geomark_id, file_format_extension, srid=None) -> web.Response:
    """Get the individual geometries within a multi-part geometry

    The geomark parts resource returns a one or more spatial features. One for each part of the Geomark&#39;s geomerty. Each part contains a single (Point, LineString, Polygon) geometry and the geomark attribution.

    :param geomark_id: The unique identifier for the geomark
    :type geomark_id: str
    :param file_format_extension: The file format name extension used to represent the geomark download.
    :type file_format_extension: str
    :param srid: The srid of the coordinate system the geometry should be converted to.
    :type srid: int

    """
    return web.Response(status=200)
