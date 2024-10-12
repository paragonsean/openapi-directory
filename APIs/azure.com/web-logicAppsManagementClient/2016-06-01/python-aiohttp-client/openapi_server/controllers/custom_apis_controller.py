from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_api_definition import CustomApiDefinition
from openapi_server.models.custom_api_definition_collection import CustomApiDefinitionCollection
from openapi_server.models.custom_api_reference import CustomApiReference
from openapi_server.models.wsdl_definition import WsdlDefinition
from openapi_server.models.wsdl_service_collection import WsdlServiceCollection
from openapi_server import util


async def custom_apis_create_or_update(request: web.Request, subscription_id, resource_group_name, api_name, api_version, custom_api) -> web.Response:
    """Replaces an existing custom API

    Creates or updates an existing custom API

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param api_name: API name
    :type api_name: str
    :param api_version: API Version
    :type api_version: str
    :param custom_api: The custom API
    :type custom_api: dict | bytes

    """
    custom_api = CustomApiDefinition.from_dict(custom_api)
    return web.Response(status=200)


async def custom_apis_delete(request: web.Request, subscription_id, resource_group_name, api_name, api_version) -> web.Response:
    """Delete a custom API

    Deletes a custom API from the resource group

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param api_name: API name
    :type api_name: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def custom_apis_extract_api_definition_from_wsdl(request: web.Request, subscription_id, location, api_version, wsdl_definition) -> web.Response:
    """Returns API definition from WSDL

    Parses the specified WSDL and extracts the API definition

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param location: The location
    :type location: str
    :param api_version: API Version
    :type api_version: str
    :param wsdl_definition: WSDL definition
    :type wsdl_definition: dict | bytes

    """
    wsdl_definition = WsdlDefinition.from_dict(wsdl_definition)
    return web.Response(status=200)


async def custom_apis_get(request: web.Request, subscription_id, resource_group_name, api_name, api_version) -> web.Response:
    """Get a custom API

    Gets a custom API by name for a specific subscription and resource group

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param api_name: API name
    :type api_name: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def custom_apis_list(request: web.Request, subscription_id, api_version, top=None, skiptoken=None) -> web.Response:
    """List of custom APIs

    Gets a list of all custom APIs for a subscription id

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param top: The number of items to be included in the result
    :type top: int
    :param skiptoken: Skip Token
    :type skiptoken: str

    """
    return web.Response(status=200)


async def custom_apis_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, top=None, skiptoken=None) -> web.Response:
    """List of custom APIs

    Gets a list of all custom APIs in a subscription for a specific resource group

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param api_version: API Version
    :type api_version: str
    :param top: The number of items to be included in the result
    :type top: int
    :param skiptoken: Skip Token
    :type skiptoken: str

    """
    return web.Response(status=200)


async def custom_apis_list_wsdl_interfaces(request: web.Request, subscription_id, location, api_version, wsdl_definition) -> web.Response:
    """Lists WSDL interfaces

    This returns the list of interfaces in the WSDL

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param location: The location
    :type location: str
    :param api_version: API Version
    :type api_version: str
    :param wsdl_definition: WSDL definition
    :type wsdl_definition: dict | bytes

    """
    wsdl_definition = WsdlDefinition.from_dict(wsdl_definition)
    return web.Response(status=200)


async def custom_apis_move(request: web.Request, subscription_id, resource_group_name, api_name, api_version, custom_api_reference) -> web.Response:
    """Moves the custom API

    Moves a specific custom API

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param api_name: API name
    :type api_name: str
    :param api_version: API Version
    :type api_version: str
    :param custom_api_reference: The custom API reference
    :type custom_api_reference: dict | bytes

    """
    custom_api_reference = CustomApiReference.from_dict(custom_api_reference)
    return web.Response(status=200)


async def custom_apis_update(request: web.Request, subscription_id, resource_group_name, api_name, api_version, custom_api) -> web.Response:
    """Update an existing custom API

    Updates an existing custom API&#39;s tags

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param api_name: API name
    :type api_name: str
    :param api_version: API Version
    :type api_version: str
    :param custom_api: The custom API
    :type custom_api: dict | bytes

    """
    custom_api = CustomApiDefinition.from_dict(custom_api)
    return web.Response(status=200)
