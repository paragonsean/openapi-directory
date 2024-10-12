from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.secret_value import SecretValue
from openapi_server.models.secret_value_resource_description import SecretValueResourceDescription
from openapi_server.models.secret_value_resource_description_list import SecretValueResourceDescriptionList
from openapi_server import util


async def secret_value_create(request: web.Request, subscription_id, api_version, resource_group_name, secret_resource_name, secret_value_resource_name, secret_value_resource_description) -> web.Response:
    """Adds the specified value as a new version of the specified secret resource.

    Creates a new value of the specified secret resource. The name of the value is typically the version identifier. Once created the value cannot be changed.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param secret_resource_name: The name of the secret resource.
    :type secret_resource_name: str
    :param secret_value_resource_name: The name of the secret resource value which is typically the version identifier for the value.
    :type secret_value_resource_name: str
    :param secret_value_resource_description: Description for creating a value of a secret resource.
    :type secret_value_resource_description: dict | bytes

    """
    secret_value_resource_description = SecretValueResourceDescription.from_dict(secret_value_resource_description)
    return web.Response(status=200)


async def secret_value_delete(request: web.Request, subscription_id, api_version, resource_group_name, secret_resource_name, secret_value_resource_name) -> web.Response:
    """Deletes the specified  value of the named secret resource.

    Deletes the secret value resource identified by the name. The name of the resource is typically the version associated with that value. Deletion will fail if the specified value is in use.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param secret_resource_name: The name of the secret resource.
    :type secret_resource_name: str
    :param secret_value_resource_name: The name of the secret resource value which is typically the version identifier for the value.
    :type secret_value_resource_name: str

    """
    return web.Response(status=200)


async def secret_value_get(request: web.Request, subscription_id, api_version, resource_group_name, secret_resource_name, secret_value_resource_name) -> web.Response:
    """Gets the specified secret value resource.

    Get the information about the specified named secret value resources. The information does not include the actual value of the secret.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param secret_resource_name: The name of the secret resource.
    :type secret_resource_name: str
    :param secret_value_resource_name: The name of the secret resource value which is typically the version identifier for the value.
    :type secret_value_resource_name: str

    """
    return web.Response(status=200)


async def secret_value_list(request: web.Request, subscription_id, api_version, resource_group_name, secret_resource_name) -> web.Response:
    """List names of all values of the specified secret resource.

    Gets information about all secret value resources of the specified secret resource. The information includes the names of the secret value resources, but not the actual values.

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


async def secret_value_list_value(request: web.Request, subscription_id, api_version, resource_group_name, secret_resource_name, secret_value_resource_name) -> web.Response:
    """Lists the specified value of the secret resource.

    Lists the decrypted value of the specified named value of the secret resource. This is a privileged operation.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param secret_resource_name: The name of the secret resource.
    :type secret_resource_name: str
    :param secret_value_resource_name: The name of the secret resource value which is typically the version identifier for the value.
    :type secret_value_resource_name: str

    """
    return web.Response(status=200)
