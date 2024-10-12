from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.secret_resource_description import SecretResourceDescription
from openapi_server.models.secret_resource_description_list import SecretResourceDescriptionList
from openapi_server import util


async def secret_create(request: web.Request, subscription_id, api_version, resource_group_name, secret_resource_name, secret_resource_description) -> web.Response:
    """Creates or updates a secret resource.

    Creates a secret resource with the specified name, description and properties. If a secret resource with the same name exists, then it is updated with the specified description and properties.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param secret_resource_name: The name of the secret resource.
    :type secret_resource_name: str
    :param secret_resource_description: Description for creating a secret resource.
    :type secret_resource_description: dict | bytes

    """
    secret_resource_description = SecretResourceDescription.from_dict(secret_resource_description)
    return web.Response(status=200)


async def secret_delete(request: web.Request, subscription_id, api_version, resource_group_name, secret_resource_name) -> web.Response:
    """Deletes the secret resource.

    Deletes the secret resource identified by the name.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param secret_resource_name: The name of the secret resource.
    :type secret_resource_name: str

    """
    return web.Response(status=200)


async def secret_get(request: web.Request, subscription_id, api_version, resource_group_name, secret_resource_name) -> web.Response:
    """Gets the secret resource with the given name.

    Gets the information about the secret resource with the given name. The information include the description and other properties of the secret.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param secret_resource_name: The name of the secret resource.
    :type secret_resource_name: str

    """
    return web.Response(status=200)


async def secret_list_by_resource_group(request: web.Request, subscription_id, api_version, resource_group_name) -> web.Response:
    """Gets all the secret resources in a given resource group.

    Gets the information about all secret resources in a given resource group. The information include the description and other properties of the Secret.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def secret_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets all the secret resources in a given subscription.

    Gets the information about all secret resources in a given resource group. The information include the description and other properties of the secret.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str

    """
    return web.Response(status=200)
