from typing import List, Dict
from aiohttp import web

from openapi_server.models.comment import Comment
from openapi_server.models.create_comment_alt1_request import CreateCommentAlt1Request
from openapi_server.models.create_comment_reply_request import CreateCommentReplyRequest
from openapi_server.models.edit_comment_request import EditCommentRequest
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError
from openapi_server import util


async def create_comment(request: web.Request, video_id, body) -> web.Response:
    """Add a comment to a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCommentAlt1Request.from_dict(body)
    return web.Response(status=200)


async def create_comment_alt1(request: web.Request, channel_id, video_id, body) -> web.Response:
    """Add a comment to a video

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCommentAlt1Request.from_dict(body)
    return web.Response(status=200)


async def create_comment_reply(request: web.Request, comment_id, video_id, body) -> web.Response:
    """Add a reply to a video comment

    

    :param comment_id: The ID of the comment.
    :type comment_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCommentReplyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_comment(request: web.Request, comment_id, video_id) -> web.Response:
    """Delete a video comment

    

    :param comment_id: The ID of the comment.
    :type comment_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def edit_comment(request: web.Request, comment_id, video_id, body) -> web.Response:
    """Edit a video comment

    

    :param comment_id: The ID of the comment.
    :type comment_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditCommentRequest.from_dict(body)
    return web.Response(status=200)


async def get_comment(request: web.Request, comment_id, video_id) -> web.Response:
    """Get a specific video comment

    

    :param comment_id: The ID of the comment.
    :type comment_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_comment_replies(request: web.Request, comment_id, video_id, page=None, per_page=None) -> web.Response:
    """Get all the replies to a video comment

    

    :param comment_id: The ID of the comment.
    :type comment_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)


async def get_comments(request: web.Request, video_id, direction=None, page=None, per_page=None) -> web.Response:
    """Get all the comments on a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)


async def get_comments_alt1(request: web.Request, channel_id, video_id, direction=None, page=None, per_page=None) -> web.Response:
    """Get all the comments on a video

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)
