from typing import List, Dict
from aiohttp import web

from openapi_server.models.advanced_threat_protection_setting import AdvancedThreatProtectionSetting
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def advanced_threat_protection_create(request: web.Request, api_version, resource_id, setting_name, advanced_threat_protection_setting) -> web.Response:
    """advanced_threat_protection_create

    Creates or updates the Advanced Threat Protection settings on a specified resource.

    :param api_version: API version for the operation
    :type api_version: str
    :param resource_id: The identifier of the resource.
    :type resource_id: str
    :param setting_name: Advanced Threat Protection setting name.
    :type setting_name: str
    :param advanced_threat_protection_setting: Advanced Threat Protection Settings
    :type advanced_threat_protection_setting: dict | bytes

    """
    advanced_threat_protection_setting = AdvancedThreatProtectionSetting.from_dict(advanced_threat_protection_setting)
    return web.Response(status=200)


async def advanced_threat_protection_get(request: web.Request, api_version, resource_id, setting_name) -> web.Response:
    """advanced_threat_protection_get

    Gets the Advanced Threat Protection settings for the specified resource.

    :param api_version: API version for the operation
    :type api_version: str
    :param resource_id: The identifier of the resource.
    :type resource_id: str
    :param setting_name: Advanced Threat Protection setting name.
    :type setting_name: str

    """
    return web.Response(status=200)
