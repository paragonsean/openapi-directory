from typing import List, Dict
from aiohttp import web

from openapi_server.models.quota import Quota
from openapi_server import util


async def quotas_create_or_update(request: web.Request, subscription_id, location, resource_name, api_version, quota) -> web.Response:
    """quotas_create_or_update

    Create or update a quota.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param resource_name: Name of the resource.
    :type resource_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param quota: New network quota to create.
    :type quota: dict | bytes

    """
    quota = Quota.from_dict(quota)
    return web.Response(status=200)


async def quotas_delete(request: web.Request, subscription_id, location, resource_name, api_version) -> web.Response:
    """quotas_delete

    Delete a quota by name.

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
