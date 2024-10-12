from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.get2_spaces_by_creator_ids_response import Get2SpacesByCreatorIdsResponse
from openapi_server.models.get2_spaces_id_buyers_response import Get2SpacesIdBuyersResponse
from openapi_server.models.get2_spaces_id_response import Get2SpacesIdResponse
from openapi_server.models.get2_spaces_id_tweets_response import Get2SpacesIdTweetsResponse
from openapi_server.models.get2_spaces_response import Get2SpacesResponse
from openapi_server.models.get2_spaces_search_response import Get2SpacesSearchResponse
from openapi_server.models.problem import Problem
from openapi_server import util


async def find_space_by_id(request: web.Request, id, space_fields=None, expansions=None, user_fields=None, topic_fields=None) -> web.Response:
    """Space lookup by Space ID

    Returns a variety of information about the Space specified by the requested ID

    :param id: The ID of the Space to be retrieved.
    :type id: str
    :param space_fields: A comma separated list of Space fields to display.
    :type space_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param topic_fields: A comma separated list of Topic fields to display.
    :type topic_fields: List[str]

    """
    return web.Response(status=200)


async def find_spaces_by_creator_ids(request: web.Request, user_ids, space_fields=None, expansions=None, user_fields=None, topic_fields=None) -> web.Response:
    """Space lookup by their creators

    Returns a variety of information about the Spaces created by the provided User IDs

    :param user_ids: The IDs of Users to search through.
    :type user_ids: List[str]
    :param space_fields: A comma separated list of Space fields to display.
    :type space_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param topic_fields: A comma separated list of Topic fields to display.
    :type topic_fields: List[str]

    """
    return web.Response(status=200)


async def find_spaces_by_ids(request: web.Request, ids, space_fields=None, expansions=None, user_fields=None, topic_fields=None) -> web.Response:
    """Space lookup up Space IDs

    Returns a variety of information about the Spaces specified by the requested IDs

    :param ids: The list of Space IDs to return.
    :type ids: List[str]
    :param space_fields: A comma separated list of Space fields to display.
    :type space_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param topic_fields: A comma separated list of Topic fields to display.
    :type topic_fields: List[str]

    """
    return web.Response(status=200)


async def search_spaces(request: web.Request, query, state=None, max_results=None, space_fields=None, expansions=None, user_fields=None, topic_fields=None) -> web.Response:
    """Search for Spaces

    Returns Spaces that match the provided query.

    :param query: The search query.
    :type query: str
    :param state: The state of Spaces to search for.
    :type state: str
    :param max_results: The number of results to return.
    :type max_results: int
    :param space_fields: A comma separated list of Space fields to display.
    :type space_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param topic_fields: A comma separated list of Topic fields to display.
    :type topic_fields: List[str]

    """
    return web.Response(status=200)


async def space_buyers(request: web.Request, id, pagination_token=None, max_results=None, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """Retrieve the list of Users who purchased a ticket to the given space

    Retrieves the list of Users who purchased a ticket to the given space

    :param id: The ID of the Space to be retrieved.
    :type id: str
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def space_tweets(request: web.Request, id, max_results=None, tweet_fields=None, expansions=None, media_fields=None, poll_fields=None, user_fields=None, place_fields=None) -> web.Response:
    """Retrieve Tweets from a Space.

    Retrieves Tweets shared in the specified Space.

    :param id: The ID of the Space to be retrieved.
    :type id: str
    :param max_results: The number of Tweets to fetch from the provided space. If not provided, the value will default to the maximum of 100.
    :type max_results: int
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
