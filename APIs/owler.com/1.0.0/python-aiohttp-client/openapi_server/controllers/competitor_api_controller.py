from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_competitor_vo import CompanyCompetitorVO
from openapi_server import util


async def v1_company_competitor_id_company_id_get(request: web.Request, company_id, format=None) -> web.Response:
    """Get Competitor information by Id

    The Competitors API provides basic information about top 3 competitors of a company specified in the Company Id

    :param company_id: Company Id
    :type company_id: str
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str

    """
    return web.Response(status=200)


async def v1_company_competitor_url_website_get(request: web.Request, website, format=None) -> web.Response:
    """Get Competitor information by URL

    The Competitors API provides basic information about top 3 competitors of a company specified in the website

    :param website: Company Id
    :type website: str
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str

    """
    return web.Response(status=200)
