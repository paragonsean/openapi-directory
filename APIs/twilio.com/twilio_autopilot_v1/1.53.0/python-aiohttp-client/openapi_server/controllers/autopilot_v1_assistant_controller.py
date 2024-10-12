from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant import AutopilotV1Assistant
from openapi_server.models.list_assistant_response import ListAssistantResponse
from openapi_server import util


async def create_assistant(request: web.Request, callback_events=None, callback_url=None, defaults=None, friendly_name=None, log_queries=None, style_sheet=None, unique_name=None) -> web.Response:
    """create_assistant

    

    :param callback_events: Reserved.
    :type callback_events: str
    :param callback_url: Reserved.
    :type callback_url: str
    :param defaults: A JSON object that defines the Assistant&#39;s [default tasks](https://www.twilio.com/docs/autopilot/api/assistant/defaults) for various scenarios, including initiation actions and fallback tasks.
    :type defaults: dict | bytes
    :param friendly_name: A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str
    :param log_queries: Whether queries should be logged and kept after training. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;true&#x60;. If &#x60;true&#x60;, queries are stored for 30 days, and then deleted. If &#x60;false&#x60;, no queries are stored.
    :type log_queries: bool
    :param style_sheet: The JSON string that defines the Assistant&#39;s [style sheet](https://www.twilio.com/docs/autopilot/api/assistant/stylesheet)
    :type style_sheet: dict | bytes
    :param unique_name: An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. The first 64 characters must be unique.
    :type unique_name: str

    """
    defaults = object.from_dict(defaults)
    style_sheet = object.from_dict(style_sheet)
    return web.Response(status=200)


async def delete_assistant(request: web.Request, sid) -> web.Response:
    """delete_assistant

    

    :param sid: The Twilio-provided string that uniquely identifies the Assistant resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_assistant(request: web.Request, sid) -> web.Response:
    """fetch_assistant

    

    :param sid: The Twilio-provided string that uniquely identifies the Assistant resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_assistant(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_assistant

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_assistant(request: web.Request, sid, callback_events=None, callback_url=None, defaults=None, development_stage=None, friendly_name=None, log_queries=None, style_sheet=None, unique_name=None) -> web.Response:
    """update_assistant

    

    :param sid: The Twilio-provided string that uniquely identifies the Assistant resource to update.
    :type sid: str
    :param callback_events: Reserved.
    :type callback_events: str
    :param callback_url: Reserved.
    :type callback_url: str
    :param defaults: A JSON object that defines the Assistant&#39;s [default tasks](https://www.twilio.com/docs/autopilot/api/assistant/defaults) for various scenarios, including initiation actions and fallback tasks.
    :type defaults: dict | bytes
    :param development_stage: A string describing the state of the assistant.
    :type development_stage: str
    :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str
    :param log_queries: Whether queries should be logged and kept after training. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;true&#x60;. If &#x60;true&#x60;, queries are stored for 30 days, and then deleted. If &#x60;false&#x60;, no queries are stored.
    :type log_queries: bool
    :param style_sheet: The JSON string that defines the Assistant&#39;s [style sheet](https://www.twilio.com/docs/autopilot/api/assistant/stylesheet)
    :type style_sheet: dict | bytes
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. The first 64 characters must be unique.
    :type unique_name: str

    """
    defaults = object.from_dict(defaults)
    style_sheet = object.from_dict(style_sheet)
    return web.Response(status=200)
