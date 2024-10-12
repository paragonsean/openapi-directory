from typing import List, Dict
from aiohttp import web

from openapi_server.models.vote import Vote
from openapi_server.models.votes_post_request import VotesPostRequest
from openapi_server import util


async def votes_get(request: web.Request, user_id=None, feature_id=None, positive=None, negative=None, offset=None, limit=None) -> web.Response:
    """votes_get

    

    :param user_id: Include only votes by User that voted on a feature.
    :type user_id: int
    :param feature_id: Include only votes for Feature with this Feature ID
    :type feature_id: int
    :param positive: Include only votes that are positive
    :type positive: bool
    :param negative: Include only votes that are negative
    :type negative: bool
    :param offset: Offset to start at
    :type offset: 
    :param limit: Limit the number of records returned
    :type limit: 

    """
    return web.Response(status=200)


async def votes_post(request: web.Request, data) -> web.Response:
    """update specified votes for a User

    Automatically subscribes/unsubscribes the User to the specifed feature depending on the quantity value

    :param data: 
    :type data: dict | bytes

    """
    data = VotesPostRequest.from_dict(data)
    return web.Response(status=200)
