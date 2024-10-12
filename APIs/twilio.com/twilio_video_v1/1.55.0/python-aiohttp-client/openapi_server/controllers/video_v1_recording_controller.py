from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_recording_response import ListRecordingResponse
from openapi_server.models.recording_enum_status import RecordingEnumStatus
from openapi_server.models.recording_enum_type import RecordingEnumType
from openapi_server.models.video_v1_recording import VideoV1Recording
from openapi_server import util


async def delete_recording(request: web.Request, sid) -> web.Response:
    """delete_recording

    Delete a Recording resource identified by a Recording SID.

    :param sid: The SID of the Recording resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_recording(request: web.Request, sid) -> web.Response:
    """fetch_recording

    Returns a single Recording resource identified by a Recording SID.

    :param sid: The SID of the Recording resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_recording(request: web.Request, status=None, source_sid=None, grouping_sid=None, date_created_after=None, date_created_before=None, media_type=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_recording

    List of all Track recordings.

    :param status: Read only the recordings that have this status. Can be: &#x60;processing&#x60;, &#x60;completed&#x60;, or &#x60;deleted&#x60;.
    :type status: str
    :param source_sid: Read only the recordings that have this &#x60;source_sid&#x60;.
    :type source_sid: str
    :param grouping_sid: Read only recordings with this &#x60;grouping_sid&#x60;, which may include a &#x60;participant_sid&#x60; and/or a &#x60;room_sid&#x60;.
    :type grouping_sid: List[str]
    :param date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
    :type date_created_after: str
    :param date_created_before: Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as &#x60;YYYY-MM-DDThh:mm:ss+|-hh:mm&#x60; or &#x60;YYYY-MM-DDThh:mm:ssZ&#x60;.
    :type date_created_before: str
    :param media_type: Read only recordings that have this media type. Can be either &#x60;audio&#x60; or &#x60;video&#x60;.
    :type media_type: str
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
