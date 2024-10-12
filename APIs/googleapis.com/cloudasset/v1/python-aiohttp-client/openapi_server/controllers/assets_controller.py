from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_assets_response import ListAssetsResponse
from openapi_server import util


async def cloudasset_assets_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, asset_types=None, content_type=None, page_size=None, page_token=None, read_time=None, relationship_types=None) -> web.Response:
    """cloudasset_assets_list

    Lists assets with time and resource types and returns paged results in response.

    :param parent: Required. Name of the organization, folder, or project the assets belong to. Format: \&quot;organizations/[organization-number]\&quot; (such as \&quot;organizations/123\&quot;), \&quot;projects/[project-id]\&quot; (such as \&quot;projects/my-project-id\&quot;), \&quot;projects/[project-number]\&quot; (such as \&quot;projects/12345\&quot;), or \&quot;folders/[folder-number]\&quot; (such as \&quot;folders/12345\&quot;).
    :type parent: str
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
    :param asset_types: A list of asset types to take a snapshot for. For example: \&quot;compute.googleapis.com/Disk\&quot;. Regular expression is also supported. For example: * \&quot;compute.googleapis.com.*\&quot; snapshots resources whose asset type starts with \&quot;compute.googleapis.com\&quot;. * \&quot;.*Instance\&quot; snapshots resources whose asset type ends with \&quot;Instance\&quot;. * \&quot;.*Instance.*\&quot; snapshots resources whose asset type contains \&quot;Instance\&quot;. See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned. If specified, only matching assets will be returned, otherwise, it will snapshot all asset types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types.
    :type asset_types: List[str]
    :param content_type: Asset content type. If not specified, no content but the asset name will be returned.
    :type content_type: str
    :param page_size: The maximum number of assets to be returned in a single response. Default is 100, minimum is 1, and maximum is 1000.
    :type page_size: int
    :param page_token: The &#x60;next_page_token&#x60; returned from the previous &#x60;ListAssetsResponse&#x60;, or unspecified for the first &#x60;ListAssetsRequest&#x60;. It is a continuation of a prior &#x60;ListAssets&#x60; call, and the API should return the next page of assets.
    :type page_token: str
    :param read_time: Timestamp to take an asset snapshot. This can only be set to a timestamp between the current time and the current time minus 35 days (inclusive). If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query may get different results.
    :type read_time: str
    :param relationship_types: A list of relationship types to output, for example: &#x60;INSTANCE_TO_INSTANCEGROUP&#x60;. This field should only be specified if content_type&#x3D;RELATIONSHIP. * If specified: it snapshots specified relationships. It returns an error if any of the [relationship_types] doesn&#39;t belong to the supported relationship types of the [asset_types] or if any of the [asset_types] doesn&#39;t belong to the source types of the [relationship_types]. * Otherwise: it snapshots the supported relationships for all [asset_types] or returns an error if any of the [asset_types] has no relationship support. An unspecified asset types field means all supported asset_types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.
    :type relationship_types: List[str]

    """
    return web.Response(status=200)
