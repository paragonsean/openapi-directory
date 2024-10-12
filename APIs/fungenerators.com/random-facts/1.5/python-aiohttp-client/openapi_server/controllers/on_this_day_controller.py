from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def fact_onthisday_born_get(request: web.Request, month=None, day=None) -> web.Response:
    """fact_onthisday_born_get

    Returns a random ( famous/ relatively famous ) person born on a given day and month

    :param month: Optional month (1-12). Defaults to current month
    :type month: str
    :param day: Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month.
    :type day: str

    """
    return web.Response(status=200)


async def fact_onthisday_died_get(request: web.Request, month=None, day=None) -> web.Response:
    """fact_onthisday_died_get

    Returns a random ( famous/ relatively famous ) person died on a given day and month

    :param month: Optional month (1-12). Defaults to current month
    :type month: str
    :param day: Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month.
    :type day: str

    """
    return web.Response(status=200)


async def fact_onthisday_event_get(request: web.Request, month=None, day=None) -> web.Response:
    """fact_onthisday_event_get

    Returns a random ( famous/ relatively famous ) historic event on a given day and month

    :param month: Optional month (1-12). Defaults to current month
    :type month: str
    :param day: Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month.
    :type day: str

    """
    return web.Response(status=200)
