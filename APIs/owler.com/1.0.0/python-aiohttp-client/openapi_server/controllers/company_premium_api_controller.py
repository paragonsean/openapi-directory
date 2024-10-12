from typing import List, Dict
from aiohttp import web

from openapi_server.models.company import Company
from openapi_server import util


async def v1_companypremium_id_company_id_get(request: web.Request, company_id, format=None) -> web.Response:
    """Get Complete Company Info by Id

    The Company Premium Data API provides complete information about a company for the specified Company Id 

    :param company_id: Company Id
    :type company_id: str
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str

    """
    return web.Response(status=200)


async def v1_companypremium_url_website_get(request: web.Request, website, format=None) -> web.Response:
    """Get Basic Company Info by Url

    The Company Data API provides complete information about a company for the specified URL 

    :param website: Company Domain
    :type website: str
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str

    """
    return web.Response(status=200)
