from typing import List, Dict
from aiohttp import web

from openapi_server.models.families import Families
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_families_request import PatchFamiliesRequest
from openapi_server.models.post_families_family_code_variants_request import PostFamiliesFamilyCodeVariantsRequest
from openapi_server.models.post_families_request import PostFamiliesRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_families(request: web.Request, search=None, page=None, limit=None, with_count=None) -> web.Response:
    """Get list of families

    This endpoint allows you to get a list of families. Families are paginated and sorted by code.

    :param search: Filter families, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-families\&quot;&gt;Filters&lt;/a&gt; section.
    :type search: str
    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool

    """
    return web.Response(status=200)


async def get_families_code(request: web.Request, code) -> web.Response:
    """Get a family

    This endpoint allows you to get the information about a given family.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_families(request: web.Request, body=None) -> web.Response:
    """Update/create several families

    This endpoint allows you to update and/or create several families at once.

    :param body: 
    :type body: dict | bytes

    """
    body = PatchFamiliesRequest.from_dict(body)
    return web.Response(status=200)


async def patch_families_code(request: web.Request, code, body) -> web.Response:
    """Update/create a family

    This endpoint allows you to update a given family. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no family exists for the given code, it creates it.

    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostFamiliesRequest.from_dict(body)
    return web.Response(status=200)


async def post_families(request: web.Request, body=None) -> web.Response:
    """Create a new family

    This endpoint allows you to create a new family.

    :param body: 
    :type body: dict | bytes

    """
    body = PostFamiliesRequest.from_dict(body)
    return web.Response(status=200)


async def post_families_family_code_variants(request: web.Request, family_code, body=None) -> web.Response:
    """Create a new family variant

    This endpoint allows you to create a family variant.

    :param family_code: Code of the family
    :type family_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostFamiliesFamilyCodeVariantsRequest.from_dict(body)
    return web.Response(status=200)
