from typing import List, Dict
from aiohttp import web

from openapi_server.models.issue import Issue
from openapi_server import util


async def get_v3_issues(request: web.Request, state=None, labels=None, milestone=None, order_by=None, sort=None, page=None, per_page=None) -> web.Response:
    """Get currently authenticated user&#39;s issues

    Get currently authenticated user&#39;s issues

    :param state: Return opened, closed, or all issues
    :type state: str
    :param labels: Comma-separated list of label names
    :type labels: str
    :param milestone: Return issues for a specific milestone
    :type milestone: str
    :param order_by: Return issues ordered by &#x60;created_at&#x60; or &#x60;updated_at&#x60; fields.
    :type order_by: str
    :param sort: Return issues sorted in &#x60;asc&#x60; or &#x60;desc&#x60; order.
    :type sort: str
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)
