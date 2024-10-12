from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def geomarks_geomark_id_file_format_extension_get(request: web.Request, geomark_id, file_format_extension, srid=None) -> web.Response:
    """Get information about a particular geomark

    The attribution can be downloaded as a info file format. The download files can then be processed by a client application to access the geomark info fields and to get the URLs to the geometry download resources.

    :param geomark_id: The unique identifier for the geomark.
    :type geomark_id: str
    :param file_format_extension: The file format name extension used to represent the geomark download.
    :type file_format_extension: str
    :param srid: The srid of the coordinate system the geometry should be converted to.
    :type srid: int

    """
    return web.Response(status=200)
