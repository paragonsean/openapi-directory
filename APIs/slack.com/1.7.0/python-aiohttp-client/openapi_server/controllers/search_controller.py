from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def search_messages(request: web.Request, token, query, count=None, highlight=None, page=None, sort=None, sort_dir=None) -> web.Response:
    """search_messages

    Searches for messages matching a query.

    :param token: Authentication token. Requires scope: &#x60;search:read&#x60;
    :type token: str
    :param query: Search query.
    :type query: str
    :param count: Pass the number of results you want per \&quot;page\&quot;. Maximum of &#x60;100&#x60;.
    :type count: int
    :param highlight: Pass a value of &#x60;true&#x60; to enable query highlight markers (see below).
    :type highlight: bool
    :param page: 
    :type page: int
    :param sort: Return matches sorted by either &#x60;score&#x60; or &#x60;timestamp&#x60;.
    :type sort: str
    :param sort_dir: Change sort direction to ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;).
    :type sort_dir: str

    """
    return web.Response(status=200)
