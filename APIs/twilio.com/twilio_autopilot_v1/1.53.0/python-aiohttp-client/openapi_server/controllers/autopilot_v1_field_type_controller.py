from typing import List, Dict
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_field_type import AutopilotV1AssistantFieldType
from openapi_server.models.list_field_type_response import ListFieldTypeResponse
from openapi_server import util


async def create_field_type(request: web.Request, assistant_sid, unique_name, friendly_name=None) -> web.Response:
    """create_field_type

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the new resource.
    :type assistant_sid: str
    :param unique_name: An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. The first 64 characters must be unique.
    :type unique_name: str
    :param friendly_name: A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_field_type(request: web.Request, assistant_sid, sid) -> web.Response:
    """delete_field_type

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to delete.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the FieldType resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_field_type(request: web.Request, assistant_sid, sid) -> web.Response:
    """fetch_field_type

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the FieldType resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_field_type(request: web.Request, assistant_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_field_type

    

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


async def update_field_type(request: web.Request, assistant_sid, sid, friendly_name=None, unique_name=None) -> web.Response:
    """update_field_type

    

    :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the to update.
    :type assistant_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the FieldType resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
    :type friendly_name: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. The first 64 characters must be unique.
    :type unique_name: str

    """
    return web.Response(status=200)
