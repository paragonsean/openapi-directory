from typing import List, Dict
from aiohttp import web

from openapi_server.models.project_resource import ProjectResource
from openapi_server.models.project_resource_list_result import ProjectResourceListResult
from openapi_server.models.project_resource_update_parameters import ProjectResourceUpdateParameters
from openapi_server import util


async def project_list_by_account_resource(request: web.Request, resource_group_name, subscription_id, api_version, root_resource_name) -> web.Response:
    """Projects_ListByAccountResource

    Gets all Visual Studio Team Services project resources created in the specified Team Services account.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param root_resource_name: Name of the Team Services account.
    :type root_resource_name: str

    """
    return web.Response(status=200)


async def projects_create(request: web.Request, resource_group_name, subscription_id, api_version, root_resource_name, resource_name, body, validating=None) -> web.Response:
    """Projects_Create

    Creates a Team Services project in the collection with the specified name. &#39;VersionControlOption&#39; and &#39;ProcessTemplateId&#39; must be specified in the resource properties. Valid values for VersionControlOption: Git, Tfvc. Valid values for ProcessTemplateId: 6B724908-EF14-45CF-84F8-768B5384DA45, ADCC42AB-9882-485E-A3ED-7678F01F66BC, 27450541-8E31-4150-9947-DC59F998FC01 (these IDs correspond to Scrum, Agile, and CMMI process templates).

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param root_resource_name: Name of the Team Services account.
    :type root_resource_name: str
    :param resource_name: Name of the Team Services project.
    :type resource_name: str
    :param body: The request data.
    :type body: dict | bytes
    :param validating: This parameter is ignored and should be set to an empty string.
    :type validating: str

    """
    body = ProjectResource.from_dict(body)
    return web.Response(status=200)


async def projects_get(request: web.Request, resource_group_name, subscription_id, api_version, root_resource_name, resource_name) -> web.Response:
    """Projects_Get

    Gets the details of a Team Services project resource.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param root_resource_name: Name of the Team Services account.
    :type root_resource_name: str
    :param resource_name: Name of the Team Services project.
    :type resource_name: str

    """
    return web.Response(status=200)


async def projects_update(request: web.Request, resource_group_name, subscription_id, api_version, root_resource_name, resource_name, body) -> web.Response:
    """Projects_Update

    Updates the tags of the specified Team Services project.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param root_resource_name: Name of the Team Services account.
    :type root_resource_name: str
    :param resource_name: Name of the Team Services project.
    :type resource_name: str
    :param body: The request data.
    :type body: dict | bytes

    """
    body = ProjectResourceUpdateParameters.from_dict(body)
    return web.Response(status=200)
