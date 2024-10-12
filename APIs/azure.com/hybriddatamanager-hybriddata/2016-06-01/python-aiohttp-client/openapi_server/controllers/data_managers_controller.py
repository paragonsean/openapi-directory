from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_manager import DataManager
from openapi_server.models.data_manager_list import DataManagerList
from openapi_server.models.data_manager_update_parameter import DataManagerUpdateParameter
from openapi_server import util


async def data_managers_create(request: web.Request, subscription_id, resource_group_name, data_manager_name, api_version, data_manager) -> web.Response:
    """data_managers_create

    Creates a new data manager resource with the specified parameters. Existing resources cannot be updated with this API  and should instead be updated with the Update data manager resource API.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str
    :param data_manager: Data manager resource details from request body.
    :type data_manager: dict | bytes

    """
    data_manager = DataManager.from_dict(data_manager)
    return web.Response(status=200)


async def data_managers_delete(request: web.Request, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """data_managers_delete

    Deletes a data manager resource in Microsoft Azure.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def data_managers_get(request: web.Request, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """data_managers_get

    Gets information about the specified data manager resource.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def data_managers_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """data_managers_list

    Lists all the data manager resources available under the subscription.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def data_managers_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """data_managers_list_by_resource_group

    Lists all the data manager resources available under the given resource group.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def data_managers_update(request: web.Request, subscription_id, resource_group_name, data_manager_name, api_version, data_manager_update_parameter, if_match=None) -> web.Response:
    """data_managers_update

    Updates the properties of an existing data manager resource.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str
    :param data_manager_update_parameter: Data manager resource details from request body.
    :type data_manager_update_parameter: dict | bytes
    :param if_match: Defines the If-Match condition. The patch will be performed only if the ETag of the data manager resource on the server matches this value.
    :type if_match: str

    """
    data_manager_update_parameter = DataManagerUpdateParameter.from_dict(data_manager_update_parameter)
    return web.Response(status=200)
