from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_media_recording_response import ListMediaRecordingResponse
from openapi_server.models.media_recording_enum_order import MediaRecordingEnumOrder
from openapi_server.models.media_recording_enum_status import MediaRecordingEnumStatus
from openapi_server.models.media_v1_media_recording import MediaV1MediaRecording
from openapi_server import util


async def delete_media_recording(request: web.Request, sid) -> web.Response:
    """delete_media_recording

    Deletes a MediaRecording resource identified by a SID.

    :param sid: The SID of the MediaRecording resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_media_recording(request: web.Request, sid) -> web.Response:
    """fetch_media_recording

    Returns a single MediaRecording resource identified by a SID.

    :param sid: The SID of the MediaRecording resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_media_recording(request: web.Request, order=None, status=None, processor_sid=None, source_sid=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_media_recording

    Returns a list of MediaRecordings.

    :param order: The sort order of the list by &#x60;date_created&#x60;. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) with &#x60;desc&#x60; as the default.
    :type order: str
    :param status: Status to filter by, with possible values &#x60;processing&#x60;, &#x60;completed&#x60;, &#x60;deleted&#x60;, or &#x60;failed&#x60;.
    :type status: str
    :param processor_sid: SID of a MediaProcessor to filter by.
    :type processor_sid: str
    :param source_sid: SID of a MediaRecording source to filter by.
    :type source_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
