from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_daily_report_totals200_response_inner import GetDailyReportTotals200ResponseInner
from openapi_server.models.get_latest_totals200_response_inner import GetLatestTotals200ResponseInner
from openapi_server import util


async def get_daily_report_totals(request: web.Request, _date=None, date_format=None, format=None) -> web.Response:
    """getDailyReportTotals

    Get daily report data for whole world.

    :param _date: Date of the report. If you don&#39;t put this field all dates will be returned.
    :type _date: str
    :param date_format: Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format.
    :type date_format: str
    :param format: Format of the response. If you don&#39;t put this field JSON will be response format.
    :type format: str

    """
    return web.Response(status=200)


async def get_latest_totals(request: web.Request, format=None) -> web.Response:
    """getLatestTotals

    Get latest data for whole world.

    :param format: Format of the response
    :type format: str

    """
    return web.Response(status=200)
