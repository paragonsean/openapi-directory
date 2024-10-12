from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_factchecking_factchecktools_v1alpha1_fact_checked_claim_search_response import GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse
from openapi_server import util


async def factchecktools_claims_search(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, language_code=None, max_age_days=None, offset=None, page_size=None, page_token=None, query=None, review_publisher_site_filter=None) -> web.Response:
    """factchecktools_claims_search

    Search through fact-checked claims.

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
    :param language_code: The BCP-47 language code, such as \&quot;en-US\&quot; or \&quot;sr-Latn\&quot;. Can be used to restrict results by language, though we do not currently consider the region.
    :type language_code: str
    :param max_age_days: The maximum age of the returned search results, in days. Age is determined by either claim date or review date, whichever is newer.
    :type max_age_days: int
    :param offset: An integer that specifies the current offset (that is, starting result location) in search results. This field is only considered if &#x60;page_token&#x60; is unset. For example, 0 means to return results starting from the first matching result, and 10 means to return from the 11th result.
    :type offset: int
    :param page_size: The pagination size. We will return up to that many results. Defaults to 10 if not set.
    :type page_size: int
    :param page_token: The pagination token. You may provide the &#x60;next_page_token&#x60; returned from a previous List request, if any, in order to get the next page. All other fields must have the same values as in the previous request.
    :type page_token: str
    :param query: Textual query string. Required unless &#x60;review_publisher_site_filter&#x60; is specified.
    :type query: str
    :param review_publisher_site_filter: The review publisher site to filter results by, e.g. nytimes.com.
    :type review_publisher_site_filter: str

    """
    return web.Response(status=200)
