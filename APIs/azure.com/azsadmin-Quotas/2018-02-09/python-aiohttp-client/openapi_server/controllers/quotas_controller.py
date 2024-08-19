from typing import List, Dict
from aiohttp import web

from openapi_server.models.quotas_get200_response import QuotasGet200Response
from openapi_server.models.quotas_list200_response import QuotasList200Response
from openapi_server import util


async def quotas_create_or_update(request: web.Request, subscription_id, location, quota_name, api_version, new_quota) -> web.Response:
    """Creates or Updates a Compute Quota.

    Creates or Updates a Compute Quota with the provided quota parameters.

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
    new_quota = QuotasGet200Response.from_dict(new_quota)
    return web.Response(status=200)


async def quotas_delete(request: web.Request, subscription_id, location, quota_name, api_version) -> web.Response:
    """Deletes specified Compute quota

    Delete an existing Compute quota.

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
    """Returns the requested Compute quota.

    Get an existing Compute Quota.

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
    """Lists all Compute quotas.

    Get a list of existing Compute quotas.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
