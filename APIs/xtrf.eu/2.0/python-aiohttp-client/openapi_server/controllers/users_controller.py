from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.entity_with_name_dto import EntityWithNameDTO
from openapi_server.models.time_zone_dto import TimeZoneDTO
from openapi_server.models.user_dto import UserDTO
from openapi_server import util


async def change_password(request: web.Request, user_id, new_password=None, old_password=None) -> web.Response:
    """Sets user&#39;s password to a new value.

    Sets user&#39;s password to a new value.

    :param user_id: user&#39;s internal identifier
    :type user_id: int
    :param new_password: new password
    :type new_password: str
    :param old_password: old password
    :type old_password: str

    """
    return web.Response(status=200)


async def get_all_names_with_ids1(request: web.Request, ) -> web.Response:
    """Returns list of simple users representations

    Returns list of simple users representations


    """
    return web.Response(status=200)


async def get_by_id6(request: web.Request, user_id) -> web.Response:
    """Returns user details.

    Returns user details.

    :param user_id: user&#39;s internal identifier
    :type user_id: int

    """
    return web.Response(status=200)


async def get_custom_field1(request: web.Request, user_id, custom_field_key) -> web.Response:
    """Returns custom field of a given user.

    Returns custom field of a given user.

    :param user_id: user&#39;s internal identifier
    :type user_id: int
    :param custom_field_key: custom field&#39;s key
    :type custom_field_key: str

    """
    return web.Response(status=200)


async def get_custom_fields4(request: web.Request, user_id) -> web.Response:
    """Returns custom fields of a given user.

    Returns custom fields of a given user.

    :param user_id: user&#39;s internal identifier
    :type user_id: int

    """
    return web.Response(status=200)


async def get_me(request: web.Request, ) -> web.Response:
    """Returns currently signed in user details.

    Returns currently signed in user details.


    """
    return web.Response(status=200)


async def get_time_zone(request: web.Request, ) -> web.Response:
    """Returns time zone preferred by user currently signed in.

    Returns time zone preferred by user currently signed in.


    """
    return web.Response(status=200)


async def update3(request: web.Request, user_id, body) -> web.Response:
    """Updates an existing user.

    Updates an existing user.

    :param user_id: user&#39;s internal identifier
    :type user_id: int
    :param body: Updated existing user.
    :type body: dict | bytes

    """
    body = UserDTO.from_dict(body)
    return web.Response(status=200)


async def update_custom_field1(request: web.Request, user_id, custom_field_key, body) -> web.Response:
    """Updates given custom field of a given user.

    Updates given custom field of a given user.

    :param user_id: user&#39;s internal identifier
    :type user_id: int
    :param custom_field_key: custom field&#39;s key
    :type custom_field_key: str
    :param body: Updated custom fields of a given user.
    :type body: dict | bytes

    """
    body = CustomFieldDTO.from_dict(body)
    return web.Response(status=200)


async def update_custom_fields2(request: web.Request, user_id, body) -> web.Response:
    """Updates custom fields of a given user.

    Updates custom fields of a given user.

    :param user_id: user&#39;s internal identifier
    :type user_id: int
    :param body: Updated custom fields of a given user.

    """
    return web.Response(status=200)
