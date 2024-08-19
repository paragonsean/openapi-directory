from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def geomarks_geomark_id_point_file_format_extension_get(request: web.Request, geomark_id, file_format_extension, srid=None) -> web.Response:
    """Gets a single spatial point representative of the geomark.

    The geomark point resource returns a single spatial feature with a single Point and the geomark attribution.  The point geometry will be created from the first geometry part of the Geomark. Point geomarks will return the first Point part in the geomark.  LineString geomarks will return the first coordinate of the first LineString part in the geomark. Polygon geomarks will return the centroid or another point inside the first Polygon part in the geomark. The geometry and attribution can be downloaded as a spatial download file format in a supported coordinate system. The download files can then be used in a desktop GIS application (e.g. ArcMap), Google Earth or a web mapping application.

    :param geomark_id: The unique identifier for the geomark.
    :type geomark_id: str
    :param file_format_extension: The file format name extension used to represent the geomark download.
    :type file_format_extension: str
    :param srid: The srid of the coordinate system the geometry should be converted to.
    :type srid: int

    """
    return web.Response(status=200)
