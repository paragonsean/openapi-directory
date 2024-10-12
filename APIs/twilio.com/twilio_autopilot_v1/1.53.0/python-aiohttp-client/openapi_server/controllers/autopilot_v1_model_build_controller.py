from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_model_build import AutopilotV1AssistantModelBuild
from openapi_server.models.list_model_build_response import ListModelBuildResponse
from openapi_server import util


async def create_model_build(request: web.Request, assistant_sid, status_callback=None, unique_name=None) -> web.Response:
    """create_model_build

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the new resource.
    :type assistant_sid: str
    :param status_callback: The URL we should call using a POST method to send status information to your application.
    :type status_callback: str
    :param unique_name: An application-defined string that uniquely identifies the new resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource.
    :type unique_name: str

    """
    return web.Response(status=200)


async def delete_model_build(request: web.Request, assistant_sid, sid) -> web.Response:
    """delete_model_build

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to delete.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the ModelBuild resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_model_build(request: web.Request, assistant_sid, sid) -> web.Response:
    """fetch_model_build

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the ModelBuild resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_model_build(request: web.Request, assistant_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_model_build

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.
    :type assistant_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_model_build(request: web.Request, assistant_sid, sid, unique_name=None) -> web.Response:
    """update_model_build

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the ModelBuild resource to update.
    :type sid: str
    :param unique_name: An application-defined string that uniquely identifies the resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource.
    :type unique_name: str

    """
    return web.Response(status=200)
