from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint import Endpoint
from openapi_server.models.get_iam_policy_request import GetIamPolicyRequest
from openapi_server.models.list_endpoints_response import ListEndpointsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_namespaces_response import ListNamespacesResponse
from openapi_server.models.list_services_response import ListServicesResponse
from openapi_server.models.namespace import Namespace
from openapi_server.models.policy import Policy
from openapi_server.models.resolve_service_request import ResolveServiceRequest
from openapi_server.models.resolve_service_response import ResolveServiceResponse
from openapi_server.models.service import Service
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server import util


async def servicedirectory_projects_locations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """servicedirectory_projects_locations_list

    Lists information about the supported locations for this service.

    :param name: The resource that owns the locations collection, if applicable.
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
    :param filter: A filter to narrow down results to a preferred subset. The filtering language accepts strings like &#x60;\&quot;displayName&#x3D;tokyo\&quot;&#x60;, and is documented in more detail in [AIP-160](https://google.aip.dev/160).
    :type filter: str
    :param page_size: The maximum number of results to return. If not set, the service selects a default.
    :type page_size: int
    :param page_token: A page token received from the &#x60;next_page_token&#x60; field in the response. Send that page token to receive the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def servicedirectory_projects_locations_namespaces_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, namespace_id=None, body=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_create

    Creates a namespace, and returns the new namespace.

    :param parent: Required. The resource name of the project and location the namespace will be created in.
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
    :param namespace_id: Required. The Resource ID must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression &#x60;[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?&#x60; which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
    :type namespace_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Namespace.from_dict(body)
    return web.Response(status=200)


async def servicedirectory_projects_locations_namespaces_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_list

    Lists all namespaces.

    :param parent: Required. The resource name of the project and location whose namespaces you&#39;d like to list.
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
    :param filter: Optional. The filter to list results by. General &#x60;filter&#x60; string syntax: &#x60; ()&#x60; * &#x60;&#x60; can be &#x60;name&#x60; or &#x60;labels.&#x60; for map field * &#x60;&#x60; can be &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&#x3D;&#x60;, &#x60;:&#x60;. Of which &#x60;:&#x60; means &#x60;HAS&#x60;, and is roughly the same as &#x60;&#x3D;&#x60; * &#x60;&#x60; must be the same data type as field * &#x60;&#x60; can be &#x60;AND&#x60;, &#x60;OR&#x60;, &#x60;NOT&#x60; Examples of valid filters: * &#x60;labels.owner&#x60; returns namespaces that have a label with the key &#x60;owner&#x60;, this is the same as &#x60;labels:owner&#x60; * &#x60;labels.owner&#x3D;sd&#x60; returns namespaces that have key/value &#x60;owner&#x3D;sd&#x60; * &#x60;name&gt;projects/my-project/locations/us-east1/namespaces/namespace-c&#x60; returns namespaces that have name that is alphabetically later than the string, so \&quot;namespace-e\&quot; is returned but \&quot;namespace-a\&quot; is not * &#x60;labels.owner!&#x3D;sd AND labels.foo&#x3D;bar&#x60; returns namespaces that have &#x60;owner&#x60; in label key but value is not &#x60;sd&#x60; AND have key/value &#x60;foo&#x3D;bar&#x60; * &#x60;doesnotexist.foo&#x3D;bar&#x60; returns an empty list. Note that namespace doesn&#39;t have a field called \&quot;doesnotexist\&quot;. Since the filter does not match any namespaces, it returns no results For more information about filtering, see [API Filtering](https://aip.dev/160).
    :type filter: str
    :param order_by: Optional. The order to list results by. General &#x60;order_by&#x60; string syntax: &#x60; () (,)&#x60; * &#x60;&#x60; allows value: &#x60;name&#x60; * &#x60;&#x60; ascending or descending order by &#x60;&#x60;. If this is left blank, &#x60;asc&#x60; is used Note that an empty &#x60;order_by&#x60; string results in default order, which is order by &#x60;name&#x60; in ascending order.
    :type order_by: str
    :param page_size: Optional. The maximum number of items to return.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def servicedirectory_projects_locations_namespaces_services_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, service_id=None, body=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_services_create

    Creates a service, and returns the new service.

    :param parent: Required. The resource name of the namespace this service will belong to.
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
    :param service_id: Required. The Resource ID must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression &#x60;[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?&#x60; which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
    :type service_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Service.from_dict(body)
    return web.Response(status=200)


async def servicedirectory_projects_locations_namespaces_services_endpoints_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, endpoint_id=None, body=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_services_endpoints_create

    Creates an endpoint, and returns the new endpoint.

    :param parent: Required. The resource name of the service that this endpoint provides.
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
    :param endpoint_id: Required. The Resource ID must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression &#x60;[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?&#x60; which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
    :type endpoint_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Endpoint.from_dict(body)
    return web.Response(status=200)


async def servicedirectory_projects_locations_namespaces_services_endpoints_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_services_endpoints_delete

    Deletes an endpoint.

    :param name: Required. The name of the endpoint to delete.
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


async def servicedirectory_projects_locations_namespaces_services_endpoints_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_services_endpoints_get

    Gets an endpoint.

    :param name: Required. The name of the endpoint to get.
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


async def servicedirectory_projects_locations_namespaces_services_endpoints_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_services_endpoints_list

    Lists all endpoints.

    :param parent: Required. The resource name of the service whose endpoints you&#39;d like to list.
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
    :param filter: Optional. The filter to list results by. General &#x60;filter&#x60; string syntax: &#x60; ()&#x60; * &#x60;&#x60; can be &#x60;name&#x60;, &#x60;address&#x60;, &#x60;port&#x60;, or &#x60;annotations.&#x60; for map field * &#x60;&#x60; can be &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&#x3D;&#x60;, &#x60;:&#x60;. Of which &#x60;:&#x60; means &#x60;HAS&#x60;, and is roughly the same as &#x60;&#x3D;&#x60; * &#x60;&#x60; must be the same data type as field * &#x60;&#x60; can be &#x60;AND&#x60;, &#x60;OR&#x60;, &#x60;NOT&#x60; Examples of valid filters: * &#x60;annotations.owner&#x60; returns endpoints that have a annotation with the key &#x60;owner&#x60;, this is the same as &#x60;annotations:owner&#x60; * &#x60;annotations.protocol&#x3D;gRPC&#x60; returns endpoints that have key/value &#x60;protocol&#x3D;gRPC&#x60; * &#x60;address&#x3D;192.108.1.105&#x60; returns endpoints that have this address * &#x60;port&gt;8080&#x60; returns endpoints that have port number larger than 8080 * &#x60;name&gt;projects/my-project/locations/us-east1/namespaces/my-namespace/services/my-service/endpoints/endpoint-c&#x60; returns endpoints that have name that is alphabetically later than the string, so \&quot;endpoint-e\&quot; is returned but \&quot;endpoint-a\&quot; is not * &#x60;annotations.owner!&#x3D;sd AND annotations.foo&#x3D;bar&#x60; returns endpoints that have &#x60;owner&#x60; in annotation key but value is not &#x60;sd&#x60; AND have key/value &#x60;foo&#x3D;bar&#x60; * &#x60;doesnotexist.foo&#x3D;bar&#x60; returns an empty list. Note that endpoint doesn&#39;t have a field called \&quot;doesnotexist\&quot;. Since the filter does not match any endpoints, it returns no results For more information about filtering, see [API Filtering](https://aip.dev/160).
    :type filter: str
    :param order_by: Optional. The order to list results by. General &#x60;order_by&#x60; string syntax: &#x60; () (,)&#x60; * &#x60;&#x60; allows values: &#x60;name&#x60;, &#x60;address&#x60;, &#x60;port&#x60; * &#x60;&#x60; ascending or descending order by &#x60;&#x60;. If this is left blank, &#x60;asc&#x60; is used Note that an empty &#x60;order_by&#x60; string results in default order, which is order by &#x60;name&#x60; in ascending order.
    :type order_by: str
    :param page_size: Optional. The maximum number of items to return.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def servicedirectory_projects_locations_namespaces_services_endpoints_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_services_endpoints_patch

    Updates an endpoint.

    :param name: Immutable. The resource name for the endpoint in the format &#x60;projects/*/locations/*/namespaces/*/services/*/endpoints/*&#x60;.
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
    :param update_mask: Required. List of fields to be updated in this request.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Endpoint.from_dict(body)
    return web.Response(status=200)


async def servicedirectory_projects_locations_namespaces_services_get_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_services_get_iam_policy

    Gets the IAM Policy for a resource (namespace or service only).

    :param resource: REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
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
    body = GetIamPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def servicedirectory_projects_locations_namespaces_services_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_services_list

    Lists all services belonging to a namespace.

    :param parent: Required. The resource name of the namespace whose services you&#39;d like to list.
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
    :param filter: Optional. The filter to list results by. General &#x60;filter&#x60; string syntax: &#x60; ()&#x60; * &#x60;&#x60; can be &#x60;name&#x60; or &#x60;annotations.&#x60; for map field * &#x60;&#x60; can be &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&#x3D;&#x60;, &#x60;:&#x60;. Of which &#x60;:&#x60; means &#x60;HAS&#x60;, and is roughly the same as &#x60;&#x3D;&#x60; * &#x60;&#x60; must be the same data type as field * &#x60;&#x60; can be &#x60;AND&#x60;, &#x60;OR&#x60;, &#x60;NOT&#x60; Examples of valid filters: * &#x60;annotations.owner&#x60; returns services that have a annotation with the key &#x60;owner&#x60;, this is the same as &#x60;annotations:owner&#x60; * &#x60;annotations.protocol&#x3D;gRPC&#x60; returns services that have key/value &#x60;protocol&#x3D;gRPC&#x60; * &#x60;name&gt;projects/my-project/locations/us-east1/namespaces/my-namespace/services/service-c&#x60; returns services that have name that is alphabetically later than the string, so \&quot;service-e\&quot; is returned but \&quot;service-a\&quot; is not * &#x60;annotations.owner!&#x3D;sd AND annotations.foo&#x3D;bar&#x60; returns services that have &#x60;owner&#x60; in annotation key but value is not &#x60;sd&#x60; AND have key/value &#x60;foo&#x3D;bar&#x60; * &#x60;doesnotexist.foo&#x3D;bar&#x60; returns an empty list. Note that service doesn&#39;t have a field called \&quot;doesnotexist\&quot;. Since the filter does not match any services, it returns no results For more information about filtering, see [API Filtering](https://aip.dev/160).
    :type filter: str
    :param order_by: Optional. The order to list results by. General &#x60;order_by&#x60; string syntax: &#x60; () (,)&#x60; * &#x60;&#x60; allows value: &#x60;name&#x60; * &#x60;&#x60; ascending or descending order by &#x60;&#x60;. If this is left blank, &#x60;asc&#x60; is used Note that an empty &#x60;order_by&#x60; string results in default order, which is order by &#x60;name&#x60; in ascending order.
    :type order_by: str
    :param page_size: Optional. The maximum number of items to return.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def servicedirectory_projects_locations_namespaces_services_resolve(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_services_resolve

    Returns a service and its associated endpoints. Resolving a service is not considered an active developer method.

    :param name: Required. The name of the service to resolve.
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
    :param body: 
    :type body: dict | bytes

    """
    body = ResolveServiceRequest.from_dict(body)
    return web.Response(status=200)


async def servicedirectory_projects_locations_namespaces_services_set_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_services_set_iam_policy

    Sets the IAM Policy for a resource (namespace or service only).

    :param resource: REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
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
    body = SetIamPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def servicedirectory_projects_locations_namespaces_services_test_iam_permissions(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """servicedirectory_projects_locations_namespaces_services_test_iam_permissions

    Tests IAM permissions for a resource (namespace or service only).

    :param resource: REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
    :type resource: str
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
    body = TestIamPermissionsRequest.from_dict(body)
    return web.Response(status=200)
