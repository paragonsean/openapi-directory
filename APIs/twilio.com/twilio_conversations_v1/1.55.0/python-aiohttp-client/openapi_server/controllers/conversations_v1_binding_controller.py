from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversations_v1_service_service_binding import ConversationsV1ServiceServiceBinding
from openapi_server.models.list_service_binding_response import ListServiceBindingResponse
from openapi_server.models.service_binding_enum_binding_type import ServiceBindingEnumBindingType
from openapi_server import util


async def delete_service_binding(request: web.Request, chat_service_sid, sid) -> web.Response:
    """delete_service_binding

    Remove a push notification binding from the conversation service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to delete the Binding resource from.
    :type chat_service_sid: str
    :param sid: The SID of the Binding resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_service_binding(request: web.Request, chat_service_sid, sid) -> web.Response:
    """fetch_service_binding

    Fetch a push notification binding from the conversation service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Binding resource is associated with.
    :type chat_service_sid: str
    :param sid: A 34 character string that uniquely identifies this resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_service_binding(request: web.Request, chat_service_sid, binding_type=None, identity=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_service_binding

    Retrieve a list of all push notification bindings in the conversation service

    :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Binding resource is associated with.
    :type chat_service_sid: str
    :param binding_type: The push technology used by the Binding resources to read.  Can be: &#x60;apn&#x60;, &#x60;gcm&#x60;, or &#x60;fcm&#x60;.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
    :type binding_type: list | bytes
    :param identity: The identity of a [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) this binding belongs to. See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more details.
    :type identity: List[str]
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    binding_type = [ServiceBindingEnumBindingType.from_dict(d) for d in binding_type]
    return web.Response(status=200)
