from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse
from openapi_server.models.report_notification_request import ReportNotificationRequest
from openapi_server import util


async def post_balance_platform_report_created(request: web.Request, report_notification_request=None) -> web.Response:
    """Report generated

    Adyen sends this webhook after a report is generated and ready to be downloaded. The webhook contains the URL at which the report can be downloaded.  Before you download reports, ask your Adyen contact for your report credentials. You must use your the credentials to authenticate your GET request.

    :param report_notification_request: 
    :type report_notification_request: dict | bytes

    """
    report_notification_request = ReportNotificationRequest.from_dict(report_notification_request)
    return web.Response(status=200)
