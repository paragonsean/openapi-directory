from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sync_document_permission_response import ListSyncDocumentPermissionResponse
from openapi_server.models.preview_sync_service_document_document_permission import PreviewSyncServiceDocumentDocumentPermission
from openapi_server import util


async def delete_sync_document_permission(request: web.Request, service_sid, document_sid, identity) -> web.Response:
    """delete_sync_document_permission

    Delete a specific Sync Document Permission.

    :param service_sid: 
    :type service_sid: str
    :param document_sid: Identifier of the Sync Document. Either a SID or a unique name.
    :type document_sid: str
    :param identity: Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
    :type identity: str

    """
    return web.Response(status=200)


async def fetch_sync_document_permission(request: web.Request, service_sid, document_sid, identity) -> web.Response:
    """fetch_sync_document_permission

    Fetch a specific Sync Document Permission.

    :param service_sid: 
    :type service_sid: str
    :param document_sid: Identifier of the Sync Document. Either a SID or a unique name.
    :type document_sid: str
    :param identity: Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
    :type identity: str

    """
    return web.Response(status=200)


async def list_sync_document_permission(request: web.Request, service_sid, document_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sync_document_permission

    Retrieve a list of all Permissions applying to a Sync Document.

    :param service_sid: 
    :type service_sid: str
    :param document_sid: Identifier of the Sync Document. Either a SID or a unique name.
    :type document_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sync_document_permission(request: web.Request, service_sid, document_sid, identity, manage, read, write) -> web.Response:
    """update_sync_document_permission

    Update an identity&#39;s access to a specific Sync Document.

    :param service_sid: The unique SID identifier of the Sync Service Instance.
    :type service_sid: str
    :param document_sid: Identifier of the Sync Document. Either a SID or a unique name.
    :type document_sid: str
    :param identity: Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer.
    :type identity: str
    :param manage: Boolean flag specifying whether the identity can delete the Sync Document.
    :type manage: bool
    :param read: Boolean flag specifying whether the identity can read the Sync Document.
    :type read: bool
    :param write: Boolean flag specifying whether the identity can update the Sync Document.
    :type write: bool

    """
    return web.Response(status=200)
