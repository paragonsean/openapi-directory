from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_resource_description import ApplicationResourceDescription
from openapi_server.models.application_resource_description_list import ApplicationResourceDescriptionList
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def application_create(request: web.Request, subscription_id, api_version, resource_group_name, application_resource_name, application_resource_description) -> web.Response:
    """Creates or updates an application resource.

    Creates an application resource with the specified name, description and properties. If an application resource with the same name exists, then it is updated with the specified description and properties.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str
    :param application_resource_description: Description for creating a Application resource.
    :type application_resource_description: dict | bytes

    """
    application_resource_description = ApplicationResourceDescription.from_dict(application_resource_description)
    return web.Response(status=200)


async def application_delete(request: web.Request, subscription_id, api_version, resource_group_name, application_resource_name) -> web.Response:
    """Deletes the application resource.

    Deletes the application resource identified by the name.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str

    """
    return web.Response(status=200)


async def application_get(request: web.Request, subscription_id, api_version, resource_group_name, application_resource_name) -> web.Response:
    """Gets the application resource with the given name.

    Gets the information about the application resource with the given name. The information include the description and other properties of the application.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str

    """
    return web.Response(status=200)


async def application_list_by_resource_group(request: web.Request, subscription_id, api_version, resource_group_name) -> web.Response:
    """Gets all the application resources in a given resource group.

    Gets the information about all application resources in a given resource group. The information include the description and other properties of the Application.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def application_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets all the application resources in a given subscription.

    Gets the information about all application resources in a given resource group. The information include the description and other properties of the application.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str

    """
    return web.Response(status=200)
