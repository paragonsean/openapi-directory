from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel_enum_channel_type import ChannelEnumChannelType
from openapi_server.models.channel_enum_webhook_enabled_type import ChannelEnumWebhookEnabledType
from openapi_server.models.chat_v2_service_channel import ChatV2ServiceChannel
from openapi_server.models.list_channel_response import ListChannelResponse
from openapi_server import util


async def create_channel(request: web.Request, service_sid, x_twilio_webhook_enabled=None, attributes=None, created_by=None, date_created=None, date_updated=None, friendly_name=None, type=None, unique_name=None) -> web.Response:
    """create_channel

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Channel resource under.
    :type service_sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: A valid JSON string that contains application-specific data.
    :type attributes: str
    :param created_by: The &#x60;identity&#x60; of the User that created the channel. Default is: &#x60;system&#x60;.
    :type created_by: str
    :param date_created: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this should only be used in cases where a Channel is being recreated from a backup/separate source.
    :type date_created: str
    :param date_updated: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. The default value is &#x60;null&#x60;. Note that this parameter should only be used in cases where a Channel is being recreated from a backup/separate source  and where a Message was previously updated.
    :type date_updated: str
    :param friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param type: 
    :type type: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the Channel resource&#39;s &#x60;sid&#x60; in the URL. This value must be 64 characters or less in length and be unique within the Service.
    :type unique_name: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)


async def delete_channel(request: web.Request, service_sid, sid, x_twilio_webhook_enabled=None) -> web.Response:
    """delete_channel

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.
    :type service_sid: str
    :param sid: The SID of the Channel resource to delete.  This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the Channel resource to delete.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str

    """
    return web.Response(status=200)


async def fetch_channel(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_channel

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Channel resource from.
    :type service_sid: str
    :param sid: The SID of the Channel resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the Channel resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_channel(request: web.Request, service_sid, type=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_channel

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Channel resources from.
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


async def update_channel(request: web.Request, service_sid, sid, x_twilio_webhook_enabled=None, attributes=None, created_by=None, date_created=None, date_updated=None, friendly_name=None, unique_name=None) -> web.Response:
    """update_channel

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Channel resource in.
    :type service_sid: str
    :param sid: The SID of the Channel resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the Channel resource to update.
    :type sid: str
    :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
    :type x_twilio_webhook_enabled: str
    :param attributes: A valid JSON string that contains application-specific data.
    :type attributes: str
    :param created_by: The &#x60;identity&#x60; of the User that created the channel. Default is: &#x60;system&#x60;.
    :type created_by: str
    :param date_created: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this should only be used in cases where a Channel is being recreated from a backup/separate source.
    :type date_created: str
    :param date_updated: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
    :type date_updated: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 256 characters long.
    :type friendly_name: str
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. This value must be 256 characters or less in length and unique within the Service.
    :type unique_name: str

    """
    date_created = util.deserialize_datetime(date_created)
    date_updated = util.deserialize_datetime(date_updated)
    return web.Response(status=200)
