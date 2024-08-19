from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_collection import EventCollection
from openapi_server.models.migrate_event import MigrateEvent
from openapi_server import util


async def events_delete_event(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version, event_name) -> web.Response:
    """Delete the migrate event

    Delete the migrate event. Deleting non-existent migrate event is a no-operation.

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param event_name: Unique name of an event within a migrate project.
    :type event_name: str

    """
    return web.Response(status=200)


async def events_enumerate_events(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version, continuation_token=None, page_size=None, accept_language=None) -> web.Response:
    """Gets a list of events in the migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param continuation_token: The continuation token.
    :type continuation_token: str
    :param page_size: The number of items to be returned in a single page. This value is honored only if it is less than the 100.
    :type page_size: int
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def events_get_event(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version, event_name) -> web.Response:
    """Gets an event in the migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param event_name: Unique name of an event within a migrate project.
    :type event_name: str

    """
    return web.Response(status=200)
