from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sites_response import ListSitesResponse
from openapi_server import util


async def list_sites(request: web.Request, ) -> web.Response:
    """ListSites

    Lists the Square Online sites that belong to a seller.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).


    """
    return web.Response(status=200)
