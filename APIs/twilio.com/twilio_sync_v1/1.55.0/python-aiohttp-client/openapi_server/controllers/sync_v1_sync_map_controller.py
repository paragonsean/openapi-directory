from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sync_map_response import ListSyncMapResponse
from openapi_server.models.sync_v1_service_sync_map import SyncV1ServiceSyncMap
from openapi_server import util


async def create_sync_map(request: web.Request, service_sid, collection_ttl=None, ttl=None, unique_name=None) -> web.Response:
    """create_sync_map

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the Sync Map in.
    :type service_sid: str
    :param collection_ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Map expires (time-to-live) and is deleted.
    :type collection_ttl: int
    :param ttl: An alias for &#x60;collection_ttl&#x60;. If both parameters are provided, this value is ignored.
    :type ttl: int
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource.
    :type unique_name: str

    """
    return web.Response(status=200)


async def delete_sync_map(request: web.Request, service_sid, sid) -> web.Response:
    """delete_sync_map

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to delete.
    :type service_sid: str
    :param sid: The SID of the Sync Map resource to delete. Can be the Sync Map&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sync_map(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_sync_map

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to fetch.
    :type service_sid: str
    :param sid: The SID of the Sync Map resource to fetch. Can be the Sync Map&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sync_map(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sync_map

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resources to read.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sync_map(request: web.Request, service_sid, sid, collection_ttl=None, ttl=None) -> web.Response:
    """update_sync_map

    

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to update.
    :type service_sid: str
    :param sid: The SID of the Sync Map resource to update. Can be the Sync Map&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type sid: str
    :param collection_ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Map expires (time-to-live) and is deleted.
    :type collection_ttl: int
    :param ttl: An alias for &#x60;collection_ttl&#x60;. If both parameters are provided, this value is ignored.
    :type ttl: int

    """
    return web.Response(status=200)
