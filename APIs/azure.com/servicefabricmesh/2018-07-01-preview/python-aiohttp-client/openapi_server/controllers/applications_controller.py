from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_resource_description import ApplicationResourceDescription
from openapi_server.models.application_resource_description_list import ApplicationResourceDescriptionList
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def application_create(request: web.Request, subscription_id, api_version, resource_group_name, application_name, application_resource_description) -> web.Response:
    """Creates or updates an application resource.

    Creates an application resource with the specified name and description. If an application with the same name already exists, then its description is updated to the one indicated in this request.  Use network resources to provide public connectivity to the services of an application. 

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_name: The identity of the application.
    :type application_name: str
    :param application_resource_description: Description for creating an application resource.
    :type application_resource_description: dict | bytes

    """
    application_resource_description = ApplicationResourceDescription.from_dict(application_resource_description)
    return web.Response(status=200)


async def application_delete(request: web.Request, subscription_id, api_version, resource_group_name, application_name) -> web.Response:
    """Deletes the application resource.

    Deletes the application resource identified by the name.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_name: The identity of the application.
    :type application_name: str

    """
    return web.Response(status=200)


async def application_get(request: web.Request, subscription_id, api_version, resource_group_name, application_name) -> web.Response:
    """Gets the application resource.

    Gets the information about the application resource with a given name. The information includes the information about the application&#39;s services and other runtime properties.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_name: The identity of the application.
    :type application_name: str

    """
    return web.Response(status=200)


async def application_list_by_resource_group(request: web.Request, subscription_id, api_version, resource_group_name) -> web.Response:
    """Gets all the application resources in a given resource group.

    Gets the information about all application resources in a given resource group. The information includes the information about the application&#39;s services and other runtime properties.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def application_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets all the application resources in a given subscription.

    Gets the information about all application resources in a given subscription. The information includes the information about the application&#39;s services and other runtime properties.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str

    """
    return web.Response(status=200)
