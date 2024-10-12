from typing import List, Dict
from aiohttp import web

from openapi_server.models.protection_policy_resource import ProtectionPolicyResource
from openapi_server import util


async def protection_policy_operation_results_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, policy_name, operation_id) -> web.Response:
    """protection_policy_operation_results_get

    Provides the result of an operation.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param policy_name: The backup policy name used in this GET operation.
    :type policy_name: str
    :param operation_id: The ID associated with this GET operation.
    :type operation_id: str

    """
    return web.Response(status=200)
