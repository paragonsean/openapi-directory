from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_text_track_alt1_request import CreateTextTrackAlt1Request
from openapi_server.models.edit_text_track_request import EditTextTrackRequest
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.text_track import TextTrack
from openapi_server import util


async def create_text_track(request: web.Request, video_id, body) -> web.Response:
    """Add a text track to a video

    For additional information, see our [text track upload guide](https://developer.vimeo.com/api/upload/texttracks).

    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateTextTrackAlt1Request.from_dict(body)
    return web.Response(status=200)


async def create_text_track_alt1(request: web.Request, channel_id, video_id, body) -> web.Response:
    """Add a text track to a video

    For additional information, see our [text track upload guide](https://developer.vimeo.com/api/upload/texttracks).

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateTextTrackAlt1Request.from_dict(body)
    return web.Response(status=200)


async def delete_text_track(request: web.Request, texttrack_id, video_id) -> web.Response:
    """Delete a text track

    

    :param texttrack_id: The ID of the text track.
    :type texttrack_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def edit_text_track(request: web.Request, texttrack_id, video_id, body=None) -> web.Response:
    """Edit a text track

    

    :param texttrack_id: The ID of the text track.
    :type texttrack_id: 
    :param video_id: The ID of the video.
    :type video_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditTextTrackRequest.from_dict(body)
    return web.Response(status=200)


async def get_text_track(request: web.Request, texttrack_id, video_id) -> web.Response:
    """Get a specific text track

    

    :param texttrack_id: The ID of the text track.
    :type texttrack_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_text_tracks(request: web.Request, video_id) -> web.Response:
    """Get all the text tracks of a video

    

    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_text_tracks_alt1(request: web.Request, channel_id, video_id) -> web.Response:
    """Get all the text tracks of a video

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)
