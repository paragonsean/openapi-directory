from typing import List, Dict
from aiohttp import web

from openapi_server.models.video_v1_room_room_participant_room_participant_subscribe_rule import VideoV1RoomRoomParticipantRoomParticipantSubscribeRule
from openapi_server import util


async def fetch_room_participant_subscribe_rule(request: web.Request, room_sid, participant_sid) -> web.Response:
    """fetch_room_participant_subscribe_rule

    Returns a list of Subscribe Rules for the Participant.

    :param room_sid: The SID of the Room resource where the subscribe rules to fetch apply.
    :type room_sid: str
    :param participant_sid: The SID of the Participant resource with the subscribe rules to fetch.
    :type participant_sid: str

    """
    return web.Response(status=200)


async def update_room_participant_subscribe_rule(request: web.Request, room_sid, participant_sid, rules=None) -> web.Response:
    """update_room_participant_subscribe_rule

    Update the Subscribe Rules for the Participant

    :param room_sid: The SID of the Room resource where the subscribe rules to update apply.
    :type room_sid: str
    :param participant_sid: The SID of the Participant resource to update the Subscribe Rules.
    :type participant_sid: str
    :param rules: A JSON-encoded array of subscribe rules. See the [Specifying Subscribe Rules](https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr) section for further information.
    :type rules: dict | bytes

    """
    rules = object.from_dict(rules)
    return web.Response(status=200)
