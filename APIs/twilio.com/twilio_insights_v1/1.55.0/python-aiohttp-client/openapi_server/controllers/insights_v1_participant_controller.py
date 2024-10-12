from typing import List, Dict
from aiohttp import web

from openapi_server.models.insights_v1_video_room_summary_video_participant_summary import InsightsV1VideoRoomSummaryVideoParticipantSummary
from openapi_server.models.list_video_participant_summary_response import ListVideoParticipantSummaryResponse
from openapi_server import util


async def fetch_video_participant_summary(request: web.Request, room_sid, participant_sid) -> web.Response:
    """fetch_video_participant_summary

    Get Video Log Analyzer data for a Room Participant.

    :param room_sid: The SID of the Room resource.
    :type room_sid: str
    :param participant_sid: The SID of the Participant resource.
    :type participant_sid: str

    """
    return web.Response(status=200)


async def list_video_participant_summary(request: web.Request, room_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_video_participant_summary

    Get a list of room participants.

    :param room_sid: The SID of the Room resource.
    :type room_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
