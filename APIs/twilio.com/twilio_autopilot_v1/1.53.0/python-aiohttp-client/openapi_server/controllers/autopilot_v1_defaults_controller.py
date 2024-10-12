from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_defaults import AutopilotV1AssistantDefaults
from openapi_server import util


async def fetch_defaults(request: web.Request, assistant_sid) -> web.Response:
    """fetch_defaults

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    :type assistant_sid: str

    """
    return web.Response(status=200)


async def update_defaults(request: web.Request, assistant_sid, defaults=None) -> web.Response:
    """update_defaults

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
    :type assistant_sid: str
    :param defaults: A JSON string that describes the default task links for the &#x60;assistant_initiation&#x60;, &#x60;collect&#x60;, and &#x60;fallback&#x60; situations.
    :type defaults: dict | bytes

    """
    defaults = object.from_dict(defaults)
    return web.Response(status=200)
