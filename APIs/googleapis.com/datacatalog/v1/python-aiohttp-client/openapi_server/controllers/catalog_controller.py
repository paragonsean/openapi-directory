from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_datacatalog_v1_search_catalog_request import GoogleCloudDatacatalogV1SearchCatalogRequest
from openapi_server.models.google_cloud_datacatalog_v1_search_catalog_response import GoogleCloudDatacatalogV1SearchCatalogResponse
from openapi_server import util


async def datacatalog_catalog_search(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """datacatalog_catalog_search

    Searches Data Catalog for multiple resources like entries and tags that match a query. This is a [Custom Method] (https://cloud.google.com/apis/design/custom_methods) that doesn&#39;t return all information on a resource, only its ID and high level fields. To get more information, you can subsequently call specific get methods. Note: Data Catalog search queries don&#39;t guarantee full recall. Results that match your query might not be returned, even in subsequent result pages. Additionally, returned (and not returned) results can vary if you repeat search queries. For more information, see [Data Catalog search syntax] (https://cloud.google.com/data-catalog/docs/how-to/search-reference).

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
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudDatacatalogV1SearchCatalogRequest.from_dict(body)
    return web.Response(status=200)
