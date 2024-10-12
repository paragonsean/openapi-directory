from typing import List, Dict
from aiohttp import web

from openapi_server.models.email import Email
from openapi_server.models.event import Event
from openapi_server.models.post_v3_user_keys_request import PostV3UserKeysRequest
from openapi_server.models.post_v3_users_id_emails_request import PostV3UsersIdEmailsRequest
from openapi_server.models.post_v3_users_request import PostV3UsersRequest
from openapi_server.models.put_v3_users_id_request import PutV3UsersIdRequest
from openapi_server.models.ssh_key import SSHKey
from openapi_server.models.user_basic import UserBasic
from openapi_server.models.user_public import UserPublic
from openapi_server import util


async def delete_v3_users_id(request: web.Request, id) -> web.Response:
    """Delete a user. Available only for admins.

    Delete a user. Available only for admins.

    :param id: The ID of the user
    :type id: int

    """
    return web.Response(status=200)


async def delete_v3_users_id_emails_email_id(request: web.Request, id, email_id) -> web.Response:
    """Delete an email address of a specified user. Available only for admins.

    Delete an email address of a specified user. Available only for admins.

    :param id: The ID of the user
    :type id: int
    :param email_id: The ID of the email
    :type email_id: int

    """
    return web.Response(status=200)


async def delete_v3_users_id_keys_key_id(request: web.Request, id, key_id) -> web.Response:
    """Delete an existing SSH key from a specified user. Available only for admins.

    Delete an existing SSH key from a specified user. Available only for admins.

    :param id: The ID of the user
    :type id: int
    :param key_id: The ID of the SSH key
    :type key_id: int

    """
    return web.Response(status=200)


async def get_v3_users(request: web.Request, username=None, search=None, active=None, external=None, blocked=None, page=None, per_page=None) -> web.Response:
    """Get the list of users

    Get the list of users

    :param username: Get a single user with a specific username
    :type username: str
    :param search: Search for a username
    :type search: str
    :param active: Filters only active users
    :type active: bool
    :param external: Filters only external users
    :type external: bool
    :param blocked: Filters only blocked users
    :type blocked: bool
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_users_id(request: web.Request, id) -> web.Response:
    """Get a single user

    Get a single user

    :param id: The ID of the user
    :type id: int

    """
    return web.Response(status=200)


async def get_v3_users_id_emails(request: web.Request, id) -> web.Response:
    """Get the emails addresses of a specified user. Available only for admins.

    Get the emails addresses of a specified user. Available only for admins.

    :param id: The ID of the user
    :type id: int

    """
    return web.Response(status=200)


async def get_v3_users_id_events(request: web.Request, id, page=None, per_page=None) -> web.Response:
    """Get the contribution events of a specified user

    This feature was introduced in GitLab 8.13.

    :param id: The ID of the user
    :type id: int
    :param page: Current page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)


async def get_v3_users_id_keys(request: web.Request, id) -> web.Response:
    """Get the SSH keys of a specified user. Available only for admins.

    Get the SSH keys of a specified user. Available only for admins.

    :param id: The ID of the user
    :type id: int

    """
    return web.Response(status=200)


async def post_v3_users(request: web.Request, body) -> web.Response:
    """Create a user. Available only for admins.

    Create a user. Available only for admins.

    :param body: 
    :type body: dict | bytes

    """
    body = PostV3UsersRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_users_id_emails(request: web.Request, id, body) -> web.Response:
    """Add an email address to a specified user. Available only for admins.

    Add an email address to a specified user. Available only for admins.

    :param id: The ID of the user
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3UsersIdEmailsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_users_id_keys(request: web.Request, id, body) -> web.Response:
    """Add an SSH key to a specified user. Available only for admins.

    Add an SSH key to a specified user. Available only for admins.

    :param id: The ID of the user
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PostV3UserKeysRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_users_id(request: web.Request, id, body=None) -> web.Response:
    """Update a user. Available only for admins.

    Update a user. Available only for admins.

    :param id: The ID of the user
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PutV3UsersIdRequest.from_dict(body)
    return web.Response(status=200)


async def put_v3_users_id_block(request: web.Request, id) -> web.Response:
    """Block a user. Available only for admins.

    Block a user. Available only for admins.

    :param id: The ID of the user
    :type id: int

    """
    return web.Response(status=200)


async def put_v3_users_id_unblock(request: web.Request, id) -> web.Response:
    """Unblock a user. Available only for admins.

    Unblock a user. Available only for admins.

    :param id: The ID of the user
    :type id: int

    """
    return web.Response(status=200)
