from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.account_list import AccountList
from openapi_server.models.account_patch import AccountPatch
from openapi_server.models.channel_type_description_list import ChannelTypeDescriptionList
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.key_description import KeyDescription
from openapi_server.models.key_description_list import KeyDescriptionList
from openapi_server.models.regenerate_key_parameter import RegenerateKeyParameter
from openapi_server import util


async def accounts_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, api_version, account) -> web.Response:
    """Create or Update the EngagementFabric account

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param account_name: Account Name
    :type account_name: str
    :param api_version: API version
    :type api_version: str
    :param account: The EngagementFabric account description
    :type account: dict | bytes

    """
    account = Account.from_dict(account)
    return web.Response(status=200)


async def accounts_delete(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """Delete the EngagementFabric account

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param account_name: Account Name
    :type account_name: str
    :param api_version: API version
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_get(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """Get the EngagementFabric account

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param account_name: Account Name
    :type account_name: str
    :param api_version: API version
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """List the EngagementFabric accounts in given subscription

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param api_version: API version
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """List EngagementFabric accounts in given resource group

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param api_version: API version
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_list_channel_types(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """List available EngagementFabric channel types and functions

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param account_name: Account Name
    :type account_name: str
    :param api_version: API version
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_list_keys(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """List keys of the EngagementFabric account

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param account_name: Account Name
    :type account_name: str
    :param api_version: API version
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_regenerate_key(request: web.Request, subscription_id, resource_group_name, account_name, api_version, parameter) -> web.Response:
    """Regenerate key of the EngagementFabric account

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param account_name: Account Name
    :type account_name: str
    :param api_version: API version
    :type api_version: str
    :param parameter: Parameters specifying the key to be regenerated
    :type parameter: dict | bytes

    """
    parameter = RegenerateKeyParameter.from_dict(parameter)
    return web.Response(status=200)


async def accounts_update(request: web.Request, subscription_id, resource_group_name, account_name, api_version, account_patch) -> web.Response:
    """Update EngagementFabric account

    

    :param subscription_id: Subscription ID
    :type subscription_id: str
    :param resource_group_name: Resource Group Name
    :type resource_group_name: str
    :param account_name: Account Name
    :type account_name: str
    :param api_version: API version
    :type api_version: str
    :param account_patch: The account patch
    :type account_patch: dict | bytes

    """
    account_patch = AccountPatch.from_dict(account_patch)
    return web.Response(status=200)
