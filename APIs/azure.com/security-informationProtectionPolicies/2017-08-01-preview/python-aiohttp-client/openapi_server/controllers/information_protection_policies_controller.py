from typing import List, Dict
from aiohttp import web

from openapi_server.models.information_protection_policies_list_default_response import InformationProtectionPoliciesListDefaultResponse
from openapi_server.models.information_protection_policy import InformationProtectionPolicy
from openapi_server.models.information_protection_policy_list import InformationProtectionPolicyList
from openapi_server import util


async def information_protection_policies_create_or_update(request: web.Request, api_version, scope, information_protection_policy_name) -> web.Response:
    """information_protection_policies_create_or_update

    Details of the information protection policy.

    :param api_version: API version for the operation
    :type api_version: str
    :param scope: Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
    :type scope: str
    :param information_protection_policy_name: Name of the information protection policy.
    :type information_protection_policy_name: str

    """
    return web.Response(status=200)


async def information_protection_policies_get(request: web.Request, api_version, scope, information_protection_policy_name) -> web.Response:
    """information_protection_policies_get

    Details of the information protection policy.

    :param api_version: API version for the operation
    :type api_version: str
    :param scope: Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
    :type scope: str
    :param information_protection_policy_name: Name of the information protection policy.
    :type information_protection_policy_name: str

    """
    return web.Response(status=200)


async def information_protection_policies_list(request: web.Request, api_version, scope) -> web.Response:
    """information_protection_policies_list

    Information protection policies of a specific management group.

    :param api_version: API version for the operation
    :type api_version: str
    :param scope: Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
    :type scope: str

    """
    return web.Response(status=200)
