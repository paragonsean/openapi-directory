from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_function_response import ListFunctionResponse
from openapi_server.models.serverless_v1_service_function import ServerlessV1ServiceFunction
from openapi_server import util


async def create_function(request: web.Request, service_sid, friendly_name) -> web.Response:
    """create_function

    Create a new Function resource.

    :param service_sid: The SID of the Service to create the Function resource under.
    :type service_sid: str
    :param friendly_name: A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_function(request: web.Request, service_sid, sid) -> web.Response:
    """delete_function

    Delete a Function resource.

    :param service_sid: The SID of the Service to delete the Function resource from.
    :type service_sid: str
    :param sid: The SID of the Function resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_function(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_function

    Retrieve a specific Function resource.

    :param service_sid: The SID of the Service to fetch the Function resource from.
    :type service_sid: str
    :param sid: The SID of the Function resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_function(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_function

    Retrieve a list of all Functions.

    :param service_sid: The SID of the Service to read the Function resources from.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_function(request: web.Request, service_sid, sid, friendly_name) -> web.Response:
    """update_function

    Update a specific Function resource.

    :param service_sid: The SID of the Service to update the Function resource from.
    :type service_sid: str
    :param sid: The SID of the Function resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.
    :type friendly_name: str

    """
    return web.Response(status=200)
