from typing import List, Dict
from aiohttp import web

from openapi_server.models.video_v1_room_room_recording_rule import VideoV1RoomRoomRecordingRule
from openapi_server import util


async def fetch_room_recording_rule(request: web.Request, room_sid) -> web.Response:
    """fetch_room_recording_rule

    Returns a list of Recording Rules for the Room.

    :param room_sid: The SID of the Room resource where the recording rules to fetch apply.
    :type room_sid: str

    """
    return web.Response(status=200)


async def update_room_recording_rule(request: web.Request, room_sid, rules=None) -> web.Response:
    """update_room_recording_rule

    Update the Recording Rules for the Room

    :param room_sid: The SID of the Room resource where the recording rules to update apply.
    :type room_sid: str
    :param rules: A JSON-encoded array of recording rules.
    :type rules: dict | bytes

    """
    rules = object.from_dict(rules)
    return web.Response(status=200)
