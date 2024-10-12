from typing import List, Dict
from aiohttp import web

from openapi_server.models.basic_results import BasicResults
from openapi_server.models.company import Company
from openapi_server.models.results import Results
from openapi_server import util


async def basic_company_search(request: web.Request, q, fields=None, limit=None, format=None) -> web.Response:
    """Basic Search Company by Ticker or Website or Name or PermID

    The Company Basic Search API searches for a company based on the input and will returns results containing basic details about matching companies. By default the API returns the top 10 available results unless the limit is specified. The maximum limit is restricted to 30.

    :param q: Search term
    :type q: str
    :param fields: Fields to be searched - name, website, ticker, permid. If not specfied, will be searched against all fields
    :type fields: List[str]
    :param limit: Number of results to be displayed - 10 (by default, if not specified) to 30
    :type limit: str
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str

    """
    return web.Response(status=200)


async def fuzzy_company_search(request: web.Request, q, fields, limit=None, format=None) -> web.Response:
    """Fuzzy Search Company by Name or Address or Phone

    The Company Fuzzy Search API searches for a company based on the input and will return results containing basic details about matching companies. By default the API returns at most top 10 available results unless the limit is specified. The maximum limit is restricted to 30.

    :param q: Search term
    :type q: str
    :param fields: Fields to be searched - name, website, ticker, permid, address, phone. Each field and its corresponding value has to be specified
    :type fields: List[str]
    :param limit: Number of results to be displayed - 10 (by default, if not specified) to 30
    :type limit: str
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str

    """
    return web.Response(status=200)


async def search_company(request: web.Request, q, fields=None, limit=None, format=None) -> web.Response:
    """Search Company by Ticker or Website or Name or PermID

    The Company Search API searches for a company based on the input and will returns results containing basic details about matching companies. By default the API returns the top 10 available results unless the limit is specified. The maximum limit is restricted to 30.

    :param q: Search term
    :type q: str
    :param fields: Fields to be searched - name, website, ticker. If not specified, will be searched against all fields
    :type fields: List[str]
    :param limit: Number of results to be displayed - 10 (by default, if not specified) to 30
    :type limit: str
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str

    """
    return web.Response(status=200)


async def v1_company_id_company_id_get(request: web.Request, company_id, format=None) -> web.Response:
    """Get Company by Id

    The Company Data API provides complete information about a company for the specified Company Id 

    :param company_id: Company Id
    :type company_id: str
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str

    """
    return web.Response(status=200)


async def v1_company_url_website_get(request: web.Request, website, format=None) -> web.Response:
    """Get Company by URL

    The Company Data API provides complete information about a company for the specified URL 

    :param website: Company Domain
    :type website: str
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str

    """
    return web.Response(status=200)
