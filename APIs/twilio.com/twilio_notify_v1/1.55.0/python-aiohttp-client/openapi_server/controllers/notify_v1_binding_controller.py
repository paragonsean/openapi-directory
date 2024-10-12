from typing import List, Dict
from aiohttp import web

from openapi_server.models.binding_enum_binding_type import BindingEnumBindingType
from openapi_server.models.list_binding_response import ListBindingResponse
from openapi_server.models.notify_v1_service_binding import NotifyV1ServiceBinding
from openapi_server import util


async def create_binding(request: web.Request, service_sid, address, binding_type, identity, credential_sid=None, endpoint=None, notification_protocol_version=None, tag=None) -> web.Response:
    """create_binding

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to create the resource under.
    :type service_sid: str
    :param address: The channel-specific address. For APNS, the device token. For FCM and GCM, the registration token. For SMS, a phone number in E.164 format. For Facebook Messenger, the Messenger ID of the user or a phone number in E.164 format.
    :type address: str
    :param binding_type: 
    :type binding_type: str
    :param identity: The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Up to 20 Bindings can be created for the same Identity in a given Service.
    :type identity: str
    :param credential_sid: The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) resource to be used to send notifications to this Binding. If present, this overrides the Credential specified in the Service resource. Applies to only &#x60;apn&#x60;, &#x60;fcm&#x60;, and &#x60;gcm&#x60; type Bindings.
    :type credential_sid: str
    :param endpoint: Deprecated.
    :type endpoint: str
    :param notification_protocol_version: The protocol version to use to send the notification. This defaults to the value of &#x60;default_xxxx_notification_protocol_version&#x60; for the protocol in the [Service](https://www.twilio.com/docs/notify/api/service-resource). The current version is &#x60;\\\&quot;3\\\&quot;&#x60; for &#x60;apn&#x60;, &#x60;fcm&#x60;, and &#x60;gcm&#x60; type Bindings. The parameter is not applicable to &#x60;sms&#x60; and &#x60;facebook-messenger&#x60; type Bindings as the data format is fixed.
    :type notification_protocol_version: str
    :param tag: A tag that can be used to select the Bindings to notify. Repeat this parameter to specify more than one tag, up to a total of 20 tags.
    :type tag: List[str]

    """
    return web.Response(status=200)


async def delete_binding(request: web.Request, service_sid, sid) -> web.Response:
    """delete_binding

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to delete the resource from.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Binding resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_binding(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_binding

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to fetch the resource from.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Binding resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_binding(request: web.Request, service_sid, start_date=None, end_date=None, identity=None, tag=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_binding

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to read the resource from.
    :type service_sid: str
    :param start_date: Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.
    :type start_date: str
    :param end_date: Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;.
    :type end_date: str
    :param identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)&#39;s &#x60;identity&#x60; value of the resources to read.
    :type identity: List[str]
    :param tag: Only list Bindings that have all of the specified Tags. The following implicit tags are available: &#x60;all&#x60;, &#x60;apn&#x60;, &#x60;fcm&#x60;, &#x60;gcm&#x60;, &#x60;sms&#x60;, &#x60;facebook-messenger&#x60;. Up to 5 tags are allowed.
    :type tag: List[str]
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)
