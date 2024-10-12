from typing import List, Dict
from aiohttp import web

from openapi_server.models.email import Email
from openapi_server.models.email_data import EmailData
from openapi_server.models.email_error import EmailError
from openapi_server.models.not_found import NotFound
from openapi_server.models.user import User
from openapi_server.models.user_data import UserData
from openapi_server.models.user_error import UserError
from openapi_server import util


async def me(request: web.Request, ) -> web.Response:
    """A convenience endpoint that is equivalent to GET /v1/users/profiles/&lt;my user id&gt;/

    


    """
    return web.Response(status=200)


async def user_avatar_delete(request: web.Request, user) -> web.Response:
    """Delete avatar

    

    :param user: User unique identifier expressed as UUID or username.
    :type user: str

    """
    return web.Response(status=200)


async def user_avatar_get(request: web.Request, user) -> web.Response:
    """Retrieve user&#39;s avatar

    

    :param user: User unique identifier expressed as UUIDor username.
    :type user: str

    """
    return web.Response(status=200)


async def user_avatar_set(request: web.Request, user) -> web.Response:
    """Add user avatar

    

    :param user: User unique identifier expressed as UUID or username.
    :type user: str

    """
    return web.Response(status=200)


async def user_avatar_update(request: web.Request, user) -> web.Response:
    """Update a project file

    

    :param user: User unique identifier expressed as UUID or username.
    :type user: str

    """
    return web.Response(status=200)


async def users_api_key_list(request: web.Request, user) -> web.Response:
    """Retrieve account&#39;s API key

    

    :param user: User unique identifier expressed as UUID or username.
    :type user: str

    """
    return web.Response(status=200)


async def users_create(request: web.Request, user_data=None) -> web.Response:
    """Create new user

    Only admin users can create new users. New users have active status by default.

    :param user_data: 
    :type user_data: dict | bytes

    """
    user_data = UserData.from_dict(user_data)
    return web.Response(status=200)


async def users_delete(request: web.Request, user) -> web.Response:
    """Delete a user

    

    :param user: User identifier expressed as UUID or username.
    :type user: str

    """
    return web.Response(status=200)


async def users_emails_create(request: web.Request, user, email_data=None) -> web.Response:
    """Create an email address

    

    :param user: User unique identifier expressed as UUID or username.
    :type user: str
    :param email_data: 
    :type email_data: dict | bytes

    """
    email_data = EmailData.from_dict(email_data)
    return web.Response(status=200)


async def users_emails_delete(request: web.Request, email_id, user) -> web.Response:
    """Delete an email address

    

    :param email_id: Email unique identifier expressed as UUID.
    :type email_id: str
    :param user: User unique identifier expressed as UUID or username.
    :type user: str

    """
    return web.Response(status=200)


async def users_emails_list(request: web.Request, user, limit=None, offset=None, ordering=None) -> web.Response:
    """Retrieve account email addresses

    

    :param user: User unique identifier as expressed as UUID or username.
    :type user: str
    :param limit: Limite when getting email list.
    :type limit: str
    :param offset: Offset when getting email list.
    :type offset: str
    :param ordering: Ordering when getting email list.
    :type ordering: str

    """
    return web.Response(status=200)


async def users_emails_read(request: web.Request, email_id, user) -> web.Response:
    """Retrieve a user&#39;s email addresses

    

    :param email_id: Email unique identifier expressed as UUID.
    :type email_id: str
    :param user: User unique identifier expressed as UUID or username.
    :type user: str

    """
    return web.Response(status=200)


async def users_emails_replace(request: web.Request, email_id, user, email_data=None) -> web.Response:
    """Replace an email address

    

    :param email_id: Email unique identifier expressed as UUID.
    :type email_id: str
    :param user: User unique identifier expressed as UUID or username.
    :type user: str
    :param email_data: 
    :type email_data: dict | bytes

    """
    email_data = EmailData.from_dict(email_data)
    return web.Response(status=200)


async def users_emails_update(request: web.Request, email_id, user, email_data=None) -> web.Response:
    """Update an email address

    

    :param email_id: Email unique identifier expressed as UUID.
    :type email_id: str
    :param user: User unique identifier expressed as UUID or username.
    :type user: str
    :param email_data: 
    :type email_data: dict | bytes

    """
    email_data = EmailData.from_dict(email_data)
    return web.Response(status=200)


async def users_list(request: web.Request, limit=None, offset=None, username=None, email=None, ordering=None) -> web.Response:
    """Get user list

    

    :param limit: Limit user list.
    :type limit: str
    :param offset: Offset when getting users.
    :type offset: str
    :param username: User username.
    :type username: str
    :param email: User email.
    :type email: str
    :param ordering: Ordering when getting users.
    :type ordering: str

    """
    return web.Response(status=200)


async def users_read(request: web.Request, user) -> web.Response:
    """Retrieve a user

    

    :param user: Unique identifier expressed as UUID or username.
    :type user: str

    """
    return web.Response(status=200)


async def users_ssh_key_list(request: web.Request, user) -> web.Response:
    """Retrieve an SSH key

    

    :param user: User unique identifier expressed as UUID or username.
    :type user: str

    """
    return web.Response(status=200)


async def users_ssh_key_reset(request: web.Request, user) -> web.Response:
    """Recreate an SSH key

    

    :param user: User unique identifier expressed as UUID or username.
    :type user: str

    """
    return web.Response(status=200)


async def users_update(request: web.Request, user, user_data=None) -> web.Response:
    """Update a user

    

    :param user: User unique identifier expressed as UUID or username.
    :type user: str
    :param user_data: 
    :type user_data: dict | bytes

    """
    user_data = UserData.from_dict(user_data)
    return web.Response(status=200)
