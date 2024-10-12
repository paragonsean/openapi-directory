from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_message import ApiV2010AccountMessage
from openapi_server.models.list_message_response import ListMessageResponse
from openapi_server.models.message_enum_address_retention import MessageEnumAddressRetention
from openapi_server.models.message_enum_content_retention import MessageEnumContentRetention
from openapi_server.models.message_enum_risk_check import MessageEnumRiskCheck
from openapi_server.models.message_enum_schedule_type import MessageEnumScheduleType
from openapi_server.models.message_enum_update_status import MessageEnumUpdateStatus
from openapi_server import util


async def create_message(request: web.Request, account_sid, to, address_retention=None, application_sid=None, attempt=None, body=None, content_retention=None, content_sid=None, content_variables=None, force_delivery=None, _from=None, max_price=None, media_url=None, messaging_service_sid=None, persistent_action=None, provide_feedback=None, risk_check=None, schedule_type=None, send_as_mms=None, send_at=None, shorten_urls=None, smart_encoded=None, status_callback=None, validity_period=None) -> web.Response:
    """create_message

    Send a message

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) creating the Message resource.
    :type account_sid: str
    :param to: The recipient&#39;s phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format (for SMS/MMS) or [channel address](https://www.twilio.com/docs/messaging/channels), e.g. &#x60;whatsapp:+15552229999&#x60;.
    :type to: str
    :param address_retention: 
    :type address_retention: str
    :param application_sid: The SID of the associated [TwiML Application](https://www.twilio.com/docs/usage/api/applications). If this parameter is provided, the &#x60;status_callback&#x60; parameter of this request is ignored; [Message status callback requests](https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url) are sent to the TwiML App&#39;s &#x60;message_status_callback&#x60; URL.
    :type application_sid: str
    :param attempt: Total number of attempts made (including this request) to send the message regardless of the provider used
    :type attempt: int
    :param body: The text content of the outgoing message. Can be up to 1,600 characters in length. SMS only: If the &#x60;body&#x60; contains more than 160 [GSM-7](https://www.twilio.com/docs/glossary/what-is-gsm-7-character-encoding) characters (or 70 [UCS-2](https://www.twilio.com/docs/glossary/what-is-ucs-2-character-encoding) characters), the message is segmented and charged accordingly. For long &#x60;body&#x60; text, consider using the [send_as_mms parameter](https://www.twilio.com/blog/mms-for-long-text-messages).
    :type body: str
    :param content_retention: 
    :type content_retention: str
    :param content_sid: For [Content Editor/API](https://www.twilio.com/docs/content) only: The SID of the Content Template to be used with the Message, e.g., &#x60;HXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&#x60;. If this parameter is not provided, a Content Template is not used. Find the SID in the Console on the Content Editor page. For Content API users, the SID is found in Twilio&#39;s response when [creating the Template](https://www.twilio.com/docs/content/content-api-resources#create-templates) or by [fetching your Templates](https://www.twilio.com/docs/content/content-api-resources#fetch-all-content-resources).
    :type content_sid: str
    :param content_variables: For [Content Editor/API](https://www.twilio.com/docs/content) only: Key-value pairs of [Template variables](https://www.twilio.com/docs/content/using-variables-with-content-api) and their substitution values. &#x60;content_sid&#x60; parameter must also be provided. If values are not defined in the &#x60;content_variables&#x60; parameter, the [Template&#39;s default placeholder values](https://www.twilio.com/docs/content/content-api-resources#create-templates) are used.
    :type content_variables: str
    :param force_delivery: Reserved
    :type force_delivery: bool
    :param _from: The sender&#39;s Twilio phone number (in [E.164](https://en.wikipedia.org/wiki/E.164) format), [alphanumeric sender ID](https://www.twilio.com/docs/sms/quickstart), [Wireless SIM](https://www.twilio.com/docs/iot/wireless/programmable-wireless-send-machine-machine-sms-commands), [short code](https://www.twilio.com/en-us/messaging/channels/sms/short-codes), or [channel address](https://www.twilio.com/docs/messaging/channels) (e.g., &#x60;whatsapp:+15554449999&#x60;). The value of the &#x60;from&#x60; parameter must be a sender that is hosted within Twilio and belongs to the Account creating the Message. If you are using &#x60;messaging_service_sid&#x60;, this parameter can be empty (Twilio assigns a &#x60;from&#x60; value from the Messaging Service&#39;s Sender Pool) or you can provide a specific sender from your Sender Pool.
    :type _from: str
    :param max_price: The maximum price in US dollars that you are willing to pay for this Message&#39;s delivery. The value can have up to four decimal places. When the &#x60;max_price&#x60; parameter is provided, the cost of a message is checked before it is sent. If the cost exceeds &#x60;max_price&#x60;, the message is not sent and the Message &#x60;status&#x60; is &#x60;failed&#x60;.
    :type max_price: 
    :param media_url: The URL of media to include in the Message content. &#x60;jpeg&#x60;, &#x60;jpg&#x60;, &#x60;gif&#x60;, and &#x60;png&#x60; file types are fully supported by Twilio and content is formatted for delivery on destination devices. The media size limit is 5 MB for supported file types (&#x60;jpeg&#x60;, &#x60;jpg&#x60;, &#x60;png&#x60;, &#x60;gif&#x60;) and 500 KB for [other types](https://www.twilio.com/docs/messaging/guides/accepted-mime-types) of accepted media. To send more than one image in the message, provide multiple &#x60;media_url&#x60; parameters in the POST request. You can include up to ten &#x60;media_url&#x60; parameters per message. [International](https://support.twilio.com/hc/en-us/articles/223179808-Sending-and-receiving-MMS-messages) and [carrier](https://support.twilio.com/hc/en-us/articles/223133707-Is-MMS-supported-for-all-carriers-in-US-and-Canada-) limits apply.
    :type media_url: List[str]
    :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services) you want to associate with the Message. When this parameter is provided and the &#x60;from&#x60; parameter is omitted, Twilio selects the optimal sender from the Messaging Service&#39;s Sender Pool. You may also provide a &#x60;from&#x60; parameter if you want to use a specific Sender from the Sender Pool.
    :type messaging_service_sid: str
    :param persistent_action: Rich actions for non-SMS/MMS channels. Used for [sending location in WhatsApp messages](https://www.twilio.com/docs/whatsapp/message-features#location-messages-with-whatsapp).
    :type persistent_action: List[str]
    :param provide_feedback: Boolean indicating whether or not you intend to provide delivery confirmation feedback to Twilio (used in conjunction with the [Message Feedback subresource](https://www.twilio.com/docs/sms/api/message-feedback-resource)). Default value is &#x60;false&#x60;.
    :type provide_feedback: bool
    :param risk_check: 
    :type risk_check: str
    :param schedule_type: 
    :type schedule_type: str
    :param send_as_mms: If set to &#x60;true&#x60;, Twilio delivers the message as a single MMS message, regardless of the presence of media.
    :type send_as_mms: bool
    :param send_at: The time that Twilio will send the message. Must be in ISO 8601 format.
    :type send_at: str
    :param shorten_urls: For Messaging Services with [Link Shortening configured](https://www.twilio.com/docs/messaging/features/link-shortening) only: A Boolean indicating whether or not Twilio should shorten links in the &#x60;body&#x60; of the Message. Default value is &#x60;false&#x60;. If &#x60;true&#x60;, the &#x60;messaging_service_sid&#x60; parameter must also be provided.
    :type shorten_urls: bool
    :param smart_encoded: Whether to detect Unicode characters that have a similar GSM-7 character and replace them. Can be: &#x60;true&#x60; or &#x60;false&#x60;.
    :type smart_encoded: bool
    :param status_callback: The URL of the endpoint to which Twilio sends [Message status callback requests](https://www.twilio.com/docs/sms/api/message-resource#twilios-request-to-the-statuscallback-url). URL must contain a valid hostname and underscores are not allowed. If you include this parameter with the &#x60;messaging_service_sid&#x60;, Twilio uses this URL instead of the Status Callback URL of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource). 
    :type status_callback: str
    :param validity_period: The maximum length in seconds that the Message can remain in Twilio&#39;s outgoing message queue. If a queued Message exceeds the &#x60;validity_period&#x60;, the Message is not sent. Accepted values are integers from &#x60;1&#x60; to &#x60;14400&#x60;. Default value is &#x60;14400&#x60;. A &#x60;validity_period&#x60; greater than &#x60;5&#x60; is recommended. [Learn more about the validity period](https://www.twilio.com/blog/take-more-control-of-outbound-messages-using-validity-period-html)
    :type validity_period: int

    """
    send_at = util.deserialize_datetime(send_at)
    return web.Response(status=200)


