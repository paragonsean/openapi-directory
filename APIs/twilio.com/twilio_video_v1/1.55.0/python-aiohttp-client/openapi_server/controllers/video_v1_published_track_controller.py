from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_room_participant_published_track_response import ListRoomParticipantPublishedTrackResponse
from openapi_server.models.video_v1_room_room_participant_room_participant_published_track import VideoV1RoomRoomParticipantRoomParticipantPublishedTrack
from openapi_server import util


async def fetch_room_participant_published_track(request: web.Request, room_sid, participant_sid, sid) -> web.Response:
    """fetch_room_participant_published_track

    Returns a single Track resource represented by TrackName or SID.

    :param room_sid: The SID of the Room resource where the Track resource to fetch is published.
    :type room_sid: str
    :param participant_sid: The SID of the Participant resource with the published track to fetch.
    :type participant_sid: str
    :param sid: The SID of the RoomParticipantPublishedTrack resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_room_participant_published_track(request: web.Request, room_sid, participant_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_room_participant_published_track

    Returns a list of tracks associated with a given Participant. Only &#x60;currently&#x60; Published Tracks are in the list resource.

    :param room_sid: The SID of the Room resource where the Track resources to read are published.
    :type room_sid: str
    :param participant_sid: The SID of the Participant resource with the published tracks to read.
    :type participant_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
