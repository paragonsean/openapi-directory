from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.reference_data_set_create_or_update_parameters import ReferenceDataSetCreateOrUpdateParameters
from openapi_server.models.reference_data_set_list_response import ReferenceDataSetListResponse
from openapi_server.models.reference_data_set_resource import ReferenceDataSetResource
from openapi_server.models.reference_data_set_update_parameters import ReferenceDataSetUpdateParameters
from openapi_server import util


async def reference_data_sets_create_or_update(request: web.Request, subscription_id, resource_group_name, environment_name, reference_data_set_name, api_version, parameters) -> web.Response:
    """reference_data_sets_create_or_update

    Create or update a reference data set in the specified environment.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param reference_data_set_name: Name of the reference data set.
    :type reference_data_set_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Parameters for creating a reference data set.
    :type parameters: dict | bytes

    """
    parameters = ReferenceDataSetCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def reference_data_sets_delete(request: web.Request, subscription_id, resource_group_name, environment_name, reference_data_set_name, api_version) -> web.Response:
    """reference_data_sets_delete

    Deletes the reference data set with the specified name in the specified subscription, resource group, and environment

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param reference_data_set_name: The name of the Time Series Insights reference data set associated with the specified environment.
    :type reference_data_set_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def reference_data_sets_get(request: web.Request, subscription_id, resource_group_name, environment_name, reference_data_set_name, api_version) -> web.Response:
    """reference_data_sets_get

    Gets the reference data set with the specified name in the specified environment.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param reference_data_set_name: The name of the Time Series Insights reference data set associated with the specified environment.
    :type reference_data_set_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def reference_data_sets_list_by_environment(request: web.Request, subscription_id, resource_group_name, environment_name, api_version) -> web.Response:
    """reference_data_sets_list_by_environment

    Lists all the available reference data sets associated with the subscription and within the specified resource group and environment.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def reference_data_sets_update(request: web.Request, subscription_id, resource_group_name, environment_name, reference_data_set_name, api_version, reference_data_set_update_parameters) -> web.Response:
    """reference_data_sets_update

    Updates the reference data set with the specified name in the specified subscription, resource group, and environment.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :type environment_name: str
    :param reference_data_set_name: The name of the Time Series Insights reference data set associated with the specified environment.
    :type reference_data_set_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param reference_data_set_update_parameters: Request object that contains the updated information for the reference data set.
    :type reference_data_set_update_parameters: dict | bytes

    """
    reference_data_set_update_parameters = ReferenceDataSetUpdateParameters.from_dict(reference_data_set_update_parameters)
    return web.Response(status=200)
