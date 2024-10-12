from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_v_center_request import AddVCenterRequest
from openapi_server.models.update_v_center_request import UpdateVCenterRequest
from openapi_server.models.v_center import VCenter
from openapi_server.models.v_center_collection import VCenterCollection
from openapi_server import util


async def replicationv_centers_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, v_center_name, add_v_center_request) -> web.Response:
    """Add vCenter.

    The operation to create a vCenter object..

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param v_center_name: vCenter name.
    :type v_center_name: str
    :param add_v_center_request: The input to the add vCenter operation.
    :type add_v_center_request: dict | bytes

    """
    add_v_center_request = AddVCenterRequest.from_dict(add_v_center_request)
    return web.Response(status=200)


async def replicationv_centers_delete(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, v_center_name) -> web.Response:
    """Remove vCenter operation.

    The operation to remove(unregister) a registered vCenter server from the vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param v_center_name: vCenter name.
    :type v_center_name: str

    """
    return web.Response(status=200)


async def replicationv_centers_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, v_center_name) -> web.Response:
    """Gets the details of a vCenter.

    Gets the details of a registered vCenter server(Add vCenter server.)

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param v_center_name: vCenter name.
    :type v_center_name: str

    """
    return web.Response(status=200)


async def replicationv_centers_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the list of vCenter registered under the vault.

    Lists the vCenter servers registered in the vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def replicationv_centers_list_by_replication_fabrics(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name) -> web.Response:
    """Gets the list of vCenter registered under a fabric.

    Lists the vCenter servers registered in a fabric.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str

    """
    return web.Response(status=200)


async def replicationv_centers_update(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, v_center_name, update_v_center_request) -> web.Response:
    """Update vCenter operation.

    The operation to update a registered vCenter.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param v_center_name: vCenter name
    :type v_center_name: str
    :param update_v_center_request: The input to the update vCenter operation.
    :type update_v_center_request: dict | bytes

    """
    update_v_center_request = UpdateVCenterRequest.from_dict(update_v_center_request)
    return web.Response(status=200)
