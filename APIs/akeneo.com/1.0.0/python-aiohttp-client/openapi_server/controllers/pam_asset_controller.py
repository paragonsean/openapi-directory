from typing import List, Dict
from aiohttp import web

from openapi_server.models.pam_assets import PAMAssets
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_pam_assets_request import PatchPamAssetsRequest
from openapi_server.models.post_pam_assets_request import PostPamAssetsRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_pam_assets(request: web.Request, pagination_type=None, page=None, search_after=None, limit=None, with_count=None) -> web.Response:
    """Get list of PAM assets

    This endpoint allows you to get a list of PAM assets. PAM assets are paginated.

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


async def get_pam_assets_code(request: web.Request, code) -> web.Response:
    """Get a PAM asset

    This endpoint allows you to get the information about a given PAM asset.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_pam_assets(request: web.Request, body=None) -> web.Response:
    """Update/create several PAM assets

    This endpoint allows you to update several PAM assets at once.

    :param body: 
    :type body: dict | bytes

    """
    body = PatchPamAssetsRequest.from_dict(body)
    return web.Response(status=200)


async def patch_pam_assets_code(request: web.Request, code, body) -> web.Response:
    """Update/create a PAM asset

    This endpoint allows you to update a given PAM asset. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no asset exists for the given code, it creates it.

    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostPamAssetsRequest.from_dict(body)
    return web.Response(status=200)


async def post_pam_assets(request: web.Request, body=None) -> web.Response:
    """Create a new PAM asset

    This endpoint allows you to create a new PAM asset.

    :param body: 
    :type body: dict | bytes

    """
    body = PostPamAssetsRequest.from_dict(body)
    return web.Response(status=200)
