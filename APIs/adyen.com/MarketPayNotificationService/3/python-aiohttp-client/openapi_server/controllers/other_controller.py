from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification_response import NotificationResponse
from openapi_server.models.payment_failure_notification import PaymentFailureNotification
from openapi_server.models.report_available_notification import ReportAvailableNotification
from openapi_server import util


async def post_paymentfailure(request: web.Request, payment_failure_notification=None) -> web.Response:
    """Booking for a capture or refund failed

    Adyen sends this notification when a [split payment](https://docs.adyen.com/marketplaces-and-platforms/classic/processing-payments#providing-split-information) booking for a capture or refund fails. When a booking fails due to an invalid account status or an unknown &#x60;accountCode&#x60;, the funds are credited or debited to or fromyour platform&#39;s liable account instead of the account specified in the split data.

    :param payment_failure_notification: 
    :type payment_failure_notification: dict | bytes

    """
    payment_failure_notification = PaymentFailureNotification.from_dict(payment_failure_notification)
    return web.Response(status=200)


async def post_reportavailable(request: web.Request, report_available_notification=None) -> web.Response:
    """Report available

    Adyen sends this notification when a report has been generated and it is available for download.

    :param report_available_notification: 
    :type report_available_notification: dict | bytes

    """
    report_available_notification = ReportAvailableNotification.from_dict(report_available_notification)
    return web.Response(status=200)
