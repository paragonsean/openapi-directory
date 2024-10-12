from typing import List, Dict
from aiohttp import web

from openapi_server.models.send_an_sms200_response import SendAnSms200Response
from openapi_server.models.send_an_sms200_response1 import SendAnSms200Response1
from openapi_server import util


async def send_an_sms(request: web.Request, format, api_key, _from, to, account_ref=None, api_secret=None, body=None, param_callback=None, client_ref=None, content_id=None, entity_id=None, message_class=None, protocol_id=None, sig=None, status_report_req=None, text=None, ttl=None, type=None, udh=None) -> web.Response:
    """Send an SMS

    Send an outbound SMS from your Vonage account

    :param format: The format of the response
    :type format: str
    :param api_key: Your API key
    :type api_key: str
    :param _from: The name or number the message should be sent from. Alphanumeric senderID&#39;s are not supported in all countries, see [Global Messaging](/messaging/sms/guides/global-messaging#country-specific-features) for more details. If alphanumeric, spaces will be ignored. Numbers are specified in E.164 format.
    :type _from: str
    :param to: The number that the message should be sent to. Numbers are specified in E.164 format.
    :type to: str
    :param account_ref: **Advanced**: An optional string used to identify separate accounts using the SMS endpoint for billing purposes. To use this feature, please email [support@nexmo.com](mailto:support@nexmo.com)
    :type account_ref: str
    :param api_secret: Your API secret. Required unless &#x60;sig&#x60; is provided
    :type api_secret: str
    :param body: **Advanced**: Hex encoded binary data. Depends on &#x60;type&#x60; parameter having the value &#x60;binary&#x60;.
    :type body: str
    :param param_callback: **Advanced**: The webhook endpoint the delivery receipt for this sms is sent to. This parameter overrides the webhook endpoint you set in Dashboard. Max 100 characters.
    :type param_callback: str
    :param client_ref: **Advanced**: You can optionally include your own reference of up to 100 characters.
    :type client_ref: str
    :param content_id: **Advanced**: A string parameter that satisfies regulatory requirements when sending an SMS to specific countries. For more information please refer to the [Country-Specific Outbound SMS Features](https://help.nexmo.com/hc/en-us/articles/115011781468)
    :type content_id: str
    :param entity_id: **Advanced**: A string parameter that satisfies regulatory requirements when sending an SMS to specific countries. For more information please refer to the [Country-Specific Outbound SMS Features](https://help.nexmo.com/hc/en-us/articles/115011781468)
    :type entity_id: str
    :param message_class: **Advanced**: The Data Coding Scheme value of the message
    :type message_class: int
    :param protocol_id: **Advanced**: The value of the [protocol identifier](https://en.wikipedia.org/wiki/GSM_03.40#Protocol_Identifier) to use. Ensure that the value is aligned with &#x60;udh&#x60;.
    :type protocol_id: int
    :param sig: The hash of the request parameters in alphabetical order, a timestamp and the signature secret. See [Signing Requests](/concepts/guides/signing-messages) for more details.
    :type sig: str
    :param status_report_req: **Advanced**: Boolean indicating if you like to receive a [Delivery Receipt](/messaging/sms/building-blocks/receive-a-delivery-receipt).
    :type status_report_req: bool
    :param text: The body of the message being sent. If your message contains characters that can be encoded according to the GSM Standard and Extended tables then you can set the &#x60;type&#x60; to &#x60;text&#x60;. If your message contains characters outside this range, then you will need to set the &#x60;type&#x60; to &#x60;unicode&#x60;.
    :type text: str
    :param ttl: **Advanced**: The duration in milliseconds the delivery of an SMS will be attempted.§§ By default Vonage attempts delivery for 72 hours, however the maximum effective value depends on the operator and is typically 24 - 48 hours. We recommend this value should be kept at its default or at least 30 minutes.
    :type ttl: int
    :param type: **Advanced**: The format of the message body
    :type type: str
    :param udh: **Advanced**: Your custom Hex encoded [User Data Header](https://en.wikipedia.org/wiki/User_Data_Header). Depends on &#x60;type&#x60; parameter having the value &#x60;binary&#x60;.
    :type udh: str

    """
    return web.Response(status=200)
