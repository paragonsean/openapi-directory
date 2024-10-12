from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_all_resources_response import SearchAllResourcesResponse
from openapi_server import util


async def cloudasset_resources_search_all(request: web.Request, scope, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, asset_types=None, order_by=None, page_size=None, page_token=None, query=None) -> web.Response:
    """cloudasset_resources_search_all

    Searches all the resources within a given accessible Resource Manager scope (project/folder/organization). This RPC gives callers especially administrators the ability to search all the resources within a scope, even if they don&#39;t have &#x60;.get&#x60; permission of all the resources. Callers should have &#x60;cloud.assets.SearchAllResources&#x60; permission on the requested scope, otherwise the request will be rejected.

    :param scope: Required. The relative name of an asset. The search is limited to the resources within the &#x60;scope&#x60;. The allowed value must be: * Organization number (such as \&quot;organizations/123\&quot;) * Folder number (such as \&quot;folders/1234\&quot;) * Project number (such as \&quot;projects/12345\&quot;) * Project ID (such as \&quot;projects/abc\&quot;)
    :type scope: str
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
    :param asset_types: Optional. A list of asset types that this request searches for. If empty, it will search all the supported asset types.
    :type asset_types: List[str]
    :param order_by: Optional. A comma separated list of fields specifying the sorting order of the results. The default order is ascending. Add &#x60; DESC&#x60; after the field name to indicate descending order. Redundant space characters are ignored. For example, &#x60; location DESC , name &#x60;.
    :type order_by: str
    :param page_size: Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as &#x60;next_page_token&#x60; is returned.
    :type page_size: int
    :param page_token: Optional. If present, then retrieve the next batch of results from the preceding call to this method. &#x60;page_token&#x60; must be the value of &#x60;next_page_token&#x60; from the previous response. The values of all other method parameters, must be identical to those in the previous call.
    :type page_token: str
    :param query: Optional. The query statement.
    :type query: str

    """
    return web.Response(status=200)
