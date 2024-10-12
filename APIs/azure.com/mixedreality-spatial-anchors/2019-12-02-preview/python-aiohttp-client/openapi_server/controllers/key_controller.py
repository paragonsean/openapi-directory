from typing import List, Dict
from aiohttp import web

from openapi_server.models.spatial_anchors_accounts_get_keys200_response import SpatialAnchorsAccountsGetKeys200Response
from openapi_server.models.spatial_anchors_accounts_list_by_subscription_default_response import SpatialAnchorsAccountsListBySubscriptionDefaultResponse
from openapi_server.models.spatial_anchors_accounts_regenerate_keys_request import SpatialAnchorsAccountsRegenerateKeysRequest
from openapi_server import util


async def spatial_anchors_accounts_get_keys(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """spatial_anchors_accounts_get_keys

    Get Both of the 2 Keys of a Spatial Anchors Account

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


async def spatial_anchors_accounts_regenerate_keys(request: web.Request, subscription_id, resource_group_name, account_name, api_version, regenerate) -> web.Response:
    """spatial_anchors_accounts_regenerate_keys

    Regenerate specified Key of a Spatial Anchors Account

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Name of an Mixed Reality Account.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param regenerate: Required information for key regeneration.
    :type regenerate: dict | bytes

    """
    regenerate = SpatialAnchorsAccountsRegenerateKeysRequest.from_dict(regenerate)
    return web.Response(status=200)
