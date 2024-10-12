from typing import List, Dict
from aiohttp import web

from openapi_server.models.tags_resource import TagsResource
from openapi_server.models.web_test import WebTest
from openapi_server.models.web_test_list_result import WebTestListResult
from openapi_server import util


async def web_tests_create_or_update(request: web.Request, resource_group_name, api_version, subscription_id, web_test_name, web_test_definition) -> web.Response:
    """web_tests_create_or_update

    Creates or updates an Application Insights web test definition.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param web_test_name: The name of the Application Insights webtest resource.
    :type web_test_name: str
    :param web_test_definition: Properties that need to be specified to create or update an Application Insights web test definition.
    :type web_test_definition: dict | bytes

    """
    web_test_definition = WebTest.from_dict(web_test_definition)
    return web.Response(status=200)


async def web_tests_delete(request: web.Request, subscription_id, resource_group_name, web_test_name, api_version) -> web.Response:
    """web_tests_delete

    Deletes an Application Insights web test.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param web_test_name: The name of the Application Insights webtest resource.
    :type web_test_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def web_tests_get(request: web.Request, resource_group_name, api_version, subscription_id, web_test_name) -> web.Response:
    """web_tests_get

    Get a specific Application Insights web test definition.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param web_test_name: The name of the Application Insights webtest resource.
    :type web_test_name: str

    """
    return web.Response(status=200)


async def web_tests_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """web_tests_list

    Get all Application Insights web test alerts definitions within a subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def web_tests_list_by_component(request: web.Request, component_name, resource_group_name, api_version, subscription_id) -> web.Response:
    """web_tests_list_by_component

    Get all Application Insights web tests defined for the specified component.

    :param component_name: The name of the Application Insights component resource.
    :type component_name: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def web_tests_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """web_tests_list_by_resource_group

    Get all Application Insights web tests defined within a specified resource group.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def web_tests_update_tags(request: web.Request, resource_group_name, api_version, subscription_id, web_test_name, web_test_tags) -> web.Response:
    """web_tests_update_tags

    Creates or updates an Application Insights web test definition.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param web_test_name: The name of the Application Insights webtest resource.
    :type web_test_name: str
    :param web_test_tags: Updated tag information to set into the web test instance.
    :type web_test_tags: dict | bytes

    """
    web_test_tags = TagsResource.from_dict(web_test_tags)
    return web.Response(status=200)
