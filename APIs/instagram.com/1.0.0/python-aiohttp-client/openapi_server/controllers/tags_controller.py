from typing import List, Dict
from aiohttp import web

from openapi_server.models.tag_info_response import TagInfoResponse
from openapi_server.models.tag_media_list_response import TagMediaListResponse
from openapi_server.models.tag_search_response import TagSearchResponse
from openapi_server import util


async def tags_search_get(request: web.Request, q) -> web.Response:
    """Search for tags by name.

    Search for tags by name.

    :param q: A valid tag name without a leading \\#. (eg. snowy, nofilter)
    :type q: str

    """
    return web.Response(status=200)


async def tags_tag_name_get(request: web.Request, tag_name) -> web.Response:
    """Get information about a tag object.

    Get information about a tag object.

    :param tag_name: The tag name.
    :type tag_name: str

    """
    return web.Response(status=200)


async def tags_tag_name_media_recent_get(request: web.Request, tag_name, count=None, min_tag_id=None, max_tag_id=None) -> web.Response:
    """Get a list of recently tagged media.

    Get a list of recently tagged media. Use the &#x60;max_tag_id&#x60; and &#x60;min_tag_id&#x60; parameters in the pagination response to paginate through these objects. 

    :param tag_name: The tag name.
    :type tag_name: str
    :param count: Count of tagged media to return.
    :type count: int
    :param min_tag_id: Return media before this &#x60;min_tag_id&#x60;.
    :type min_tag_id: str
    :param max_tag_id: Return media after this &#x60;max_tag_id&#x60;.
    :type max_tag_id: str

    """
    return web.Response(status=200)
