from typing import List, Dict
from aiohttp import web

from openapi_server.models.encryption_settings import EncryptionSettings
from openapi_server.models.feature_list import FeatureList
from openapi_server.models.key import Key
from openapi_server.models.manager import Manager
from openapi_server.models.manager_extended_info import ManagerExtendedInfo
from openapi_server.models.manager_list import ManagerList
from openapi_server.models.manager_patch import ManagerPatch
from openapi_server.models.metric_definition_list import MetricDefinitionList
from openapi_server.models.metric_list import MetricList
from openapi_server.models.public_key import PublicKey
from openapi_server.models.symmetric_encrypted_secret import SymmetricEncryptedSecret
from openapi_server import util


async def managers_create_extended_info(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """managers_create_extended_info

    Creates the extended info of the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The manager extended information.
    :type parameters: dict | bytes

    """
    parameters = ManagerExtendedInfo.from_dict(parameters)
    return web.Response(status=200)


async def managers_create_or_update(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """managers_create_or_update

    Creates or updates the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The manager.
    :type parameters: dict | bytes

    """
    parameters = Manager.from_dict(parameters)
    return web.Response(status=200)


async def managers_delete(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_delete

    Deletes the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_delete_extended_info(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_delete_extended_info

    Deletes the extended info of the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_get(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_get

    Returns the properties of the specified manager name.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_get_activation_key(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_get_activation_key

    Returns the activation key of the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_get_device_public_encryption_key(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_get_device_public_encryption_key

    Returns the public encryption key of the device.

    :param device_name: The device name
    :type device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_get_encryption_settings(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_get_encryption_settings

    Returns the encryption settings of the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_get_extended_info(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_get_extended_info

    Returns the extended information of the specified manager name.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_get_public_encryption_key(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_get_public_encryption_key

    Returns the symmetric encrypted public encryption key of the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """managers_list

    Retrieves all the managers in a subscription.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """managers_list_by_resource_group

    Retrieves all the managers in a resource group.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_list_feature_support_status(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, filter=None) -> web.Response:
    """managers_list_feature_support_status

    Lists the features and their support status

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)


async def managers_list_metric_definition(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_list_metric_definition

    Gets the metric definitions for the specified manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_list_metrics(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, filter) -> web.Response:
    """managers_list_metrics

    Gets the metrics for the specified manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)


async def managers_regenerate_activation_key(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """managers_regenerate_activation_key

    Re-generates and returns the activation key of the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def managers_update(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """managers_update

    Updates the StorSimple Manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The manager update parameters.
    :type parameters: dict | bytes

    """
    parameters = ManagerPatch.from_dict(parameters)
    return web.Response(status=200)


async def managers_update_extended_info(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, if_match, parameters) -> web.Response:
    """managers_update_extended_info

    Updates the extended info of the manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param if_match: Pass the ETag of ExtendedInfo fetched from GET call
    :type if_match: str
    :param parameters: The manager extended information.
    :type parameters: dict | bytes

    """
    parameters = ManagerExtendedInfo.from_dict(parameters)
    return web.Response(status=200)
