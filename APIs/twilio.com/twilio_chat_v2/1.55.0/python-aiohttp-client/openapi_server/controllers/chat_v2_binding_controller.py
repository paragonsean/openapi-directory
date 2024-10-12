from typing import List, Dict
from aiohttp import web

from openapi_server.models.binding_enum_binding_type import BindingEnumBindingType
from openapi_server.models.chat_v2_service_binding import ChatV2ServiceBinding
from openapi_server.models.list_binding_response import ListBindingResponse
from openapi_server import util


async def delete_binding(request: web.Request, service_sid, sid) -> web.Response:
    """delete_binding

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the Binding resource from.
    :type service_sid: str
    :param sid: The SID of the Binding resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_binding(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_binding

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Binding resource from.
    :type service_sid: str
    :param sid: The SID of the Binding resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_binding(request: web.Request, service_sid, binding_type=None, identity=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_binding

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Binding resources from.
    :type service_sid: str
    :param binding_type: The push technology used by the Binding resources to read.  Can be: &#x60;apn&#x60;, &#x60;gcm&#x60;, or &#x60;fcm&#x60;.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
    :type binding_type: list | bytes
    :param identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)&#39;s &#x60;identity&#x60; value of the resources to read. See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more details.
    :type identity: List[str]
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    binding_type = [BindingEnumBindingType.from_dict(d) for d in binding_type]
    return web.Response(status=200)
