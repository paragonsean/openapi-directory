from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.run import Run
from openapi_server.models.run_get_log_result import RunGetLogResult
from openapi_server.models.run_list_result import RunListResult
from openapi_server.models.run_update_parameters import RunUpdateParameters
from openapi_server import util


async def runs_cancel(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, run_id) -> web.Response:
    """runs_cancel

    Cancel an existing run.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param run_id: The run ID.
    :type run_id: str

    """
    return web.Response(status=200)


async def runs_get(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, run_id) -> web.Response:
    """runs_get

    Gets the detailed information for a given run.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param run_id: The run ID.
    :type run_id: str

    """
    return web.Response(status=200)


async def runs_get_log_sas_url(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, run_id) -> web.Response:
    """runs_get_log_sas_url

    Gets a link to download the run logs.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param run_id: The run ID.
    :type run_id: str

    """
    return web.Response(status=200)


async def runs_list(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, filter=None, top=None) -> web.Response:
    """runs_list

    Gets all the runs for a registry.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param filter: The runs filter to apply on the operation. Arithmetic operators are not supported. The allowed string function is &#39;contains&#39;. All logical operators except &#39;Not&#39;, &#39;Has&#39;, &#39;All&#39; are allowed.
    :type filter: str
    :param top: $top is supported for get list of runs, which limits the maximum number of runs to return.
    :type top: int

    """
    return web.Response(status=200)


async def runs_update(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, run_id, run_update_parameters) -> web.Response:
    """runs_update

    Patch the run properties.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param run_id: The run ID.
    :type run_id: str
    :param run_update_parameters: The run update properties.
    :type run_update_parameters: dict | bytes

    """
    run_update_parameters = RunUpdateParameters.from_dict(run_update_parameters)
    return web.Response(status=200)
