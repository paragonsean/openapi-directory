from typing import List, Dict
from aiohttp import web

from openapi_server.models.label import Label
from openapi_server.models.presence import Presence
from openapi_server.models.support_info import SupportInfo
from openapi_server.models.user import User
from openapi_server import util


async def get_label(request: web.Request, ) -> web.Response:
    """Returns all user labels

    Returns all labels of the user that were defined either explicit or implicit via assignment to conversations. OauthScopes: READ_USER_PROFILE, ORGANIZE_CONVERSATIONS


    """
    return web.Response(status=200)


async def get_presence(request: web.Request, user_ids) -> web.Response:
    """Gets the presence status

    Gets the presence status of the users whose IDs or email addresses are given. OauthScopes: READ_USER

    :param user_ids: A list of unique user IDs or email addresses of the users you want to query the presence state for
    :type user_ids: List[str]

    """
    return web.Response(status=200)


async def get_profile(request: web.Request, ) -> web.Response:
    """Gets the authenticated user&#39;s profile information

    Gets the authenticated user&#39;s profile information. OauthScopes: READ_USER_PROFILE


    """
    return web.Response(status=200)


async def get_support_info(request: web.Request, ) -> web.Response:
    """Gets the support information

    Gets the support information for the tenant of the requesting user OauthScopes: READ_USER_PROFILE


    """
    return web.Response(status=200)


async def get_user_by_email_address(request: web.Request, email_address, secondary_lookup=None) -> web.Response:
    """Get user by email

    Get user by first or secondary email address OauthScopes: READ_USER_PROFILE

    :param email_address: The main or secondary email address of a user.
    :type email_address: str
    :param secondary_lookup: secondaryLookup enabled (default &#x3D; false)
    :type secondary_lookup: bool

    """
    return web.Response(status=200)


async def get_user_by_id(request: web.Request, id) -> web.Response:
    """Gets the user&#39;s profile information

    Gets the profile information of the user with the given ID. OauthScopes: READ_USER

    :param id: The unique ID or the email address of the user to fetch
    :type id: str

    """
    return web.Response(status=200)


async def get_user_presence(request: web.Request, id) -> web.Response:
    """Gets the presence status

    Gets the presence status of the users whose ID or email address is given. OauthScopes: READ_USER

    :param id: The unique ID or the email address of the user to fetch.
    :type id: str

    """
    return web.Response(status=200)


async def search_user(request: web.Request, name) -> web.Response:
    """Search for users

    Search for users based on an email address or username OauthScopes: READ_USER

    :param name: Search for a user by name
    :type name: str

    """
    return web.Response(status=200)


async def search_users_list(request: web.Request, name, return_full_user_info=None, secondary_lookup=None) -> web.Response:
    """Search multiple users.

    Search multiple users given by id or email address. OauthScopes: READ_USER

    :param name: Multiple email addresses or UUIDs.
    :type name: List[str]
    :param return_full_user_info: Boolean, return full user info?
    :type return_full_user_info: bool
    :param secondary_lookup: Boolean, lookup secondary email?
    :type secondary_lookup: bool

    """
    return web.Response(status=200)


async def set_user_presence(request: web.Request, state, clear_dnd=None, dnd_until=None, status_message=None) -> web.Response:
    """Updates the presence status

    Updates the presence status of the authenticated user. OauthScopes: WRITE_USER_PROFILE, MANAGE_PRESENCE

    :param state: The user&#39;s presence.
    :type state: str
    :param clear_dnd: Clear the DND of the user.
    :type clear_dnd: bool
    :param dnd_until: Timestamp until the DND state of the user is active. This field is mandatory when the state is set to DND.
    :type dnd_until: str
    :param status_message: An optional status message that is displayed instead of the location
    :type status_message: str

    """
    dnd_until = util.deserialize_datetime(dnd_until)
    return web.Response(status=200)
