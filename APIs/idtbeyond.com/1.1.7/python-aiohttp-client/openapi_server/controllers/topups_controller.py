from typing import List, Dict
from aiohttp import web

from openapi_server.models.topups import Topups
from openapi_server.models.topups_reports import TopupsReports
from openapi_server.models.topups_reversal import TopupsReversal
from openapi_server import util


async def iatu_topups_post(request: web.Request, x_idt_beyond_app_id, x_idt_beyond_app_key, body) -> web.Response:
    """Topup a mobile phone

    Submits an IATU transaction request.

    :param x_idt_beyond_app_id: Application ID you would like to use
    :type x_idt_beyond_app_id: str
    :param x_idt_beyond_app_key: Application KEY you would like to use
    :type x_idt_beyond_app_key: str
    :param body: Topups details
    :type body: dict | bytes

    """
    body = Topups.from_dict(body)
    return web.Response(status=200)


async def iatu_topups_reports_all_csv_get(request: web.Request, x_idt_beyond_app_id, x_idt_beyond_app_key, date_from, date_to) -> web.Response:
    """List of account topups in CSV

    Returns topups by date range in CSV.

    :param x_idt_beyond_app_id: Application ID you would like to use
    :type x_idt_beyond_app_id: str
    :param x_idt_beyond_app_key: Application KEY you would like to use
    :type x_idt_beyond_app_key: str
    :param date_from: The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39;
    :type date_from: str
    :param date_to: The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39;
    :type date_to: str

    """
    return web.Response(status=200)


async def iatu_topups_reports_all_get(request: web.Request, x_idt_beyond_app_id, x_idt_beyond_app_key, date_from, date_to) -> web.Response:
    """List of account topups in JSON

    Returns topups by date range.

    :param x_idt_beyond_app_id: Application ID you would like to use
    :type x_idt_beyond_app_id: str
    :param x_idt_beyond_app_key: Application KEY you would like to use
    :type x_idt_beyond_app_key: str
    :param date_from: The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39;
    :type date_from: str
    :param date_to: The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39;
    :type date_to: str

    """
    return web.Response(status=200)


async def iatu_topups_reports_post(request: web.Request, x_idt_beyond_app_id, x_idt_beyond_app_key, body) -> web.Response:
    """Search topups transactions

    Search topups transactions, by date, with client_transaction_id or to_service_number. Use &#39;client_transaction_id&#39; to search by transaction number, or &#39;to_service_number&#39; to get transaction status.

    :param x_idt_beyond_app_id: Application ID you would like to use
    :type x_idt_beyond_app_id: str
    :param x_idt_beyond_app_key: Application KEY you would like to use
    :type x_idt_beyond_app_key: str
    :param body: Topups reports request details
    :type body: dict | bytes

    """
    body = TopupsReports.from_dict(body)
    return web.Response(status=200)


async def iatu_topups_reports_totals_get(request: web.Request, x_idt_beyond_app_id, x_idt_beyond_app_key, date_from, date_to) -> web.Response:
    """Summary of account topups in JSON

    Returns topups totals by date range.

    :param x_idt_beyond_app_id: Application ID you would like to use
    :type x_idt_beyond_app_id: str
    :param x_idt_beyond_app_key: Application KEY you would like to use
    :type x_idt_beyond_app_key: str
    :param date_from: The beginning date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39;
    :type date_from: str
    :param date_to: The ending date of the search IN YYYY-MM-DD format (America/New_York timezone). &#39;2016-01-28&#39;
    :type date_to: str

    """
    return web.Response(status=200)


async def iatu_topups_reverse_post(request: web.Request, x_idt_beyond_app_id, x_idt_beyond_app_key, body) -> web.Response:
    """Reversal of a Topup

    Occasionally, a carrier will not be able to successfully complete a topup request. In this case, we will attempt to automatically reverse the transaction for you, and return the money into your account. In the case when this is not possible, you may need to request a reverse on the transaction that has a status of &#39;transaction_status&#39; &#39;notredeemed&#39;.

    :param x_idt_beyond_app_id: Application ID you would like to use
    :type x_idt_beyond_app_id: str
    :param x_idt_beyond_app_key: Application KEY you would like to use
    :type x_idt_beyond_app_key: str
    :param body: Topups details
    :type body: dict | bytes

    """
    body = TopupsReversal.from_dict(body)
    return web.Response(status=200)
