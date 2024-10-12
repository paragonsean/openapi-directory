from typing import List, Dict
from aiohttp import web

from openapi_server.models.report_response import ReportResponse
from openapi_server.models.subscription_report import SubscriptionReport
from openapi_server import util


async def api_rns_pvt_reports_get(request: web.Request, content_type, accept) -> web.Response:
    """List report templates

    List all report templates available.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def api_rns_pvt_reports_report_name_documents_document_id_get(request: web.Request, report_name, document_id, content_type, accept) -> web.Response:
    """Get report document details

    Retrieve a specific report document by its Id.

    :param report_name: Name of the report
    :type report_name: str
    :param document_id: Id from the desired report document
    :type document_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def api_rns_pvt_reports_report_name_documents_post(request: web.Request, report_name, content_type, accept, email=None, begin_date=None, end_date=None) -> web.Response:
    """Generate report

    This endpoint creates a new report in the format of a CSV file and sends it via email. You can generate one of the following reports:    - subscriptionsWithStatus    - subscriptionsScheduledBetweenDate    - subscriptionsUpdatedBetweenDate    - subscriptionsCreatedBetweenDate    - executionsBetweenDate

    :param report_name: Name of the type of report in wish to generate. The following values are accepted:    - &#x60;subscriptionsWithStatus&#x60;    - &#x60;subscriptionsScheduledBetweenDate&#x60;    - &#x60;subscriptionsUpdatedBetweenDate&#x60;    - &#x60;subscriptionsCreatedBetweenDate&#x60;    - &#x60;executionsBetweenDate&#x60;
    :type report_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param email: The report is sent to the email in this field.
    :type email: str
    :param begin_date: Start date of the report with the format &#x60;yyyy-mm-dd&#x60;. This field is required for any type of report.
    :type begin_date: str
    :param end_date: End date of the report with the format &#x60;yyyy-mm-dd&#x60;. This field is required for any type of report.
    :type end_date: str

    """
    return web.Response(status=200)
