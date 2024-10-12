from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_bean_string import PageBeanString
from openapi_server import util


async def get_all_labels(request: web.Request, start_at=None, max_results=None) -> web.Response:
    """Get all labels

    Returns a [paginated](#pagination) list of labels.

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)
