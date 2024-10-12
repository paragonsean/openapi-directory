from typing import List, Dict
from aiohttp import web

from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.product_uuids import ProductUuids
from openapi_server.models.products import Products
from openapi_server import util


async def get_app_catalog_mapped_products(request: web.Request, id, search_after=None, limit=None, updated_before=None, updated_after=None) -> web.Response:
    """Get the list of mapped products related to a catalog

    This endpoint allows you to get the list of products related to a catalog when the mapping is enabled. Please, note that a disabled catalog can return an HTTP 200 with a payload containing an error message, for more details see the &lt;a href&#x3D;\&quot;apps/catalogs.html#troubleshooting\&quot;&gt;App Catalog&lt;/a&gt; section.

    :param id: Catalog ID
    :type id: str
    :type id: str
    :param search_after: Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type search_after: str
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param updated_before: Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints)
    :type updated_before: str
    :param updated_after: Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints)
    :type updated_after: str

    """
    updated_before = util.deserialize_date(updated_before)
    updated_after = util.deserialize_date(updated_after)
    return web.Response(status=200)


async def get_app_catalog_product_uuids(request: web.Request, id, search_after=None, limit=None, updated_before=None, updated_after=None) -> web.Response:
    """Get the list of product uuids

    This endpoint allows you to get the list of uuids of products contained in a catalog. Please, note that a disabled catalog can return an HTTP 200 with a payload containing an error message, for more details see the &lt;a href&#x3D;\&quot;apps/catalogs.html#troubleshooting\&quot;&gt;App Catalog&lt;/a&gt; section.

    :param id: Id of the catalog
    :type id: str
    :type id: str
    :param search_after: Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type search_after: str
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param updated_before: Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints)
    :type updated_before: str
    :param updated_after: Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints)
    :type updated_after: str

    """
    updated_before = util.deserialize_date(updated_before)
    updated_after = util.deserialize_date(updated_after)
    return web.Response(status=200)


async def get_app_catalog_products(request: web.Request, id, search_after=None, limit=None, updated_before=None, updated_after=None) -> web.Response:
    """Get the list of products related to a catalog

    This endpoint allows you to get the list of products related to a catalog. Products are paginated and they can be filtered. In the Enterprise Edition, permissions based on your app settings are applied to the set of products you request. Please, note that a disabled catalog can return an HTTP 200 with a payload containing an error message, for more details see the &lt;a href&#x3D;\&quot;apps/catalogs.html#troubleshooting\&quot;&gt;App Catalog&lt;/a&gt; section.

    :param id: Catalog ID
    :type id: str
    :type id: str
    :param search_after: Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type search_after: str
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param updated_before: Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints)
    :type updated_before: str
    :param updated_after: Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints)
    :type updated_after: str

    """
    updated_before = util.deserialize_date(updated_before)
    updated_after = util.deserialize_date(updated_after)
    return web.Response(status=200)


async def get_app_catalog_products_uuid(request: web.Request, id, uuid) -> web.Response:
    """Get a product related to a catalog

    This endpoint allows you to get a specific product related to a catalog. In the Enterprise Edition, permissions based on your app settings are applied on the product you request. Please, note that a disabled catalog can return an HTTP 200 with a payload containing an error message, for more details see the &lt;a href&#x3D;\&quot;apps/catalogs.html#troubleshooting\&quot;&gt;App Catalog&lt;/a&gt; section.

    :param id: Catalog ID
    :type id: str
    :type id: str
    :param uuid: Product UUID
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)
