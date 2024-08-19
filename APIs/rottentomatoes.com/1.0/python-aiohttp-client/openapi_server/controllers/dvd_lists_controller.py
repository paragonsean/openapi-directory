from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def current_release_dvds_dvd_lists(request: web.Request, page_limit=None, page=None, country=None) -> web.Response:
    """current_release_dvds_dvd_lists

    

    :param page_limit: The amount of new release dvds to show per page
    :type page_limit: str
    :param page: The selected page of current DVD releases
    :type page: str
    :param country: Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.
    :type country: str

    """
    return web.Response(status=200)


async def new_release_dvds_dvd_lists(request: web.Request, page_limit=None, page=None, country=None) -> web.Response:
    """new_release_dvds_dvd_lists

    

    :param page_limit: The amount of new release dvds to show per page
    :type page_limit: str
    :param page: The selected page of new release DVDs
    :type page: str
    :param country: Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.
    :type country: str

    """
    return web.Response(status=200)


async def top_rentals_dvd_lists(request: web.Request, limit=None, country=None) -> web.Response:
    """top_rentals_dvd_lists

    

    :param limit: Limits the number of top rentals returned
    :type limit: str
    :param country: Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.
    :type country: str

    """
    return web.Response(status=200)


async def upcoming_dvds_dvd_lists(request: web.Request, page_limit=None, page=None, country=None) -> web.Response:
    """upcoming_dvds_dvd_lists

    

    :param page_limit: The amount of upcoming dvds to show per page
    :type page_limit: str
    :param page: The selected page of upcoming DVDs
    :type page: str
    :param country: Provides localized data for the selected country (ISO 3166-1 alpha-2) if available. Otherwise, returns US data.
    :type country: str

    """
    return web.Response(status=200)
