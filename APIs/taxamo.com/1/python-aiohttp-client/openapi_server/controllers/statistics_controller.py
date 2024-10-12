from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_daily_settlement_stats_out import GetDailySettlementStatsOut
from openapi_server.models.get_settlement_stats_by_country_out import GetSettlementStatsByCountryOut
from openapi_server.models.get_settlement_stats_by_taxation_type_out import GetSettlementStatsByTaxationTypeOut
from openapi_server.models.get_transactions_stats_by_country_out import GetTransactionsStatsByCountryOut
from openapi_server.models.get_transactions_stats_out import GetTransactionsStatsOut
from openapi_server import util


async def get_daily_settlement_stats(request: web.Request, interval, date_from, date_to) -> web.Response:
    """Settlement stats over time

    

    :param interval: Interval type - day, week, month.
    :type interval: str
    :param date_from: Date from in yyyy-MM format.
    :type date_from: str
    :param date_to: Date to in yyyy-MM format.
    :type date_to: str

    """
    return web.Response(status=200)


async def get_settlement_stats_by_country(request: web.Request, date_from, date_to) -> web.Response:
    """Settlement by country

    

    :param date_from: Date from in yyyy-MM format.
    :type date_from: str
    :param date_to: Date to in yyyy-MM format.
    :type date_to: str

    """
    return web.Response(status=200)


async def get_settlement_stats_by_taxation_type(request: web.Request, date_from, date_to) -> web.Response:
    """Settlement by tax type

    

    :param date_from: Date from in yyyy-MM format.
    :type date_from: str
    :param date_to: Date to in yyyy-MM format.
    :type date_to: str

    """
    return web.Response(status=200)


async def get_transactions_stats(request: web.Request, date_from, date_to, interval=None) -> web.Response:
    """Transaction stats

    

    :param date_from: Date from in yyyy-MM format.
    :type date_from: str
    :param date_to: Date to in yyyy-MM format.
    :type date_to: str
    :param interval: Interval. Accepted values are &#39;day&#39;, &#39;week&#39; and &#39;month&#39;.
    :type interval: str

    """
    return web.Response(status=200)


async def get_transactions_stats_by_country(request: web.Request, date_from, date_to, global_currency_code=None) -> web.Response:
    """Settlement by country

    

    :param date_from: Date from in yyyy-MM format.
    :type date_from: str
    :param date_to: Date to in yyyy-MM format.
    :type date_to: str
    :param global_currency_code: Global currency code to use for conversion - in addition to country&#39;s currency if rate is available. Conversion is indicative and based on most-recent rate from ECB.
    :type global_currency_code: str

    """
    return web.Response(status=200)
