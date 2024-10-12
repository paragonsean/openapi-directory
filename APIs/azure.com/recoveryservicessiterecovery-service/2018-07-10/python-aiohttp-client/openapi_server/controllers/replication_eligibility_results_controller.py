from typing import List, Dict
from aiohttp import web

from openapi_server.models.replication_eligibility_results import ReplicationEligibilityResults
from openapi_server.models.replication_eligibility_results_collection import ReplicationEligibilityResultsCollection
from openapi_server import util


async def replication_eligibility_results_get(request: web.Request, api_version, resource_group_name, subscription_id, virtual_machine_name) -> web.Response:
    """Gets the validation errors in case the VM is unsuitable for protection.

    Validates whether a given VM can be protected or not in which case returns list of errors.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param virtual_machine_name: Virtual Machine name.
    :type virtual_machine_name: str

    """
    return web.Response(status=200)


async def replication_eligibility_results_list(request: web.Request, api_version, resource_group_name, subscription_id, virtual_machine_name) -> web.Response:
    """Gets the validation errors in case the VM is unsuitable for protection.

    Validates whether a given VM can be protected or not in which case returns list of errors.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param virtual_machine_name: Virtual Machine name.
    :type virtual_machine_name: str

    """
    return web.Response(status=200)
