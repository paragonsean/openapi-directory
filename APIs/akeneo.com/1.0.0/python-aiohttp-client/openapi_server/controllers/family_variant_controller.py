from typing import List, Dict
from aiohttp import web

from openapi_server.models.family_variants import FamilyVariants
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_families_family_code_variants_request import PatchFamiliesFamilyCodeVariantsRequest
from openapi_server.models.post_families_family_code_variants_request import PostFamiliesFamilyCodeVariantsRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_families_family_code_variants(request: web.Request, family_code, page=None, limit=None, with_count=None) -> web.Response:
    """Get list of family variants

    This endpoint allows you to get a list of family variants. Family variants are paginated and sorted by code.

    :param family_code: Code of the family
    :type family_code: str
    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool

    """
    return web.Response(status=200)


async def get_families_family_code_variants_code(request: web.Request, family_code, code) -> web.Response:
    """Get a family variant

    This endpoint allows you to get the information about a given family variant.

    :param family_code: Code of the family
    :type family_code: str
    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_families_family_code_variants(request: web.Request, family_code, body=None) -> web.Response:
    """Update/create several family variants

    This endpoint allows you to update and/or create several family variants at once, for a given family.

    :param family_code: Code of the family
    :type family_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchFamiliesFamilyCodeVariantsRequest.from_dict(body)
    return web.Response(status=200)


async def patch_families_family_code_variants_code(request: web.Request, family_code, code, body) -> web.Response:
    """Update/create a family variant

    This endpoint allows you to update a given family variant. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no family variant exists for the given code, it creates it.

    :param family_code: Code of the family
    :type family_code: str
    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostFamiliesFamilyCodeVariantsRequest.from_dict(body)
    return web.Response(status=200)
