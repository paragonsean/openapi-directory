from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.settings_change_request import SettingsChangeRequest
from openapi_server.models.settings_response import SettingsResponse
from openapi_server import util


async def delete_webhooks_v3_app_id_settings_clear(request: web.Request, app_id) -> web.Response:
    """delete_webhooks_v3_app_id_settings_clear

    

    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)


async def get_webhooks_v3_app_id_settings_get_all(request: web.Request, app_id) -> web.Response:
    """get_webhooks_v3_app_id_settings_get_all

    

    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)


async def put_webhooks_v3_app_id_settings_configure(request: web.Request, app_id, body) -> web.Response:
    """put_webhooks_v3_app_id_settings_configure

    

    :param app_id: 
    :type app_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SettingsChangeRequest.from_dict(body)
    return web.Response(status=200)
