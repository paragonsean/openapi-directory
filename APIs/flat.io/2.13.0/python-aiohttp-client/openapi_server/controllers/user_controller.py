from typing import List, Dict
from aiohttp import web

from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.score_details import ScoreDetails
from openapi_server.models.user_public import UserPublic
from openapi_server import util


async def ger_user_likes(request: web.Request, user, ids=None) -> web.Response:
    """List liked scores

    

    :param user: Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user. 
    :type user: str
    :param ids: Return only the identifiers of the scores
    :type ids: bool

    """
    return web.Response(status=200)


async def get_user(request: web.Request, user) -> web.Response:
    """Get a public user profile

    Get a public profile of a Flat User. 

    :param user: This route parameter is the unique identifier of the user. You can specify an email instead of an unique identifier. If you are executing this request authenticated, you can use &#x60;me&#x60; as a value instead of the current User unique identifier to work on the current authenticated user. 
    :type user: str

    """
    return web.Response(status=200)


async def get_user_scores(request: web.Request, user, parent=None) -> web.Response:
    """List user&#39;s scores

    Get the list of public scores owned by a User.  **DEPRECATED**: Please note that the current behavior will be deprecrated on **2019-01-01**. This method will no longer list private and shared scores, but only public scores of a Flat account. If you want to access to private scores, please use the [Collections API](#tag/Collection) instead. 

    :param user: Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user. 
    :type user: str
    :param parent: Filter the score forked from the score id &#x60;parent&#x60;
    :type parent: str

    """
    return web.Response(status=200)
