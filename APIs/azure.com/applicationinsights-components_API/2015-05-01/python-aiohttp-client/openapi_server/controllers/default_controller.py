from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_insights_component import ApplicationInsightsComponent
from openapi_server.models.application_insights_component_list_result import ApplicationInsightsComponentListResult
from openapi_server.models.component_purge_body import ComponentPurgeBody
from openapi_server.models.component_purge_response import ComponentPurgeResponse
from openapi_server.models.component_purge_status_response import ComponentPurgeStatusResponse
from openapi_server.models.tags_resource import TagsResource
from openapi_server import util


async def components_create_or_update(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, insight_properties) -> web.Response:
    """components_create_or_update

    Creates (or updates) an Application Insights component. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param insight_properties: Properties that need to be specified to create an Application Insights component.
    :type insight_properties: dict | bytes

    """
    insight_properties = ApplicationInsightsComponent.from_dict(insight_properties)
    return web.Response(status=200)


async def components_delete(request: web.Request, resource_group_name, api_version, subscription_id, resource_name) -> web.Response:
    """components_delete

    Deletes an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def components_get(request: web.Request, resource_group_name, api_version, subscription_id, resource_name) -> web.Response:
    """components_get

    Returns an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def components_get_purge_status(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, purge_id) -> web.Response:
    """components_get_purge_status

    Get status for an ongoing purge operation.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param purge_id: In a purge status request, this is the Id of the operation the status of which is returned.
    :type purge_id: str

    """
    return web.Response(status=200)


async def components_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """components_list

    Gets a list of all Application Insights components within a subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def components_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """components_list_by_resource_group

    Gets a list of Application Insights components within a resource group.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def components_purge(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, body) -> web.Response:
    """components_purge

    Purges data in an Application Insights component by a set of user-defined filters.  In order to manage system resources, purge requests are throttled at 50 requests per hour. You should batch the execution of purge requests by sending a single command whose predicate includes all user identities that require purging. Use the in operator to specify multiple identities. You should run the query prior to using for a purge request to verify that the results are expected.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param body: Describes the body of a request to purge data in a single table of an Application Insights component
    :type body: dict | bytes

    """
    body = ComponentPurgeBody.from_dict(body)
    return web.Response(status=200)


async def components_update_tags(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, component_tags) -> web.Response:
    """components_update_tags

    Updates an existing component&#39;s tags. To update other fields use the CreateOrUpdate method.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param component_tags: Updated tag information to set into the component instance.
    :type component_tags: dict | bytes

    """
    component_tags = TagsResource.from_dict(component_tags)
    return web.Response(status=200)
