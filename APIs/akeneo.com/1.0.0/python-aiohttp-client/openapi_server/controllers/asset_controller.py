from typing import List, Dict
from aiohttp import web

from openapi_server.models.asset import Asset
from openapi_server.models.patch_assets200_response_inner import PatchAssets200ResponseInner
from openapi_server.models.patch_assets_request_inner import PatchAssetsRequestInner
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def delete_assets_code(request: web.Request, asset_family_code, code) -> web.Response:
    """Delete an asset

    This endpoint allows you to delete a given asset. This endpoint is case sensitive on the asset family code.

    :param asset_family_code: Code of the asset family
    :type asset_family_code: str
    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def get_assets(request: web.Request, asset_family_code, search=None, channel=None, locales=None, search_after=None) -> web.Response:
    """Get the list of the assets of a given asset family

    This endpoint allows you to get a list of assets of a given asset family. Assets are paginated. This endpoint is case sensitive on the asset family code.

    :param asset_family_code: Code of the asset family
    :type asset_family_code: str
    :param search: Filter assets, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-assets\&quot;&gt;Asset filters&lt;/a&gt; section
    :type search: str
    :param channel: Filter asset values to return scopable asset attributes for the given channel as well as the non localizable/non scopable asset attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#asset-values-by-channel\&quot;&gt;Filter asset values by channel&lt;/a&gt; section
    :type channel: str
    :param locales: Filter asset values to return localizable attributes for the given locales as well as the non localizable/non scopable asset attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#asset-values-by-locale\&quot;&gt;Filter asset values by locale&lt;/a&gt; section
    :type locales: str
    :param search_after: Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type search_after: str

    """
    return web.Response(status=200)


async def get_assets_code(request: web.Request, asset_family_code, code) -> web.Response:
    """Get an asset of a given asset family

    This endpoint allows you to get the information about a given asset for a given asset family. This endpoint is case sensitive on the asset family code.

    :param asset_family_code: Code of the asset family
    :type asset_family_code: str
    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_asset_code(request: web.Request, asset_family_code, code, body) -> web.Response:
    """Update/create an asset

    This endpoint allows you to update a given asset of a given asset family. Learn more about the &lt;a href&#x3D;\&quot;/documentation/update.html#patch-asset-attribute-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the asset does not already exist for the given asset family, it creates it. This endpoint is case sensitive on the asset family code.

    :param asset_family_code: Code of the asset family
    :type asset_family_code: str
    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchAssetsRequestInner.from_dict(body)
    return web.Response(status=200)


async def patch_assets(request: web.Request, asset_family_code, body) -> web.Response:
    """Update/create several assets

    This endpoint allows you to update and/or create several assets of one given asset family at once. Learn more about the &lt;a href&#x3D;\&quot;/documentation/update.html#patch-asset-attribute-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the asset does not already exist for the given asset family, it creates it. This endpoint is case sensitive on the asset family code.

    :param asset_family_code: Code of the asset family
    :type asset_family_code: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchAssetsRequestInner.from_dict(d) for d in body]
    return web.Response(status=200)
