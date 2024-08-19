from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def geomarks_geomark_id_feature_file_format_extension_get(request: web.Request, geomark_id, file_format_extension, srid=None) -> web.Response:
    """Get the feature and attribution of the geomark

    The geomark feature resource returns a single spatial feature with either a single (Point, LineString, Polygon) or multi-part geometry (MultiPoint, MultiLineString, MultiPolygon) and the geomark attribution.  The geometry and attribution can be downloaded as a spatial download file format in a supported coordinate system. The download files can then be used in a desktop GIS application (e.g. ArcMap), Google Earth or a web mapping application.

    :param geomark_id: The unique identifier for the geomark
    :type geomark_id: str
    :param file_format_extension: The file format name extension used to represent the geomark download.
    :type file_format_extension: str
    :param srid: The srid of the coordinate system the geometry should be converted to.
    :type srid: int

    """
    return web.Response(status=200)
