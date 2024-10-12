from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_message import ActivityMessage
from openapi_server import util


async def get_sandboxes_activity(request: web.Request, from_timestamp=None, source_sandboxes=None, keyword=None, all_types=None, max_results=None) -> web.Response:
    """searchActivity

    

    :param from_timestamp: Timestamp to start search from, epoch time in milliseconds.
    :type from_timestamp: int
    :param source_sandboxes: Comma-separated list of Sandbox names to search.
    :type source_sandboxes: str
    :param keyword: A keyword to search activities by, will match any part of the ActivityMessage.
    :type keyword: str
    :param all_types: Flag to return all types of activity, defaults to just Requests
    :type all_types: bool
    :param max_results: Maximum number of results to return
    :type max_results: int

    """
    return web.Response(status=200)
