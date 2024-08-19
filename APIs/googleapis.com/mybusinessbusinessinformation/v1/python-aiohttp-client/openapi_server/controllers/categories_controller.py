from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_get_categories_response import BatchGetCategoriesResponse
from openapi_server.models.list_categories_response import ListCategoriesResponse
from openapi_server import util


async def mybusinessbusinessinformation_categories_batch_get(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, language_code=None, names=None, region_code=None, view=None) -> web.Response:
    """mybusinessbusinessinformation_categories_batch_get

    Returns a list of business categories for the provided language and GConcept ids.

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
    :param language_code: Required. The BCP 47 code of language that the category names should be returned in.
    :type language_code: str
    :param names: Required. At least one name must be set. The GConcept ids the localized category names should be returned for. To return details for more than one category, repeat this parameter in the request.
    :type names: List[str]
    :param region_code: Optional. The ISO 3166-1 alpha-2 country code used to infer non-standard language.
    :type region_code: str
    :param view: Required. Specifies which parts to the Category resource should be returned in the response.
    :type view: str

    """
    return web.Response(status=200)


async def mybusinessbusinessinformation_categories_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, language_code=None, page_size=None, page_token=None, region_code=None, view=None) -> web.Response:
    """mybusinessbusinessinformation_categories_list

    Returns a list of business categories. Search will match the category name but not the category ID. Search only matches the front of a category name (that is, &#39;food&#39; may return &#39;Food Court&#39; but not &#39;Fast Food Restaurant&#39;).

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
    :param filter: Optional. Filter string from user. The only field that supported is &#x60;displayName&#x60;. Eg: &#x60;filter&#x3D;displayName&#x3D;foo&#x60;.
    :type filter: str
    :param language_code: Required. The BCP 47 code of language.
    :type language_code: str
    :param page_size: Optional. How many categories to fetch per page. Default is 100, minimum is 1, and maximum page size is 100.
    :type page_size: int
    :param page_token: Optional. If specified, the next page of categories will be fetched.
    :type page_token: str
    :param region_code: Required. The ISO 3166-1 alpha-2 country code.
    :type region_code: str
    :param view: Required. Specifies which parts to the Category resource should be returned in the response.
    :type view: str

    """
    return web.Response(status=200)
