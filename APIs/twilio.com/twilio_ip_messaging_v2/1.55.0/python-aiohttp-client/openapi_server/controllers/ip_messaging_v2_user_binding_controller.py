from typing import List, Dict
from aiohttp import web

from openapi_server.models.ip_messaging_v2_service_user_user_binding import IpMessagingV2ServiceUserUserBinding
from openapi_server.models.list_user_binding_response import ListUserBindingResponse
from openapi_server.models.user_binding_enum_binding_type import UserBindingEnumBindingType
from openapi_server import util


async def delete_user_binding(request: web.Request, service_sid, user_sid, sid) -> web.Response:
    """delete_user_binding

    

    :param service_sid: 
    :type service_sid: str
    :param user_sid: 
    :type user_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_user_binding(request: web.Request, service_sid, user_sid, sid) -> web.Response:
    """fetch_user_binding

    

    :param service_sid: 
    :type service_sid: str
    :param user_sid: 
    :type user_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_user_binding(request: web.Request, service_sid, user_sid, binding_type=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_user_binding

    

    :param service_sid: 
    :type service_sid: str
    :param user_sid: 
    :type user_sid: str
    :param binding_type: 
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
