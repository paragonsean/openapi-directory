from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_room_participant_subscribed_track_response import ListRoomParticipantSubscribedTrackResponse
from openapi_server.models.video_v1_room_room_participant_room_participant_subscribed_track import VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack
from openapi_server import util


async def fetch_room_participant_subscribed_track(request: web.Request, room_sid, participant_sid, sid) -> web.Response:
    """fetch_room_participant_subscribed_track

    Returns a single Track resource represented by &#x60;track_sid&#x60;.  Note: This is one resource with the Video API that requires a SID, be Track Name on the subscriber side is not guaranteed to be unique.

    :param room_sid: The SID of the Room where the Track resource to fetch is subscribed.
    :type room_sid: str
    :param participant_sid: The SID of the participant that subscribes to the Track resource to fetch.
    :type participant_sid: str
    :param sid: The SID of the RoomParticipantSubscribedTrack resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_room_participant_subscribed_track(request: web.Request, room_sid, participant_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_room_participant_subscribed_track

    Returns a list of tracks that are subscribed for the participant.

    :param room_sid: The SID of the Room resource with the Track resources to read.
    :type room_sid: str
    :param participant_sid: The SID of the participant that subscribes to the Track resources to read.
    :type participant_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