async def delete_message(request: web.Request, account_sid, sid) -> web.Response:
    """delete_message

    Deletes a Message resource from your account

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource
    :type account_sid: str
    :param sid: The SID of the Message resource you wish to delete
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_message(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_message

    Fetch a specific Message

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource
    :type account_sid: str
    :param sid: The SID of the Message resource to be fetched
    :type sid: str

    """
    return web.Response(status=200)


async def list_message(request: web.Request, account_sid, to=None, _from=None, date_sent=None, date_sent2=None, date_sent3=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_message

    Retrieve a list of Message resources associated with a Twilio Account

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resources.
    :type account_sid: str
    :param to: Filter by recipient. For example: Set this &#x60;to&#x60; parameter to &#x60;+15558881111&#x60; to retrieve a list of Message resources with &#x60;to&#x60; properties of &#x60;+15558881111&#x60;
    :type to: str
    :param _from: Filter by sender. For example: Set this &#x60;from&#x60; parameter to &#x60;+15552229999&#x60; to retrieve a list of Message resources with &#x60;from&#x60; properties of &#x60;+15552229999&#x60;
    :type _from: str
    :param date_sent: Filter by Message &#x60;sent_date&#x60;. Accepts GMT dates in the following formats: &#x60;YYYY-MM-DD&#x60; (to find Messages with a specific &#x60;sent_date&#x60;), &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; (to find Messages with &#x60;sent_date&#x60;s on and before a specific date), and &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; (to find Messages with &#x60;sent_dates&#x60; on and after a specific date).
    :type date_sent: str
    :param date_sent2: Filter by Message &#x60;sent_date&#x60;. Accepts GMT dates in the following formats: &#x60;YYYY-MM-DD&#x60; (to find Messages with a specific &#x60;sent_date&#x60;), &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; (to find Messages with &#x60;sent_date&#x60;s on and before a specific date), and &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; (to find Messages with &#x60;sent_dates&#x60; on and after a specific date).
    :type date_sent2: str
    :param date_sent3: Filter by Message &#x60;sent_date&#x60;. Accepts GMT dates in the following formats: &#x60;YYYY-MM-DD&#x60; (to find Messages with a specific &#x60;sent_date&#x60;), &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; (to find Messages with &#x60;sent_date&#x60;s on and before a specific date), and &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; (to find Messages with &#x60;sent_dates&#x60; on and after a specific date).
    :type date_sent3: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    date_sent = util.deserialize_datetime(date_sent)
    date_sent2 = util.deserialize_datetime(date_sent2)
    date_sent3 = util.deserialize_datetime(date_sent3)
    return web.Response(status=200)


async def update_message(request: web.Request, account_sid, sid, body=None, status=None) -> web.Response:
    """update_message

    Update a Message resource (used to redact Message &#x60;body&#x60; text and to cancel not-yet-sent messages)

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resources to update.
    :type account_sid: str
    :param sid: The SID of the Message resource to be updated
    :type sid: str
    :param body: The new &#x60;body&#x60; of the Message resource. To redact the text content of a Message, this parameter&#39;s value must be an empty string
    :type body: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)
