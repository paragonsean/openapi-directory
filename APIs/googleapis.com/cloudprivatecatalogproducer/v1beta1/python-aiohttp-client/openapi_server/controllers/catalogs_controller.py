from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_association import GoogleCloudPrivatecatalogproducerV1beta1Association
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_catalog import GoogleCloudPrivatecatalogproducerV1beta1Catalog
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_copy_product_request import GoogleCloudPrivatecatalogproducerV1beta1CopyProductRequest
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_create_association_request import GoogleCloudPrivatecatalogproducerV1beta1CreateAssociationRequest
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_list_associations_response import GoogleCloudPrivatecatalogproducerV1beta1ListAssociationsResponse
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_list_catalogs_response import GoogleCloudPrivatecatalogproducerV1beta1ListCatalogsResponse
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_list_products_response import GoogleCloudPrivatecatalogproducerV1beta1ListProductsResponse
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_list_versions_response import GoogleCloudPrivatecatalogproducerV1beta1ListVersionsResponse
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_product import GoogleCloudPrivatecatalogproducerV1beta1Product
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_upload_icon_request import GoogleCloudPrivatecatalogproducerV1beta1UploadIconRequest
from openapi_server.models.google_cloud_privatecatalogproducer_v1beta1_version import GoogleCloudPrivatecatalogproducerV1beta1Version
from openapi_server.models.google_iam_v1_policy import GoogleIamV1Policy
from openapi_server.models.google_iam_v1_set_iam_policy_request import GoogleIamV1SetIamPolicyRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_request import GoogleIamV1TestIamPermissionsRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server import util


