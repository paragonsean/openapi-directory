from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.events import Events
from openapi_server import util


async def events_list(request: web.Request, billing_account_id, billing_profile_id, api_version, start_date, end_date) -> web.Response:
    """events_list

    Lists the events by billingAccountId and billingProfileId for given start and end date.

    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param billing_profile_id: Azure Billing Profile ID.
    :type billing_profile_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01.
    :type api_version: str
    :param start_date: Start date
    :type start_date: str
    :param end_date: End date
    :type end_date: str

    """
    return web.Response(status=200)
