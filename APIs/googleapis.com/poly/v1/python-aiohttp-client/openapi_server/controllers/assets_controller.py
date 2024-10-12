from typing import List, Dict
from aiohttp import web

from openapi_server.models.asset import Asset
from openapi_server.models.list_assets_response import ListAssetsResponse
from openapi_server import util


async def poly_assets_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """poly_assets_get

    Returns detailed information about an asset given its name. PRIVATE assets are returned only if the currently authenticated user (via OAuth token) is the author of the asset.

    :param name: Required. An asset&#39;s name in the form &#x60;assets/{ASSET_ID}&#x60;.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def poly_assets_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, category=None, curated=None, format=None, keywords=None, max_complexity=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """poly_assets_list

    Lists all public, remixable assets. These are assets with an access level of PUBLIC and published under the CC-By license.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param category: Filter assets based on the specified category. Supported values are: &#x60;animals&#x60;, &#x60;architecture&#x60;, &#x60;art&#x60;, &#x60;food&#x60;, &#x60;nature&#x60;, &#x60;objects&#x60;, &#x60;people&#x60;, &#x60;scenes&#x60;, &#x60;technology&#x60;, and &#x60;transport&#x60;.
    :type category: str
    :param curated: Return only assets that have been curated by the Poly team.
    :type curated: bool
    :param format: Return only assets with the matching format. Acceptable values are: &#x60;BLOCKS&#x60;, &#x60;FBX&#x60;, &#x60;GLTF&#x60;, &#x60;GLTF2&#x60;, &#x60;OBJ&#x60;, &#x60;TILT&#x60;.
    :type format: str
    :param keywords: One or more search terms to be matched against all text that Poly has indexed for assets, which includes display_name, description, and tags. Multiple keywords should be separated by spaces.
    :type keywords: str
    :param max_complexity: Returns assets that are of the specified complexity or less. Defaults to COMPLEX. For example, a request for MEDIUM assets also includes SIMPLE assets.
    :type max_complexity: str
    :param order_by: Specifies an ordering for assets. Acceptable values are: &#x60;BEST&#x60;, &#x60;NEWEST&#x60;, &#x60;OLDEST&#x60;. Defaults to &#x60;BEST&#x60;, which ranks assets based on a combination of popularity and other features.
    :type order_by: str
    :param page_size: The maximum number of assets to be returned. This value must be between &#x60;1&#x60; and &#x60;100&#x60;. Defaults to &#x60;20&#x60;.
    :type page_size: int
    :param page_token: Specifies a continuation token from a previous search whose results were split into multiple pages. To get the next page, submit the same request specifying the value from next_page_token.
    :type page_token: str

    """
    return web.Response(status=200)
