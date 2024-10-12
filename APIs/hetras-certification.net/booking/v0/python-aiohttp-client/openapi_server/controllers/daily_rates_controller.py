from typing import List, Dict
from aiohttp import web

from openapi_server.models.daily_rates_response import DailyRatesResponse
from openapi_server import util


async def daily_rates_get_daily_rates(request: web.Request, app_id, app_key, hotel_id, _from, to, channel_code, expand=None, rate_plan_codes=None, skip=None, top=None, inlinecount=None) -> web.Response:
    """Get a list of daily rates given a hotel Id, a channel code and a date range.

    With the rates request you can get a list of different daily rates. You will have to at least               specify the hotel, the channel code, and a calendar range. The channel code will define which rates will be               returned based on the access control configuration for the rates. Additionally rate plan codes may be specified in              the request in order to limit only those rates of the given plans, if they are not specified, it will return all the public rate plans.              If requested the caller may specify whether he wants policies or not.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: Define the hotel id to request the availability for.
    :type hotel_id: int
    :param _from: Define the first business day you would like to get availability numbers for. The day should not be in the past.
    :type _from: str
    :param to: Define the last business day you would like to get rates for (inclusive). The maximum time span between &lt;i&gt;&#39;From&#39;&lt;/i&gt; and &lt;i&gt;&#39;To&#39;&lt;/i&gt;              is limited to 365 days. This can&#39;t be less than the &#39;From&#39; date.
    :type to: str
    :param channel_code: Define the channel code in order to look up the rates for.
    :type channel_code: str
    :param expand: Define the sections you want to expand and get informed about rates for.
    :type expand: List[str]
    :param rate_plan_codes: Define the codes of rate plans to show in the response. A list of comma &#39;,&#39; separated rate plan codes.
    :type rate_plan_codes: List[str]
    :param skip: Amount of items to skip.
    :type skip: int
    :param top: Amount of items to select.
    :type top: int
    :param inlinecount: Return total number of items for a given filter criteria.
    :type inlinecount: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)
