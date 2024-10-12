from typing import List, Dict
from aiohttp import web

from openapi_server.models.workbook import Workbook
from openapi_server.models.workbook_error import WorkbookError
from openapi_server.models.workbook_update_parameters import WorkbookUpdateParameters
from openapi_server.models.workbooks_list_result import WorkbooksListResult
from openapi_server import util


async def workbooks_create_or_update(request: web.Request, subscription_id, resource_group_name, resource_name, source_id, api_version, workbook_properties) -> web.Response:
    """workbooks_create_or_update

    Create a new workbook.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param source_id: Azure Resource Id that will fetch all related workbooks.
    :type source_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param workbook_properties: Properties that need to be specified to create a new workbook.
    :type workbook_properties: dict | bytes

    """
    workbook_properties = Workbook.from_dict(workbook_properties)
    return web.Response(status=200)


async def workbooks_delete(request: web.Request, subscription_id, resource_group_name, resource_name, api_version) -> web.Response:
    """workbooks_delete

    Delete a workbook.

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


async def workbooks_get(request: web.Request, subscription_id, resource_group_name, resource_name, api_version) -> web.Response:
    """workbooks_get

    Get a single workbook by its resourceName.

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


async def workbooks_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, category, source_id, api_version, tags=None, can_fetch_content=None) -> web.Response:
    """workbooks_list_by_resource_group

    Get all Workbooks defined within a specified resource group and category.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param category: Category of workbook to return.
    :type category: str
    :param source_id: Azure Resource Id that will fetch all related workbooks.
    :type source_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param tags: Tags presents on each workbook returned.
    :type tags: List[str]
    :param can_fetch_content: Flag indicating whether or not to return the full content for each applicable workbook. If false, only return summary content for workbooks.
    :type can_fetch_content: bool

    """
    return web.Response(status=200)


async def workbooks_update(request: web.Request, subscription_id, resource_group_name, resource_name, source_id, api_version, workbook_update_parameters=None) -> web.Response:
    """workbooks_update

    Updates a workbook that has already been added.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param source_id: Azure Resource Id that will fetch all related workbooks.
    :type source_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param workbook_update_parameters: Properties that need to be specified to create a new workbook.
    :type workbook_update_parameters: dict | bytes

    """
    workbook_update_parameters = WorkbookUpdateParameters.from_dict(workbook_update_parameters)
    return web.Response(status=200)
