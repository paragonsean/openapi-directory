from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_search_ideahub_v1alpha_list_ideas_response import GoogleSearchIdeahubV1alphaListIdeasResponse
from openapi_server import util


async def ideahub_ideas_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, parent=None) -> web.Response:
    """ideahub_ideas_list

    List ideas for a given Creator and filter and sort options.

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
    :param filter: Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions are implicitly combined, as if the &#x60;AND&#x60; operator was always used. The &#x60;OR&#x60; operator is currently unsupported. * Supported functions: - &#x60;saved(bool)&#x60;: If set to true, fetches only saved ideas. If set to false, fetches all except saved ideas. Can&#39;t be simultaneously used with &#x60;dismissed(bool)&#x60;. - &#x60;dismissed(bool)&#x60;: If set to true, fetches only dismissed ideas. Can&#39;t be simultaneously used with &#x60;saved(bool)&#x60;. The &#x60;false&#x60; value is currently unsupported. Examples: * &#x60;saved(true)&#x60; * &#x60;saved(false)&#x60; * &#x60;dismissed(true)&#x60; The length of this field should be no more than 500 characters.
    :type filter: str
    :param order_by: Order semantics described below.
    :type order_by: str
    :param page_size: The maximum number of ideas per page. If unspecified, at most 10 ideas will be returned. The maximum value is 2000; values above 2000 will be coerced to 2000.
    :type page_size: int
    :param page_token: Used to fetch next page.
    :type page_token: str
    :param parent: If defined, specifies the creator for which to filter by. Format: publishers/{publisher}/properties/{property}
    :type parent: str

    """
    return web.Response(status=200)
