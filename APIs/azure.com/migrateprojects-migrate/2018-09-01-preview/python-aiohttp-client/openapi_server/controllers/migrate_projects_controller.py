from typing import List, Dict
from aiohttp import web

from openapi_server.models.migrate_project import MigrateProject
from openapi_server.models.refresh_summary_input import RefreshSummaryInput
from openapi_server.models.refresh_summary_result import RefreshSummaryResult
from openapi_server.models.register_tool_input import RegisterToolInput
from openapi_server.models.registration_result import RegistrationResult
from openapi_server import util


async def migrate_projects_delete_migrate_project(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version, accept_language=None) -> web.Response:
    """Delete the migrate project

    Delete the migrate project. Deleting non-existent project is a no-operation.

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def migrate_projects_get_migrate_project(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version) -> web.Response:
    """Method to get a migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str

    """
    return web.Response(status=200)


async def migrate_projects_patch_migrate_project(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version, body, accept_language=None) -> web.Response:
    """Update migrate project.

    Update a migrate project with specified name. Supports partial updates, for example only tags can be provided.

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param body: Body with migrate project details.
    :type body: dict | bytes
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    body = MigrateProject.from_dict(body)
    return web.Response(status=200)


async def migrate_projects_put_migrate_project(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version, body, accept_language=None) -> web.Response:
    """Method to create or update a migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param body: Body with migrate project details.
    :type body: dict | bytes
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    body = MigrateProject.from_dict(body)
    return web.Response(status=200)


async def migrate_projects_refresh_migrate_project_summary(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version, input) -> web.Response:
    """Refresh the summary of the migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param input: The goal input which needs to be refreshed.
    :type input: dict | bytes

    """
    input = RefreshSummaryInput.from_dict(input)
    return web.Response(status=200)


async def migrate_projects_register_tool(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version, input, accept_language=None) -> web.Response:
    """Registers a tool with the migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param input: Input containing the name of the tool to be registered.
    :type input: dict | bytes
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    input = RegisterToolInput.from_dict(input)
    return web.Response(status=200)
