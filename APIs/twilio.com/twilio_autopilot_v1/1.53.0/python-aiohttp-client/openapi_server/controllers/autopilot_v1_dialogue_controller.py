from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_dialogue import AutopilotV1AssistantDialogue
from openapi_server import util


async def fetch_dialogue(request: web.Request, assistant_sid, sid) -> web.Response:
    """fetch_dialogue

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Dialogue resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)
