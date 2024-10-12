from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_room_participant_response import ListRoomParticipantResponse
from openapi_server.models.room_participant_enum_status import RoomParticipantEnumStatus
from openapi_server.models.video_v1_room_room_participant import VideoV1RoomRoomParticipant
from openapi_server import util


async def fetch_room_participant(request: web.Request, room_sid, sid) -> web.Response:
    """fetch_room_participant

    

    :param room_sid: The SID of the room with the Participant resource to fetch.
    :type room_sid: str
    :param sid: The SID of the RoomParticipant resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_room_participant(request: web.Request, room_sid, status=None, identity=None, date_created_after=None, date_created_before=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_room_participant

    

    :param room_sid: The SID of the room with the Participant resources to read.
    :type room_sid: str
    :param status: Read only the participants with this status. Can be: &#x60;connected&#x60; or &#x60;disconnected&#x60;. For &#x60;in-progress&#x60; Rooms the default Status is &#x60;connected&#x60;, for &#x60;completed&#x60; Rooms only &#x60;disconnected&#x60; Participants are returned.
    :type status: str
    :param identity: Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) &#x60;identity&#x60; value.
    :type identity: str
    :param date_created_after: Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
    :type date_created_after: str
    :param date_created_before: Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
    :type date_created_before: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    date_created_after = util.deserialize_datetime(date_created_after)
    date_created_before = util.deserialize_datetime(date_created_before)
    return web.Response(status=200)


async def update_room_participant(request: web.Request, room_sid, sid, status=None) -> web.Response:
    """update_room_participant

    

    :param room_sid: The SID of the room with the participant to update.
    :type room_sid: str
    :param sid: The SID of the RoomParticipant resource to update.
    :type sid: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)
