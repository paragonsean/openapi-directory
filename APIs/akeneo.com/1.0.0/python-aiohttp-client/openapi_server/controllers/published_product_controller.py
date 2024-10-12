from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_published_products_code200_response import GetPublishedProductsCode200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.published_products import PublishedProducts
from openapi_server import util


async def get_published_products(request: web.Request, search=None, scope=None, locales=None, attributes=None, pagination_type=None, page=None, search_after=None, limit=None, with_count=None) -> web.Response:
    """Get list of published products

    This endpoint allows you to get a list of published products. Published products are paginated and they can be filtered.

    :param search: Filter published products, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html\&quot;&gt;Filters&lt;/a&gt; section
    :type search: str
    :param scope: Filter published product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-published-product-values\&quot;&gt;Filter on published product values&lt;/a&gt; section
    :type scope: str
    :param locales: Filter published product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-published-product-values\&quot;&gt;Filter on published product values&lt;/a&gt; section
    :type locales: str
    :param attributes: Filter published product values to only return those concerning the given attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-product-values\&quot;&gt;Filter on product values&lt;/a&gt; section
    :type attributes: str
    :param pagination_type: Pagination method type, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type pagination_type: str
    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param search_after: Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type search_after: str
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool

    """
    return web.Response(status=200)


async def get_published_products_code(request: web.Request, code) -> web.Response:
    """Get a published product

    This endpoint allows you to get the information about a given published product.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)
