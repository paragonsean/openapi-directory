from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.spending_pulse_list_response import SpendingPulseListResponse
from openapi_server import util


async def spendingpulse_get(request: web.Request, current_row=None, offset=None, product_line=None, publication_coverage_period=None, country=None, report_type=None, period=None, sector=None, ecomm=None) -> web.Response:
    """Returns all Spending Pulse reports (with the exception of the gasoline weekly report, which has its own resource), that one is subscribed to.

    Returns all Spending Pulse reports (with the exception of the gasoline weekly report, which has its own resource), that one is subscribed to. 

    :param current_row: Starting record number to return.
    :type current_row: str
    :param offset: Used to restrict the number of records returned if needed to be less than max.
    :type offset: str
    :param product_line: Product Line.  Either ?US Executive Report? or ?Weekly Sales?
    :type product_line: str
    :param publication_coverage_period: Publication Coverage Period indicates what period is to be covered, often the current report will include the month prior.
    :type publication_coverage_period: str
    :param country: Country code.
    :type country: str
    :param report_type: Report type name, today the only report supported is \&quot;monitor\&quot;.
    :type report_type: str
    :param period: Indicates the period covered by the data with possible values of - day, week, month, quarter, annual
    :type period: str
    :param sector: Sector name.
    :type sector: str
    :param ecomm: Ecommerce indicator.
    :type ecomm: str

    """
    return web.Response(status=200)
