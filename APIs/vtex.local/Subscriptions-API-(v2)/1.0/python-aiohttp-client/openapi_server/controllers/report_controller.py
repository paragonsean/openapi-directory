from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def getreportstatusby_id(request: web.Request, content_type, accept, report_id) -> web.Response:
    """Get report status by ID

    Retrieves the Subscription&#39;s report status, filtering by its reportId.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param report_id: Report ID.
    :type report_id: str

    """
    return web.Response(status=200)


async def requestreportby_status(request: web.Request, requester_email, status, content_type, accept) -> web.Response:
    """Retrieve Subscription report by Status

    Retrieves Subscriptions&#39; reports, filtering by status. The report will be sent by email, to the address inserted in the API&#39;s path.

    :param requester_email: Email that the report will be sent to
    :type requester_email: str
    :param status: Binary OR of the following status: 1 - ACTIVE; 2 - PAUSED; 4 - CANCELED; 8 - EXPIRED
    :type status: int
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def requestreportbydate(request: web.Request, requester_email, begin_date, end_date, content_type, accept) -> web.Response:
    """Retrieve Subscription report by date

    Retrieves a report with the subscriptions created at the date interval requested

    :param requester_email: Email that the report will be sent to
    :type requester_email: str
    :param begin_date: begin date of report interval, use format yyyyMMdd
    :type begin_date: int
    :param end_date: end date of report interval, use format yyyyMMdd
    :type end_date: int
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def requestreportbyorderdate(request: web.Request, requester_email, begin_date, end_date, content_type, accept) -> web.Response:
    """Retrieve Subscription report by order date

    Retrieves a report regarding the Subscriptions created during the date interval of orders.

    :param requester_email: Email that the report will be sent to
    :type requester_email: str
    :param begin_date: begin date of report interval, use format yyyyMMdd
    :type begin_date: int
    :param end_date: end date of report interval, use format yyyyMMdd
    :type end_date: int
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def requestreportbyschedule(request: web.Request, requester_email, begin_date, end_date, content_type, accept) -> web.Response:
    """Retrieve Subscription report by schedule

    Retrieves a report regarding the Subscriptions scheduled to execute at the date interval requested

    :param requester_email: Email that the report will be sent to
    :type requester_email: str
    :param begin_date: begin date of report interval, use format yyyyMMdd
    :type begin_date: int
    :param end_date: end date of report interval, use format yyyyMMdd
    :type end_date: int
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def requestreportbyupdate(request: web.Request, requester_email, begin_date, end_date, content_type, accept) -> web.Response:
    """Request report by update

    Retrieves a report regarding Subscriptions updated in the date interval chosen. The report will be sent by email, to the address inserted in the API&#39;s path.

    :param requester_email: Email that the report will be sent to
    :type requester_email: str
    :param begin_date: begin date of report interval, use format yyyyMMdd
    :type begin_date: int
    :param end_date: end date of report interval, use format yyyyMMdd
    :type end_date: int
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)
