from typing import List, Dict
from aiohttp import web

from openapi_server.models.retrieve_comments200_response import RetrieveComments200Response
from openapi_server import util


async def retrieve_comments(request: web.Request, block_id=None, page_size=None, notion_version=None) -> web.Response:
    """Retrieve comments

    Retrieve a user object using the ID specified in the request path.

    :param block_id: 
    :type block_id: str
    :param page_size: 
    :type page_size: str
    :param notion_version: 
    :type notion_version: str

    """
    return web.Response(status=200)
