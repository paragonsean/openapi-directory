from typing import List, Dict
from aiohttp import web

from openapi_server.models.credit_summary import CreditSummary
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def credit_summary_by_billing_profile_get(request: web.Request, billing_account_id, billing_profile_id, api_version) -> web.Response:
    """credit_summary_by_billing_profile_get

    The credit summary by billingAccountId and billingProfileId for given start and end date.

    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param billing_profile_id: Billing Profile Id.
    :type billing_profile_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)
