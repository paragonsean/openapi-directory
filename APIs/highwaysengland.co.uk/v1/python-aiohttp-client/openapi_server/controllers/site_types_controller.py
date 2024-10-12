from typing import List, Dict
from aiohttp import web

from openapi_server.models.site_type_layer import SiteTypeLayer
from openapi_server.models.site_type_response import SiteTypeResponse
from openapi_server import util


async def site_types_get_sites_for_public_facing_api(request: web.Request, site_type_id, version) -> web.Response:
    """Returns the layer metadata for the LayerId specified.

    

    :param site_type_id: 1 &#x3D; MIDAS, 2 &#x3D; TAME, 3 &#x3D; TMU, 4 &#x3D; TRADS Legacy
    :type site_type_id: int
    :param version: 
    :type version: str

    """
    return web.Response(status=200)


async def site_types_index(request: web.Request, version) -> web.Response:
    """Return list of site types

    

    :param version: 
    :type version: str

    """
    return web.Response(status=200)