async def cloudprivatecatalogproducer_catalogs_associations_create(request: web.Request, parent, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, body=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_associations_create

    Creates an Association instance under a given Catalog.

    :param parent: The &#x60;Catalog&#x60; resource&#39;s name.
    :type parent: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudPrivatecatalogproducerV1beta1CreateAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_associations_list(request: web.Request, parent, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, page_size=None, page_token=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_associations_list

    Lists all Association resources under a catalog.

    :param parent: The resource name of the &#x60;Catalog&#x60; whose &#x60;Associations&#x60; are being retrieved. In the format &#x60;catalogs/&lt;catalog&gt;&#x60;.
    :type parent: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param page_size: The maximum number of catalog associations to return.
    :type page_size: int
    :param page_token: A pagination token returned from the previous call to &#x60;ListAssociations&#x60;.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_create(request: web.Request, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, body=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_create

    Creates a new Catalog resource.

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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudPrivatecatalogproducerV1beta1Catalog.from_dict(body)
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_get_iam_policy(request: web.Request, resource, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, options_requested_policy_version=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_get_iam_policy

    Gets IAM policy for the specified Catalog.

    :param resource: REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.
    :type resource: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param options_requested_policy_version: Optional. The policy format version to be returned.  Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected.  Requests for policies with any conditional bindings must specify version 3. Policies without any conditional bindings may specify any valid value or leave the field unset.
    :type options_requested_policy_version: int

    """
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_list(request: web.Request, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, page_size=None, page_token=None, parent=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_list

    Lists Catalog resources that the producer has access to, within the scope of the parent resource.

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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param page_size: The maximum number of catalogs to return.
    :type page_size: int
    :param page_token: A pagination token returned from a previous call to ListCatalogs that indicates where this listing should continue from. This field is optional.
    :type page_token: str
    :param parent: The resource name of the parent resource.
    :type parent: str

    """
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_products_copy(request: web.Request, name, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, body=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_products_copy

    Copies a Product under another Catalog.

    :param name: The resource name of the current product that is copied from.
    :type name: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudPrivatecatalogproducerV1beta1CopyProductRequest.from_dict(body)
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_products_create(request: web.Request, parent, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, body=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_products_create

    Creates a Product instance under a given Catalog.

    :param parent: The catalog name of the new product&#39;s parent.
    :type parent: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudPrivatecatalogproducerV1beta1Product.from_dict(body)
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_products_icons_upload(request: web.Request, product, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, body=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_products_icons_upload

    Creates an Icon instance under a given Product. If Product only has a default icon, a new Icon instance is created and associated with the given Product. If Product already has a non-default icon, the action creates a new Icon instance, associates the newly created Icon with the given Product and deletes the old icon.

    :param product: The resource name of the product.
    :type product: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudPrivatecatalogproducerV1beta1UploadIconRequest.from_dict(body)
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_products_list(request: web.Request, parent, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_products_list

    Lists Product resources that the producer has access to, within the scope of the parent catalog.

    :param parent: The resource name of the parent resource.
    :type parent: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param filter: A filter expression used to restrict the returned results based upon properties of the product.
    :type filter: str
    :param page_size: The maximum number of products to return.
    :type page_size: int
    :param page_token: A pagination token returned from a previous call to ListProducts that indicates where this listing should continue from. This field is optional.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_products_versions_create(request: web.Request, parent, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, body=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_products_versions_create

    Creates a Version instance under a given Product.

    :param parent: The product name of the new version&#39;s parent.
    :type parent: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudPrivatecatalogproducerV1beta1Version.from_dict(body)
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_products_versions_delete(request: web.Request, name, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, force=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_products_versions_delete

    Hard deletes a Version.

    :param name: The resource name of the version.
    :type name: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param force: Forces deletion of the &#x60;Catalog&#x60; and its &#x60;Association&#x60; resources. If the &#x60;Catalog&#x60; is still associated with other resources and force is not set to true, then the operation fails.
    :type force: bool

    """
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_products_versions_get(request: web.Request, name, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_products_versions_get

    Returns the requested Version resource.

    :param name: The resource name of the version.
    :type name: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str

    """
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_products_versions_list(request: web.Request, parent, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, page_size=None, page_token=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_products_versions_list

    Lists Version resources that the producer has access to, within the scope of the parent Product.

    :param parent: The resource name of the parent resource.
    :type parent: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param page_size: The maximum number of versions to return.
    :type page_size: int
    :param page_token: A pagination token returned from a previous call to ListVersions that indicates where this listing should continue from. This field is optional.
    :type page_token: str

    """
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_products_versions_patch(request: web.Request, name, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, update_mask=None, body=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_products_versions_patch

    Updates a specific Version resource.

    :param name: Required. The resource name of the version, in the format &#x60;catalogs/{catalog_id}/products/{product_id}/versions/a-z*[a-z0-9]&#39;.  A unique identifier for the version under a product, which can&#39;t be changed after the version is created. The final segment of the name must between 1 and 63 characters in length.
    :type name: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param update_mask: Field mask that controls which fields of the version should be updated.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudPrivatecatalogproducerV1beta1Version.from_dict(body)
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_set_iam_policy(request: web.Request, resource, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, body=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_set_iam_policy

    Sets the IAM policy for the specified Catalog.

    :param resource: REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.
    :type resource: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleIamV1SetIamPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_test_iam_permissions(request: web.Request, resource, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, body=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_test_iam_permissions

    Tests the IAM permissions for the specified Catalog.

    :param resource: REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.
    :type resource: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleIamV1TestIamPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def cloudprivatecatalogproducer_catalogs_undelete(request: web.Request, name, alt=None, key=None, access_token=None, upload_protocol=None, pretty_print=None, quota_user=None, fields=None, upload_type=None, xgafv=None, oauth_token=None, param_callback=None, body=None) -> web.Response:
    """cloudprivatecatalogproducer_catalogs_undelete

    Undeletes a deleted Catalog and all resources under it.

    :param name: The resource name of the catalog.
    :type name: str
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
    :param xgafv: V1 error format.
    :type xgafv: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param param_callback: JSONP
    :type param_callback: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)
