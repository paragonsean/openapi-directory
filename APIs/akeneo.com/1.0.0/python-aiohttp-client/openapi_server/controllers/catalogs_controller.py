from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalogs import Catalogs
from openapi_server.models.post_app_catalog201_response import PostAppCatalog201Response
from openapi_server.models.post_app_catalog_request import PostAppCatalogRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def delete_app_catalog(request: web.Request, id) -> web.Response:
    """Delete a catalog

    This endpoint allows you to delete a catalog.

    :param id: Catalog ID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_app_catalog(request: web.Request, id) -> web.Response:
    """Get a catalog

    This endpoint allows you to get the information about a catalog.

    :param id: Catalog ID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_app_catalogs(request: web.Request, page=None, limit=None) -> web.Response:
    """Get the list of owned catalogs

    This endpoint allows you to get the list of catalogs you owned.

    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int

    """
    return web.Response(status=200)


async def patch_app_catalog(request: web.Request, id, body=None) -> web.Response:
    """Update a catalog

    This endpoint allows you to update a catalog.

    :param id: Catalog ID
    :type id: str
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostAppCatalogRequest.from_dict(body)
    return web.Response(status=200)


async def post_app_catalog(request: web.Request, body=None) -> web.Response:
    """Create a new catalog

    This endpoint allows you to create a new catalog.

    :param body: 
    :type body: dict | bytes

    """
    body = PostAppCatalogRequest.from_dict(body)
    return web.Response(status=200)
