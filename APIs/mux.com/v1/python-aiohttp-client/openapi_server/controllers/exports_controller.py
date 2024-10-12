from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_exports_response import ListExportsResponse
from openapi_server.models.list_video_view_exports_response import ListVideoViewExportsResponse
from openapi_server import util


async def list_exports(request: web.Request, ) -> web.Response:
    """List property video view export links

    The API has been replaced by the list-exports-views API call.  Lists the available video view exports along with URLs to retrieve them. 


    """
    return web.Response(status=200)


async def list_exports_views(request: web.Request, ) -> web.Response:
    """List available property view exports

    Lists the available video view exports along with URLs to retrieve them.


    """
    return web.Response(status=200)
