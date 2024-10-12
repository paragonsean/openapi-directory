from typing import List, Dict
from aiohttp import web

from openapi_server.models.asset_public_signature import AssetPublicSignature
from openapi_server.models.error import Error
from openapi_server import util


async def get_site_asset_public_signature(request: web.Request, site_id, asset_id) -> web.Response:
    """get_site_asset_public_signature

    

    :param site_id: 
    :type site_id: str
    :param asset_id: 
    :type asset_id: str

    """
    return web.Response(status=200)
