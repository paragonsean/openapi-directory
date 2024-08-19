from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def iatu_charges_reports_all_csv_get(request: web.Request, x_idt_beyond_app_id, x_idt_beyond_app_key, date_from, date_to) -> web.Response:
    """List of account charges in CSV

    Returns charges by date range in CSV.

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


async def iatu_charges_reports_all_get(request: web.Request, x_idt_beyond_app_id, x_idt_beyond_app_key, date_from, date_to) -> web.Response:
    """List of account charges in JSON

    Returns charges by date range.

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
