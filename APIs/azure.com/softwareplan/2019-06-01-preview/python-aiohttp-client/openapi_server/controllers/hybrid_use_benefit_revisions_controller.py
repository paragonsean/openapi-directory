from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.hybrid_use_benefit_list_result import HybridUseBenefitListResult
from openapi_server import util


async def hybrid_use_benefit_revision_list(request: web.Request, scope, plan_id, api_version) -> web.Response:
    """hybrid_use_benefit_revision_list

    Gets the version history of a hybrid use benefit

    :param scope: The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    :type scope: str
    :param plan_id: This is a unique identifier for a plan. Should be a guid.
    :type plan_id: str
    :param api_version: The api-version to be used by the service
    :type api_version: str

    """
    return web.Response(status=200)
