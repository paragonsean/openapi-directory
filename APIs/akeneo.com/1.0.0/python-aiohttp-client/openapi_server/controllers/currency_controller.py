from typing import List, Dict
from aiohttp import web

from openapi_server.models.currencies import Currencies
from openapi_server.models.currencies_get200_response import CurrenciesGet200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def currencies_get(request: web.Request, code) -> web.Response:
    """Get a currency

    This endpoint allows you to get the information about a given currency.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def currencies_get_list(request: web.Request, page=None, limit=None, with_count=None) -> web.Response:
    """Get a list of currencies

    This endpoint allows you to get a list of currencies. Currencies are paginated and sorted by code.

    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool

    """
    return web.Response(status=200)
