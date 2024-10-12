from typing import List, Dict
from aiohttp import web

from openapi_server.models.bounce_activation_response import BounceActivationResponse
from openapi_server.models.bounce_dump_response import BounceDumpResponse
from openapi_server.models.bounce_info_response import BounceInfoResponse
from openapi_server.models.bounce_search_response import BounceSearchResponse
from openapi_server.models.delivery_stats_response import DeliveryStatsResponse
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server import util


async def activate_bounce(request: web.Request, x_postmark_server_token, bounceid) -> web.Response:
    """Activate a bounce

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param bounceid: The ID of the Bounce to activate.
    :type bounceid: int

    """
    return web.Response(status=200)


async def bounces_bounceid_dump_get(request: web.Request, x_postmark_server_token, bounceid) -> web.Response:
    """Get bounce dump

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param bounceid: The ID for the bounce dump to retrieve.
    :type bounceid: int

    """
    return web.Response(status=200)


async def get_bounces(request: web.Request, x_postmark_server_token, count, offset, type=None, inactive=None, email_filter=None, message_id=None, tag=None, todate=None, fromdate=None) -> web.Response:
    """Get bounces

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param count: Number of bounces to return per request. Max 500.
    :type count: int
    :param offset: Number of bounces to skip.
    :type offset: int
    :param type: Filter by type of bounce
    :type type: str
    :param inactive: Filter by emails that were deactivated by Postmark due to the bounce. Set to true or false. If this isn&#39;t specified it will return both active and inactive.
    :type inactive: bool
    :param email_filter: Filter by email address
    :type email_filter: str
    :param message_id: Filter by messageID
    :type message_id: str
    :param tag: Filter by tag
    :type tag: str
    :param todate: Filter messages up to the date specified. e.g. &#x60;2014-02-01&#x60;
    :type todate: str
    :param fromdate: Filter messages starting from the date specified. e.g. &#x60;2014-02-01&#x60;
    :type fromdate: str

    """
    todate = util.deserialize_date(todate)
    fromdate = util.deserialize_date(fromdate)
    return web.Response(status=200)


async def get_delivery_stats(request: web.Request, x_postmark_server_token) -> web.Response:
    """Get delivery stats

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str

    """
    return web.Response(status=200)


async def get_single_bounce(request: web.Request, x_postmark_server_token, bounceid) -> web.Response:
    """Get a single bounce

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param bounceid: The ID of the bounce to retrieve.
    :type bounceid: int

    """
    return web.Response(status=200)
