from typing import List, Dict
from aiohttp import web

from openapi_server.models.machine import Machine
from openapi_server.models.machine_collection import MachineCollection
from openapi_server import util


async def machines_enumerate_machines(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version, continuation_token=None, page_size=None) -> web.Response:
    """Gets a list of machines in the migrate project.

    

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

    """
    return web.Response(status=200)


async def machines_get_machine(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version, machine_name) -> web.Response:
    """Gets a machine in the migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param machine_name: Unique name of a machine in Azure migration hub.
    :type machine_name: str

    """
    return web.Response(status=200)
