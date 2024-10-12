from typing import List, Dict
from aiohttp import web

from openapi_server.models.country_info import CountryInfo
from openapi_server.models.culture_dto import CultureDto
from openapi_server.models.localization_option import LocalizationOption
from openapi_server.models.parental_rating import ParentalRating
from openapi_server import util


async def get_countries(request: web.Request, ) -> web.Response:
    """Gets known countries.

    


    """
    return web.Response(status=200)


async def get_cultures(request: web.Request, ) -> web.Response:
    """Gets known cultures.

    


    """
    return web.Response(status=200)


async def get_localization_options(request: web.Request, ) -> web.Response:
    """Gets localization options.

    


    """
    return web.Response(status=200)


async def get_parental_ratings(request: web.Request, ) -> web.Response:
    """Gets known parental ratings.

    


    """
    return web.Response(status=200)
