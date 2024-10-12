from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_contributor(request: web.Request, contributor_id, aliases=None) -> web.Response:
    """Contributor Detail

    Return the content of the selected contributor.

    :param contributor_id: Filter the schedule items by contributor ID
    :type contributor_id: str
    :param aliases: Flag to display Legacy and Provider Ids.
    :type aliases: bool

    """
    return web.Response(status=200)


async def list_contributor(request: web.Request, updated_after=None, limit=None, aliases=None) -> web.Response:
    """Contributor Collection

    Return a collection of Contributors.

    :param updated_after: Updated After
    :type updated_after: str
    :param limit: Limit the the number of items to be returned per page. For example: 5.
    :type limit: int
    :param aliases: Flag to display Legacy and Provider Ids.
    :type aliases: bool

    """
    return web.Response(status=200)
