from typing import List, Dict
from aiohttp import web

from openapi_server.models.site_response import SiteResponse
from openapi_server import util


async def sites_index(request: web.Request, version) -> web.Response:
    """Get a list of sites

    

    :param version: 
    :type version: str

    """
    return web.Response(status=200)


async def vversion_sites_site_ids_get(request: web.Request, site_ids, version) -> web.Response:
    """Get selected sites

    

    :param site_ids: site id
    :type site_ids: str
    :param version: 
    :type version: str

    """
    return web.Response(status=200)
