from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversations_v1_service import ConversationsV1Service
from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server import util


async def create_service(request: web.Request, friendly_name) -> web.Response:
    """create_service

    Create a new conversation service on your account

    :param friendly_name: The human-readable name of this service, limited to 256 characters. Optional.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_service(request: web.Request, sid) -> web.Response:
    """delete_service

    Remove a conversation service with all its nested resources from your account

    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service(request: web.Request, sid) -> web.Response:
    """fetch_service

    Fetch a conversation service from your account

    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_service(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service

    Retrieve a list of all conversation services on your account

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
