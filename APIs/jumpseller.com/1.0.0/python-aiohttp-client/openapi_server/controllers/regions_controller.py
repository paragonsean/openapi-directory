from typing import List, Dict
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.region import Region
from openapi_server import util


async def countries_country_code_regions_json_get_0(request: web.Request, login, authtoken, country_code) -> web.Response:
    """Retrieve all Regions from a single Country.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param country_code: ISO3166 Country Code
    :type country_code: str

    """
    return web.Response(status=200)


async def countries_country_code_regions_region_code_json_get_0(request: web.Request, login, authtoken, country_code, region_code) -> web.Response:
    """Retrieve a single Region information object.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param country_code: ISO3166 Country Code
    :type country_code: str
    :param region_code: Region Code
    :type region_code: str

    """
    return web.Response(status=200)
