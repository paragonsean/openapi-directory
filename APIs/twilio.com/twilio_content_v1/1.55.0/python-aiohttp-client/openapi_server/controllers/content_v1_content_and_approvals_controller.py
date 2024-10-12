from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_content_and_approvals_response import ListContentAndApprovalsResponse
from openapi_server import util


async def list_content_and_approvals(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_content_and_approvals

    Retrieve a list of Contents with approval statuses belonging to the account used to make the request

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
