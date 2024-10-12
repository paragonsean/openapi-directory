from typing import List, Dict
from aiohttp import web

from openapi_server.models.recording_enum_recording_mode import RecordingEnumRecordingMode
from openapi_server.models.recording_enum_recording_trim import RecordingEnumRecordingTrim
from openapi_server.models.trunking_v1_trunk_recording import TrunkingV1TrunkRecording
from openapi_server import util


async def fetch_recording(request: web.Request, trunk_sid) -> web.Response:
    """fetch_recording

    

    :param trunk_sid: The SID of the Trunk from which to fetch the recording settings.
    :type trunk_sid: str

    """
    return web.Response(status=200)


async def update_recording(request: web.Request, trunk_sid, mode=None, trim=None) -> web.Response:
    """update_recording

    

    :param trunk_sid: The SID of the Trunk that will have its recording settings updated.
    :type trunk_sid: str
    :param mode: 
    :type mode: str
    :param trim: 
    :type trim: str

    """
    return web.Response(status=200)
