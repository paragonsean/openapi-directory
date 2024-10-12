from typing import List, Dict
from aiohttp import web

from openapi_server.models.health_monitor_policy import HealthMonitorPolicy
from openapi_server.models.node_policy_check_result import NodePolicyCheckResult
from openapi_server.models.run_policy_arg import RunPolicyArg
from openapi_server import util


async def get_policies(request: web.Request, policy_ids=None) -> web.Response:
    """Get details of health monitor policies

    Retrieves the details of all the health monitor policies when policy IDs are not specified in the query parameter. If the request includes a list of policy IDs in the query parameter, the response will include the details of the specified policies.

    :param policy_ids: Optional list of policy IDs.
    :type policy_ids: List[str]

    """
    return web.Response(status=200)


async def get_policy_status(request: web.Request, policy_ids=None, node_ids=None, has_detailed_status=None) -> web.Response:
    """Get the status of health monitor policy enforcement

    Retrieves the status of the policy enforcement for a list of nodes if specified. If nodes are not specified, the response includes the policy enforcement status for all the nodes on the Rubrik cluster.

    :param policy_ids: Optional list of policy IDs. If not provided, the response includes the status of all the policies.
    :type policy_ids: List[str]
    :param node_ids: Optional list of Node IDs. If not provided, the response includes the status of all the nodes.
    :type node_ids: List[str]
    :param has_detailed_status: Indicates if the policy enforcement status should include expanded result for each policy.
    :type has_detailed_status: bool

    """
    return web.Response(status=200)


async def run_policies(request: web.Request, body) -> web.Response:
    """Enforce health monitor policies

    Triggers on-demand enforcement of the set of policies specified in the request body. If a list of nodes is provided, policies are run against these nodes, otherwise the policies are run on all active nodes of the Rubrik cluster.

    :param body: The request object.
    :type body: dict | bytes

    """
    body = RunPolicyArg.from_dict(body)
    return web.Response(status=200)
