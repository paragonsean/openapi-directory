from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_flow_response import ListFlowResponse
from openapi_server.models.studio_v1_flow import StudioV1Flow
from openapi_server import util


async def delete_flow(request: web.Request, sid) -> web.Response:
    """delete_flow

    Delete a specific Flow.

    :param sid: The SID of the Flow resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_flow(request: web.Request, sid) -> web.Response:
    """fetch_flow

    Retrieve a specific Flow.

    :param sid: The SID of the Flow resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_flow(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_flow

    Retrieve a list of all Flows.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
