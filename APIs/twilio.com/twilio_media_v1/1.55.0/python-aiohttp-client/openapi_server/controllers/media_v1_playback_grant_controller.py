from typing import List, Dict
from aiohttp import web

from openapi_server.models.media_v1_player_streamer_player_streamer_playback_grant import MediaV1PlayerStreamerPlayerStreamerPlaybackGrant
from openapi_server import util


async def create_player_streamer_playback_grant(request: web.Request, sid, access_control_allow_origin=None, ttl=None) -> web.Response:
    """create_player_streamer_playback_grant

    

    :param sid: The unique string generated to identify the PlayerStreamer resource associated with this PlaybackGrant
    :type sid: str
    :param access_control_allow_origin: The full origin URL where the livestream can be streamed. If this is not provided, it can be streamed from any domain.
    :type access_control_allow_origin: str
    :param ttl: The time to live of the PlaybackGrant. Default value is 15 seconds. Maximum value is 60 seconds.
    :type ttl: int

    """
    return web.Response(status=200)


async def fetch_player_streamer_playback_grant(request: web.Request, sid) -> web.Response:
    """fetch_player_streamer_playback_grant

    **This method is not enabled.** Returns a single PlaybackGrant resource identified by a SID.

    :param sid: The SID of the PlayerStreamer resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)
