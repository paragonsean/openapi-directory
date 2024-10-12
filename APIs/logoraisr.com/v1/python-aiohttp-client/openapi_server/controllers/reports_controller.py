from typing import List, Dict
from aiohttp import web

from openapi_server.models.report import Report
from openapi_server.models.report_request import ReportRequest
from openapi_server.models.report_response import ReportResponse
from openapi_server import util


async def reports_create(request: web.Request, body) -> web.Response:
    """Create a new report.

    This POST-Method creates a new report.

    :param body: 
    :type body: dict | bytes

    """
    body = ReportRequest.from_dict(body)
    return web.Response(status=200)


async def reports_list(request: web.Request, ) -> web.Response:
    """Get user report list.

    This GET method lists the user&#39;s reports.


    """
    return web.Response(status=200)


async def reports_read(request: web.Request, report_number) -> web.Response:
    """Get report details.

    This GET-Method returns the details of a specific report.

    :param report_number: 
    :type report_number: str

    """
    return web.Response(status=200)
