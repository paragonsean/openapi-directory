from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_service_response import ListServiceResponse
from openapi_server.models.messaging_v1_service import MessagingV1Service
from openapi_server.models.service_enum_scan_message_content import ServiceEnumScanMessageContent
from openapi_server import util


async def create_service(request: web.Request, friendly_name, area_code_geomatch=None, fallback_method=None, fallback_to_long_code=None, fallback_url=None, inbound_method=None, inbound_request_url=None, mms_converter=None, scan_message_content=None, smart_encoding=None, status_callback=None, sticky_sender=None, synchronous_validation=None, use_inbound_webhook_on_number=None, usecase=None, validity_period=None) -> web.Response:
    """create_service

    

    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param area_code_geomatch: Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/messaging/services#area-code-geomatch) on the Service Instance.
    :type area_code_geomatch: bool
    :param fallback_method: The HTTP method we should use to call &#x60;fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type fallback_method: str
    :param fallback_to_long_code: [OBSOLETE] Former feature used to fallback to long code sender after certain short code message failures.
    :type fallback_to_long_code: bool
    :param fallback_url: The URL that we call using &#x60;fallback_method&#x60; if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the &#x60;use_inbound_webhook_on_number&#x60; field is enabled then the webhook url defined on the phone number will override the &#x60;fallback_url&#x60; defined for the Messaging Service.
    :type fallback_url: str
    :param inbound_method: The HTTP method we should use to call &#x60;inbound_request_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;.
    :type inbound_method: str
    :param inbound_request_url: The URL we call using &#x60;inbound_method&#x60; when a message is received by any phone number or short code in the Service. When this property is &#x60;null&#x60;, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the &#x60;use_inbound_webhook_on_number&#x60; field is enabled then the webhook url defined on the phone number will override the &#x60;inbound_request_url&#x60; defined for the Messaging Service.
    :type inbound_request_url: str
    :param mms_converter: Whether to enable the [MMS Converter](https://www.twilio.com/docs/messaging/services#mms-converter) for messages sent through the Service instance.
    :type mms_converter: bool
    :param scan_message_content: 
    :type scan_message_content: str
    :param smart_encoding: Whether to enable [Smart Encoding](https://www.twilio.com/docs/messaging/services#smart-encoding) for messages sent through the Service instance.
    :type smart_encoding: bool
    :param status_callback: The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.
    :type status_callback: str
    :param sticky_sender: Whether to enable [Sticky Sender](https://www.twilio.com/docs/messaging/services#sticky-sender) on the Service instance.
    :type sticky_sender: bool
    :param synchronous_validation: Reserved.
    :type synchronous_validation: bool
    :param use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone number will be used or &#x60;inbound_request_url&#x60;/&#x60;fallback_url&#x60; url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the &#x60;inbound_request_url&#x60;/&#x60;fallback_url&#x60; defined for the Messaging Service.
    :type use_inbound_webhook_on_number: bool
    :param usecase: A string that describes the scenario in which the Messaging Service will be used. Possible values are &#x60;notifications&#x60;, &#x60;marketing&#x60;, &#x60;verification&#x60;, &#x60;discussion&#x60;, &#x60;poll&#x60;, &#x60;undeclared&#x60;.
    :type usecase: str
    :param validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from &#x60;1&#x60; to &#x60;14,400&#x60;.
    :type validity_period: int

    """
    return web.Response(status=200)


async def delete_service(request: web.Request, sid) -> web.Response:
    """delete_service

    

    :param sid: The SID of the Service resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service(request: web.Request, sid) -> web.Response:
    """fetch_service

    

    :param sid: The SID of the Service resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_service(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_service(request: web.Request, sid, area_code_geomatch=None, fallback_method=None, fallback_to_long_code=None, fallback_url=None, friendly_name=None, inbound_method=None, inbound_request_url=None, mms_converter=None, scan_message_content=None, smart_encoding=None, status_callback=None, sticky_sender=None, synchronous_validation=None, use_inbound_webhook_on_number=None, usecase=None, validity_period=None) -> web.Response:
    """update_service

    

    :param sid: The SID of the Service resource to update.
    :type sid: str
    :param area_code_geomatch: Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/messaging/services#area-code-geomatch) on the Service Instance.
    :type area_code_geomatch: bool
    :param fallback_method: The HTTP method we should use to call &#x60;fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type fallback_method: str
    :param fallback_to_long_code: [OBSOLETE] Former feature used to fallback to long code sender after certain short code message failures.
    :type fallback_to_long_code: bool
    :param fallback_url: The URL that we call using &#x60;fallback_method&#x60; if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the &#x60;use_inbound_webhook_on_number&#x60; field is enabled then the webhook url defined on the phone number will override the &#x60;fallback_url&#x60; defined for the Messaging Service.
    :type fallback_url: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param inbound_method: The HTTP method we should use to call &#x60;inbound_request_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;.
    :type inbound_method: str
    :param inbound_request_url: The URL we call using &#x60;inbound_method&#x60; when a message is received by any phone number or short code in the Service. When this property is &#x60;null&#x60;, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the &#x60;use_inbound_webhook_on_number&#x60; field is enabled then the webhook url defined on the phone number will override the &#x60;inbound_request_url&#x60; defined for the Messaging Service.
    :type inbound_request_url: str
    :param mms_converter: Whether to enable the [MMS Converter](https://www.twilio.com/docs/messaging/services#mms-converter) for messages sent through the Service instance.
    :type mms_converter: bool
    :param scan_message_content: 
    :type scan_message_content: str
    :param smart_encoding: Whether to enable [Smart Encoding](https://www.twilio.com/docs/messaging/services#smart-encoding) for messages sent through the Service instance.
    :type smart_encoding: bool
    :param status_callback: The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.
    :type status_callback: str
    :param sticky_sender: Whether to enable [Sticky Sender](https://www.twilio.com/docs/messaging/services#sticky-sender) on the Service instance.
    :type sticky_sender: bool
    :param synchronous_validation: Reserved.
    :type synchronous_validation: bool
    :param use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone number will be used or &#x60;inbound_request_url&#x60;/&#x60;fallback_url&#x60; url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the &#x60;inbound_request_url&#x60;/&#x60;fallback_url&#x60; defined for the Messaging Service.
    :type use_inbound_webhook_on_number: bool
    :param usecase: A string that describes the scenario in which the Messaging Service will be used. Possible values are &#x60;notifications&#x60;, &#x60;marketing&#x60;, &#x60;verification&#x60;, &#x60;discussion&#x60;, &#x60;poll&#x60;, &#x60;undeclared&#x60;.
    :type usecase: str
    :param validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from &#x60;1&#x60; to &#x60;14,400&#x60;.
    :type validity_period: int

    """
    return web.Response(status=200)
