from typing import List, Dict
from aiohttp import web

from openapi_server.models.doctor import Doctor
from openapi_server.models.doctors_list200_response import DoctorsList200Response
from openapi_server.models.user_groups_list200_response import UserGroupsList200Response
from openapi_server.models.user_profile import UserProfile
from openapi_server.models.user_profiles_group import UserProfilesGroup
from openapi_server.models.users_list200_response import UsersList200Response
from openapi_server import util


async def doctors_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """doctors_list

    Retrieve or search doctors within practice group

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def doctors_read(request: web.Request, id, doctor=None) -> web.Response:
    """doctors_read

    Retrieve an existing dcotor

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def user_groups_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """user_groups_list

    Retrieve or search user groups

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def user_groups_read(request: web.Request, id, doctor=None) -> web.Response:
    """user_groups_read

    Retrieve an existing user group

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def users_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """users_list

    Retrieve or search users, &#x60;/api/users/current&#x60; can be used to identify logged in user, it will redirect to &#x60;/api/users/{current_user_id}&#x60;

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def users_read(request: web.Request, id, doctor=None) -> web.Response:
    """users_read

    Retrieve an existing user, &#x60;/api/users/current&#x60; can be used to identify logged in user, it will redirect to &#x60;/api/users/{current_user_id}&#x60;

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)
