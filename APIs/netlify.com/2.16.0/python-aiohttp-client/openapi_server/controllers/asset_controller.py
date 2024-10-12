from typing import List, Dict
from aiohttp import web

from openapi_server.models.asset import Asset
from openapi_server.models.asset_signature import AssetSignature
from openapi_server.models.error import Error
from openapi_server import util


async def create_site_asset(request: web.Request, site_id, name, size, content_type, visibility=None) -> web.Response:
    """create_site_asset

    

    :param site_id: 
    :type site_id: str
    :param name: 
    :type name: str
    :param size: 
    :type size: int
    :param content_type: 
    :type content_type: str
    :param visibility: 
    :type visibility: str

    """
    return web.Response(status=200)


async def delete_site_asset(request: web.Request, site_id, asset_id) -> web.Response:
    """delete_site_asset

    

    :param site_id: 
    :type site_id: str
    :param asset_id: 
    :type asset_id: str

    """
    return web.Response(status=200)


async def get_site_asset_info(request: web.Request, site_id, asset_id) -> web.Response:
    """get_site_asset_info

    

    :param site_id: 
    :type site_id: str
    :param asset_id: 
    :type asset_id: str

    """
    return web.Response(status=200)


async def list_site_assets(request: web.Request, site_id) -> web.Response:
    """list_site_assets

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def update_site_asset(request: web.Request, site_id, asset_id, state) -> web.Response:
    """update_site_asset

    

    :param site_id: 
    :type site_id: str
    :param asset_id: 
    :type asset_id: str
    :param state: 
    :type state: str

    """
    return web.Response(status=200)
