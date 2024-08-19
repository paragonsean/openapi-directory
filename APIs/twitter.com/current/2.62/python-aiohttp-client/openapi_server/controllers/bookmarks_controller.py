from typing import List, Dict
from aiohttp import web

from openapi_server.models.bookmark_add_request import BookmarkAddRequest
from openapi_server.models.bookmark_mutation_response import BookmarkMutationResponse
from openapi_server.models.error import Error
from openapi_server.models.get2_users_id_bookmarks_response import Get2UsersIdBookmarksResponse
from openapi_server.models.problem import Problem
from openapi_server import util


async def get_users_id_bookmarks(request: web.Request, id, max_results=None, pagination_token=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Bookmarks by User

    Returns Tweet objects that have been bookmarked by the requesting User

    :param id: The ID of the authenticated source User for whom to return results.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results.
    :type pagination_token: str
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param media_fields: A comma separated list of Media fields to display.
    :type media_fields: List[str]
    :param poll_fields: A comma separated list of Poll fields to display.
    :type poll_fields: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param place_fields: A comma separated list of Place fields to display.
    :type place_fields: List[str]

    """
    return web.Response(status=200)


async def post_users_id_bookmarks(request: web.Request, id, body) -> web.Response:
    """Add Tweet to Bookmarks

    Adds a Tweet (ID in the body) to the requesting User&#39;s (in the path) bookmarks

    :param id: The ID of the authenticated source User for whom to add bookmarks.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BookmarkAddRequest.from_dict(body)
    return web.Response(status=200)


async def users_id_bookmarks_delete(request: web.Request, id, tweet_id) -> web.Response:
    """Remove a bookmarked Tweet

    Removes a Tweet from the requesting User&#39;s bookmarked Tweets.

    :param id: The ID of the authenticated source User whose bookmark is to be removed.
    :type id: str
    :param tweet_id: The ID of the Tweet that the source User is removing from bookmarks.
    :type tweet_id: str

    """
    return web.Response(status=200)
