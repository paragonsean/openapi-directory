from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v2_web_channel import FlexV2WebChannel
from openapi_server import util


async def create_web_channel(request: web.Request, address_sid, chat_friendly_name=None, customer_friendly_name=None, pre_engagement_data=None) -> web.Response:
    """create_web_channel

    

    :param address_sid: The SID of the Conversations Address. See [Address Configuration Resource](https://www.twilio.com/docs/conversations/api/address-configuration-resource) for configuration details. When a conversation is created on the Flex backend, the callback URL will be set to the corresponding Studio Flow SID or webhook URL in your address configuration.
    :type address_sid: str
    :param chat_friendly_name: The Conversation&#39;s friendly name. See the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource) for an example.
    :type chat_friendly_name: str
    :param customer_friendly_name: The Conversation participant&#39;s friendly name. See the [Conversation Participant Resource](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) for an example.
    :type customer_friendly_name: str
    :param pre_engagement_data: The pre-engagement data.
    :type pre_engagement_data: str

    """
    return web.Response(status=200)
