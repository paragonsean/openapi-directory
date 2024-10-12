from typing import List, Dict
from aiohttp import web

from openapi_server.models.sync_v1_service_sync_stream_stream_message import SyncV1ServiceSyncStreamStreamMessage
from openapi_server import util


async def create_stream_message(request: web.Request, service_sid, stream_sid, data) -> web.Response:
    """create_stream_message

    Create a new Stream Message.

    :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new Stream Message in.
    :type service_sid: str
    :param stream_sid: The SID of the Sync Stream to create the new Stream Message resource for.
    :type stream_sid: str
    :param data: A JSON string that represents an arbitrary, schema-less object that makes up the Stream Message body. Can be up to 4 KiB in length.
    :type data: dict | bytes

    """
    data = object.from_dict(data)
    return web.Response(status=200)
