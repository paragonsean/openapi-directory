from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tags_result import TagsResult
from openapi_server import util


async def tags_get(request: web.Request, scope, api_version) -> web.Response:
    """tags_get

    Get all available tag keys for the defined scope

    :param scope: The scope associated with tags operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for resourceGroup scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for Billing Account scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}&#39; for Department scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}&#39; for EnrollmentAccount scope and &#39;/providers/Microsoft.Management/managementGroups/{managementGroupId}&#39; for Management Group scope..
    :type scope: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-05-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)
