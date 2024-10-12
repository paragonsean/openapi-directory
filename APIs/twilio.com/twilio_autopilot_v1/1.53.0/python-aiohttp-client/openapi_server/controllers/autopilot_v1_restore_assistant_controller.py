from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_restore_assistant import AutopilotV1RestoreAssistant
from openapi_server import util


async def update_restore_assistant(request: web.Request, assistant) -> web.Response:
    """update_restore_assistant

    

    :param assistant: The Twilio-provided string that uniquely identifies the Assistant resource to restore.
    :type assistant: str

    """
    return web.Response(status=200)
