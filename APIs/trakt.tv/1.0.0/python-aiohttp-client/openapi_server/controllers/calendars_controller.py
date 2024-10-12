from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def calendars_all_dvd_start_date_days_get(request: web.Request, start_date, days, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get DVD releases

    #### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies with a DVD release date during the time period specified.

    :param start_date: Start the calendar on this date.
    :type start_date: str
    :param days: Number of days to display.
    :type days: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def calendars_all_movies_start_date_days_get(request: web.Request, start_date, days, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get movies

    #### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies with a release date during the time period specified.

    :param start_date: Start the calendar on this date.
    :type start_date: str
    :param days: Number of days to display.
    :type days: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def calendars_all_shows_new_start_date_days_get(request: web.Request, start_date, days, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get new shows

    #### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all new show premieres (season 1, episode 1) airing during the time period specified.

    :param start_date: Start the calendar on this date.
    :type start_date: str
    :param days: Number of days to display.
    :type days: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def calendars_all_shows_premieres_start_date_days_get(request: web.Request, start_date, days, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get season premieres

    #### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all show premieres (any season, episode 1) airing during the time period specified.

    :param start_date: Start the calendar on this date.
    :type start_date: str
    :param days: Number of days to display.
    :type days: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def calendars_all_shows_start_date_days_get(request: web.Request, start_date, days, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get shows

    #### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all shows airing during the time period specified.

    :param start_date: Start the calendar on this date.
    :type start_date: str
    :param days: Number of days to display.
    :type days: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_dvd_releases(request: web.Request, start_date, days, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get DVD releases

    #### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies with a DVD release date during the time period specified.

    :param start_date: Start the calendar on this date.
    :type start_date: str
    :param days: Number of days to display.
    :type days: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_movies(request: web.Request, start_date, days, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get movies

    #### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies with a release date during the time period specified.

    :param start_date: Start the calendar on this date.
    :type start_date: str
    :param days: Number of days to display.
    :type days: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_new_shows(request: web.Request, start_date, days, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get new shows

    #### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all new show premieres (season 1, episode 1) airing during the time period specified.

    :param start_date: Start the calendar on this date.
    :type start_date: str
    :param days: Number of days to display.
    :type days: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_season_premieres(request: web.Request, start_date, days, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get season premieres

    #### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all show premieres (any season, episode 1) airing during the time period specified.

    :param start_date: Start the calendar on this date.
    :type start_date: str
    :param days: Number of days to display.
    :type days: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)


async def get_shows(request: web.Request, start_date, days, trakt_api_version=None, trakt_api_key=None) -> web.Response:
    """Get shows

    #### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all shows airing during the time period specified.

    :param start_date: Start the calendar on this date.
    :type start_date: str
    :param days: Number of days to display.
    :type days: int
    :param trakt_api_version: e.g. 2
    :type trakt_api_version: str
    :param trakt_api_key: e.g. [client_id]
    :type trakt_api_key: str

    """
    return web.Response(status=200)
