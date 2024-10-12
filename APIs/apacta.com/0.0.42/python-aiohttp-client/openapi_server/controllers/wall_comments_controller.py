from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.wall_comments_post_request import WallCommentsPostRequest
from openapi_server.models.wall_comments_wall_comment_id_get200_response import WallCommentsWallCommentIdGet200Response
from openapi_server import util


async def wall_comments_post(request: web.Request, body=None) -> web.Response:
    """Add wall comment

    

    :param body: 
    :type body: dict | bytes

    """
    body = WallCommentsPostRequest.from_dict(body)
    return web.Response(status=200)


async def wall_comments_wall_comment_id_get(request: web.Request, wall_comment_id) -> web.Response:
    """View wall comment

    

    :param wall_comment_id: 
    :type wall_comment_id: str

    """
    return web.Response(status=200)
