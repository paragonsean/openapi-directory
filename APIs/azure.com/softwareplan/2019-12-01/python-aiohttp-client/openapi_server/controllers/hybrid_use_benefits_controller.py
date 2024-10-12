from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.hybrid_use_benefit_list_result import HybridUseBenefitListResult
from openapi_server import util


async def hybrid_use_benefit_list(request: web.Request, scope, api_version, filter=None) -> web.Response:
    """hybrid_use_benefit_list

    Get all hybrid use benefits associated with an ARM resource.

    :param scope: The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    :type scope: str
    :param api_version: The api-version to be used by the service
    :type api_version: str
    :param filter: Supports applying filter on the type of SKU
    :type filter: str

    """
    return web.Response(status=200)
