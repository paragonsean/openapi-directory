from typing import List, Dict
from aiohttp import web

from openapi_server.models.quota_list import QuotaList
from openapi_server import util


async def quotas_list(request: web.Request, subscription_id, location, api_version) -> web.Response:
    """quotas_list

    Get a list of all quota objects for KeyVault at a location.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The location of the quota.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
