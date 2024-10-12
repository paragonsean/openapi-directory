from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sync_service_response import ListSyncServiceResponse
from openapi_server.models.preview_sync_service import PreviewSyncService
from openapi_server import util


async def create_sync_service(request: web.Request, acl_enabled=None, friendly_name=None, reachability_webhooks_enabled=None, webhook_url=None) -> web.Response:
    """create_sync_service

    

    :param acl_enabled: 
    :type acl_enabled: bool
    :param friendly_name: 
    :type friendly_name: str
    :param reachability_webhooks_enabled: 
    :type reachability_webhooks_enabled: bool
    :param webhook_url: 
    :type webhook_url: str

    """
    return web.Response(status=200)


async def delete_sync_service(request: web.Request, sid) -> web.Response:
    """delete_sync_service

    

    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sync_service(request: web.Request, sid) -> web.Response:
    """fetch_sync_service

    

    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_sync_service(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sync_service

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sync_service(request: web.Request, sid, acl_enabled=None, friendly_name=None, reachability_webhooks_enabled=None, webhook_url=None) -> web.Response:
    """update_sync_service

    

    :param sid: 
    :type sid: str
    :param acl_enabled: 
    :type acl_enabled: bool
    :param friendly_name: 
    :type friendly_name: str
    :param reachability_webhooks_enabled: 
    :type reachability_webhooks_enabled: bool
    :param webhook_url: 
    :type webhook_url: str

    """
    return web.Response(status=200)
