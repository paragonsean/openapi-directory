from typing import List, Dict
from aiohttp import web

from openapi_server.models.ob_error_response1 import OBErrorResponse1
from openapi_server.models.ob_read_scheduled_payment3 import OBReadScheduledPayment3
from openapi_server import util


async def accounts_account_id_scheduled_payments_get(request: web.Request, account_id, sandbox_id, x_fapi_auth_date=None, x_fapi_customer_ip_address=None, x_fapi_interaction_id=None, x_customer_user_agent=None) -> web.Response:
    """Get Scheduled Payments

    Get Scheduled Payments by Account ID

    :param account_id: AccountId
    :type account_id: str
    :param sandbox_id: The unique id of the sandbox to be used
    :type sandbox_id: str
    :param x_fapi_auth_date: The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
    :type x_fapi_auth_date: str
    :param x_fapi_customer_ip_address: The PSU&#39;s IP address if the PSU is currently logged in with the TPP.
    :type x_fapi_customer_ip_address: str
    :param x_fapi_interaction_id: An RFC4122 UID used as a correlation id.
    :type x_fapi_interaction_id: str
    :param x_customer_user_agent: Indicates the user-agent that the PSU is using.
    :type x_customer_user_agent: str

    """
    return web.Response(status=200)
