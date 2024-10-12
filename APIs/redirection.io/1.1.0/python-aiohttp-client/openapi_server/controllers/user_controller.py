from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_creation_write import UserCreationWrite
from openapi_server.models.user_edit_info import UserEditInfo
from openapi_server.models.user_list import UserList
from openapi_server.models.user_password import UserPassword
from openapi_server.models.user_read import UserRead
from openapi_server import util


async def confirm_new_email_user_item(request: web.Request, id, new_email_token) -> web.Response:
    """Retrieves a User resource.

    

    :param id: 
    :type id: str
    :param new_email_token: 
    :type new_email_token: str

    """
    return web.Response(status=200)


async def delete_user_item(request: web.Request, id) -> web.Response:
    """Removes the User resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def edit_email_user_item(request: web.Request, id, user=None) -> web.Response:
    """Replaces the User resource.

    

    :param id: 
    :type id: str
    :param user: The updated User resource
    :type user: dict | bytes

    """
    user = UserEditInfo.from_dict(user)
    return web.Response(status=200)


async def edit_info_user_item(request: web.Request, id, user=None) -> web.Response:
    """Replaces the User resource.

    

    :param id: 
    :type id: str
    :param user: The updated User resource
    :type user: dict | bytes

    """
    user = UserEditInfo.from_dict(user)
    return web.Response(status=200)


async def edit_password_user_item(request: web.Request, id, user=None) -> web.Response:
    """Replaces the User resource.

    

    :param id: 
    :type id: str
    :param user: The updated User resource
    :type user: dict | bytes

    """
    user = UserEditInfo.from_dict(user)
    return web.Response(status=200)


async def forgot_password_user_item(request: web.Request, reset_token, user=None) -> web.Response:
    """Replaces the User resource.

    

    :param reset_token: 
    :type reset_token: str
    :param user: The updated User resource
    :type user: dict | bytes

    """
    user = UserPassword.from_dict(user)
    return web.Response(status=200)


async def get_user_collection(request: web.Request, organization_id, search=None) -> web.Response:
    """Retrieves the collection of User resources.

    

    :param organization_id: 
    :type organization_id: str
    :param search: 
    :type search: str

    """
    return web.Response(status=200)


async def get_user_item(request: web.Request, id) -> web.Response:
    """Retrieves a User resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_user_collection(request: web.Request, user=None) -> web.Response:
    """Creates a User resource.

    

    :param user: The new User resource
    :type user: dict | bytes

    """
    user = UserCreationWrite.from_dict(user)
    return web.Response(status=200)
