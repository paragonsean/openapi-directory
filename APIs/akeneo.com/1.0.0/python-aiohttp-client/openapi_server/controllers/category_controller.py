from typing import List, Dict
from aiohttp import web

from openapi_server.models.categories import Categories
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_categories_request import PatchCategoriesRequest
from openapi_server.models.post_categories_request import PostCategoriesRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_categories(request: web.Request, search=None, page=None, limit=None, with_count=None, with_position=None, with_enriched_attributes=None) -> web.Response:
    """Get list of categories

    This endpoint allows you to get a list of categories. Categories are paginated and sorted by &#x60;root/left&#x60;.

    :param search: Filter categories, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-categories\&quot;&gt;Filters&lt;/a&gt; section.
    :type search: str
    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool
    :param with_position: Return information about category position into its category tree (only available since the 7.0 version)
    :type with_position: bool
    :param with_enriched_attributes: Return attribute values of the category (only available on SaaS platforms)
    :type with_enriched_attributes: bool

    """
    return web.Response(status=200)


async def get_categories_code(request: web.Request, code, with_position=None, with_enriched_attributes=None) -> web.Response:
    """Get a category

    This endpoint allows you to get the information about a given category.

    :param code: Code of the resource
    :type code: str
    :param with_position: Return information about category position into its category tree (only available since the 7.0 version)
    :type with_position: bool
    :param with_enriched_attributes: Return attribute values of the category (only available on SaaS platforms)
    :type with_enriched_attributes: bool

    """
    return web.Response(status=200)


async def get_category_media_files_code_download(request: web.Request, code) -> web.Response:
    """Download a category media file

    This endpoint allows you to download a given media file that is used as an attribute value of a enriched category.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_categories(request: web.Request, body=None) -> web.Response:
    """Update/create several categories

    This endpoint allows you to update several categories at once.

    :param body: 
    :type body: dict | bytes

    """
    body = PatchCategoriesRequest.from_dict(body)
    return web.Response(status=200)


async def patch_categories_code(request: web.Request, code, body) -> web.Response:
    """Update/create a category

    This endpoint allows you to update a given category. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no category exists for the given code, it creates it.

    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostCategoriesRequest.from_dict(body)
    return web.Response(status=200)


async def post_categories(request: web.Request, body=None) -> web.Response:
    """Create a new category

    This endpoint allows you to create a new category.

    :param body: 
    :type body: dict | bytes

    """
    body = PostCategoriesRequest.from_dict(body)
    return web.Response(status=200)
