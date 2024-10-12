from typing import List, Dict
from aiohttp import web

from openapi_server.models.buckets_bucket_key_messages_post200_response import BucketsBucketKeyMessagesPost200Response
from openapi_server.models.error import Error
from openapi_server.models.new_message import NewMessage
from openapi_server import util


async def buckets_bucket_key_errors_get(request: web.Request, bucket_key, count=None, since=None, before=None) -> web.Response:
    """Retrieve a list of error messages in a bucket

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param count: Maxiumum number of messages to return. Default 50, max 1000.
    :type count: int
    :param since: Only return messages after the given Unix timestamp
    :type since: int
    :param before: Only return messages before the given Unix timestamp
    :type before: int

    """
    return web.Response(status=200)


async def buckets_bucket_key_messages_delete(request: web.Request, bucket_key) -> web.Response:
    """Clear a bucket (remove all messages).

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str

    """
    return web.Response(status=200)


async def buckets_bucket_key_messages_get(request: web.Request, bucket_key, count=None, since=None, before=None) -> web.Response:
    """Retrieve a list of messages in a bucket

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param count: Maxiumum number of messages to return. Default 50, max 1000.
    :type count: int
    :param since: Only return messages after the given Unix timestamp
    :type since: int
    :param before: Only return messages before the given Unix timestamp
    :type before: int

    """
    return web.Response(status=200)


async def buckets_bucket_key_messages_message_id_get(request: web.Request, bucket_key, message_id) -> web.Response:
    """Retrieve the details for a single message.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param message_id: The unique identifier for this message
    :type message_id: str

    """
    return web.Response(status=200)


async def buckets_bucket_key_messages_post(request: web.Request, bucket_key, new_message) -> web.Response:
    """Create a message

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param new_message: 
    :type new_message: dict | bytes

    """
    new_message = NewMessage.from_dict(new_message)
    return web.Response(status=200)
