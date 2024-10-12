from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.spatial_anchors_account_key_regenerate_request import SpatialAnchorsAccountKeyRegenerateRequest
from openapi_server.models.spatial_anchors_account_keys import SpatialAnchorsAccountKeys
from openapi_server import util


async def spatial_anchors_accounts_get_keys(request: web.Request, subscription_id, resource_group_name, spatial_anchors_account_name, api_version) -> web.Response:
    """spatial_anchors_accounts_get_keys

    Get Both of the 2 Keys of a Spatial Anchors Account

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param spatial_anchors_account_name: Name of an Mixed Reality Spatial Anchors Account.
    :type spatial_anchors_account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def spatial_anchors_accounts_regenerate_keys(request: web.Request, subscription_id, resource_group_name, spatial_anchors_account_name, api_version, spatial_anchors_account_key_regenerate) -> web.Response:
    """spatial_anchors_accounts_regenerate_keys

    Regenerate 1 Key of a Spatial Anchors Account

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param spatial_anchors_account_name: Name of an Mixed Reality Spatial Anchors Account.
    :type spatial_anchors_account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param spatial_anchors_account_key_regenerate: Specifying which key to be regenerated.
    :type spatial_anchors_account_key_regenerate: dict | bytes

    """
    spatial_anchors_account_key_regenerate = SpatialAnchorsAccountKeyRegenerateRequest.from_dict(spatial_anchors_account_key_regenerate)
    return web.Response(status=200)
