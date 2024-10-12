from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_bounce_counts200_response import GetBounceCounts200Response
from openapi_server.models.get_outbound_open_counts200_response import GetOutboundOpenCounts200Response
from openapi_server.models.get_outbound_open_counts_by_email_client200_response import GetOutboundOpenCountsByEmailClient200Response
from openapi_server.models.get_outbound_open_counts_by_platform200_response import GetOutboundOpenCountsByPlatform200Response
from openapi_server.models.get_spam_complaints200_response import GetSpamComplaints200Response
from openapi_server.models.get_tracked_email_counts200_response import GetTrackedEmailCounts200Response
from openapi_server.models.outbound_overview_stats_response import OutboundOverviewStatsResponse
from openapi_server.models.sent_counts_response import SentCountsResponse
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server import util


async def get_bounce_counts(request: web.Request, x_postmark_server_token, tag=None, fromdate=None, todate=None) -> web.Response:
    """Get bounce counts

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param tag: Filter by tag
    :type tag: str
    :param fromdate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type fromdate: str
    :param todate: Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str

    """
    fromdate = util.deserialize_date(fromdate)
    todate = util.deserialize_date(todate)
    return web.Response(status=200)


async def get_outbound_click_counts(request: web.Request, x_postmark_server_token, tag=None, fromdate=None, todate=None) -> web.Response:
    """Get click counts

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param tag: Filter by tag
    :type tag: str
    :param fromdate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type fromdate: str
    :param todate: Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str

    """
    fromdate = util.deserialize_date(fromdate)
    todate = util.deserialize_date(todate)
    return web.Response(status=200)


async def get_outbound_click_counts_by_browser_family(request: web.Request, x_postmark_server_token, tag=None, fromdate=None, todate=None) -> web.Response:
    """Get browser usage by family

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param tag: Filter by tag
    :type tag: str
    :param fromdate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type fromdate: str
    :param todate: Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str

    """
    fromdate = util.deserialize_date(fromdate)
    todate = util.deserialize_date(todate)
    return web.Response(status=200)


async def get_outbound_click_counts_by_location(request: web.Request, x_postmark_server_token, tag=None, fromdate=None, todate=None) -> web.Response:
    """Get clicks by body location

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param tag: Filter by tag
    :type tag: str
    :param fromdate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type fromdate: str
    :param todate: Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str

    """
    fromdate = util.deserialize_date(fromdate)
    todate = util.deserialize_date(todate)
    return web.Response(status=200)


async def get_outbound_click_counts_by_platform(request: web.Request, x_postmark_server_token, tag=None, fromdate=None, todate=None) -> web.Response:
    """Get browser plaform usage

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param tag: Filter by tag
    :type tag: str
    :param fromdate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type fromdate: str
    :param todate: Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str

    """
    fromdate = util.deserialize_date(fromdate)
    todate = util.deserialize_date(todate)
    return web.Response(status=200)


async def get_outbound_open_counts(request: web.Request, x_postmark_server_token, tag=None, fromdate=None, todate=None) -> web.Response:
    """Get email open counts

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param tag: Filter by tag
    :type tag: str
    :param fromdate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type fromdate: str
    :param todate: Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str

    """
    fromdate = util.deserialize_date(fromdate)
    todate = util.deserialize_date(todate)
    return web.Response(status=200)


async def get_outbound_open_counts_by_email_client(request: web.Request, x_postmark_server_token, tag=None, fromdate=None, todate=None) -> web.Response:
    """Get email client usage

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param tag: Filter by tag
    :type tag: str
    :param fromdate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type fromdate: str
    :param todate: Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str

    """
    fromdate = util.deserialize_date(fromdate)
    todate = util.deserialize_date(todate)
    return web.Response(status=200)


async def get_outbound_open_counts_by_platform(request: web.Request, x_postmark_server_token, tag=None, fromdate=None, todate=None) -> web.Response:
    """Get email platform usage

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param tag: Filter by tag
    :type tag: str
    :param fromdate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type fromdate: str
    :param todate: Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str

    """
    fromdate = util.deserialize_date(fromdate)
    todate = util.deserialize_date(todate)
    return web.Response(status=200)


async def get_outbound_overview_statistics(request: web.Request, x_postmark_server_token, tag=None, fromdate=None, todate=None) -> web.Response:
    """Get outbound overview

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param tag: Filter by tag
    :type tag: str
    :param fromdate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type fromdate: str
    :param todate: Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str

    """
    fromdate = util.deserialize_date(fromdate)
    todate = util.deserialize_date(todate)
    return web.Response(status=200)


async def get_sent_counts(request: web.Request, x_postmark_server_token, tag=None, fromdate=None, todate=None) -> web.Response:
    """Get sent counts

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param tag: Filter by tag
    :type tag: str
    :param fromdate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type fromdate: str
    :param todate: Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str

    """
    fromdate = util.deserialize_date(fromdate)
    todate = util.deserialize_date(todate)
    return web.Response(status=200)


async def get_spam_complaints(request: web.Request, x_postmark_server_token, tag=None, fromdate=None, todate=None) -> web.Response:
    """Get spam complaints

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param tag: Filter by tag
    :type tag: str
    :param fromdate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type fromdate: str
    :param todate: Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str

    """
    fromdate = util.deserialize_date(fromdate)
    todate = util.deserialize_date(todate)
    return web.Response(status=200)


async def get_tracked_email_counts(request: web.Request, x_postmark_server_token, tag=None, fromdate=None, todate=None) -> web.Response:
    """Get tracked email counts

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param tag: Filter by tag
    :type tag: str
    :param fromdate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type fromdate: str
    :param todate: Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60;
    :type todate: str

    """
    fromdate = util.deserialize_date(fromdate)
    todate = util.deserialize_date(todate)
    return web.Response(status=200)
