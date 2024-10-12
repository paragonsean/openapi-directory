from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sync_sync_list_permission_response import ListSyncSyncListPermissionResponse
from openapi_server.models.preview_sync_service_sync_list_sync_list_permission import PreviewSyncServiceSyncListSyncListPermission
from openapi_server import util


async def delete_sync_sync_list_permission(request: web.Request, service_sid, list_sid, identity) -> web.Response:
    """delete_sync_sync_list_permission

    Delete a specific Sync List Permission.

    :param service_sid: 
    :type service_sid: str
    :param list_sid: Identifier of the Sync List. Either a SID or a unique name.
    :type list_sid: str
    :param identity: Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
    :type identity: str

    """
    return web.Response(status=200)


async def fetch_sync_sync_list_permission(request: web.Request, service_sid, list_sid, identity) -> web.Response:
    """fetch_sync_sync_list_permission

    Fetch a specific Sync List Permission.

    :param service_sid: 
    :type service_sid: str
    :param list_sid: Identifier of the Sync List. Either a SID or a unique name.
    :type list_sid: str
    :param identity: Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
    :type identity: str

    """
    return web.Response(status=200)


async def list_sync_sync_list_permission(request: web.Request, service_sid, list_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sync_sync_list_permission

    Retrieve a list of all Permissions applying to a Sync List.

    :param service_sid: 
    :type service_sid: str
    :param list_sid: Identifier of the Sync List. Either a SID or a unique name.
    :type list_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sync_sync_list_permission(request: web.Request, service_sid, list_sid, identity, manage, read, write) -> web.Response:
    """update_sync_sync_list_permission

    Update an identity&#39;s access to a specific Sync List.

    :param service_sid: The unique SID identifier of the Sync Service Instance.
    :type service_sid: str
    :param list_sid: Identifier of the Sync List. Either a SID or a unique name.
    :type list_sid: str
    :param identity: Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer.
    :type identity: str
    :param manage: Boolean flag specifying whether the identity can delete the Sync List.
    :type manage: bool
    :param read: Boolean flag specifying whether the identity can read the Sync List.
    :type read: bool
    :param write: Boolean flag specifying whether the identity can create, update and delete Items of the Sync List.
    :type write: bool

    """
    return web.Response(status=200)
