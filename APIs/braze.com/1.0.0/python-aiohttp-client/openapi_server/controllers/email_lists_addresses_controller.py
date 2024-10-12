from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def query_hard_bounced_emails(request: web.Request, start_date=None, end_date=None, limit=None, offset=None, email=None) -> web.Response:
    """Query Hard Bounced Emails

    This endpoint allows you to pull a list of email addresses that have “hard bounced” your email messages within a certain time frame.  &gt; You must provide an &#x60;end_date&#x60;, as well as either an &#x60;email&#x60; or a &#x60;start_date&#x60;.&lt;br&gt;&lt;br&gt;If your date range has more than &#x60;limit&#x60; number of hard bounces, you will need to make multiple API calls, each time increasing the &#x60;offset&#x60; until a call returns either fewer than &#x60;limit&#x60; or zero results.  ## Response  Entries are listed in descending order.  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;emails\&quot;: [     {       \&quot;email\&quot;: \&quot;example1@braze.com\&quot;,       \&quot;hard_bounced_at\&quot;: \&quot;2016-08-25 15:24:32 +0000\&quot;     },     {       \&quot;email\&quot;: \&quot;example2@braze.com\&quot;,       \&quot;hard_bounced_at\&quot;: \&quot;2016-08-24 17:41:58 +0000\&quot;     },     {       \&quot;email\&quot;: \&quot;example3@braze.com\&quot;,       \&quot;hard_bounced_at\&quot;: \&quot;2016-08-24 12:01:13 +0000\&quot;     }   ],   \&quot;message\&quot;: \&quot;success\&quot; } &#x60;&#x60;&#x60;

    :param start_date: (Optional*) String in YYYY-MM-DD format   Start date of the range to retrieve hard bounces, must be earlier than &#x60;end_date&#x60;. This is treated as midnight in UTC time by the API.  *You must provide either an &#x60;email&#x60; or a &#x60;start_date&#x60;, and an &#x60;end_date&#x60;. 
    :type start_date: str
    :param end_date: (Optional*) String in YYYY-MM-DD format  String in YYYY-MM-DD format. End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API.  *You must provide either an &#x60;email&#x60; or a &#x60;start_date&#x60;, and an &#x60;end_date&#x60;.
    :type end_date: str
    :param limit: (Optional) Integer  Optional field to limit the number of results returned. Defaults to 100, maximum is 500.
    :type limit: str
    :param offset: (Optional) Integer  Optional beginning point in the list to retrieve from.
    :type offset: str
    :param email: (Optional*) String  If provided, we will return whether or not the user has hard bounced.  *You must provide either an &#x60;email&#x60; or a &#x60;start_date&#x60;, and an &#x60;end_date&#x60;.
    :type email: str

    """
    return web.Response(status=200)


async def query_list_of_unsubscribed_email_addresses(request: web.Request, start_date=None, end_date=None, limit=None, offset=None, sort_direction=None, email=None) -> web.Response:
    """Query List of Unsubscribed Email Addresses

    Use the /email/unsubscribes endpoint to return emails that have unsubscribed during the time period from &#x60;start_date&#x60; to &#x60;end_date&#x60;. You can use this endpoint to set up a bi-directional sync between Braze and other email systems or your own database.  &gt; You must provide either an email or a start_date and an end_date. &lt;br&gt;&lt;br&gt;If your date range has more than &#x60;limit&#x60; number of unsubscribes, you will need to make multiple API calls, each time increasing the &#x60;offset&#x60; until a call returns either fewer than &#x60;limit&#x60; or zero results.

    :param start_date: (Optional*) String in YYYY-MM-DD format  Start date of the range to retrieve unsubscribes, must be earlier than end_date. This is treated as midnight in UTC time by the API.
    :type start_date: str
    :param end_date: (Optional*)  String in YYYY-MM-DD format  End date of the range to retrieve unsubscribes. This is treated as midnight in UTC time by the API.
    :type end_date: str
    :param limit: (Optional) Integer  Optional field to limit the number of results returned. Limit must be greater than 1. Defaults to 100, maximum is 500.
    :type limit: str
    :param offset: (Optional) Integer   Optional beginning point in the list to retrieve from
    :type offset: str
    :param sort_direction: (Optional) String  Pass in the value &#x60;asc&#x60; to sort unsubscribes from oldest to newest. Pass in &#x60;desc&#x60; to sort from newest to oldest. If sort_direction is not included, the default order is newest to oldest.
    :type sort_direction: str
    :param email: (Optional*) String  If provided, we will return whether or not the user has unsubscribed
    :type email: str

    """
    return web.Response(status=200)
