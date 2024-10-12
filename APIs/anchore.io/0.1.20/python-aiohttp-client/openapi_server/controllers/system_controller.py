from typing import List, Dict
from aiohttp import web

from openapi_server.models.anchore_error_code import AnchoreErrorCode
from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.feed_metadata import FeedMetadata
from openapi_server.models.feed_sync_result import FeedSyncResult
from openapi_server.models.gate_spec import GateSpec
from openapi_server.models.service import Service
from openapi_server.models.status_response import StatusResponse
from openapi_server.models.system_status_response import SystemStatusResponse
from openapi_server import util


async def delete_feed(request: web.Request, feed) -> web.Response:
    """delete_feed

    Delete the groups and data for the feed and disable the feed itself

    :param feed: 
    :type feed: str

    """
    return web.Response(status=200)


async def delete_feed_group(request: web.Request, feed, group) -> web.Response:
    """delete_feed_group

    Delete the group data and disable the group itself

    :param feed: 
    :type feed: str
    :param group: 
    :type group: str

    """
    return web.Response(status=200)


async def delete_service(request: web.Request, servicename, hostid) -> web.Response:
    """Delete the service config

    

    :param servicename: 
    :type servicename: str
    :param hostid: 
    :type hostid: str

    """
    return web.Response(status=200)


async def describe_error_codes(request: web.Request, ) -> web.Response:
    """Describe anchore engine error codes.

    Describe anchore engine error codes.


    """
    return web.Response(status=200)


async def describe_policy(request: web.Request, ) -> web.Response:
    """Describe the policy language spec implemented by this service.

    Get the policy language spec for this service


    """
    return web.Response(status=200)


async def get_service_detail(request: web.Request, ) -> web.Response:
    """System status

    Get the system status including queue lengths


    """
    return web.Response(status=200)


async def get_services_by_name(request: web.Request, servicename) -> web.Response:
    """Get a service configuration and state

    

    :param servicename: 
    :type servicename: str

    """
    return web.Response(status=200)


async def get_services_by_name_and_host(request: web.Request, servicename, hostid) -> web.Response:
    """Get service config for a specific host

    

    :param servicename: 
    :type servicename: str
    :param hostid: 
    :type hostid: str

    """
    return web.Response(status=200)


async def get_status(request: web.Request, ) -> web.Response:
    """Service status

    Get the API service status


    """
    return web.Response(status=200)


async def get_system_feeds(request: web.Request, ) -> web.Response:
    """list feeds operations and information

    Return a list of feed and their groups along with update and record count information. This data reflects the state of the policy engine, not the upstream feed service itself.


    """
    return web.Response(status=200)


async def list_services(request: web.Request, ) -> web.Response:
    """List system services

    


    """
    return web.Response(status=200)


async def post_system_feeds(request: web.Request, flush=None, sync=None) -> web.Response:
    """trigger feeds operations

    Execute a synchronous feed sync operation. The response will block until complete, then return the result summary.

    :param flush: instruct system to flush existing data feeds records from anchore-engine
    :type flush: bool
    :param sync: instruct system to re-sync data feeds
    :type sync: bool

    """
    return web.Response(status=200)


async def test_webhook(request: web.Request, webhook_type, notification_type=None) -> web.Response:
    """Adds the capabilities to test a webhook delivery for the given notification type

    Loads the Webhook configuration for webhook_type, and sends the notification out as a test

    :param webhook_type: The Webhook Type that we should test
    :type webhook_type: str
    :param notification_type: What kind of Notification to send
    :type notification_type: str

    """
    return web.Response(status=200)


async def toggle_feed_enabled(request: web.Request, feed, enabled) -> web.Response:
    """toggle_feed_enabled

    Disable the feed so that it does not sync on subsequent sync operations

    :param feed: 
    :type feed: str
    :param enabled: 
    :type enabled: bool

    """
    return web.Response(status=200)


async def toggle_group_enabled(request: web.Request, feed, group, enabled) -> web.Response:
    """toggle_group_enabled

    Disable a specific group within a feed to not sync

    :param feed: 
    :type feed: str
    :param group: 
    :type group: str
    :param enabled: 
    :type enabled: bool

    """
    return web.Response(status=200)
