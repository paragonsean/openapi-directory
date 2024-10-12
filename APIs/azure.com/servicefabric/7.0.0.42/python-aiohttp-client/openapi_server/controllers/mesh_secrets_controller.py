from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_secret_resource_description_list import PagedSecretResourceDescriptionList
from openapi_server.models.secret_resource_description import SecretResourceDescription
from openapi_server import util


async def mesh_secret_create_or_update(request: web.Request, api_version, secret_resource_name, secret_resource_description) -> web.Response:
    """Creates or updates a Secret resource.

    Creates a Secret resource with the specified name, description and properties. If Secret resource with the same name exists, then it is updated with the specified description and properties. Once created, the kind and contentType of a secret resource cannot be updated.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param secret_resource_name: The name of the secret resource.
    :type secret_resource_name: str
    :param secret_resource_description: Description for creating a secret resource.
    :type secret_resource_description: dict | bytes

    """
    secret_resource_description = SecretResourceDescription.from_dict(secret_resource_description)
    return web.Response(status=200)


async def mesh_secret_delete(request: web.Request, api_version, secret_resource_name) -> web.Response:
    """Deletes the Secret resource.

    Deletes the specified Secret resource and all of its named values.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param secret_resource_name: The name of the secret resource.
    :type secret_resource_name: str

    """
    return web.Response(status=200)


async def mesh_secret_get(request: web.Request, api_version, secret_resource_name) -> web.Response:
    """Gets the Secret resource with the given name.

    Gets the information about the Secret resource with the given name. The information include the description and other properties of the Secret.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param secret_resource_name: The name of the secret resource.
    :type secret_resource_name: str

    """
    return web.Response(status=200)


async def mesh_secret_list(request: web.Request, api_version) -> web.Response:
    """Lists all the secret resources.

    Gets the information about all secret resources in a given resource group. The information include the description and other properties of the Secret.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str

    """
    return web.Response(status=200)
