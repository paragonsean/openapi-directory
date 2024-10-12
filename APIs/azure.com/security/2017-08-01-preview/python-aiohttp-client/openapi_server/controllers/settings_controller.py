from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.setting import Setting
from openapi_server.models.settings_list import SettingsList
from openapi_server import util


async def settings_get(request: web.Request, api_version, subscription_id, setting_name) -> web.Response:
    """settings_get

    Settings of different configurations in security center

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param setting_name: Name of setting: (MCAS/WDATP)
    :type setting_name: str

    """
    return web.Response(status=200)


async def settings_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """settings_list

    Settings about different configurations in security center

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str

    """
    return web.Response(status=200)


async def settings_update(request: web.Request, api_version, subscription_id, setting_name, setting) -> web.Response:
    """settings_update

    updating settings about different configurations in security center

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param setting_name: Name of setting: (MCAS/WDATP)
    :type setting_name: str
    :param setting: Setting object
    :type setting: dict | bytes

    """
    setting = Setting.from_dict(setting)
    return web.Response(status=200)
