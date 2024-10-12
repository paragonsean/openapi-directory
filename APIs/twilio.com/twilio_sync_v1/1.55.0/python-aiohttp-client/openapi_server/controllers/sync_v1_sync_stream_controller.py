from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sync_stream_response import ListSyncStreamResponse
from openapi_server.models.sync_v1_service_sync_stream import SyncV1ServiceSyncStream
from openapi_server import util


async def create_sync_stream(request: web.Request, service_sid, ttl=None, unique_name=None) -> web.Response:
    """create_sync_stream

    Create a new Stream.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new Stream in.
    :type service_sid: str
    :param ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).
    :type ttl: int
    :param unique_name: An application-defined string that uniquely identifies the resource. This value must be unique within its Service and it can be up to 320 characters long. The &#x60;unique_name&#x60; value can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource.
    :type unique_name: str

    """
    return web.Response(status=200)


async def delete_sync_stream(request: web.Request, service_sid, sid) -> web.Response:
    """delete_sync_stream

    Delete a specific Stream.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Stream resource to delete.
    :type service_sid: str
    :param sid: The SID of the Stream resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sync_stream(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_sync_stream

    Fetch a specific Stream.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Stream resource to fetch.
    :type service_sid: str
    :param sid: The SID of the Stream resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sync_stream(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sync_stream

    Retrieve a list of all Streams in a Service Instance.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Stream resources to read.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sync_stream(request: web.Request, service_sid, sid, ttl=None) -> web.Response:
    """update_sync_stream

    Update a specific Stream.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Stream resource to update.
    :type service_sid: str
    :param sid: The SID of the Stream resource to update.
    :type sid: str
    :param ttl: How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).
    :type ttl: int

    """
    return web.Response(status=200)
