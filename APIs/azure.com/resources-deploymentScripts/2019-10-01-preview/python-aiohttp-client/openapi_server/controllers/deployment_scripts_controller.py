from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_response import DefaultErrorResponse
from openapi_server.models.deployment_script import DeploymentScript
from openapi_server.models.deployment_script_list_result import DeploymentScriptListResult
from openapi_server.models.deployment_script_update_parameter import DeploymentScriptUpdateParameter
from openapi_server.models.script_log import ScriptLog
from openapi_server.models.script_logs_list import ScriptLogsList
from openapi_server import util


async def deployment_scripts_create(request: web.Request, subscription_id, resource_group_name, script_name, api_version, deployment_script) -> web.Response:
    """deployment_scripts_create

    Creates a deployment script.

    :param subscription_id: Subscription Id which forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param script_name: Name of the deployment script.
    :type script_name: str
    :param api_version: Client Api version.
    :type api_version: str
    :param deployment_script: Deployment script supplied to the operation.
    :type deployment_script: dict | bytes

    """
    deployment_script = DeploymentScript.from_dict(deployment_script)
    return web.Response(status=200)


async def deployment_scripts_delete(request: web.Request, subscription_id, resource_group_name, script_name, api_version) -> web.Response:
    """deployment_scripts_delete

    Deletes a deployment script. When operation completes, status code 200 returned without content.

    :param subscription_id: Subscription Id which forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param script_name: Name of the deployment script.
    :type script_name: str
    :param api_version: Client Api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployment_scripts_get(request: web.Request, subscription_id, resource_group_name, script_name, api_version) -> web.Response:
    """deployment_scripts_get

    Gets a deployment script with a given name.

    :param subscription_id: Subscription Id which forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param script_name: Name of the deployment script.
    :type script_name: str
    :param api_version: Client Api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployment_scripts_get_logs(request: web.Request, subscription_id, resource_group_name, script_name, api_version) -> web.Response:
    """deployment_scripts_get_logs

    Gets deployment script logs for a given deployment script name.

    :param subscription_id: Subscription Id which forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param script_name: Name of the deployment script.
    :type script_name: str
    :param api_version: Client Api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployment_scripts_get_logs_default(request: web.Request, subscription_id, resource_group_name, script_name, api_version) -> web.Response:
    """deployment_scripts_get_logs_default

    Gets deployment script logs for a given deployment script name.

    :param subscription_id: Subscription Id which forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param script_name: Name of the deployment script.
    :type script_name: str
    :param api_version: Client Api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployment_scripts_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """deployment_scripts_list_by_resource_group

    Lists deployments scripts.

    :param subscription_id: Subscription Id which forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployment_scripts_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """deployment_scripts_list_by_subscription

    Lists all deployment scripts for a given subscription.

    :param subscription_id: Subscription Id which forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def deployment_scripts_update(request: web.Request, subscription_id, resource_group_name, script_name, api_version, deployment_script=None) -> web.Response:
    """deployment_scripts_update

    Updates deployment script tags with specified values.

    :param subscription_id: Subscription Id which forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param script_name: Name of the deployment script.
    :type script_name: str
    :param api_version: Client Api version.
    :type api_version: str
    :param deployment_script: Deployment script resource with the tags to be updated.
    :type deployment_script: dict | bytes

    """
    deployment_script = DeploymentScriptUpdateParameter.from_dict(deployment_script)
    return web.Response(status=200)
