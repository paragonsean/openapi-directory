from typing import List, Dict
from aiohttp import web

from openapi_server.models.results import Results
from openapi_server import util


async def v1_feed_get(request: web.Request, company_id, format=None, limit=None, pagination_id=None, category=None) -> web.Response:
    """Get Feeds for given Company Ids

    The Feeds API provides a list of feeds and individual feed information for the given Company Ids and Category. By default the API returns the latest 10 feeds available unless the limit is specified. The maximum result is restricted to 100 feeds per API request.

    :param company_id: Company Ids separated by comma (Maximum of 150 Company Ids)
    :type company_id: List[str]
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str
    :param limit: Number of results to be displayed - 10 (by default, if not specified) to 100
    :type limit: str
    :param pagination_id: Pass pagination_id as blank in the first API request. The API response will return the latest feeds along with the next pagination_id which can be passed in the subsequent API request to get the next set of feeds. Repeat this process until needed or till the pagination_id returned is blank
    :type pagination_id: str
    :param category: Categories separated by comma. If not specified, will search against all categories
    :type category: List[str]

    """
    return web.Response(status=200)


async def v1_feed_url_get(request: web.Request, domain, format=None, limit=None, pagination_id=None, category=None) -> web.Response:
    """Get Feeds for given Company Websites

    The Feeds API provides a list of feeds and individual feed information for the given Company Websites and Category. By default the API returns the latest 10 feeds available unless the limit is specified. The maximum result is restricted to 100 feeds per API request.

    :param domain: Company Websites separated by comma (Maximum of 10 Company Websites)
    :type domain: List[str]
    :param format: Format of the response content - json (by default if not specified), xml
    :type format: str
    :param limit: Number of results to be displayed - 10 (by default, if not specified) to 100
    :type limit: str
    :param pagination_id: Pass pagination_id as blank in the first API request. The API response will return the latest feeds along with the next pagination_id which can be passed in the subsequent API request to get the next set of feeds. Repeat this process until needed or till the pagination_id returned is blank
    :type pagination_id: str
    :param category: Categories separated by comma. If not specified, will search against all categories
    :type category: List[str]

    """
    return web.Response(status=200)
