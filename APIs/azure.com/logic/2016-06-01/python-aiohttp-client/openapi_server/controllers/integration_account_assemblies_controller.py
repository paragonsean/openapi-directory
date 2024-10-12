from typing import List, Dict
from aiohttp import web

from openapi_server.models.assembly_collection import AssemblyCollection
from openapi_server.models.assembly_definition import AssemblyDefinition
from openapi_server.models.workflow_trigger_callback_url import WorkflowTriggerCallbackUrl
from openapi_server import util


async def integration_account_assemblies_create_or_update(request: web.Request, subscription_id, resource_group_name, integration_account_name, assembly_artifact_name, api_version, assembly_artifact) -> web.Response:
    """integration_account_assemblies_create_or_update

    Create or update an assembly for an integration account.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param assembly_artifact_name: The assembly artifact name.
    :type assembly_artifact_name: str
    :param api_version: The API version.
    :type api_version: str
    :param assembly_artifact: The assembly artifact.
    :type assembly_artifact: dict | bytes

    """
    assembly_artifact = AssemblyDefinition.from_dict(assembly_artifact)
    return web.Response(status=200)


async def integration_account_assemblies_delete(request: web.Request, subscription_id, resource_group_name, integration_account_name, assembly_artifact_name, api_version) -> web.Response:
    """integration_account_assemblies_delete

    Delete an assembly for an integration account.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param assembly_artifact_name: The assembly artifact name.
    :type assembly_artifact_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_account_assemblies_get(request: web.Request, subscription_id, resource_group_name, integration_account_name, assembly_artifact_name, api_version) -> web.Response:
    """integration_account_assemblies_get

    Get an assembly for an integration account.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param assembly_artifact_name: The assembly artifact name.
    :type assembly_artifact_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_account_assemblies_list(request: web.Request, subscription_id, resource_group_name, integration_account_name, api_version) -> web.Response:
    """integration_account_assemblies_list

    List the assemblies for an integration account.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_account_assemblies_list_content_callback_url(request: web.Request, subscription_id, resource_group_name, integration_account_name, assembly_artifact_name, api_version) -> web.Response:
    """integration_account_assemblies_list_content_callback_url

    Get the content callback url for an integration account assembly.

    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param integration_account_name: The integration account name.
    :type integration_account_name: str
    :param assembly_artifact_name: The assembly artifact name.
    :type assembly_artifact_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
