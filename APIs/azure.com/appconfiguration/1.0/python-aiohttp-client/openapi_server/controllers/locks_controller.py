from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.key_value import KeyValue
from openapi_server import util


async def delete_lock(request: web.Request, key, api_version, label=None, sync_token=None, if_match=None, if_none_match=None) -> web.Response:
    """Unlocks a key-value.

    

    :param key: The key of the key-value to unlock.
    :type key: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param label: The label, if any, of the key-value to unlock.
    :type label: str
    :param sync_token: Used to guarantee real-time consistency between requests.
    :type sync_token: str
    :param if_match: Used to perform an operation only if the targeted resource&#39;s etag matches the value provided.
    :type if_match: str
    :param if_none_match: Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def put_lock(request: web.Request, key, api_version, label=None, sync_token=None, if_match=None, if_none_match=None) -> web.Response:
    """Locks a key-value.

    

    :param key: The key of the key-value to lock.
    :type key: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param label: The label, if any, of the key-value to lock.
    :type label: str
    :param sync_token: Used to guarantee real-time consistency between requests.
    :type sync_token: str
    :param if_match: Used to perform an operation only if the targeted resource&#39;s etag matches the value provided.
    :type if_match: str
    :param if_none_match: Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided.
    :type if_none_match: str

    """
    return web.Response(status=200)
