from typing import List, Dict
from aiohttp import web

from openapi_server.models.ob_error_response1 import OBErrorResponse1
from openapi_server.models.ob_read_transaction6 import OBReadTransaction6
from openapi_server import util


async def accounts_account_id_statements_statement_id_transactions_get(request: web.Request, account_id, statement_id, sandbox_id, x_fapi_auth_date=None, x_fapi_customer_ip_address=None, x_fapi_interaction_id=None, x_customer_user_agent=None) -> web.Response:
    """Get Transactions

    Get Transactions by Account ID and Statement ID

    :param account_id: AccountId
    :type account_id: str
    :param statement_id: StatementId
    :type statement_id: str
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


async def accounts_account_id_transactions_get(request: web.Request, account_id, sandbox_id, from_booking_date_time=None, to_booking_date_time=None, x_fapi_auth_date=None, x_fapi_customer_ip_address=None, x_fapi_interaction_id=None, x_customer_user_agent=None) -> web.Response:
    """Get Transactions

    Get Transactions by Account ID

    :param account_id: AccountId
    :type account_id: str
    :param sandbox_id: The unique id of the sandbox to be used
    :type sandbox_id: str
    :param from_booking_date_time: The UTC ISO 8601 Date Time to filter transactions FROM NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
    :type from_booking_date_time: str
    :param to_booking_date_time: The UTC ISO 8601 Date Time to filter transactions TO NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.
    :type to_booking_date_time: str
    :param x_fapi_auth_date: The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC
    :type x_fapi_auth_date: str
    :param x_fapi_customer_ip_address: The PSU&#39;s IP address if the PSU is currently logged in with the TPP.
    :type x_fapi_customer_ip_address: str
    :param x_fapi_interaction_id: An RFC4122 UID used as a correlation id.
    :type x_fapi_interaction_id: str
    :param x_customer_user_agent: Indicates the user-agent that the PSU is using.
    :type x_customer_user_agent: str

    """
    from_booking_date_time = util.deserialize_datetime(from_booking_date_time)
    to_booking_date_time = util.deserialize_datetime(to_booking_date_time)
    return web.Response(status=200)
