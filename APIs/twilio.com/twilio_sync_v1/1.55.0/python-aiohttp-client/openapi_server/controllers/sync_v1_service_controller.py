from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server.models.sync_v1_service import SyncV1Service
from openapi_server import util


async def create_service(request: web.Request, acl_enabled=None, friendly_name=None, reachability_debouncing_enabled=None, reachability_debouncing_window=None, reachability_webhooks_enabled=None, webhook_url=None, webhooks_from_rest_enabled=None) -> web.Response:
    """create_service

    

    :param acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
    :type acl_enabled: bool
    :param friendly_name: A string that you assign to describe the resource.
    :type friendly_name: str
    :param reachability_debouncing_enabled: Whether every &#x60;endpoint_disconnected&#x60; event should occur after a configurable delay. The default is &#x60;false&#x60;, where the &#x60;endpoint_disconnected&#x60; event occurs immediately after disconnection. When &#x60;true&#x60;, intervening reconnections can prevent the &#x60;endpoint_disconnected&#x60; event.
    :type reachability_debouncing_enabled: bool
    :param reachability_debouncing_window: The reachability event delay in milliseconds if &#x60;reachability_debouncing_enabled&#x60; &#x3D; &#x60;true&#x60;.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the &#x60;webhook_url&#x60; is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the call to &#x60;webhook_url&#x60;.
    :type reachability_debouncing_window: int
    :param reachability_webhooks_enabled: Whether the service instance should call &#x60;webhook_url&#x60; when client endpoints connect to Sync. The default is &#x60;false&#x60;.
    :type reachability_webhooks_enabled: bool
    :param webhook_url: The URL we should call when Sync objects are manipulated.
    :type webhook_url: str
    :param webhooks_from_rest_enabled: Whether the Service instance should call &#x60;webhook_url&#x60; when the REST API is used to update Sync objects. The default is &#x60;false&#x60;.
    :type webhooks_from_rest_enabled: bool

    """
    return web.Response(status=200)


async def delete_service(request: web.Request, sid) -> web.Response:
    """delete_service

    

    :param sid: The SID of the Service resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service(request: web.Request, sid) -> web.Response:
    """fetch_service

    

    :param sid: The SID of the Service resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_service(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_service(request: web.Request, sid, acl_enabled=None, friendly_name=None, reachability_debouncing_enabled=None, reachability_debouncing_window=None, reachability_webhooks_enabled=None, webhook_url=None, webhooks_from_rest_enabled=None) -> web.Response:
    """update_service

    

    :param sid: The SID of the Service resource to update.
    :type sid: str
    :param acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
    :type acl_enabled: bool
    :param friendly_name: A string that you assign to describe the resource.
    :type friendly_name: str
    :param reachability_debouncing_enabled: Whether every &#x60;endpoint_disconnected&#x60; event should occur after a configurable delay. The default is &#x60;false&#x60;, where the &#x60;endpoint_disconnected&#x60; event occurs immediately after disconnection. When &#x60;true&#x60;, intervening reconnections can prevent the &#x60;endpoint_disconnected&#x60; event.
    :type reachability_debouncing_enabled: bool
    :param reachability_debouncing_window: The reachability event delay in milliseconds if &#x60;reachability_debouncing_enabled&#x60; &#x3D; &#x60;true&#x60;.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the webhook from being called.
    :type reachability_debouncing_window: int
    :param reachability_webhooks_enabled: Whether the service instance should call &#x60;webhook_url&#x60; when client endpoints connect to Sync. The default is &#x60;false&#x60;.
    :type reachability_webhooks_enabled: bool
    :param webhook_url: The URL we should call when Sync objects are manipulated.
    :type webhook_url: str
    :param webhooks_from_rest_enabled: Whether the Service instance should call &#x60;webhook_url&#x60; when the REST API is used to update Sync objects. The default is &#x60;false&#x60;.
    :type webhooks_from_rest_enabled: bool

    """
    return web.Response(status=200)
