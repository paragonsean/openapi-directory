from typing import List, Dict
from aiohttp import web

from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.group_details import GroupDetails
from openapi_server.models.score_details import ScoreDetails
from openapi_server.models.user_public import UserPublic
from openapi_server import util


async def get_group_details(request: web.Request, group) -> web.Response:
    """Get group information

    

    :param group: Unique identifier of a Flat group 
    :type group: str

    """
    return web.Response(status=200)


async def get_group_scores(request: web.Request, group, parent=None) -> web.Response:
    """List group&#39;s scores

    Get the list of scores shared with a group. 

    :param group: Unique identifier of a Flat group 
    :type group: str
    :param parent: Filter the score forked from the score id &#x60;parent&#x60;
    :type parent: str

    """
    return web.Response(status=200)


async def list_group_users(request: web.Request, group, source=None) -> web.Response:
    """List group&#39;s users

    

    :param group: Unique identifier of a Flat group 
    :type group: str
    :param source: Filter the users by their source 
    :type source: str

    """
    return web.Response(status=200)
