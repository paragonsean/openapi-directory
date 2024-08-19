from typing import List, Dict
from aiohttp import web

from openapi_server.models.quota import Quota
from openapi_server.models.quota_list import QuotaList
from openapi_server import util


async def quotas_get(request: web.Request, subscription_id, location, resource_name, api_version) -> web.Response:
    """quotas_get

    Get a quota by name.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param resource_name: Name of the resource.
    :type resource_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def quotas_list(request: web.Request, subscription_id, location, api_version, filter=None) -> web.Response:
    """quotas_list

    List all quotas.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)
