from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def sales_reports_get_collection(request: web.Request, filter_frequency, filter_report_sub_type, filter_report_type, filter_vendor_number, filter_report_date=None, filter_version=None) -> web.Response:
    """sales_reports_get_collection

    

    :param filter_frequency: filter by attribute &#39;frequency&#39;
    :type filter_frequency: List[str]
    :param filter_report_sub_type: filter by attribute &#39;reportSubType&#39;
    :type filter_report_sub_type: List[str]
    :param filter_report_type: filter by attribute &#39;reportType&#39;
    :type filter_report_type: List[str]
    :param filter_vendor_number: filter by attribute &#39;vendorNumber&#39;
    :type filter_vendor_number: List[str]
    :param filter_report_date: filter by attribute &#39;reportDate&#39;
    :type filter_report_date: List[str]
    :param filter_version: filter by attribute &#39;version&#39;
    :type filter_version: List[str]

    """
    return web.Response(status=200)
