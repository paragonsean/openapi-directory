from typing import List, Dict
from aiohttp import web

from openapi_server.models.daily_report_view_model_search_result import DailyReportViewModelSearchResult
from openapi_server.models.house_enum import HouseEnum
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def api_dailyreports_dailyreports_get(request: web.Request, date_from=None, date_to=None, house=None, skip=None, take=None) -> web.Response:
    """Returns a list of daily reports

    

    :param date_from: Daily report with report date on or after the date specified. Date format yyyy-mm-dd
    :type date_from: str
    :param date_to: Daily report with report date on or before the date specified. Date format yyyy-mm-dd
    :type date_to: str
    :param house: Daily report relating to the House specified. Defaults to Bicameral
    :type house: dict | bytes
    :param skip: Number of records to skip, default is 0
    :type skip: int
    :param take: Number of records to take, default is 20
    :type take: int

    """
    date_from = util.deserialize_datetime(date_from)
    date_to = util.deserialize_datetime(date_to)
    house = .from_dict(house)
    return web.Response(status=200)
