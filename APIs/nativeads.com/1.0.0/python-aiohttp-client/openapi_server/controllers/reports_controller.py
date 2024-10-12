from typing import List, Dict
from aiohttp import web

from openapi_server.models.model_error import ModelError
from openapi_server.models.reports_daily_response import ReportsDailyResponse
from openapi_server.models.reports_website_response import ReportsWebsiteResponse
from openapi_server.models.reports_widget_response import ReportsWidgetResponse
from openapi_server import util


async def publisher_reports_daily_get(request: web.Request, token, start_date, end_date, limit, page) -> web.Response:
    """publisher_reports_daily_get

    Returns publisher statistics split by date

    :param token: Native Ads Publisher API authentication token
    :type token: str
    :param start_date: start date in format YYYY-MM-DD
    :type start_date: str
    :param end_date: end date in format YYYY-MM-DD
    :type end_date: str
    :param limit: maximum number of results per page
    :type limit: int
    :param page: page number
    :type page: int

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def publisher_reports_website_get(request: web.Request, token, start_date, end_date, limit, page) -> web.Response:
    """publisher_reports_website_get

    Returns publisher statistics split by website

    :param token: Native Ads Publisher API authentication token
    :type token: str
    :param start_date: start date in format YYYY-MM-DD
    :type start_date: str
    :param end_date: end date in format YYYY-MM-DD
    :type end_date: str
    :param limit: maximum number of results per page
    :type limit: int
    :param page: page number
    :type page: int

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def publisher_reports_widget_get(request: web.Request, token, start_date, end_date, limit, page) -> web.Response:
    """publisher_reports_widget_get

    Returns publisher statistics split by widget

    :param token: Native Ads Publisher API authentication token
    :type token: str
    :param start_date: start date in format YYYY-MM-DD
    :type start_date: str
    :param end_date: end date in format YYYY-MM-DD
    :type end_date: str
    :param limit: maximum number of results per page
    :type limit: int
    :param page: page number
    :type page: int

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)
