from typing import List, Dict
from aiohttp import web

from openapi_server.models.protection_policy_resource import ProtectionPolicyResource
from openapi_server import util


async def protection_policy_operation_results_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, policy_name, operation_id) -> web.Response:
    """protection_policy_operation_results_get

    Provides the result of an operation.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param policy_name: Backup policy name whose operation&#39;s result needs to be fetched.
    :type policy_name: str
    :param operation_id: Operation ID which represents the operation whose result needs to be fetched.
    :type operation_id: str

    """
    return web.Response(status=200)
