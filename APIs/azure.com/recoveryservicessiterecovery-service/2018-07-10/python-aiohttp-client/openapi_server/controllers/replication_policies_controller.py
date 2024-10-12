from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_policy_input import CreatePolicyInput
from openapi_server.models.policy import Policy
from openapi_server.models.policy_collection import PolicyCollection
from openapi_server.models.update_policy_input import UpdatePolicyInput
from openapi_server import util


async def replication_policies_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, policy_name, input) -> web.Response:
    """Creates the policy.

    The operation to create a replication policy

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param policy_name: Replication policy name
    :type policy_name: str
    :param input: Create policy input
    :type input: dict | bytes

    """
    input = CreatePolicyInput.from_dict(input)
    return web.Response(status=200)


async def replication_policies_delete(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, policy_name) -> web.Response:
    """Delete the policy.

    The operation to delete a replication policy.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param policy_name: Replication policy name.
    :type policy_name: str

    """
    return web.Response(status=200)


async def replication_policies_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, policy_name) -> web.Response:
    """Gets the requested policy.

    Gets the details of a replication policy.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param policy_name: Replication policy name.
    :type policy_name: str

    """
    return web.Response(status=200)


async def replication_policies_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the list of replication policies

    Lists the replication policies for a vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def replication_policies_update(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, policy_name, input) -> web.Response:
    """Updates the policy.

    The operation to update a replication policy.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param policy_name: Policy Id.
    :type policy_name: str
    :param input: Update Policy Input
    :type input: dict | bytes

    """
    input = UpdatePolicyInput.from_dict(input)
    return web.Response(status=200)
