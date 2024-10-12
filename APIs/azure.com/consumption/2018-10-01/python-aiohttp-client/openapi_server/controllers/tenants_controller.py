from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tenant_list_result import TenantListResult
from openapi_server import util


async def tenants_get(request: web.Request, billing_account_id, billing_profile_id, api_version) -> web.Response:
    """tenants_get

    Gets a Tenant Properties.

    :param billing_account_id: Billing Account Id.
    :type billing_account_id: str
    :param billing_profile_id: Billing Profile Id.
    :type billing_profile_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-10-01.
    :type api_version: str

    """
    return web.Response(status=200)
