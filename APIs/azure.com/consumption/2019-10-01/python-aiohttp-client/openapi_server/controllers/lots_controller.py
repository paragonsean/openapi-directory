from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.lots import Lots
from openapi_server import util


async def lots_list(request: web.Request, billing_account_id, billing_profile_id, api_version) -> web.Response:
    """lots_list

    Lists the lots by billingAccountId and billingProfileId.

    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param billing_profile_id: Azure Billing Profile ID.
    :type billing_profile_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01.
    :type api_version: str

    """
    return web.Response(status=200)
