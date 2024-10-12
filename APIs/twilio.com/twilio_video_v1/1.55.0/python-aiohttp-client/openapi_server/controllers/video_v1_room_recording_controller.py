from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_room_recording_response import ListRoomRecordingResponse
from openapi_server.models.room_recording_enum_status import RoomRecordingEnumStatus
from openapi_server.models.video_v1_room_room_recording import VideoV1RoomRoomRecording
from openapi_server import util


async def delete_room_recording(request: web.Request, room_sid, sid) -> web.Response:
    """delete_room_recording

    

    :param room_sid: The SID of the room with the RoomRecording resource to delete.
    :type room_sid: str
    :param sid: The SID of the RoomRecording resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_room_recording(request: web.Request, room_sid, sid) -> web.Response:
    """fetch_room_recording

    

    :param room_sid: The SID of the Room resource with the recording to fetch.
    :type room_sid: str
    :param sid: The SID of the RoomRecording resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_room_recording(request: web.Request, room_sid, status=None, source_sid=None, date_created_after=None, date_created_before=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_room_recording

    

    :param room_sid: The SID of the room with the RoomRecording resources to read.
    :type room_sid: str
    :param status: Read only the recordings with this status. Can be: &#x60;processing&#x60;, &#x60;completed&#x60;, or &#x60;deleted&#x60;.
    :type status: str
    :param source_sid: Read only the recordings that have this &#x60;source_sid&#x60;.
    :type source_sid: str
    :param date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
    :type date_created_after: str
    :param date_created_before: Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
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
