from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_share_error import DataShareError
from openapi_server.models.operation_response import OperationResponse
from openapi_server.models.synchronization_setting import SynchronizationSetting
from openapi_server.models.synchronization_setting_list import SynchronizationSettingList
from openapi_server import util


async def synchronization_settings_create(request: web.Request, subscription_id, resource_group_name, account_name, share_name, synchronization_setting_name, api_version, synchronization_setting) -> web.Response:
    """Adds a new synchronization setting to an existing share or updates it if existing.

    Create or update a synchronizationSetting 

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share to add the synchronization setting to.
    :type share_name: str
    :param synchronization_setting_name: The name of the synchronizationSetting.
    :type synchronization_setting_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param synchronization_setting: The new synchronization setting information.
    :type synchronization_setting: dict | bytes

    """
    synchronization_setting = SynchronizationSetting.from_dict(synchronization_setting)
    return web.Response(status=200)


async def synchronization_settings_delete(request: web.Request, subscription_id, resource_group_name, account_name, share_name, synchronization_setting_name, api_version) -> web.Response:
    """Delete synchronizationSetting in a share.

    Delete a synchronizationSetting in a share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share.
    :type share_name: str
    :param synchronization_setting_name: The name of the synchronizationSetting .
    :type synchronization_setting_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def synchronization_settings_get(request: web.Request, subscription_id, resource_group_name, account_name, share_name, synchronization_setting_name, api_version) -> web.Response:
    """Get synchronizationSetting in a share.

    Get a synchronizationSetting in a share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share.
    :type share_name: str
    :param synchronization_setting_name: The name of the synchronizationSetting.
    :type synchronization_setting_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def synchronization_settings_list_by_share(request: web.Request, subscription_id, resource_group_name, account_name, share_name, api_version, skip_token=None) -> web.Response:
    """List synchronizationSettings in a share.

    List synchronizationSettings in a share

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param share_name: The name of the share.
    :type share_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param skip_token: continuation token
    :type skip_token: str

    """
    return web.Response(status=200)
