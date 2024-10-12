from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_privatecatalog_v1beta1_search_catalogs_response import GoogleCloudPrivatecatalogV1beta1SearchCatalogsResponse
from openapi_server.models.google_cloud_privatecatalog_v1beta1_search_products_response import GoogleCloudPrivatecatalogV1beta1SearchProductsResponse
from openapi_server.models.google_cloud_privatecatalog_v1beta1_search_versions_response import GoogleCloudPrivatecatalogV1beta1SearchVersionsResponse
from openapi_server import util


async def cloudprivatecatalog_organizations_catalogs_search(request: web.Request, resource, xgafv=None, oauth_token=None, param_callback=None, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, page_size=None, page_token=None, query=None) -> web.Response:
    """cloudprivatecatalog_organizations_catalogs_search

    Search Catalog resources that consumers have access to, within the scope of the consumer cloud resource hierarchy context.

    :param resource: Required. The name of the resource context. It can be in following formats:  * &#x60;projects/{project_id}&#x60; * &#x60;folders/{folder_id}&#x60; * &#x60;organizations/{organization_id}&#x60;
    :type resource: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of entries that are requested.
    :type page_size: int
    :param page_token: A pagination token returned from a previous call to SearchCatalogs that indicates where this listing should continue from. This field is optional.
    :type page_token: str
    :param query: The query to filter the catalogs. The supported queries are:  * Get a single catalog: &#x60;name&#x3D;catalogs/{catalog_id}&#x60;
    :type query: str

    """
    return web.Response(status=200)


async def cloudprivatecatalog_organizations_products_search(request: web.Request, resource, xgafv=None, oauth_token=None, param_callback=None, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, page_size=None, page_token=None, query=None) -> web.Response:
    """cloudprivatecatalog_organizations_products_search

    Search Product resources that consumers have access to, within the scope of the consumer cloud resource hierarchy context.

    :param resource: Required. The name of the resource context. See SearchCatalogsRequest.resource for details.
    :type resource: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of entries that are requested.
    :type page_size: int
    :param page_token: A pagination token returned from a previous call to SearchProducts that indicates where this listing should continue from. This field is optional.
    :type page_token: str
    :param query: The query to filter the products.  The supported queries are: * List products of all catalogs: empty * List products under a catalog: &#x60;parent&#x3D;catalogs/{catalog_id}&#x60; * Get a product by name: &#x60;name&#x3D;catalogs/{catalog_id}/products/{product_id}&#x60;
    :type query: str

    """
    return web.Response(status=200)


async def cloudprivatecatalog_organizations_versions_search(request: web.Request, resource, xgafv=None, oauth_token=None, param_callback=None, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, page_size=None, page_token=None, query=None) -> web.Response:
    """cloudprivatecatalog_organizations_versions_search

    Search Version resources that consumers have access to, within the scope of the consumer cloud resource hierarchy context.

    :param resource: Required. The name of the resource context. See SearchCatalogsRequest.resource for details.
    :type resource: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param alt: Data format for response.
    :type alt: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: The maximum number of entries that are requested.
    :type page_size: int
    :param page_token: A pagination token returned from a previous call to SearchVersions that indicates where this listing should continue from. This field is optional.
    :type page_token: str
    :param query: The query to filter the versions. Required.  The supported queries are: * List versions under a product: &#x60;parent&#x3D;catalogs/{catalog_id}/products/{product_id}&#x60; * Get a version by name: &#x60;name&#x3D;catalogs/{catalog_id}/products/{product_id}/versions/{version_id}&#x60;
    :type query: str

    """
    return web.Response(status=200)
