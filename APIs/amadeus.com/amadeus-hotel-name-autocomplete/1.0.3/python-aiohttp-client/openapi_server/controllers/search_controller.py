from typing import List, Dict
from aiohttp import web

from openapi_server.models.gethotels400_response import Gethotels400Response
from openapi_server.models.gethotels500_response import Gethotels500Response
from openapi_server.models.success import Success
from openapi_server import util


async def gethotels(request: web.Request, keyword, sub_type, country_code=None, lang=None, max=None) -> web.Response:
    """Returns a list of hotels matching a given keyword.

    

    :param keyword: Location query keyword
    :type keyword: str
    :param sub_type: Category of search - To enter several values, repeat the query parameter   Use HOTEL_LEISURE to target aggregators or HOTEL_GDS to target directly the chains
    :type sub_type: List[str]
    :param country_code: The country in which you search the subType. Country Code in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format
    :type country_code: str
    :param lang: The language in which you want the results in following [ISO 639-1](https://fr.wikipedia.org/wiki/Liste_des_codes_ISO_639-1).   If the language entered is not available then the results will be shown in the default language, English.
    :type lang: str
    :param max: The number of results requested from 1 to 20
    :type max: int

    """
    return web.Response(status=200)
