from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_document_permission_response import ListDocumentPermissionResponse
from openapi_server.models.sync_v1_service_document_document_permission import SyncV1ServiceDocumentDocumentPermission
from openapi_server import util


async def delete_document_permission(request: web.Request, service_sid, document_sid, identity) -> web.Response:
    """delete_document_permission

    Delete a specific Sync Document Permission.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to delete.
    :type service_sid: str
    :param document_sid: The SID of the Sync Document with the Document Permission resource to delete. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type document_sid: str
    :param identity: The application-defined string that uniquely identifies the User&#39;s Document Permission resource to delete.
    :type identity: str

    """
    return web.Response(status=200)


async def fetch_document_permission(request: web.Request, service_sid, document_sid, identity) -> web.Response:
    """fetch_document_permission

    Fetch a specific Sync Document Permission.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to fetch.
    :type service_sid: str
    :param document_sid: The SID of the Sync Document with the Document Permission resource to fetch. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type document_sid: str
    :param identity: The application-defined string that uniquely identifies the User&#39;s Document Permission resource to fetch.
    :type identity: str

    """
    return web.Response(status=200)


async def list_document_permission(request: web.Request, service_sid, document_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_document_permission

    Retrieve a list of all Permissions applying to a Sync Document.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resources to read.
    :type service_sid: str
    :param document_sid: The SID of the Sync Document with the Document Permission resources to read. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type document_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_document_permission(request: web.Request, service_sid, document_sid, identity, manage, read, write) -> web.Response:
    """update_document_permission

    Update an identity&#39;s access to a specific Sync Document.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to update.
    :type service_sid: str
    :param document_sid: The SID of the Sync Document with the Document Permission resource to update. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;.
    :type document_sid: str
    :param identity: The application-defined string that uniquely identifies the User&#39;s Document Permission resource to update.
    :type identity: str
    :param manage: Whether the identity can delete the Sync Document. Default value is &#x60;false&#x60;.
    :type manage: bool
    :param read: Whether the identity can read the Sync Document. Default value is &#x60;false&#x60;.
    :type read: bool
    :param write: Whether the identity can update the Sync Document. Default value is &#x60;false&#x60;.
    :type write: bool

    """
    return web.Response(status=200)
