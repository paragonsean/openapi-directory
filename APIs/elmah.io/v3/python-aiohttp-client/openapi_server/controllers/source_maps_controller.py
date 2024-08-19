from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def source_maps_create_or_update(request: web.Request, log_id, minified_java_script, path, source_map) -> web.Response:
    """Create or update a translation between a minified JavaScript path to the minified JavaScript and source map files.

    Required permission: &#x60;sourcemaps_write&#x60;

    :param log_id: The ID of the log which should contain the minified JavaScript and source map.
    :type log_id: str
    :param minified_java_script: The minified JavaScript file. Only files with an extension of .js and content type of text/javascript will be accepted.
    :type minified_java_script: str
    :param path: An URL to the online minified JavaScript file. The URL can be absolute or relative but will always be converted to a relative path (no protocol, domain, and query parameters).  elmah.io uses this path to lookup any lines in a JS stack trace that will need de-minification.
    :type path: str
    :param source_map: The source map file. Only files with an extension of .map and content type of application/json will be accepted.
    :type source_map: str

    """
    return web.Response(status=200)
