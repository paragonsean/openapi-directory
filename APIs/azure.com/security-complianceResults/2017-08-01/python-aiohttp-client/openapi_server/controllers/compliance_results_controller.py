from typing import List, Dict
from aiohttp import web

from openapi_server.models.compliance_result import ComplianceResult
from openapi_server.models.compliance_result_list import ComplianceResultList
from openapi_server.models.compliance_results_get_default_response import ComplianceResultsGetDefaultResponse
from openapi_server import util


async def compliance_results_get(request: web.Request, api_version, resource_id, compliance_result_name) -> web.Response:
    """compliance_results_get

    Security Compliance Result

    :param api_version: API version for the operation
    :type api_version: str
    :param resource_id: The identifier of the resource.
    :type resource_id: str
    :param compliance_result_name: name of the desired assessment compliance result
    :type compliance_result_name: str

    """
    return web.Response(status=200)


async def compliance_results_list(request: web.Request, api_version, scope) -> web.Response:
    """compliance_results_list

    Security compliance results in the subscription

    :param api_version: API version for the operation
    :type api_version: str
    :param scope: Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
    :type scope: str

    """
    return web.Response(status=200)
