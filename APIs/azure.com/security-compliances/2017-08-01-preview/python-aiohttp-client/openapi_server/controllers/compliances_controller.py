from typing import List, Dict
from aiohttp import web

from openapi_server.models.compliance import Compliance
from openapi_server.models.compliance_list import ComplianceList
from openapi_server.models.compliances_list_default_response import CompliancesListDefaultResponse
from openapi_server import util


async def compliances_get(request: web.Request, api_version, scope, compliance_name) -> web.Response:
    """compliances_get

    Details of a specific Compliance.

    :param api_version: API version for the operation
    :type api_version: str
    :param scope: Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
    :type scope: str
    :param compliance_name: name of the Compliance
    :type compliance_name: str

    """
    return web.Response(status=200)


async def compliances_list(request: web.Request, api_version, scope) -> web.Response:
    """compliances_list

    The Compliance scores of the specific management group.

    :param api_version: API version for the operation
    :type api_version: str
    :param scope: Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
    :type scope: str

    """
    return web.Response(status=200)
