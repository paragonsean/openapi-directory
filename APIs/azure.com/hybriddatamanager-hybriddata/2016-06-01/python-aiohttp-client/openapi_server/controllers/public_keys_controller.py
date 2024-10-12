from typing import List, Dict
from aiohttp import web

from openapi_server.models.public_key import PublicKey
from openapi_server.models.public_key_list import PublicKeyList
from openapi_server import util


async def public_keys_get(request: web.Request, public_key_name, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """public_keys_get

    This method gets the public keys.

    :param public_key_name: Name of the public key.
    :type public_key_name: str
    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def public_keys_list_by_data_manager(request: web.Request, subscription_id, resource_group_name, data_manager_name, api_version) -> web.Response:
    """public_keys_list_by_data_manager

    This method gets the list view of public keys, however it will only have one element.

    :param subscription_id: The Subscription Id
    :type subscription_id: str
    :param resource_group_name: The Resource Group Name
    :type resource_group_name: str
    :param data_manager_name: The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    :type data_manager_name: str
    :param api_version: The API Version
    :type api_version: str

    """
    return web.Response(status=200)
