from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def finance_reports_get_collection(request: web.Request, filter_region_code, filter_report_date, filter_report_type, filter_vendor_number) -> web.Response:
    """finance_reports_get_collection

    

    :param filter_region_code: filter by attribute &#39;regionCode&#39;
    :type filter_region_code: List[str]
    :param filter_report_date: filter by attribute &#39;reportDate&#39;
    :type filter_report_date: List[str]
    :param filter_report_type: filter by attribute &#39;reportType&#39;
    :type filter_report_type: List[str]
    :param filter_vendor_number: filter by attribute &#39;vendorNumber&#39;
    :type filter_vendor_number: List[str]

    """
    return web.Response(status=200)
