from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sync_sync_map_response import ListSyncSyncMapResponse
from openapi_server.models.preview_sync_service_sync_map import PreviewSyncServiceSyncMap
from openapi_server import util


async def create_sync_sync_map(request: web.Request, service_sid, unique_name=None) -> web.Response:
    """create_sync_sync_map

    

    :param service_sid: 
    :type service_sid: str
    :param unique_name: 
    :type unique_name: str

    """
    return web.Response(status=200)


async def delete_sync_sync_map(request: web.Request, service_sid, sid) -> web.Response:
    """delete_sync_sync_map

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sync_sync_map(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_sync_sync_map

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_sync_sync_map(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sync_sync_map

    

    :param service_sid: 
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
