from typing import List, Dict
from aiohttp import web

from openapi_server.models.competitors import Competitors
from openapi_server import util


async def v1_company_competitorpremium_id_company_id_get(request: web.Request, company_id, pagination_id=None, format=None) -> web.Response:
    """Get Competitor information by Id

    The Competitors API provides basic information about all competitors of a given company Id

    :param company_id: Company Id
    :type company_id: str
    :param pagination_id: Pass pagination_id as * in the first API request. The API response will return top competitors along with the next pagination_id which can be passed in the subsequent API request to get the next set of competitors. Repeat this process until needed or till the pagination_id returned is blank. Note:Every response will have maximum of 50 competitors.
    :type pagination_id: str
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str

    """
    return web.Response(status=200)


async def v1_company_competitorpremium_url_website_get(request: web.Request, website, pagination_id=None, format=None) -> web.Response:
    """Get Competitor information by Url

    The Competitors API provides basic information about all competitors of a given company Id

    :param website: Company Id
    :type website: str
    :param pagination_id: Pass pagination_id as * in the first API request. The API response will return top competitors along with the next pagination_id which can be passed in the subsequent API request to get the next set of competitors. Repeat this process until needed or till the pagination_id returned is blank. Note:Every response will have maximum of 50 competitors.
    :type pagination_id: str
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str

    """
    return web.Response(status=200)
