from typing import List, Dict
from aiohttp import web

from openapi_server.models.render_account_issues_request_payload import RenderAccountIssuesRequestPayload
from openapi_server.models.render_account_issues_response import RenderAccountIssuesResponse
from openapi_server.models.render_product_issues_request_payload import RenderProductIssuesRequestPayload
from openapi_server.models.render_product_issues_response import RenderProductIssuesResponse
from openapi_server import util


async def content_merchantsupport_renderaccountissues(request: web.Request, merchant_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, language_code=None, time_zone=None, body=None) -> web.Response:
    """content_merchantsupport_renderaccountissues

    Provide a list of merchant&#39;s issues with a support content and available actions. This content and actions are meant to be rendered and shown in third-party applications.

    :param merchant_id: Required. The ID of the account to fetch issues for.
    :type merchant_id: str
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
    :param language_code: Optional. The [IETF BCP-47](https://tools.ietf.org/html/bcp47) language code used to localize support content. If not set, the result will be in default language &#x60;en-US&#x60;.
    :type language_code: str
    :param time_zone: Optional. The [IANA](https://www.iana.org/time-zones) timezone used to localize times in support content. For example &#39;America/Los_Angeles&#39;. If not set, results will use as a default UTC.
    :type time_zone: str
    :param body: 
    :type body: dict | bytes

    """
    body = RenderAccountIssuesRequestPayload.from_dict(body)
    return web.Response(status=200)


async def content_merchantsupport_renderproductissues(request: web.Request, merchant_id, product_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, language_code=None, time_zone=None, body=None) -> web.Response:
    """content_merchantsupport_renderproductissues

    Provide a list of issues for merchant&#39;s product with a support content and available actions. This content and actions are meant to be rendered and shown in third-party applications.

    :param merchant_id: Required. The ID of the account that contains the product.
    :type merchant_id: str
    :param product_id: Required. The [REST_ID](https://developers.google.com/shopping-content/reference/rest/v2.1/products#Product.FIELDS.id) of the product to fetch issues for.
    :type product_id: str
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
    :param language_code: Optional. The [IETF BCP-47](https://tools.ietf.org/html/bcp47) language code used to localize support content. If not set, the result will be in default language &#x60;en-US&#x60;.
    :type language_code: str
    :param time_zone: Optional. The [IANA](https://www.iana.org/time-zones) timezone used to localize times in support content. For example &#39;America/Los_Angeles&#39;. If not set, results will use as a default UTC.
    :type time_zone: str
    :param body: 
    :type body: dict | bytes

    """
    body = RenderProductIssuesRequestPayload.from_dict(body)
    return web.Response(status=200)
