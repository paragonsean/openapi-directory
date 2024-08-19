from typing import List, Dict
from aiohttp import web

from openapi_server.models.auto_provisioning_setting import AutoProvisioningSetting
from openapi_server.models.auto_provisioning_setting_list import AutoProvisioningSettingList
from openapi_server.models.auto_provisioning_settings_list_default_response import AutoProvisioningSettingsListDefaultResponse
from openapi_server import util


async def auto_provisioning_settings_create(request: web.Request, api_version, subscription_id, setting_name, setting) -> web.Response:
    """auto_provisioning_settings_create

    Details of a specific setting

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param setting_name: Auto provisioning setting key
    :type setting_name: str
    :param setting: Auto provisioning setting key
    :type setting: dict | bytes

    """
    setting = AutoProvisioningSetting.from_dict(setting)
    return web.Response(status=200)


async def auto_provisioning_settings_get(request: web.Request, api_version, subscription_id, setting_name) -> web.Response:
    """auto_provisioning_settings_get

    Details of a specific setting

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param setting_name: Auto provisioning setting key
    :type setting_name: str

    """
    return web.Response(status=200)


async def auto_provisioning_settings_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """auto_provisioning_settings_list

    Exposes the auto provisioning settings of the subscriptions

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str

    """
    return web.Response(status=200)
