from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.workspace_setting import WorkspaceSetting
from openapi_server.models.workspace_setting_list import WorkspaceSettingList
from openapi_server import util


async def workspace_settings_create(request: web.Request, api_version, subscription_id, workspace_setting_name, workspace_setting) -> web.Response:
    """workspace_settings_create

    creating settings about where we should store your security data and logs

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param workspace_setting_name: Name of the security setting
    :type workspace_setting_name: str
    :param workspace_setting: Security data setting object
    :type workspace_setting: dict | bytes

    """
    workspace_setting = WorkspaceSetting.from_dict(workspace_setting)
    return web.Response(status=200)


async def workspace_settings_delete(request: web.Request, api_version, subscription_id, workspace_setting_name) -> web.Response:
    """workspace_settings_delete

    Deletes the custom workspace settings for this subscription. new VMs will report to the default workspace

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param workspace_setting_name: Name of the security setting
    :type workspace_setting_name: str

    """
    return web.Response(status=200)


async def workspace_settings_get(request: web.Request, api_version, subscription_id, workspace_setting_name) -> web.Response:
    """workspace_settings_get

    Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param workspace_setting_name: Name of the security setting
    :type workspace_setting_name: str

    """
    return web.Response(status=200)


async def workspace_settings_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """workspace_settings_list

    Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str

    """
    return web.Response(status=200)


async def workspace_settings_update(request: web.Request, api_version, subscription_id, workspace_setting_name, workspace_setting) -> web.Response:
    """workspace_settings_update

    Settings about where we should store your security data and logs

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param workspace_setting_name: Name of the security setting
    :type workspace_setting_name: str
    :param workspace_setting: Security data setting object
    :type workspace_setting: dict | bytes

    """
    workspace_setting = WorkspaceSetting.from_dict(workspace_setting)
    return web.Response(status=200)
