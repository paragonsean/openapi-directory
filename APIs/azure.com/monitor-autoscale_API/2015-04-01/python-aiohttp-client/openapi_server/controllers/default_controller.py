from typing import List, Dict
from aiohttp import web

from openapi_server.models.autoscale_setting_resource import AutoscaleSettingResource
from openapi_server.models.autoscale_setting_resource_patch import AutoscaleSettingResourcePatch
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def autoscale_settings_update(request: web.Request, subscription_id, resource_group_name, autoscale_setting_name, api_version, autoscale_setting_resource) -> web.Response:
    """autoscale_settings_update

    Updates an existing AutoscaleSettingsResource. To update other fields use the CreateOrUpdate method.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param autoscale_setting_name: The autoscale setting name.
    :type autoscale_setting_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param autoscale_setting_resource: Parameters supplied to the operation.
    :type autoscale_setting_resource: dict | bytes

    """
    autoscale_setting_resource = AutoscaleSettingResourcePatch.from_dict(autoscale_setting_resource)
    return web.Response(status=200)
