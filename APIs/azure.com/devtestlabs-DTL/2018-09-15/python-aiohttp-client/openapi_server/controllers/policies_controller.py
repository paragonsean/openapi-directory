from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.policy import Policy
from openapi_server.models.policy_fragment import PolicyFragment
from openapi_server.models.policy_list import PolicyList
from openapi_server import util


async def policies_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, policy_set_name, name, api_version, policy) -> web.Response:
    """policies_create_or_update

    Create or replace an existing policy.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param policy_set_name: The name of the policy set.
    :type policy_set_name: str
    :param name: The name of the policy.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param policy: A Policy.
    :type policy: dict | bytes

    """
    policy = Policy.from_dict(policy)
    return web.Response(status=200)


async def policies_delete(request: web.Request, subscription_id, resource_group_name, lab_name, policy_set_name, name, api_version) -> web.Response:
    """policies_delete

    Delete policy.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param policy_set_name: The name of the policy set.
    :type policy_set_name: str
    :param name: The name of the policy.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def policies_get(request: web.Request, subscription_id, resource_group_name, lab_name, policy_set_name, name, api_version, expand=None) -> web.Response:
    """policies_get

    Get policy.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param policy_set_name: The name of the policy set.
    :type policy_set_name: str
    :param name: The name of the policy.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;description)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def policies_list(request: web.Request, subscription_id, resource_group_name, lab_name, policy_set_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """policies_list

    List policies in a given policy set.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param policy_set_name: The name of the policy set.
    :type policy_set_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;description)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;)
    :type filter: str
    :param top: The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39;
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39;
    :type orderby: str

    """
    return web.Response(status=200)


async def policies_update(request: web.Request, subscription_id, resource_group_name, lab_name, policy_set_name, name, api_version, policy) -> web.Response:
    """policies_update

    Allows modifying tags of policies. All other properties will be ignored.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param policy_set_name: The name of the policy set.
    :type policy_set_name: str
    :param name: The name of the policy.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param policy: A Policy.
    :type policy: dict | bytes

    """
    policy = PolicyFragment.from_dict(policy)
    return web.Response(status=200)
