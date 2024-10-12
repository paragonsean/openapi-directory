from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.response_with_continuation_secret import ResponseWithContinuationSecret
from openapi_server.models.secret import Secret
from openapi_server import util


async def secrets_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, secret) -> web.Response:
    """secrets_create_or_update

    Create or replace an existing secret.

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
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)
