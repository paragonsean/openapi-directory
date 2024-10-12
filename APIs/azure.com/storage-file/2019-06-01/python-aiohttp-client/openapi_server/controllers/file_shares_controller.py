from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.file_share import FileShare
from openapi_server.models.file_share_items import FileShareItems
from openapi_server import util


async def file_shares_create(request: web.Request, resource_group_name, account_name, share_name, api_version, subscription_id, file_share) -> web.Response:
    """file_shares_create

    Creates a new share under the specified account as described by request body. The share resource includes metadata and properties for that share. It does not include a list of the files contained by the share. 

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param share_name: The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type share_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param file_share: Properties of the file share to create.
    :type file_share: dict | bytes

    """
    file_share = FileShare.from_dict(file_share)
    return web.Response(status=200)


async def file_shares_delete(request: web.Request, resource_group_name, account_name, share_name, api_version, subscription_id) -> web.Response:
    """file_shares_delete

    Deletes specified share under its account.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param share_name: The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type share_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def file_shares_get(request: web.Request, resource_group_name, account_name, share_name, api_version, subscription_id) -> web.Response:
    """file_shares_get

    Gets properties of a specified share.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param share_name: The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type share_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def file_shares_list(request: web.Request, resource_group_name, account_name, api_version, subscription_id, maxpagesize=None, filter=None) -> web.Response:
    """file_shares_list

    Lists all shares.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param maxpagesize: Optional. Specified maximum number of shares that can be included in the list.
    :type maxpagesize: str
    :param filter: Optional. When specified, only share names starting with the filter will be listed.
    :type filter: str

    """
    return web.Response(status=200)


async def file_shares_update(request: web.Request, resource_group_name, account_name, share_name, api_version, subscription_id, file_share) -> web.Response:
    """file_shares_update

    Updates share properties as specified in request body. Properties not mentioned in the request will not be changed. Update fails if the specified share does not already exist. 

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param share_name: The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
    :type share_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param file_share: Properties to update for the file share.
    :type file_share: dict | bytes

    """
    file_share = FileShare.from_dict(file_share)
    return web.Response(status=200)
