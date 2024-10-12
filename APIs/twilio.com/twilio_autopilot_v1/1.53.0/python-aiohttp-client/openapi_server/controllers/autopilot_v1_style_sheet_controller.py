from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_style_sheet import AutopilotV1AssistantStyleSheet
from openapi_server import util


async def fetch_style_sheet(request: web.Request, assistant_sid) -> web.Response:
    """fetch_style_sheet

    Returns Style sheet JSON object for the Assistant

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    :type assistant_sid: str

    """
    return web.Response(status=200)


async def update_style_sheet(request: web.Request, assistant_sid, style_sheet=None) -> web.Response:
    """update_style_sheet

    Updates the style sheet for an Assistant identified by &#x60;assistant_sid&#x60;.

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
    :type assistant_sid: str
    :param style_sheet: The JSON string that describes the style sheet object.
    :type style_sheet: dict | bytes

    """
    style_sheet = object.from_dict(style_sheet)
    return web.Response(status=200)
