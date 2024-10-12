from typing import List, Dict
from aiohttp import web

from openapi_server.models.pam_asset_categories import PAMAssetCategories
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_asset_categories_request import PatchAssetCategoriesRequest
from openapi_server.models.post_asset_categories_request import PostAssetCategoriesRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_asset_categories(request: web.Request, page=None, limit=None, with_count=None) -> web.Response:
    """Get list of PAM asset categories

    This endpoint allows you to get a list of PAM asset categories. PAM asset categories are paginated and sorted by &#x60;root/left&#x60;.

    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool

    """
    return web.Response(status=200)


async def get_asset_categories_code(request: web.Request, code) -> web.Response:
    """Get a PAM asset category

    This endpoint allows you to get the information about a given PAM asset category.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_asset_categories(request: web.Request, body=None) -> web.Response:
    """Update/create several PAM asset categories

    This endpoint allows you to update several PAM asset categories at once.

    :param body: 
    :type body: dict | bytes

    """
    body = PatchAssetCategoriesRequest.from_dict(body)
    return web.Response(status=200)


async def patch_asset_categories_code(request: web.Request, code, body) -> web.Response:
    """Update/create a PAM asset category

    This endpoint allows you to update a given PAM asset category. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no category exists for the given code, it creates it.

    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostAssetCategoriesRequest.from_dict(body)
    return web.Response(status=200)


async def post_asset_categories(request: web.Request, body=None) -> web.Response:
    """Create a new PAM asset category

    This endpoint allows you to create a new PAM asset category.

    :param body: 
    :type body: dict | bytes

    """
    body = PostAssetCategoriesRequest.from_dict(body)
    return web.Response(status=200)
