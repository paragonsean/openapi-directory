from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel_webhook_enum_method import ChannelWebhookEnumMethod
from openapi_server.models.channel_webhook_enum_type import ChannelWebhookEnumType
from openapi_server.models.chat_v2_service_channel_channel_webhook import ChatV2ServiceChannelChannelWebhook
from openapi_server.models.list_channel_webhook_response import ListChannelWebhookResponse
from openapi_server import util


async def create_channel_webhook(request: web.Request, service_sid, channel_sid, type, configuration_filters=None, configuration_flow_sid=None, configuration_method=None, configuration_retry_count=None, configuration_triggers=None, configuration_url=None) -> web.Response:
    """create_channel_webhook

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to create the Webhook resource under.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Channel Webhook resource belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param type: 
    :type type: str
    :param configuration_filters: The events that cause us to call the Channel Webhook. Used when &#x60;type&#x60; is &#x60;webhook&#x60;. This parameter takes only one event. To specify more than one event, repeat this parameter for each event. For the list of possible events, see [Webhook Event Triggers](https://www.twilio.com/docs/chat/webhook-events#webhook-event-trigger).
    :type configuration_filters: List[str]
    :param configuration_flow_sid: The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-api/flow) to call when an event in &#x60;configuration.filters&#x60; occurs. Used only when &#x60;type&#x60; is &#x60;studio&#x60;.
    :type configuration_flow_sid: str
    :param configuration_method: 
    :type configuration_method: str
    :param configuration_retry_count: The number of times to retry the webhook if the first attempt fails. Can be an integer between 0 and 3, inclusive, and the default is 0.
    :type configuration_retry_count: int
    :param configuration_triggers: A string that will cause us to call the webhook when it is present in a message body. This parameter takes only one trigger string. To specify more than one, repeat this parameter for each trigger string up to a total of 5 trigger strings. Used only when &#x60;type&#x60; &#x3D; &#x60;trigger&#x60;.
    :type configuration_triggers: List[str]
    :param configuration_url: The URL of the webhook to call using the &#x60;configuration.method&#x60;.
    :type configuration_url: str

    """
    return web.Response(status=200)


async def delete_channel_webhook(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """delete_channel_webhook

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to delete the Webhook resource from.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to delete belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param sid: The SID of the Channel Webhook resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_channel_webhook(request: web.Request, service_sid, channel_sid, sid) -> web.Response:
    """fetch_channel_webhook

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to fetch the Webhook resource from.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to fetch belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param sid: The SID of the Channel Webhook resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_channel_webhook(request: web.Request, service_sid, channel_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_channel_webhook

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to read the resources from.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resources to read belong to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_channel_webhook(request: web.Request, service_sid, channel_sid, sid, configuration_filters=None, configuration_flow_sid=None, configuration_method=None, configuration_retry_count=None, configuration_triggers=None, configuration_url=None) -> web.Response:
    """update_channel_webhook

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel that has the Webhook resource to update.
    :type service_sid: str
    :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to update belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;.
    :type channel_sid: str
    :param sid: The SID of the Channel Webhook resource to update.
    :type sid: str
    :param configuration_filters: The events that cause us to call the Channel Webhook. Used when &#x60;type&#x60; is &#x60;webhook&#x60;. This parameter takes only one event. To specify more than one event, repeat this parameter for each event. For the list of possible events, see [Webhook Event Triggers](https://www.twilio.com/docs/chat/webhook-events#webhook-event-trigger).
    :type configuration_filters: List[str]
    :param configuration_flow_sid: The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-api/flow) to call when an event in &#x60;configuration.filters&#x60; occurs. Used only when &#x60;type&#x60; &#x3D; &#x60;studio&#x60;.
    :type configuration_flow_sid: str
    :param configuration_method: 
    :type configuration_method: str
    :param configuration_retry_count: The number of times to retry the webhook if the first attempt fails. Can be an integer between 0 and 3, inclusive, and the default is 0.
    :type configuration_retry_count: int
    :param configuration_triggers: A string that will cause us to call the webhook when it is present in a message body. This parameter takes only one trigger string. To specify more than one, repeat this parameter for each trigger string up to a total of 5 trigger strings. Used only when &#x60;type&#x60; &#x3D; &#x60;trigger&#x60;.
    :type configuration_triggers: List[str]
    :param configuration_url: The URL of the webhook to call using the &#x60;configuration.method&#x60;.
    :type configuration_url: str

    """
    return web.Response(status=200)
