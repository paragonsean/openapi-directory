from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_connection_policy_response import ListConnectionPolicyResponse
from openapi_server.models.voice_v1_connection_policy import VoiceV1ConnectionPolicy
from openapi_server import util


async def create_connection_policy(request: web.Request, friendly_name=None) -> web.Response:
    """create_connection_policy

    

    :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_connection_policy(request: web.Request, sid) -> web.Response:
    """delete_connection_policy

    

    :param sid: The unique string that we created to identify the Connection Policy resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_connection_policy(request: web.Request, sid) -> web.Response:
    """fetch_connection_policy

    

    :param sid: The unique string that we created to identify the Connection Policy resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_connection_policy(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_connection_policy

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_connection_policy(request: web.Request, sid, friendly_name=None) -> web.Response:
    """update_connection_policy

    

    :param sid: The unique string that we created to identify the Connection Policy resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
