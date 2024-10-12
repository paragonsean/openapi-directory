from typing import List, Dict
from aiohttp import web

from openapi_server.models.admin_user import AdminUser
from openapi_server.models.admin_user_response import AdminUserResponse
from openapi_server.models.app_user import AppUser
from openapi_server.models.app_user_response import AppUserResponse
from openapi_server.models.authorize_url_response import AuthorizeUrlResponse
from openapi_server.models.rule_full_response import RuleFullResponse
from openapi_server.models.rule_short_response import RuleShortResponse
from openapi_server.models.user_channel import UserChannel
from openapi_server import util


async def add_admin_user(request: web.Request, admin_user_object) -> web.Response:
    """add_admin_user

    Create a new admin user

    :param admin_user_object: Admin User information
    :type admin_user_object: dict | bytes

    """
    admin_user_object = AdminUser.from_dict(admin_user_object)
    return web.Response(status=200)


async def add_app_user(request: web.Request, app_user_object) -> web.Response:
    """add_app_user

    Create a new App User

    :param app_user_object: App User information
    :type app_user_object: dict | bytes

    """
    app_user_object = AppUser.from_dict(app_user_object)
    return web.Response(status=200)


async def add_app_user_to_channel(request: web.Request, user_id, channel_id) -> web.Response:
    """add_app_user_to_channel

    Assign a channel to a user

    :param user_id: Id of user
    :type user_id: str
    :param channel_id: Id of Channel
    :type channel_id: str

    """
    return web.Response(status=200)


async def add_app_user_to_rule(request: web.Request, user_id, rule_id) -> web.Response:
    """add_app_user_to_rule

    Assign a user to a rule

    :param user_id: Id of User
    :type user_id: str
    :param rule_id: Id of Rule
    :type rule_id: str

    """
    return web.Response(status=200)


async def authenticate_app_user_for_channel(request: web.Request, user_id, channel_id) -> web.Response:
    """authenticate_app_user_for_channel

    Authenticate a user for a channel

    :param user_id: Id of User
    :type user_id: str
    :param channel_id: Id of Channel
    :type channel_id: str

    """
    return web.Response(status=200)


async def get_admin_user(request: web.Request, user_id) -> web.Response:
    """get_admin_user

    Get an admin user

    :param user_id: Id of Admin_User
    :type user_id: str

    """
    return web.Response(status=200)


async def get_app_user(request: web.Request, user_id) -> web.Response:
    """get_app_user

    Get an App User

    :param user_id: Id of App User
    :type user_id: str

    """
    return web.Response(status=200)


async def get_app_user_channel(request: web.Request, user_id, channel_id) -> web.Response:
    """get_app_user_channel

    Get a user channel

    :param user_id: Id of User
    :type user_id: str
    :param channel_id: Id of Channel
    :type channel_id: str

    """
    return web.Response(status=200)


async def get_app_user_rule(request: web.Request, user_id, rule_id) -> web.Response:
    """get_app_user_rule

    Get a user

    :param user_id: Id of User
    :type user_id: str
    :param rule_id: Id of Rule
    :type rule_id: str

    """
    return web.Response(status=200)


async def list_admin_users(request: web.Request, ) -> web.Response:
    """list_admin_users

    Admin users


    """
    return web.Response(status=200)


async def list_app_user_channels(request: web.Request, user_id) -> web.Response:
    """list_app_user_channels

    Channels available to a User

    :param user_id: Id of user
    :type user_id: str

    """
    return web.Response(status=200)


async def list_app_user_rules(request: web.Request, user_id) -> web.Response:
    """list_app_user_rules

    Rules for a User

    :param user_id: Id of user
    :type user_id: str

    """
    return web.Response(status=200)


async def list_app_users(request: web.Request, ) -> web.Response:
    """list_app_users

    Users


    """
    return web.Response(status=200)


async def remove_admin_user(request: web.Request, user_id) -> web.Response:
    """remove_admin_user

    Remove an admin user

    :param user_id: Id of Admin_User
    :type user_id: str

    """
    return web.Response(status=200)


async def remove_app_user(request: web.Request, user_id) -> web.Response:
    """remove_app_user

    Remove a user

    :param user_id: Id of user
    :type user_id: str

    """
    return web.Response(status=200)


async def remove_app_user_from_channel(request: web.Request, user_id, channel_id) -> web.Response:
    """remove_app_user_from_channel

    Remove a user channel assignment

    :param user_id: Id of User
    :type user_id: str
    :param channel_id: Id of Channel
    :type channel_id: str

    """
    return web.Response(status=200)


async def remove_app_user_from_rule(request: web.Request, user_id, rule_id) -> web.Response:
    """remove_app_user_from_rule

    Remove a rule user

    :param user_id: Id of User
    :type user_id: str
    :param rule_id: Id of Rule
    :type rule_id: str

    """
    return web.Response(status=200)


async def run_rule_for_app_user(request: web.Request, user_id, rule_id) -> web.Response:
    """run_rule_for_app_user

    Run rule for a user

    :param user_id: Id of User
    :type user_id: str
    :param rule_id: Id of Rule
    :type rule_id: str

    """
    return web.Response(status=200)


async def update_admin_user(request: web.Request, user_id, admin_user_object) -> web.Response:
    """update_admin_user

    Update information about an admin user

    :param user_id: Id of user
    :type user_id: str
    :param admin_user_object: Admin User information
    :type admin_user_object: dict | bytes

    """
    admin_user_object = AdminUser.from_dict(admin_user_object)
    return web.Response(status=200)


async def update_app_user(request: web.Request, user_id, app_user_object) -> web.Response:
    """update_app_user

    Update information about an App User

    :param user_id: Id of user
    :type user_id: str
    :param app_user_object: App User information
    :type app_user_object: dict | bytes

    """
    app_user_object = AppUser.from_dict(app_user_object)
    return web.Response(status=200)
