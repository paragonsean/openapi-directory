from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def reports_index(request: web.Request, report_type, sites, start_date, end_date, page, page_size, version, report_sub_type_id=None) -> web.Response:
    """Gets the daily report.

    Get&#39;s the report.

    :param report_type: Report Type Id (i.e Daily, Monthly, Annual)
    :type report_type: str
    :param sites: Comma separated list of site Ids.
    :type sites: str
    :param start_date: The start date of the report in the format ddmmyyyy (i.e 31012016)
    :type start_date: str
    :param end_date: The end date of the report in the format ddmmyyyy (i.e 31012016)
    :type end_date: str
    :param page: The page offset to return.
    :type page: int
    :param page_size: The number of rows to return.
    :type page_size: int
    :param version: 
    :type version: str
    :param report_sub_type_id: 
    :type report_sub_type_id: int

    """
    return web.Response(status=200)


async def vversion_reports_start_date_to_end_date_report_type_get(request: web.Request, report_type, sites, start_date, end_date, page, page_size, version, report_sub_type_id=None) -> web.Response:
    """Gets the daily report.

    Get&#39;s the report.

    :param report_type: Report Type Id (i.e Daily, Monthly, Annual)
    :type report_type: str
    :param sites: Comma separated list of site Ids.
    :type sites: str
    :param start_date: The start date of the report in the format ddmmyyyy (i.e 31012016)
    :type start_date: str
    :param end_date: The end date of the report in the format ddmmyyyy (i.e 31012016)
    :type end_date: str
    :param page: The page offset to return.
    :type page: int
    :param page_size: The number of rows to return.
    :type page_size: int
    :param version: 
    :type version: str
    :param report_sub_type_id: 
    :type report_sub_type_id: int

    """
    return web.Response(status=200)
