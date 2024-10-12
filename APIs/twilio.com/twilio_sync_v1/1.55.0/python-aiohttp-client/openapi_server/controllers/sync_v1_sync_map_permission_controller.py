from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sync_map_permission_response import ListSyncMapPermissionResponse
from openapi_server.models.sync_v1_service_sync_map_sync_map_permission import SyncV1ServiceSyncMapSyncMapPermission
from openapi_server import util


async def delete_sync_map_permission(request: web.Request, service_sid, map_sid, identity) -> web.Response:
    """delete_sync_map_permission

    Delete a specific Sync Map Permission.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to delete. Can be the Service&#39;s &#x60;sid&#x60; value or &#x60;default&#x60;.
    :type service_sid: str
    :param map_sid: The SID of the Sync Map with the Sync Map Permission resource to delete. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type map_sid: str
    :param identity: The application-defined string that uniquely identifies the User&#39;s Sync Map Permission resource to delete.
    :type identity: str

    """
    return web.Response(status=200)


async def fetch_sync_map_permission(request: web.Request, service_sid, map_sid, identity) -> web.Response:
    """fetch_sync_map_permission

    Fetch a specific Sync Map Permission.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to fetch. Can be the Service&#39;s &#x60;sid&#x60; value or &#x60;default&#x60;.
    :type service_sid: str
    :param map_sid: The SID of the Sync Map with the Sync Map Permission resource to fetch. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type map_sid: str
    :param identity: The application-defined string that uniquely identifies the User&#39;s Sync Map Permission resource to fetch.
    :type identity: str

    """
    return web.Response(status=200)


async def list_sync_map_permission(request: web.Request, service_sid, map_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sync_map_permission

    Retrieve a list of all Permissions applying to a Sync Map.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resources to read. Can be the Service&#39;s &#x60;sid&#x60; value or &#x60;default&#x60;.
    :type service_sid: str
    :param map_sid: The SID of the Sync Map with the Permission resources to read. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type map_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sync_map_permission(request: web.Request, service_sid, map_sid, identity, manage, read, write) -> web.Response:
    """update_sync_map_permission

    Update an identity&#39;s access to a specific Sync Map.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to update. Can be the Service&#39;s &#x60;sid&#x60; value or &#x60;default&#x60;.
    :type service_sid: str
    :param map_sid: The SID of the Sync Map with the Sync Map Permission resource to update. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type map_sid: str
    :param identity: The application-defined string that uniquely identifies the User&#39;s Sync Map Permission resource to update.
    :type identity: str
    :param manage: Whether the identity can delete the Sync Map. Default value is &#x60;false&#x60;.
    :type manage: bool
    :param read: Whether the identity can read the Sync Map and its Items. Default value is &#x60;false&#x60;.
    :type read: bool
    :param write: Whether the identity can create, update, and delete Items in the Sync Map. Default value is &#x60;false&#x60;.
    :type write: bool

    """
    return web.Response(status=200)
