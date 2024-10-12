from typing import List, Dict
from aiohttp import web

from openapi_server.models.email import Email
from openapi_server.models.post_v3_user_emails_request import PostV3UserEmailsRequest
from openapi_server.models.post_v3_user_keys_request import PostV3UserKeysRequest
from openapi_server.models.ssh_key import SSHKey
from openapi_server.models.user_public import UserPublic
from openapi_server import util


async def delete_v3_user_emails_email_id(request: web.Request, email_id) -> web.Response:
    """Delete an email address from the currently authenticated user

    Delete an email address from the currently authenticated user

    :param email_id: The ID of the email
    :type email_id: int

    """
    return web.Response(status=200)


async def delete_v3_user_keys_key_id(request: web.Request, key_id) -> web.Response:
    """Delete an SSH key from the currently authenticated user

    Delete an SSH key from the currently authenticated user

    :param key_id: The ID of the SSH key
    :type key_id: int

    """
    return web.Response(status=200)


async def get_v3_user(request: web.Request, ) -> web.Response:
    """Get the currently authenticated user

    Get the currently authenticated user


    """
    return web.Response(status=200)


async def get_v3_user_emails(request: web.Request, ) -> web.Response:
    """Get the currently authenticated user&#39;s email addresses

    Get the currently authenticated user&#39;s email addresses


    """
    return web.Response(status=200)


async def get_v3_user_emails_email_id(request: web.Request, email_id) -> web.Response:
    """Get a single email address owned by the currently authenticated user

    Get a single email address owned by the currently authenticated user

    :param email_id: The ID of the email
    :type email_id: int

    """
    return web.Response(status=200)


async def get_v3_user_keys(request: web.Request, ) -> web.Response:
    """Get the currently authenticated user&#39;s SSH keys

    Get the currently authenticated user&#39;s SSH keys


    """
    return web.Response(status=200)


async def get_v3_user_keys_key_id(request: web.Request, key_id) -> web.Response:
    """Get a single key owned by currently authenticated user

    Get a single key owned by currently authenticated user

    :param key_id: The ID of the SSH key
    :type key_id: int

    """
    return web.Response(status=200)


async def post_v3_user_emails(request: web.Request, body) -> web.Response:
    """Add new email address to the currently authenticated user

    Add new email address to the currently authenticated user

    :param body: 
    :type body: dict | bytes

    """
    body = PostV3UserEmailsRequest.from_dict(body)
    return web.Response(status=200)


async def post_v3_user_keys(request: web.Request, body) -> web.Response:
    """Add a new SSH key to the currently authenticated user

    Add a new SSH key to the currently authenticated user

    :param body: 
    :type body: dict | bytes

    """
    body = PostV3UserKeysRequest.from_dict(body)
    return web.Response(status=200)
