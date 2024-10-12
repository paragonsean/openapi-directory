from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel_enum_channel_type import ChannelEnumChannelType
from openapi_server.models.chat_v1_service_channel import ChatV1ServiceChannel
from openapi_server.models.list_channel_response import ListChannelResponse
from openapi_server import util


async def create_channel(request: web.Request, service_sid, attributes=None, friendly_name=None, type=None, unique_name=None) -> web.Response:
    """create_channel

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to create the resource under.
    :type service_sid: str
    :param attributes: A valid JSON string that contains application-specific data.
    :type attributes: str
    :param friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param type: 
    :type type: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. This value must be 64 characters or less in length and be unique within the Service.
    :type unique_name: str

    """
    return web.Response(status=200)


async def delete_channel(request: web.Request, service_sid, sid) -> web.Response:
    """delete_channel

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to delete the resource from.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Channel resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_channel(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_channel

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Channel resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_channel(request: web.Request, service_sid, type=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_channel

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
    :type service_sid: str
    :param type: The visibility of the Channels to read. Can be: &#x60;public&#x60; or &#x60;private&#x60; and defaults to &#x60;public&#x60;.
    :type type: list | bytes
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    type = [ChannelEnumChannelType.from_dict(d) for d in type]
    return web.Response(status=200)


async def update_channel(request: web.Request, service_sid, sid, attributes=None, friendly_name=None, unique_name=None) -> web.Response:
    """update_channel

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to update the resource from.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Channel resource to update.
    :type sid: str
    :param attributes: A valid JSON string that contains application-specific data.
    :type attributes: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. This value must be 64 characters or less in length and be unique within the Service.
    :type unique_name: str

    """
    return web.Response(status=200)
