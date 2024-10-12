from typing import List, Dict
from aiohttp import web

from openapi_server.models.users_user_id_user_custom_field_value_get200_response import UsersUserIdUserCustomFieldValueGet200Response
from openapi_server.models.users_user_id_user_custom_field_value_user_custom_field_value_id_get200_response import UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response
from openapi_server.models.users_user_id_user_custom_field_value_user_custom_field_value_id_put200_response import UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response
from openapi_server import util


async def users_user_id_user_custom_field_value_get(request: web.Request, user_id) -> web.Response:
    """Get a list of user custom field values

    

    :param user_id: Automatically added
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_user_custom_field_value_user_custom_field_value_id_get(request: web.Request, user_id, user_custom_field_value_id) -> web.Response:
    """Get a single record of user custom field value

    

    :param user_id: Automatically added
    :type user_id: str
    :param user_custom_field_value_id: Automatically added
    :type user_custom_field_value_id: str

    """
    return web.Response(status=200)


async def users_user_id_user_custom_field_value_user_custom_field_value_id_put(request: web.Request, user_id, user_custom_field_value_id) -> web.Response:
    """Update a single record of user custom field value

    

    :param user_id: Automatically added
    :type user_id: str
    :param user_custom_field_value_id: Automatically added
    :type user_custom_field_value_id: str

    """
    return web.Response(status=200)
