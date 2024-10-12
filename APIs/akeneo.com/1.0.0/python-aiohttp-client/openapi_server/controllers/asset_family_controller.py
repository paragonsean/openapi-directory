from typing import List, Dict
from aiohttp import web

from openapi_server.models.asset_families import AssetFamilies
from openapi_server.models.get_asset_family_code200_response import GetAssetFamilyCode200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_asset_families(request: web.Request, search_after=None) -> web.Response:
    """Get list of asset families

    This endpoint allows you to get a list of asset families. Asset families are paginated.

    :param search_after: Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type search_after: str

    """
    return web.Response(status=200)


async def get_asset_family_code(request: web.Request, code) -> web.Response:
    """Get an asset family

    This endpoint allows you to get the information about a given asset family.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_asset_family_code(request: web.Request, code, body) -> web.Response:
    """Update/create an asset family

    This endpoint allows you to update a given asset family. Note that if the asset family does not already exist, it creates it.

    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetAssetFamilyCode200Response.from_dict(body)
    return web.Response(status=200)
