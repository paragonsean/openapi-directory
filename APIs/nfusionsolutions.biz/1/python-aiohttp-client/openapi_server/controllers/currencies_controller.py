from typing import List, Dict
from aiohttp import web

from openapi_server.models.interval_collection_response import IntervalCollectionResponse
from openapi_server.models.rate_response import RateResponse
from openapi_server.models.summary_response import SummaryResponse
from openapi_server import util


async def currencies_history_get(request: web.Request, pairs, start, end=None, interval=None, format=None) -> web.Response:
    """Get historical prices for requested currency pairs

    Historical OHLC data for the specified period and interval size    The combination of the interval parameter and start and end dates can result in results  being truncated to conform to result size limits. See comments on interval parameter for details on valid interval values.

    :param pairs: comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD
    :type pairs: str
    :param start: start date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt;
    :type start: str
    :param end: end date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt;. Default is current date.
    :type end: str
    :param interval: aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y&#x3D;year,  m&#x3D;month,  w&#x3D;week,  d&#x3D;day,  h&#x3D;hour,  mi&#x3D;minute    For example, a yearly interval can be specified as \&quot;y\&quot; and 6 month interval as \&quot;6m\&quot;.     If not specified the interval parameter default is 1 Day.
    :type interval: str
    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def currencies_rate_get(request: web.Request, pairs, format=None) -> web.Response:
    """Get latest mid rate for requested currency pairs

    Current Mid Rate

    :param pairs: comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD
    :type pairs: str
    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    return web.Response(status=200)


async def currencies_summary_get(request: web.Request, pairs, format=None) -> web.Response:
    """Get latest Summary for requested currency pairs

    Current and daily summary information combined into a single quote

    :param pairs: comma separated list of currency pairs. For example: USD/CAD,USD/EUR,USD/AUD
    :type pairs: str
    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    return web.Response(status=200)


async def currencies_supported_currencies_history_get(request: web.Request, format=None) -> web.Response:
    """Get list of currency pairs supported by the history endpoint

    Only the currency pairs in the direction noted can be used with the history endpoint.  For example: USD/CAD is not the same as CAD/USD

    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    return web.Response(status=200)


async def currencies_supported_currencies_rate_get(request: web.Request, format=None) -> web.Response:
    """Get list of currencies supported by the rate endpoint

    Any of the currencies in this list can be paired with any other currency in this list when supplied to the Rate endpoint.  For example: USD/CAD,CAD/USD,USD/EUR,EUR/CAD

    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    return web.Response(status=200)


async def currencies_supported_currencies_summary_get(request: web.Request, format=None) -> web.Response:
    """Get list of currency pairs supported by the Summary endpoint

    Only the currency pairs in the direction noted can be used with the Summary endpoint.  For example: USD/CAD is not the same as CAD/USD

    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    return web.Response(status=200)
