from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_video_credit_alt1_request import AddVideoCreditAlt1Request
from openapi_server.models.credit import Credit
from openapi_server.models.edit_video_credit_request import EditVideoCreditRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server import util


async def add_video_credit(request: web.Request, video_id, body) -> web.Response:
    """Credit a user in a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = AddVideoCreditAlt1Request.from_dict(body)
    return web.Response(status=200)


async def add_video_credit_alt1(request: web.Request, channel_id, video_id, body) -> web.Response:
    """Credit a user in a video

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = AddVideoCreditAlt1Request.from_dict(body)
    return web.Response(status=200)


async def delete_video_credit(request: web.Request, credit_id, video_id) -> web.Response:
    """Delete a credit for a user in a video

    

    :param credit_id: The ID of the credit.
    :type credit_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def edit_video_credit(request: web.Request, credit_id, video_id, body=None) -> web.Response:
    """Edit a credit for a user in a video

    

    :param credit_id: The ID of the credit.
    :type credit_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditVideoCreditRequest.from_dict(body)
    return web.Response(status=200)


async def get_video_credit(request: web.Request, credit_id, video_id) -> web.Response:
    """Get a specific credited user in a video

    

    :param credit_id: The ID of the credit.
    :type credit_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_video_credits(request: web.Request, video_id, direction=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the credited users in a video

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_video_credits_alt1(request: web.Request, channel_id, video_id, direction=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the credited users in a video

    

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
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)
