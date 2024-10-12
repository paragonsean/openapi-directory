from typing import List, Dict
from aiohttp import web

from openapi_server.models.chat_v2_service_role import ChatV2ServiceRole
from openapi_server.models.list_role_response import ListRoleResponse
from openapi_server.models.role_enum_role_type import RoleEnumRoleType
from openapi_server import util


async def create_role(request: web.Request, service_sid, friendly_name, permission, type) -> web.Response:
    """create_role

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Role resource under.
    :type service_sid: str
    :param friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param permission: A permission that you grant to the new role. Only one permission can be granted per parameter. To assign more than one permission, repeat this parameter for each permission value. The values for this parameter depend on the role&#39;s &#x60;type&#x60;.
    :type permission: List[str]
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def delete_role(request: web.Request, service_sid, sid) -> web.Response:
    """delete_role

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the Role resource from.
    :type service_sid: str
    :param sid: The SID of the Role resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_role(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_role

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Role resource from.
    :type service_sid: str
    :param sid: The SID of the Role resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_role(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_role

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Role resources from.
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

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Role resource in.
    :type service_sid: str
    :param sid: The SID of the Role resource to update.
    :type sid: str
    :param permission: A permission that you grant to the role. Only one permission can be granted per parameter. To assign more than one permission, repeat this parameter for each permission value. Note that the update action replaces all previously assigned permissions with those defined in the update action. To remove a permission, do not include it in the subsequent update action. The values for this parameter depend on the role&#39;s &#x60;type&#x60;.
    :type permission: List[str]

    """
    return web.Response(status=200)
