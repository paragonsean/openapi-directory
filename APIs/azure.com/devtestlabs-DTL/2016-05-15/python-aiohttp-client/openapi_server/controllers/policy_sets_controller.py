from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.evaluate_policies_request import EvaluatePoliciesRequest
from openapi_server.models.evaluate_policies_response import EvaluatePoliciesResponse
from openapi_server import util


async def policy_sets_evaluate_policies(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, evaluate_policies_request) -> web.Response:
    """policy_sets_evaluate_policies

    Evaluates lab policy.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the policy set.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param evaluate_policies_request: Request body for evaluating a policy set.
    :type evaluate_policies_request: dict | bytes

    """
    evaluate_policies_request = EvaluatePoliciesRequest.from_dict(evaluate_policies_request)
    return web.Response(status=200)
