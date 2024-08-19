from typing import List, Dict
from aiohttp import web

from openapi_server.models.interval_collection_response import IntervalCollectionResponse
from openapi_server.models.summary_response import SummaryResponse
from openapi_server import util


async def metals_benchmark_history_get(request: web.Request, metals, start, end=None, interval=None, historicalfx=None, currency=None, unitofmeasure=None, format=None) -> web.Response:
    """Get historical benchmark prices for requested metals

    Historical OHLC data for the specified period and interval size    The combination of the interval parameter and start and end dates can result in results  being truncated to conform to result size limits. See comments on interval parameter for details on valid interval values.    The historicalfx flag is used to determine whether to apply today&#39;s fx rates to a historical period, or to apply the historical rates from that same time frame.

    :param metals: comma separated list of metals
    :type metals: str
    :param start: start date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt;
    :type start: str
    :param end: end date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt;. Default is current date.
    :type end: str
    :param interval: aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y&#x3D;year,  m&#x3D;month,  w&#x3D;week,  d&#x3D;day,  h&#x3D;hour,  mi&#x3D;minute    For example, a yearly interval can be specified as \&quot;y\&quot; and 6 month interval as \&quot;6m\&quot;.     If not specified the interval parameter default is 1 Day.
    :type interval: str
    :param historicalfx: if true use historical currency rates otherwise current currency rates. Defaults to true.
    :type historicalfx: bool
    :param currency: comma separated list of conversion currencies, defaults to USD
    :type currency: str
    :param unitofmeasure: unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight
    :type unitofmeasure: str
    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def metals_benchmark_summary_get(request: web.Request, metals, currency=None, unitofmeasure=None, format=None) -> web.Response:
    """Get latest Benchmark prices for requested metals

    Benchmark price information

    :param metals: comma separated list of metals
    :type metals: str
    :param currency: comma separated list of conversion currencies, defaults to USD
    :type currency: str
    :param unitofmeasure: unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight
    :type unitofmeasure: str
    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    return web.Response(status=200)


async def metals_benchmark_supported_metals_get(request: web.Request, format=None) -> web.Response:
    """Get list of symbols supported by the benchmark endpoints

    

    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    return web.Response(status=200)


async def metals_spot_annual_historical_performance_get(request: web.Request, metals, currency=None, unitofmeasure=None, format=None, years=None) -> web.Response:
    """Get Historical Annual Performance for requested metals

    Annual Historical Performance information

    :param metals: comma separated list of metals
    :type metals: str
    :param currency: comma separated list of conversion currencies, defaults to USD
    :type currency: str
    :param unitofmeasure: unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight
    :type unitofmeasure: str
    :param format: to override content negotiation specify a value of json or xml
    :type format: str
    :param years: Number of years of history to return. Defaults to 10.
    :type years: int

    """
    return web.Response(status=200)


async def metals_spot_historical_performance_get(request: web.Request, metals, currency=None, unitofmeasure=None, format=None) -> web.Response:
    """Get Historical Performance for requested metals

    Historical Performance information

    :param metals: comma separated list of metals
    :type metals: str
    :param currency: comma separated list of conversion currencies, defaults to USD
    :type currency: str
    :param unitofmeasure: unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight
    :type unitofmeasure: str
    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    return web.Response(status=200)


async def metals_spot_history_get(request: web.Request, metals, start, end=None, interval=None, historicalfx=None, currency=None, unitofmeasure=None, format=None) -> web.Response:
    """Get historical Spot prices for requested metals

    Historical OHLC data for the specified period and interval size    The combination of the interval parameter and start and end dates can result in results  being truncated to conform to result size limits. See comments on interval parameter for details on valid interval values.    The historicalfx flag is used to determine whether to apply today&#39;s fx rates to a historical period, or to apply the historical rates from that same time frame.

    :param metals: comma separated list of metals
    :type metals: str
    :param start: start date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt;
    :type start: str
    :param end: end date of time period. format is &lt;i&gt;yyyy-mm-dd&lt;/i&gt;. Default is current date.
    :type end: str
    :param interval: aggregation interval. Composed of an optional integer value (which defaults to 1 when not specified),   followed by a type string which must be one of the following values:  y&#x3D;year,  m&#x3D;month,  w&#x3D;week,  d&#x3D;day,  h&#x3D;hour,  mi&#x3D;minute    For example, a yearly interval can be specified as \&quot;y\&quot; and 6 month interval as \&quot;6m\&quot;.     If not specified the interval parameter default is 1 Day.
    :type interval: str
    :param historicalfx: if true use historical currency rates otherwise current currency rates. Defaults to true.
    :type historicalfx: bool
    :param currency: comma separated list of conversion currencies, defaults to USD
    :type currency: str
    :param unitofmeasure: unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight
    :type unitofmeasure: str
    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return web.Response(status=200)


async def metals_spot_ratio_history_get(request: web.Request, pairs, start, end=None, interval=None, format=None) -> web.Response:
    """Get historical Spot Ratio prices for requested metals

    Historical data for the specified period and interval size    The combination of the interval parameter and start and end dates can result in results  being truncated to conform to result size limits. See comments on interval parameter for details on valid interval values.

    :param pairs: comma separated list of metals
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


async def metals_spot_ratio_summary_get(request: web.Request, pairs, format=None) -> web.Response:
    """Get latest Spot Summary for requested metal ratios

    Ratios between prices of two metals

    :param pairs: comma separated list of metal pairs. For example: gold/silver,gold/platinum,silver/palladium
    :type pairs: str
    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    return web.Response(status=200)


async def metals_spot_summary_get(request: web.Request, metals, currency=None, unitofmeasure=None, format=None) -> web.Response:
    """Get latest Spot Summary for requested metals

    Current and daily summary information combined into a single quote

    :param metals: comma separated list of metals
    :type metals: str
    :param currency: comma separated list of conversion currencies, defaults to USD
    :type currency: str
    :param unitofmeasure: unit of meaure, defaults to troy ounces. allowed values are:  mg&#x3D;milligram  g&#x3D;gram  kg&#x3D;kilogram  gr&#x3D;grain  oz&#x3D;ounce  toz&#x3D;troy ounce  ct&#x3D;carat  dwt&#x3D;pennyweight
    :type unitofmeasure: str
    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    return web.Response(status=200)


async def metals_spot_supported_metals_get(request: web.Request, format=None) -> web.Response:
    """Get list of symbols supported by the spot endpoints

    

    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    return web.Response(status=200)


async def metals_supported_currencies_metals_get(request: web.Request, format=None) -> web.Response:
    """Get list of currencies supported by metals endpoints for currency conversion

    

    :param format: to override content negotiation specify a value of json or xml
    :type format: str

    """
    return web.Response(status=200)
