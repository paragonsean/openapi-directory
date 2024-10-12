from typing import List, Dict
from aiohttp import web

from openapi_server.models.tags_collection import TagsCollection
from openapi_server import util


async def list_tags(request: web.Request, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List Tags

    Returns an array of Tag objects

    :param limit: The numbers of items to return per page.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param filter: Filter for querying collections.
    :type filter: dict | bytes
    :type filter: Dict[str, ]
    :param sort_by: The list of attribute and order to sort the result set by.
    :type sort_by: dict | bytes
    :type sort_by: Dict[str, ]

    """
    filter = .from_dict(filter)
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)
