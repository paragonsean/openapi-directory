from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_definition import JobDefinition
from openapi_server.models.job_definition_list import JobDefinitionList
from openapi_server.models.run_parameters import RunParameters
from openapi_server import util


async def job_definitions_create_or_update(request: web.Request, data_service_name, job_definition_name, subscription_id, resource_group_name, data_manager_name, api_version, job_definition) -> web.Response:
    """job_definitions_create_or_update

    Creates or updates a job definition.

    :param data_service_name: The data service type of the job definition.
    :type data_service_name: str
    :param job_definition_name: The job definition name to be created or updated.
    :type job_definition_name: str
    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str
    :param job_definition: Job Definition object to be created or updated.
    :type job_definition: dict | bytes

    """
    job_definition = JobDefinition.from_dict(job_definition)
    return web.Response(status=200)


async def job_definitions_delete(request: web.Request, data_service_name, job_definition_name, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """job_definitions_delete

    This method deletes the given job definition.

    :param data_service_name: The data service type of the job definition.
    :type data_service_name: str
    :param job_definition_name: The job definition name to be deleted.
    :type job_definition_name: str
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


async def job_definitions_get(request: web.Request, data_service_name, job_definition_name, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """job_definitions_get

    This method gets job definition object by name.

    :param data_service_name: The data service name of the job definition
    :type data_service_name: str
    :param job_definition_name: The job definition name that is being queried.
    :type job_definition_name: str
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


async def job_definitions_list_by_data_manager(request: web.Request, subscription_id, resource_group_name, data_manager_name, api_version, filter=None) -> web.Response:
    """job_definitions_list_by_data_manager

    This method gets all the job definitions of the given data manager resource.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)


async def job_definitions_list_by_data_service(request: web.Request, data_service_name, subscription_id, resource_group_name, data_manager_name, api_version, filter=None) -> web.Response:
    """job_definitions_list_by_data_service

    This method gets all the job definitions of the given data service name.

    :param data_service_name: The data service type of interest.
    :type data_service_name: str
    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)


async def job_definitions_run(request: web.Request, data_service_name, job_definition_name, subscription_id, resource_group_name, data_manager_name, api_version, run_parameters) -> web.Response:
    """job_definitions_run

    This method runs a job instance of the given job definition.

    :param data_service_name: The data service type of the job definition.
    :type data_service_name: str
    :param job_definition_name: Name of the job definition.
    :type job_definition_name: str
    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str
    :param run_parameters: Run time parameters for the job definition.
    :type run_parameters: dict | bytes

    """
    run_parameters = RunParameters.from_dict(run_parameters)
    return web.Response(status=200)
