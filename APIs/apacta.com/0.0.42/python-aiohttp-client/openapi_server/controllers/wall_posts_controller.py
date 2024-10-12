from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.wall_posts_get200_response import WallPostsGet200Response
from openapi_server.models.wall_posts_post_request import WallPostsPostRequest
from openapi_server.models.wall_posts_wall_post_id_get200_response import WallPostsWallPostIdGet200Response
from openapi_server.models.wall_posts_wall_post_id_wall_comments_get200_response import WallPostsWallPostIdWallCommentsGet200Response
from openapi_server import util


async def wall_posts_get(request: web.Request, project_id=None, user_id=None) -> web.Response:
    """View list of wall posts

    

    :param project_id: 
    :type project_id: str
    :type project_id: str
    :param user_id: 
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def wall_posts_post(request: web.Request, body=None) -> web.Response:
    """Add a wall post

    

    :param body: 
    :type body: dict | bytes

    """
    body = WallPostsPostRequest.from_dict(body)
    return web.Response(status=200)


async def wall_posts_wall_post_id_get(request: web.Request, wall_post_id) -> web.Response:
    """View wall post

    

    :param wall_post_id: 
    :type wall_post_id: str

    """
    return web.Response(status=200)


async def wall_posts_wall_post_id_wall_comments_get(request: web.Request, wall_post_id) -> web.Response:
    """See wall comments to a wall post

    

    :param wall_post_id: 
    :type wall_post_id: str

    """
    return web.Response(status=200)
