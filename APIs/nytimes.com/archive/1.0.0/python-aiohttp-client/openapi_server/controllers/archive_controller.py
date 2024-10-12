from typing import List, Dict
from aiohttp import web

from openapi_server.models.year_month_json_get200_response import YearMonthJsonGet200Response
from openapi_server import util


async def year_month_json_get(request: web.Request, year, month) -> web.Response:
    """Archive API

    The Archive API provides lists of NYT articles by month going back to 1851.  Simply pass in the year and month you want and it returns a JSON object with all articles for that month. 

    :param year: The year (e.g. 2016).
    :type year: int
    :param month: The month number (e.g. 1 for January).
    :type month: int

    """
    return web.Response(status=200)
