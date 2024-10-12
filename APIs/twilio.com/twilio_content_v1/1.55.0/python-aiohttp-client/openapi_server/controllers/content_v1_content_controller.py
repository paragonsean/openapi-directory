from typing import List, Dict
from aiohttp import web

from openapi_server.models.content_v1_content import ContentV1Content
from openapi_server.models.list_content_response import ListContentResponse
from openapi_server import util


async def delete_content(request: web.Request, sid) -> web.Response:
    """delete_content

    Deletes a Content resource

    :param sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_content(request: web.Request, sid) -> web.Response:
    """fetch_content

    Fetch a Content resource by its unique Content Sid

    :param sid: The Twilio-provided string that uniquely identifies the Content resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_content(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_content

    Retrieve a list of Contents belonging to the account used to make the request

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
