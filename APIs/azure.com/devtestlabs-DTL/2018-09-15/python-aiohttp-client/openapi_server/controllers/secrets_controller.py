from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.secret import Secret
from openapi_server.models.secret_fragment import SecretFragment
from openapi_server.models.secret_list import SecretList
from openapi_server import util


async def secrets_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, secret) -> web.Response:
    """secrets_create_or_update

    Create or replace an existing secret. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the secret.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param secret: A secret.
    :type secret: dict | bytes

    """
    secret = Secret.from_dict(secret)
    return web.Response(status=200)


async def secrets_delete(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version) -> web.Response:
    """secrets_delete

    Delete secret.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the secret.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def secrets_get(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, expand=None) -> web.Response:
    """secrets_get

    Get secret.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the secret.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;value)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def secrets_list(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """secrets_list

    List secrets in a given user profile.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;value)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;)
    :type filter: str
    :param top: The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39;
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39;
    :type orderby: str

    """
    return web.Response(status=200)


async def secrets_update(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, secret) -> web.Response:
    """secrets_update

    Allows modifying tags of secrets. All other properties will be ignored.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the secret.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param secret: A secret.
    :type secret: dict | bytes

    """
    secret = SecretFragment.from_dict(secret)
    return web.Response(status=200)
