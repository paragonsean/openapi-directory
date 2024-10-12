from typing import List, Dict
from aiohttp import web

from openapi_server.models.app import App
from openapi_server.models.app_channel_response import AppChannelResponse
from openapi_server.models.app_external_credentials import AppExternalCredentials
from openapi_server.models.app_external_credentials_response import AppExternalCredentialsResponse
from openapi_server.models.app_response import AppResponse
from openapi_server.models.rule_results import RuleResults
from openapi_server import util


async def add_app(request: web.Request, app_object) -> web.Response:
    """add_app

    Create a new app

    :param app_object: App information
    :type app_object: dict | bytes

    """
    app_object = App.from_dict(app_object)
    return web.Response(status=200)


async def add_app_channel_user(request: web.Request, channel_id, user_id) -> web.Response:
    """add_app_channel_user

    Create user channel

    :param channel_id: Id of Channel
    :type channel_id: str
    :param user_id: Id of User
    :type user_id: str

    """
    return web.Response(status=200)


async def add_channel_external_credentials(request: web.Request, app_external_credentials_object) -> web.Response:
    """add_channel_external_credentials

    Create new external credentials

    :param app_external_credentials_object: App_External_Credentials information
    :type app_external_credentials_object: dict | bytes

    """
    app_external_credentials_object = AppExternalCredentials.from_dict(app_external_credentials_object)
    return web.Response(status=200)


async def get_app(request: web.Request, app_id) -> web.Response:
    """get_app

    Get app information

    :param app_id: Id of App
    :type app_id: str

    """
    return web.Response(status=200)


async def get_app_channel_user(request: web.Request, channel_id, user_id) -> web.Response:
    """get_app_channel_user

    Get user of a specified channel

    :param channel_id: Id of Channel
    :type channel_id: str
    :param user_id: Id of User
    :type user_id: str

    """
    return web.Response(status=200)


async def get_channel_external_credentials(request: web.Request, channel_id) -> web.Response:
    """get_channel_external_credentials

    Get credentials for a channel in an app

    :param channel_id: Id of Channel
    :type channel_id: str

    """
    return web.Response(status=200)


async def list_app_channel_users(request: web.Request, channel_id) -> web.Response:
    """list_app_channel_users

    Get users of a specified channel

    :param channel_id: Id of Channel
    :type channel_id: str

    """
    return web.Response(status=200)


async def list_app_channels(request: web.Request, ) -> web.Response:
    """list_app_channels

    Get app channels


    """
    return web.Response(status=200)


async def list_apps(request: web.Request, ) -> web.Response:
    """list_apps

    Get apps information


    """
    return web.Response(status=200)


async def list_channel_external_credentials(request: web.Request, ) -> web.Response:
    """list_channel_external_credentials

    Get external credentials


    """
    return web.Response(status=200)


async def remove_app(request: web.Request, app_id) -> web.Response:
    """remove_app

    Delete an app

    :param app_id: Id of App
    :type app_id: str

    """
    return web.Response(status=200)


async def remove_channel_external_credentials(request: web.Request, channel_id) -> web.Response:
    """remove_channel_external_credentials

    Delete credentials for a channel

    :param channel_id: Id of Channel
    :type channel_id: str

    """
    return web.Response(status=200)


async def run_app(request: web.Request, break_when_rule_fires=None, initial_data=None) -> web.Response:
    """run_app

    Run active app rules

    :param break_when_rule_fires: Do not continue with remaining rules after a rule fires
    :type break_when_rule_fires: bool
    :param initial_data: Initial data
    :type initial_data: 

    """
    return web.Response(status=200)


async def run_rule_group(request: web.Request, rule_id_list, break_when_rule_fires=None, initial_data=None) -> web.Response:
    """run_rule_group

    Run specified rule group in the app

    :param rule_id_list: Ids of rules in the group, separated by commas, no spaces
    :type rule_id_list: str
    :param break_when_rule_fires: Do not continue with remaining rules after a rule fires
    :type break_when_rule_fires: bool
    :param initial_data: Initial data
    :type initial_data: 

    """
    return web.Response(status=200)


async def update_app(request: web.Request, app_id, app_object) -> web.Response:
    """update_app

    Update an app

    :param app_id: Id of app
    :type app_id: str
    :param app_object: App information
    :type app_object: dict | bytes

    """
    app_object = App.from_dict(app_object)
    return web.Response(status=200)


async def update_channel_external_credentials(request: web.Request, channel_id, app_external_credentials_object) -> web.Response:
    """update_channel_external_credentials

    Update credentials for a channel

    :param channel_id: Id of Channel
    :type channel_id: str
    :param app_external_credentials_object: App_External_Credentials information
    :type app_external_credentials_object: dict | bytes

    """
    app_external_credentials_object = AppExternalCredentials.from_dict(app_external_credentials_object)
    return web.Response(status=200)
