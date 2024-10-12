from typing import List, Dict
from aiohttp import web

from openapi_server.models.insights_v1_video_room_summary import InsightsV1VideoRoomSummary
from openapi_server.models.list_video_room_summary_response import ListVideoRoomSummaryResponse
from openapi_server.models.video_room_summary_enum_codec import VideoRoomSummaryEnumCodec
from openapi_server.models.video_room_summary_enum_room_type import VideoRoomSummaryEnumRoomType
from openapi_server import util


async def fetch_video_room_summary(request: web.Request, room_sid) -> web.Response:
    """fetch_video_room_summary

    Get Video Log Analyzer data for a Room.

    :param room_sid: The SID of the Room resource.
    :type room_sid: str

    """
    return web.Response(status=200)


async def list_video_room_summary(request: web.Request, room_type=None, codec=None, room_name=None, created_after=None, created_before=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_video_room_summary

    Get a list of Programmable Video Rooms.

    :param room_type: Type of room. Can be &#x60;go&#x60;, &#x60;peer_to_peer&#x60;, &#x60;group&#x60;, or &#x60;group_small&#x60;.
    :type room_type: list | bytes
    :param codec: Codecs used by participants in the room. Can be &#x60;VP8&#x60;, &#x60;H264&#x60;, or &#x60;VP9&#x60;.
    :type codec: list | bytes
    :param room_name: Room friendly name.
    :type room_name: str
    :param created_after: Only read rooms that started on or after this ISO 8601 timestamp.
    :type created_after: str
    :param created_before: Only read rooms that started before this ISO 8601 timestamp.
    :type created_before: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    room_type = [VideoRoomSummaryEnumRoomType.from_dict(d) for d in room_type]
    codec = [VideoRoomSummaryEnumCodec.from_dict(d) for d in codec]
    created_after = util.deserialize_datetime(created_after)
    created_before = util.deserialize_datetime(created_before)
    return web.Response(status=200)
