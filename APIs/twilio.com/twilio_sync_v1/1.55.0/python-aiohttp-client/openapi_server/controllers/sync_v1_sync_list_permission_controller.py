from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sync_list_permission_response import ListSyncListPermissionResponse
from openapi_server.models.sync_v1_service_sync_list_sync_list_permission import SyncV1ServiceSyncListSyncListPermission
from openapi_server import util


async def delete_sync_list_permission(request: web.Request, service_sid, list_sid, identity) -> web.Response:
    """delete_sync_list_permission

    Delete a specific Sync List Permission.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to delete.
    :type service_sid: str
    :param list_sid: The SID of the Sync List with the Sync List Permission resource to delete. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type list_sid: str
    :param identity: The application-defined string that uniquely identifies the User&#39;s Sync List Permission resource to delete.
    :type identity: str

    """
    return web.Response(status=200)


async def fetch_sync_list_permission(request: web.Request, service_sid, list_sid, identity) -> web.Response:
    """fetch_sync_list_permission

    Fetch a specific Sync List Permission.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to fetch.
    :type service_sid: str
    :param list_sid: The SID of the Sync List with the Sync List Permission resource to fetch. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type list_sid: str
    :param identity: The application-defined string that uniquely identifies the User&#39;s Sync List Permission resource to fetch.
    :type identity: str

    """
    return web.Response(status=200)


async def list_sync_list_permission(request: web.Request, service_sid, list_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sync_list_permission

    Retrieve a list of all Permissions applying to a Sync List.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resources to read.
    :type service_sid: str
    :param list_sid: The SID of the Sync List with the Sync List Permission resources to read. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type list_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sync_list_permission(request: web.Request, service_sid, list_sid, identity, manage, read, write) -> web.Response:
    """update_sync_list_permission

    Update an identity&#39;s access to a specific Sync List.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to update.
    :type service_sid: str
    :param list_sid: The SID of the Sync List with the Sync List Permission resource to update. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type list_sid: str
    :param identity: The application-defined string that uniquely identifies the User&#39;s Sync List Permission resource to update.
    :type identity: str
    :param manage: Whether the identity can delete the Sync List. Default value is &#x60;false&#x60;.
    :type manage: bool
    :param read: Whether the identity can read the Sync List and its Items. Default value is &#x60;false&#x60;.
    :type read: bool
    :param write: Whether the identity can create, update, and delete Items in the Sync List. Default value is &#x60;false&#x60;.
    :type write: bool

    """
    return web.Response(status=200)
