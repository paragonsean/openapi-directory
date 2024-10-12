from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.label_list_result import LabelListResult
from openapi_server import util


async def check_labels(request: web.Request, api_version, name=None, sync_token=None, after=None, accept_datetime=None, select=None) -> web.Response:
    """Requests the headers and status of the given resource.

    

    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param name: A filter for the name of the returned labels.
    :type name: str
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


async def get_labels(request: web.Request, api_version, name=None, sync_token=None, after=None, accept_datetime=None, select=None) -> web.Response:
    """Gets a list of labels.

    

    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param name: A filter for the name of the returned labels.
    :type name: str
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
