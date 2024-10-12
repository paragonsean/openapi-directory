from typing import List, Dict
from aiohttp import web

from openapi_server.models.chat_v2_service_user_user_binding import ChatV2ServiceUserUserBinding
from openapi_server.models.list_user_binding_response import ListUserBindingResponse
from openapi_server.models.user_binding_enum_binding_type import UserBindingEnumBindingType
from openapi_server import util


async def delete_user_binding(request: web.Request, service_sid, user_sid, sid) -> web.Response:
    """delete_user_binding

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the User Binding resource from.
    :type service_sid: str
    :param user_sid: The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) with the User Binding resources to delete.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
    :type user_sid: str
    :param sid: The SID of the User Binding resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_user_binding(request: web.Request, service_sid, user_sid, sid) -> web.Response:
    """fetch_user_binding

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the User Binding resource from.
    :type service_sid: str
    :param user_sid: The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) with the User Binding resource to fetch.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
    :type user_sid: str
    :param sid: The SID of the User Binding resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_user_binding(request: web.Request, service_sid, user_sid, binding_type=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_user_binding

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the User Binding resources from.
    :type service_sid: str
    :param user_sid: The SID of the [User](https://www.twilio.com/docs/chat/rest/user-resource) with the User Binding resources to read.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
    :type user_sid: str
    :param binding_type: The push technology used by the User Binding resources to read. Can be: &#x60;apn&#x60;, &#x60;gcm&#x60;, or &#x60;fcm&#x60;.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
    :type binding_type: list | bytes
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    binding_type = [UserBindingEnumBindingType.from_dict(d) for d in binding_type]
    return web.Response(status=200)
