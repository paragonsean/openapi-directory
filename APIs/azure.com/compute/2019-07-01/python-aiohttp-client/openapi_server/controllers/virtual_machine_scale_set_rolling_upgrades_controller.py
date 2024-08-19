from typing import List, Dict
from aiohttp import web

from openapi_server.models.rolling_upgrade_status_info import RollingUpgradeStatusInfo
from openapi_server import util


async def virtual_machine_scale_set_rolling_upgrades_cancel(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_rolling_upgrades_cancel

    Cancels the current virtual machine scale set rolling upgrade.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_rolling_upgrades_get_latest(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_rolling_upgrades_get_latest

    Gets the status of the latest virtual machine scale set rolling upgrade.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_rolling_upgrades_start_extension_upgrade(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_rolling_upgrades_start_extension_upgrade

    Starts a rolling upgrade to move all extensions for all virtual machine scale set instances to the latest available extension version. Instances which are already running the latest extension versions are not affected.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_scale_set_rolling_upgrades_start_os_upgrade(request: web.Request, resource_group_name, vm_scale_set_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_scale_set_rolling_upgrades_start_os_upgrade

    Starts a rolling upgrade to move all virtual machine scale set instances to the latest available Platform Image OS version. Instances which are already running the latest available OS version are not affected.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
