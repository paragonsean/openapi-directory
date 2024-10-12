from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_all_list_comments(request: web.Request, id, sort, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all list comments

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a list. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, and most &#x60;replies&#x60;.

    :param id: Trakt ID
    :type id: int
    :param sort: how to sort
    :type sort: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_all_users_who_liked_a_list(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get all users who liked a list

    #### &amp;#128196; Pagination  Returns all users who liked a list.

    :param id: Trakt ID
    :type id: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_items_on_a_list(request: web.Request, id, type, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get items on a list

    #### &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Get all items on a personal list. Items can be a &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;person&#x60;. You can optionally specify the &#x60;type&#x60; parameter with a single value or comma delimited string for multiple item types.  #### Notes  Each list item contains a &#x60;notes&#x60; field with text entered by the user.  #### Sorting Headers  All list items are sorted by ascending &#x60;rank&#x60;. We also send &#x60;X-Sort-By&#x60; and &#x60;X-Sort-How&#x60; headers which can be used to custom sort the list _**in your app**_ based on the user&#39;s preference. Values for &#x60;X-Sort-By&#x60; include &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, &#x60;votes&#x60;, &#x60;my_rating&#x60;, &#x60;random&#x60;, &#x60;watched&#x60;, and &#x60;collected&#x60;. Values for &#x60;X-Sort-How&#x60; include &#x60;asc&#x60; and &#x60;desc&#x60;.

    :param id: Trakt ID
    :type id: str
    :param type: Filter for a specific item type
    :type type: str
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_list(request: web.Request, id, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get list

    #### &amp;#128513; Emojis  Returns a single list. Use the [**/lists/:id/items**](#reference/lists/list-items) method to get the actual items this list contains.  **Note:** You must use an integer &#x60;id&#x60;, and only public lists will return data.

    :param id: Trakt ID
    :type id: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_popular_lists(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get popular lists

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns the most popular lists. Popularity is calculated using total number of likes and comments.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_trending_lists(request: web.Request, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get trending lists

    #### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists with the most likes and comments over the last 7 days.

    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)
