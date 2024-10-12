from typing import List, Dict
from aiohttp import web

from openapi_server.models.workload_item_resource_list import WorkloadItemResourceList
from openapi_server import util


async def backup_workload_items_list(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, filter=None, skip_token=None) -> web.Response:
    """backup_workload_items_list

    Provides a pageable list of workload item of a specific container according to the query filter and the pagination  parameters.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the container.
    :type fabric_name: str
    :param container_name: Name of the container.
    :type container_name: str
    :param filter: OData filter options.
    :type filter: str
    :param skip_token: skipToken Filter.
    :type skip_token: str

    """
    return web.Response(status=200)
