from typing import List, Dict
from aiohttp import web

from openapi_server.models.quota import Quota
from openapi_server.models.quota_list import QuotaList
from openapi_server import util


async def quotas_create_or_update(request: web.Request, subscription_id, location, quota_name, api_version, new_quota) -> web.Response:
    """Creates or Updates a Quota.

    Creates or Updates a Quota.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param quota_name: Name of the quota.
    :type quota_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param new_quota: New quota to create.
    :type new_quota: dict | bytes

    """
    new_quota = Quota.from_dict(new_quota)
    return web.Response(status=200)


async def quotas_delete(request: web.Request, subscription_id, location, quota_name, api_version) -> web.Response:
    """Deletes specified quota

    Delete an existing quota.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param quota_name: Name of the quota.
    :type quota_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def quotas_get(request: web.Request, subscription_id, location, quota_name, api_version) -> web.Response:
    """Returns the requested quota.

    Get an existing Quota.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param quota_name: Name of the quota.
    :type quota_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def quotas_list(request: web.Request, subscription_id, location, api_version) -> web.Response:
    """Lists all quotas.

    Get a list of existing quotas.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
