from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.string_items_wrapper import StringItemsWrapper
from openapi_server.models.update_password_info import UpdatePasswordInfo
from openapi_server.models.user_duty_info import UserDutyInfo
from openapi_server.models.user_image import UserImage
from openapi_server.models.user_info import UserInfo
from openapi_server.models.user_profile import UserProfile
from openapi_server.models.user_setup_progress import UserSetupProgress
from openapi_server import util


async def users_get(request: web.Request, ) -> web.Response:
    """Get all Users

    Returns a list of user objects with details such as their email address and duty information. Only users who  are part of your team will be returned.


    """
    return web.Response(status=200)


async def users_user_id_change_password_put(request: web.Request, user_id, body=None) -> web.Response:
    """Updates the password of a user

    

    :param user_id: User ID of user whose password should be changed.
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePasswordInfo.from_dict(body)
    return web.Response(status=200)


async def users_user_id_check_permissions_post(request: web.Request, user_id, team_id=None, body=None) -> web.Response:
    """Checks if a user has the provided permission.

    

    :param user_id: ID of the user to check permissions for.
    :type user_id: str
    :param team_id: 
    :type team_id: str
    :param body: List of permissions to check
    :type body: dict | bytes

    """
    body = StringItemsWrapper.from_dict(body)
    return web.Response(status=200)


async def users_user_id_duty_status_get(request: web.Request, user_id) -> web.Response:
    """Get duty status by user Id

    Returns a object with duty information.

    :param user_id: Identifier of the user to get. Use &#39;Me&#39; to get information about the currently logged in user. This is not possible with an api key.  Can also be an email address of a user in the team or the unique id of an according user object.”
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_get(request: web.Request, user_id) -> web.Response:
    """Get User by Id

    Returns a user object with details such as his email address and duty information.

    :param user_id: Identifier of the user to get. Use &#39;Me&#39; to get information about the currently logged in user. This is not possible with an api key.  Can also be an email address of a user in the team or the unique id of an according user object.”
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_image_get(request: web.Request, user_id, height=None, width=None) -> web.Response:
    """users_user_id_image_get

    

    :param user_id: 
    :type user_id: str
    :param height: 
    :type height: int
    :param width: 
    :type width: int

    """
    return web.Response(status=200)


async def users_user_id_image_post(request: web.Request, user_id) -> web.Response:
    """Uploaded a profile image for a specified user.

    

    :param user_id: Id of the user.
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_profile_put(request: web.Request, user_id, body=None) -> web.Response:
    """Updates user profile of an user

    

    :param user_id: ID of user to update.
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserProfile.from_dict(body)
    return web.Response(status=200)


async def users_user_id_punch_in_as_manager_post(request: web.Request, user_id) -> web.Response:
    """Punch User in as Manager

    The specified user will be punched in to duty as a manager.

    :param user_id: Identifier of the user to punch in. Use &#39;Me&#39; to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.”
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_punch_in_post(request: web.Request, user_id) -> web.Response:
    """Punch User in

    The specified user will be punched in to duty.

    :param user_id: Identifier of the user to punch in. Use &#39;Me&#39; to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.”
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_punch_out_post(request: web.Request, user_id) -> web.Response:
    """Punch User out

    The specified user will be punched out from duty.

    :param user_id: Identifier of the user to punch out. Use &#39;Me&#39; to get information about the currently logged in  user. This is not possible with an api key. Can also be an email address of a user in the team or the unique id of an according user object.”
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_setup_progress_get(request: web.Request, user_id) -> web.Response:
    """Gets setup progress of a specific user.

    

    :param user_id: ID of the user the progress should be retrieved for.
    :type user_id: str

    """
    return web.Response(status=200)
