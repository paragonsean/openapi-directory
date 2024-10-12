from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_sm_device_device_profiles200_response_inner import GetNetworkSmDeviceDeviceProfiles200ResponseInner
from openapi_server.models.get_network_sm_device_softwares200_response_inner import GetNetworkSmDeviceSoftwares200ResponseInner
from openapi_server.models.get_network_sm_users200_response_inner import GetNetworkSmUsers200ResponseInner
from openapi_server import util


async def delete_organization_user_1(request: web.Request, organization_id, user_id) -> web.Response:
    """Delete a user and all of its authentication methods.

    Delete a user and all of its authentication methods.

    :param organization_id: 
    :type organization_id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_network_sm_user_device_profiles_1(request: web.Request, network_id, user_id) -> web.Response:
    """Get the profiles associated with a user

    Get the profiles associated with a user

    :param network_id: 
    :type network_id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_network_sm_user_softwares_1(request: web.Request, network_id, user_id) -> web.Response:
    """Get a list of softwares associated with a user

    Get a list of softwares associated with a user

    :param network_id: 
    :type network_id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_network_sm_users_1(request: web.Request, network_id, ids=None, usernames=None, emails=None, scope=None) -> web.Response:
    """List the owners in an SM network with various specified fields and filters

    List the owners in an SM network with various specified fields and filters

    :param network_id: 
    :type network_id: str
    :param ids: Filter users by id(s).
    :type ids: List[str]
    :param usernames: Filter users by username(s).
    :type usernames: List[str]
    :param emails: Filter users by email(s).
    :type emails: List[str]
    :param scope: Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags.
    :type scope: List[str]

    """
    return web.Response(status=200)
