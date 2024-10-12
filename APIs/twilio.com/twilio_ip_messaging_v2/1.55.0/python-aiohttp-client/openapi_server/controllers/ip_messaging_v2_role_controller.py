from typing import List, Dict
from aiohttp import web

from openapi_server.models.ip_messaging_v2_service_role import IpMessagingV2ServiceRole
from openapi_server.models.list_role_response import ListRoleResponse
from openapi_server.models.role_enum_role_type import RoleEnumRoleType
from openapi_server import util


async def create_role(request: web.Request, service_sid, friendly_name, permission, type) -> web.Response:
    """create_role

    

    :param service_sid: 
    :type service_sid: str
    :param friendly_name: 
    :type friendly_name: str
    :param permission: 
    :type permission: List[str]
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def delete_role(request: web.Request, service_sid, sid) -> web.Response:
    """delete_role

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_role(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_role

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_role(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_role

    

    :param service_sid: 
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_role(request: web.Request, service_sid, sid, permission) -> web.Response:
    """update_role

    

    :param service_sid: 
    :type service_sid: str
    :param sid: 
    :type sid: str
    :param permission: 
    :type permission: List[str]

    """
    return web.Response(status=200)
