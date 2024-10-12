from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.key_value import KeyValue
from openapi_server.models.key_value_list_result import KeyValueListResult
from openapi_server import util


async def check_key_value(request: web.Request, key, api_version, label=None, sync_token=None, accept_datetime=None, if_match=None, if_none_match=None, select=None) -> web.Response:
    """Requests the headers and status of the given resource.

    

    :param key: The key of the key-value to retrieve.
    :type key: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param label: The label of the key-value to retrieve.
    :type label: str
    :param sync_token: Used to guarantee real-time consistency between requests.
    :type sync_token: str
    :param accept_datetime: Requests the server to respond with the state of the resource at the specified time.
    :type accept_datetime: str
    :param if_match: Used to perform an operation only if the targeted resource&#39;s etag matches the value provided.
    :type if_match: str
    :param if_none_match: Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided.
    :type if_none_match: str
    :param select: Used to select what fields are present in the returned resource(s).
    :type select: List[str]

    """
    return web.Response(status=200)


async def check_key_values(request: web.Request, api_version, key=None, label=None, sync_token=None, after=None, accept_datetime=None, select=None) -> web.Response:
    """Requests the headers and status of the given resource.

    

    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param key: A filter used to match keys.
    :type key: str
    :param label: A filter used to match labels
    :type label: str
    :param sync_token: Used to guarantee real-time consistency between requests.
    :type sync_token: str
    :param after: Instructs the server to return elements that appear after the element referred to by the specified token.
    :type after: str
    :param accept_datetime: Requests the server to respond with the state of the resource at the specified time.
    :type accept_datetime: str
    :param select: Used to select what fields are present in the returned resource(s).
    :type select: List[str]

    """
    return web.Response(status=200)


async def delete_key_value(request: web.Request, key, api_version, label=None, sync_token=None, if_match=None) -> web.Response:
    """Deletes a key-value.

    

    :param key: The key of the key-value to delete.
    :type key: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param label: The label of the key-value to delete.
    :type label: str
    :param sync_token: Used to guarantee real-time consistency between requests.
    :type sync_token: str
    :param if_match: Used to perform an operation only if the targeted resource&#39;s etag matches the value provided.
    :type if_match: str

    """
    return web.Response(status=200)


async def get_key_value(request: web.Request, key, api_version, label=None, sync_token=None, accept_datetime=None, if_match=None, if_none_match=None, select=None) -> web.Response:
    """Gets a single key-value.

    

    :param key: The key of the key-value to retrieve.
    :type key: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param label: The label of the key-value to retrieve.
    :type label: str
    :param sync_token: Used to guarantee real-time consistency between requests.
    :type sync_token: str
    :param accept_datetime: Requests the server to respond with the state of the resource at the specified time.
    :type accept_datetime: str
    :param if_match: Used to perform an operation only if the targeted resource&#39;s etag matches the value provided.
    :type if_match: str
    :param if_none_match: Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided.
    :type if_none_match: str
    :param select: Used to select what fields are present in the returned resource(s).
    :type select: List[str]

    """
    return web.Response(status=200)


async def get_key_values(request: web.Request, api_version, key=None, label=None, sync_token=None, after=None, accept_datetime=None, select=None) -> web.Response:
    """Gets a list of key-values.

    

    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param key: A filter used to match keys.
    :type key: str
    :param label: A filter used to match labels
    :type label: str
    :param sync_token: Used to guarantee real-time consistency between requests.
    :type sync_token: str
    :param after: Instructs the server to return elements that appear after the element referred to by the specified token.
    :type after: str
    :param accept_datetime: Requests the server to respond with the state of the resource at the specified time.
    :type accept_datetime: str
    :param select: Used to select what fields are present in the returned resource(s).
    :type select: List[str]

    """
    return web.Response(status=200)


async def put_key_value(request: web.Request, key, api_version, label=None, sync_token=None, if_match=None, if_none_match=None, entity=None) -> web.Response:
    """Creates a key-value.

    

    :param key: The key of the key-value to create.
    :type key: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param label: The label of the key-value to create.
    :type label: str
    :param sync_token: Used to guarantee real-time consistency between requests.
    :type sync_token: str
    :param if_match: Used to perform an operation only if the targeted resource&#39;s etag matches the value provided.
    :type if_match: str
    :param if_none_match: Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided.
    :type if_none_match: str
    :param entity: The key-value to create.
    :type entity: dict | bytes

    """
    entity = KeyValue.from_dict(entity)
    return web.Response(status=200)
