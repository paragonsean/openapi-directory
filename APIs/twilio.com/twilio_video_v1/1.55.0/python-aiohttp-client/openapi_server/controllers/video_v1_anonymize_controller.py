from typing import List, Dict
from aiohttp import web

from openapi_server.models.video_v1_room_room_participant_room_participant_anonymize import VideoV1RoomRoomParticipantRoomParticipantAnonymize
from openapi_server import util


async def update_room_participant_anonymize(request: web.Request, room_sid, sid) -> web.Response:
    """update_room_participant_anonymize

    

    :param room_sid: The SID of the room with the participant to update.
    :type room_sid: str
    :param sid: The SID of the RoomParticipant resource to update.
    :type sid: str

    """
    return web.Response(status=200)
