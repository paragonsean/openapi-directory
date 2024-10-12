from typing import List, Dict
from aiohttp import web

from openapi_server.models.workbook_error import WorkbookError
from openapi_server.models.workbook_template import WorkbookTemplate
from openapi_server.models.workbook_template_update_parameters import WorkbookTemplateUpdateParameters
from openapi_server.models.workbook_templates_list_result import WorkbookTemplatesListResult
from openapi_server import util


async def workbook_templates_create_or_update(request: web.Request, subscription_id, resource_group_name, resource_name, api_version, workbook_template_properties) -> web.Response:
    """workbook_templates_create_or_update

    Create a new workbook template.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param workbook_template_properties: Properties that need to be specified to create a new workbook.
    :type workbook_template_properties: dict | bytes

    """
    workbook_template_properties = WorkbookTemplate.from_dict(workbook_template_properties)
    return web.Response(status=200)


async def workbook_templates_delete(request: web.Request, subscription_id, resource_group_name, resource_name, api_version) -> web.Response:
    """workbook_templates_delete

    Delete a workbook template.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def workbook_templates_get(request: web.Request, subscription_id, resource_group_name, resource_name, api_version) -> web.Response:
    """workbook_templates_get

    Get a single workbook template by its resourceName.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def workbook_templates_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """workbook_templates_list_by_resource_group

    Get all Workbook templates defined within a specified resource group.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def workbook_templates_update(request: web.Request, subscription_id, resource_group_name, resource_name, api_version, workbook_template_update_parameters=None) -> web.Response:
    """workbook_templates_update

    Updates a workbook template that has already been added.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param workbook_template_update_parameters: Properties that need to be specified to patch a workbook template.
    :type workbook_template_update_parameters: dict | bytes

    """
    workbook_template_update_parameters = WorkbookTemplateUpdateParameters.from_dict(workbook_template_update_parameters)
    return web.Response(status=200)
