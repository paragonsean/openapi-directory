from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key_request import APIKeyRequest
from openapi_server.models.application_insights_component_api_key import ApplicationInsightsComponentAPIKey
from openapi_server.models.application_insights_component_api_key_list_result import ApplicationInsightsComponentAPIKeyListResult
from openapi_server import util


async def a_pi_keys_create(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, api_key_properties) -> web.Response:
    """a_pi_keys_create

    Create an API Key of an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param api_key_properties: Properties that need to be specified to create an API key of a Application Insights component.
    :type api_key_properties: dict | bytes

    """
    api_key_properties = APIKeyRequest.from_dict(api_key_properties)
    return web.Response(status=200)


async def a_pi_keys_delete(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, key_id) -> web.Response:
    """a_pi_keys_delete

    Delete an API Key of an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param key_id: The API Key ID. This is unique within a Application Insights component.
    :type key_id: str

    """
    return web.Response(status=200)


async def a_pi_keys_get(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, key_id) -> web.Response:
    """a_pi_keys_get

    Get the API Key for this key id.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param key_id: The API Key ID. This is unique within a Application Insights component.
    :type key_id: str

    """
    return web.Response(status=200)


async def a_pi_keys_list(request: web.Request, resource_group_name, api_version, subscription_id, resource_name) -> web.Response:
    """a_pi_keys_list

    Gets a list of API keys of an Application Insights component.

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
