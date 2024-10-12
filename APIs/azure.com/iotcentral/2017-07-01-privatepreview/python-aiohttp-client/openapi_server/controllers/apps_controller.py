from typing import List, Dict
from aiohttp import web

from openapi_server.models.app import App
from openapi_server.models.app_list_result import AppListResult
from openapi_server.models.app_name_availability_info import AppNameAvailabilityInfo
from openapi_server.models.app_patch import AppPatch
from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.operation_inputs import OperationInputs
from openapi_server import util


async def apps_check_name_availability(request: web.Request, api_version, subscription_id, operation_inputs) -> web.Response:
    """apps_check_name_availability

    Check if an IoT Central application name is available.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param operation_inputs: Set the name parameter in the OperationInputs structure to the name of the IoT Central application to check.
    :type operation_inputs: dict | bytes

    """
    operation_inputs = OperationInputs.from_dict(operation_inputs)
    return web.Response(status=200)


async def apps_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, app) -> web.Response:
    """apps_create_or_update

    Create or update the metadata of an IoT Central application. The usual pattern to modify a property is to retrieve the IoT Central application metadata and security metadata, and then combine them with the modified values in a new body to update the IoT Central application.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT Central application.
    :type resource_group_name: str
    :param resource_name: The ARM resource name of the IoT Central application.
    :type resource_name: str
    :param app: The IoT Central application metadata and security metadata.
    :type app: dict | bytes

    """
    app = App.from_dict(app)
    return web.Response(status=200)


async def apps_delete(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """apps_delete

    Delete an IoT Central application.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT Central application.
    :type resource_group_name: str
    :param resource_name: The ARM resource name of the IoT Central application.
    :type resource_name: str

    """
    return web.Response(status=200)


async def apps_get(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """apps_get

    Get the metadata of an IoT Central application.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT Central application.
    :type resource_group_name: str
    :param resource_name: The ARM resource name of the IoT Central application.
    :type resource_name: str

    """
    return web.Response(status=200)


async def apps_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """apps_list_by_resource_group

    Get all the IoT Central Applications in a resource group.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT Central application.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def apps_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """apps_list_by_subscription

    Get all IoT Central Applications in a subscription.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def apps_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, app_patch) -> web.Response:
    """apps_update

    Update the metadata of an IoT Central application.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT Central application.
    :type resource_group_name: str
    :param resource_name: The ARM resource name of the IoT Central application.
    :type resource_name: str
    :param app_patch: The IoT Central application metadata and security metadata.
    :type app_patch: dict | bytes

    """
    app_patch = AppPatch.from_dict(app_patch)
    return web.Response(status=200)
