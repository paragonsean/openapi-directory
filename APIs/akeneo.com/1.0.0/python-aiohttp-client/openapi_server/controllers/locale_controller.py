from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_locales_code200_response import GetLocalesCode200Response
from openapi_server.models.locales import Locales
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_locales(request: web.Request, search=None, page=None, limit=None, with_count=None) -> web.Response:
    """Get a list of locales

    This endpoint allows you to get a list of locales. Locales are paginated and sorted by code.

    :param search: Filter locales, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html\&quot;&gt;Filters&lt;/a&gt; section
    :type search: str
    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool

    """
    return web.Response(status=200)


async def get_locales_code(request: web.Request, code) -> web.Response:
    """Get a locale

    This endpoint allows you to get the information about a given locale.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)
