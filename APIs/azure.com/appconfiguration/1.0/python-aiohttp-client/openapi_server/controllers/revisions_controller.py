from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.key_value_list_result import KeyValueListResult
from openapi_server import util


async def check_revisions(request: web.Request, api_version, key=None, label=None, sync_token=None, after=None, accept_datetime=None, select=None) -> web.Response:
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


async def get_revisions(request: web.Request, api_version, key=None, label=None, sync_token=None, after=None, accept_datetime=None, select=None) -> web.Response:
    """Gets a list of key-value revisions.

    

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
