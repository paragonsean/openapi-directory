from typing import List, Dict
from aiohttp import web

from openapi_server.models.spatial_anchors_account_page import SpatialAnchorsAccountPage
from openapi_server.models.spatial_anchors_accounts_list_by_subscription_default_response import SpatialAnchorsAccountsListBySubscriptionDefaultResponse
from openapi_server import util


async def spatial_anchors_accounts_list_by_subscription_0(request: web.Request, subscription_id, api_version) -> web.Response:
    """spatial_anchors_accounts_list_by_subscription_0

    List Spatial Anchors Accounts by Subscription

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
