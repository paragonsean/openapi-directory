from typing import List, Dict
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server.models.event_collection import EventCollection
from openapi_server import util


async def replication_events_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, event_name) -> web.Response:
    """Get the details of an Azure Site recovery event.

    The operation to get the details of an Azure Site recovery event.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param event_name: The name of the Azure Site Recovery event.
    :type event_name: str

    """
    return web.Response(status=200)


async def replication_events_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, filter=None) -> web.Response:
    """Gets the list of Azure Site Recovery events.

    Gets the list of Azure Site Recovery events for the vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param filter: OData filter options.
    :type filter: str

    """
    return web.Response(status=200)
