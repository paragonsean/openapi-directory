from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_statistice_daily_value_v1_statistics_individual_daily200_response import UserStatisticeDailyValueV1StatisticsIndividualDaily200Response
from openapi_server.models.user_statistics_accumulated_value_v1_statistics_individual200_response import UserStatisticsAccumulatedValueV1StatisticsIndividual200Response
from openapi_server import util


async def user_statistice_daily_value_v1_statistics_individual_daily_0(request: web.Request, start_date=None, end_date=None) -> web.Response:
    """User statistice - Daily value - v1/Statistics/individual/daily

    User statistice - Daily value - v1/Statistics/individual/daily

    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str

    """
    return web.Response(status=200)


async def user_statistics_accumulated_value_v1_statistics_individual_0(request: web.Request, start_date=None, end_date=None) -> web.Response:
    """User statistics - Accumulated value - /v1/Statistics/individual

    User statistics - Accumulated value - /v1/Statistics/individual

    :param start_date: 
    :type start_date: str
    :param end_date: 
    :type end_date: str

    """
    return web.Response(status=200)
