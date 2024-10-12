from typing import List, Dict
from aiohttp import web

from openapi_server.models.recording_setting import RecordingSetting
from openapi_server import util


async def v2_phone_numbers_recording_settings_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch recording setting

    Fetches the recording status for a given phone number, based on Do Not Record and Recording Governance for your team. Phone number should be in E.164 format. 

    :param id: E.164 Phone Number
    :type id: str

    """
    return web.Response(status=200)
