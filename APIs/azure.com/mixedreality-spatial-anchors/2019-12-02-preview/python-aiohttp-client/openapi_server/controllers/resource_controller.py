from typing import List, Dict
from aiohttp import web

from openapi_server.models.spatial_anchors_account import SpatialAnchorsAccount
from openapi_server.models.spatial_anchors_account_page import SpatialAnchorsAccountPage
from openapi_server.models.spatial_anchors_accounts_list_by_subscription_default_response import SpatialAnchorsAccountsListBySubscriptionDefaultResponse
from openapi_server import util


async def spatial_anchors_accounts_create(request: web.Request, subscription_id, resource_group_name, account_name, api_version, spatial_anchors_account) -> web.Response:
    """spatial_anchors_accounts_create

    Creating or Updating a Spatial Anchors Account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Name of an Mixed Reality Account.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param spatial_anchors_account: Spatial Anchors Account parameter.
    :type spatial_anchors_account: dict | bytes

    """
    spatial_anchors_account = SpatialAnchorsAccount.from_dict(spatial_anchors_account)
    return web.Response(status=200)


async def spatial_anchors_accounts_delete(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """spatial_anchors_accounts_delete

    Delete a Spatial Anchors Account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Name of an Mixed Reality Account.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def spatial_anchors_accounts_get(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """spatial_anchors_accounts_get

    Retrieve a Spatial Anchors Account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Name of an Mixed Reality Account.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def spatial_anchors_accounts_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """spatial_anchors_accounts_list_by_resource_group

    List Resources by Resource Group

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def spatial_anchors_accounts_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """spatial_anchors_accounts_list_by_subscription

    List Spatial Anchors Accounts by Subscription

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def spatial_anchors_accounts_update(request: web.Request, subscription_id, resource_group_name, account_name, api_version, spatial_anchors_account) -> web.Response:
    """spatial_anchors_accounts_update

    Updating a Spatial Anchors Account

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Name of an Mixed Reality Account.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param spatial_anchors_account: Spatial Anchors Account parameter.
    :type spatial_anchors_account: dict | bytes

    """
    spatial_anchors_account = SpatialAnchorsAccount.from_dict(spatial_anchors_account)
    return web.Response(status=200)
