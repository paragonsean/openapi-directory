from typing import List, Dict
from aiohttp import web

from openapi_server.models.country import Country
from openapi_server.models.networks import Networks
from openapi_server.models.schedule import Schedule
from openapi_server.models.show_seasons import ShowSeasons
from openapi_server import util


async def calendar_by_show_name_get(request: web.Request, access_token, name, year) -> web.Response:
    """Will return show schedule for queried showname and year

    

    :param access_token: 
    :type access_token: str
    :param name: 
    :type name: str
    :param year: 
    :type year: str

    """
    return web.Response(status=200)


async def calendar_countries_get(request: web.Request, access_token) -> web.Response:
    """Returns list of available countries in calendar database

    

    :param access_token: 
    :type access_token: str

    """
    return web.Response(status=200)


async def calendar_networks_get(request: web.Request, access_token) -> web.Response:
    """Gets a list of available networks

    

    :param access_token: 
    :type access_token: str

    """
    return web.Response(status=200)


async def calendar_show_seasons_get(request: web.Request, access_token, name) -> web.Response:
    """Returns list of seasons available in the calendar for show

    

    :param access_token: 
    :type access_token: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def calendar_today_get(request: web.Request, access_token) -> web.Response:
    """Will return show schedule for today for all countries in database

    

    :param access_token: 
    :type access_token: str

    """
    return web.Response(status=200)


async def calendarby_showname_season_get(request: web.Request, access_token, name, season) -> web.Response:
    """Get Calendar by showname and season

    

    :param access_token: 
    :type access_token: str
    :param name: 
    :type name: str
    :param season: 
    :type season: str

    """
    return web.Response(status=200)


async def schedule_by_date_get(request: web.Request, access_token, _date, country) -> web.Response:
    """Gets TV Schedule for selected data

    

    :param access_token: 
    :type access_token: str
    :param _date: date format year-month-day
    :type _date: str
    :param country: US / CA / NL / BE / DE / GB or FR
    :type country: str

    """
    return web.Response(status=200)
