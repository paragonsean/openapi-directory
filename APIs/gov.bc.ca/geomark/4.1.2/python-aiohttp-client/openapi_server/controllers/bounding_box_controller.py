from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def geomarks_geomark_id_bounding_box_file_format_extension_get(request: web.Request, geomark_id, file_format_extension, srid=None) -> web.Response:
    """Gets the bounding box of the geomark

    The source geomarks can be specified by with the geomarkUrl parameter.  Repeat the parameter if sourcing from multiple geomarks

    :param geomark_id: The unique identifier for the geomark
    :type geomark_id: str
    :param file_format_extension: The file format name extension used to represent the geomark download.
    :type file_format_extension: str
    :param srid: The srid of the coordinate system the geometry should be converted to.
    :type srid: int

    """
    return web.Response(status=200)
