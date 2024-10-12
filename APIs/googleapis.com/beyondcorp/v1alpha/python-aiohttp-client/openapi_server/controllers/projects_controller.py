from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_gateway import AppGateway
from openapi_server.models.connection import Connection
from openapi_server.models.connector import Connector
from openapi_server.models.google_cloud_beyondcorp_appconnections_v1alpha_app_connection import GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection
from openapi_server.models.google_cloud_beyondcorp_appconnections_v1alpha_list_app_connections_response import GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse
from openapi_server.models.google_cloud_beyondcorp_appconnections_v1alpha_resolve_app_connections_response import GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse
from openapi_server.models.google_cloud_beyondcorp_appconnectors_v1alpha_app_connector import GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector
from openapi_server.models.google_cloud_beyondcorp_appconnectors_v1alpha_list_app_connectors_response import GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse
from openapi_server.models.google_cloud_beyondcorp_appconnectors_v1alpha_report_status_request import GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest
from openapi_server.models.google_cloud_beyondcorp_appconnectors_v1alpha_resolve_instance_config_response import GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse
from openapi_server.models.google_cloud_beyondcorp_saasplatform_insights_v1alpha_configured_insight_response import GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse
from openapi_server.models.google_cloud_beyondcorp_saasplatform_insights_v1alpha_list_insights_response import GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse
from openapi_server.models.google_cloud_location_list_locations_response import GoogleCloudLocationListLocationsResponse
from openapi_server.models.google_iam_v1_policy import GoogleIamV1Policy
from openapi_server.models.google_iam_v1_set_iam_policy_request import GoogleIamV1SetIamPolicyRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_request import GoogleIamV1TestIamPermissionsRequest
from openapi_server.models.google_iam_v1_test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server.models.list_app_gateways_response import ListAppGatewaysResponse
from openapi_server.models.list_connections_response import ListConnectionsResponse
from openapi_server.models.list_connectors_response import ListConnectorsResponse
from openapi_server.models.report_status_request import ReportStatusRequest
from openapi_server.models.resolve_connections_response import ResolveConnectionsResponse
from openapi_server.models.resolve_instance_config_response import ResolveInstanceConfigResponse
from openapi_server import util


async def beyondcorp_projects_locations_app_connections_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, app_connection_id=None, request_id=None, validate_only=None, body=None) -> web.Response:
    """beyondcorp_projects_locations_app_connections_create

    Creates a new AppConnection in a given project and location.

    :param parent: Required. The resource project name of the AppConnection location using the form: &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param app_connection_id: Optional. User-settable AppConnection resource ID. * Must start with a letter. * Must contain between 4-63 characters from &#x60;/a-z-/&#x60;. * Must end with a number or a letter.
    :type app_connection_id: str
    :param request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param validate_only: Optional. If set, validates request by executing a dry-run which would not alter the resource in any way.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_projects_locations_app_connections_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """beyondcorp_projects_locations_app_connections_list

    Lists AppConnections in a given project and location.

    :param parent: Required. The resource name of the AppConnection location using the form: &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param filter: Optional. A filter specifying constraints of a list operation.
    :type filter: str
    :param order_by: Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.
    :type order_by: str
    :param page_size: Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous ListAppConnectionsRequest, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_app_connections_resolve(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, app_connector_id=None, page_size=None, page_token=None) -> web.Response:
    """beyondcorp_projects_locations_app_connections_resolve

    Resolves AppConnections details for a given AppConnector. An internal method called by a connector to find AppConnections to connect to.

    :param parent: Required. The resource name of the AppConnection location using the form: &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param app_connector_id: Required. BeyondCorp Connector name of the connector associated with those AppConnections using the form: &#x60;projects/{project_id}/locations/{location_id}/appConnectors/{app_connector_id}&#x60;
    :type app_connector_id: str
    :param page_size: Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous ResolveAppConnectionsResponse, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_app_connectors_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, app_connector_id=None, request_id=None, validate_only=None, body=None) -> web.Response:
    """beyondcorp_projects_locations_app_connectors_create

    Creates a new AppConnector in a given project and location.

    :param parent: Required. The resource project name of the AppConnector location using the form: &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param app_connector_id: Optional. User-settable AppConnector resource ID. * Must start with a letter. * Must contain between 4-63 characters from &#x60;/a-z-/&#x60;. * Must end with a number or a letter.
    :type app_connector_id: str
    :param request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param validate_only: Optional. If set, validates request by executing a dry-run which would not alter the resource in any way.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_projects_locations_app_connectors_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """beyondcorp_projects_locations_app_connectors_list

    Lists AppConnectors in a given project and location.

    :param parent: Required. The resource name of the AppConnector location using the form: &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param filter: Optional. A filter specifying constraints of a list operation.
    :type filter: str
    :param order_by: Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.
    :type order_by: str
    :param page_size: Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous ListAppConnectorsRequest, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_app_connectors_report_status(request: web.Request, app_connector, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """beyondcorp_projects_locations_app_connectors_report_status

    Report status for a given connector.

    :param app_connector: Required. BeyondCorp Connector name using the form: &#x60;projects/{project_id}/locations/{location_id}/connectors/{connector}&#x60;
    :type app_connector: str
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
    body = GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_projects_locations_app_connectors_resolve_instance_config(request: web.Request, app_connector, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """beyondcorp_projects_locations_app_connectors_resolve_instance_config

    Gets instance configuration for a given AppConnector. An internal method called by a AppConnector to get its container config.

    :param app_connector: Required. BeyondCorp AppConnector name using the form: &#x60;projects/{project_id}/locations/{location_id}/appConnectors/{app_connector}&#x60;
    :type app_connector: str
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


async def beyondcorp_projects_locations_app_gateways_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, app_gateway_id=None, request_id=None, validate_only=None, body=None) -> web.Response:
    """beyondcorp_projects_locations_app_gateways_create

    Creates a new AppGateway in a given project and location.

    :param parent: Required. The resource project name of the AppGateway location using the form: &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param app_gateway_id: Optional. User-settable AppGateway resource ID. * Must start with a letter. * Must contain between 4-63 characters from &#x60;/a-z-/&#x60;. * Must end with a number or a letter.
    :type app_gateway_id: str
    :param request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param validate_only: Optional. If set, validates request by executing a dry-run which would not alter the resource in any way.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = AppGateway.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_projects_locations_app_gateways_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """beyondcorp_projects_locations_app_gateways_list

    Lists AppGateways in a given project and location.

    :param parent: Required. The resource name of the AppGateway location using the form: &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param filter: Optional. A filter specifying constraints of a list operation.
    :type filter: str
    :param order_by: Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.
    :type order_by: str
    :param page_size: Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous ListAppGatewaysRequest, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_connections_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, connection_id=None, request_id=None, validate_only=None, body=None) -> web.Response:
    """beyondcorp_projects_locations_connections_create

    Creates a new Connection in a given project and location.

    :param parent: Required. The resource project name of the connection location using the form: &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param connection_id: Optional. User-settable connection resource ID. * Must start with a letter. * Must contain between 4-63 characters from &#x60;/a-z-/&#x60;. * Must end with a number or a letter.
    :type connection_id: str
    :param request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param validate_only: Optional. If set, validates request by executing a dry-run which would not alter the resource in any way.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Connection.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_projects_locations_connections_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """beyondcorp_projects_locations_connections_list

    Lists Connections in a given project and location.

    :param parent: Required. The resource name of the connection location using the form: &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param filter: Optional. A filter specifying constraints of a list operation.
    :type filter: str
    :param order_by: Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.
    :type order_by: str
    :param page_size: Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous ListConnectionsRequest, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_connections_resolve(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, connector_id=None, page_size=None, page_token=None) -> web.Response:
    """beyondcorp_projects_locations_connections_resolve

    Resolves connections details for a given connector. An internal method called by a connector to find connections to connect to.

    :param parent: Required. The resource name of the connection location using the form: &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param connector_id: Required. BeyondCorp Connector name of the connector associated with those connections using the form: &#x60;projects/{project_id}/locations/{location_id}/connectors/{connector_id}&#x60;
    :type connector_id: str
    :param page_size: Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous ResolveConnectionsResponse, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_connectors_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, connector_id=None, request_id=None, validate_only=None, body=None) -> web.Response:
    """beyondcorp_projects_locations_connectors_create

    Creates a new Connector in a given project and location.

    :param parent: Required. The resource project name of the connector location using the form: &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param connector_id: Optional. User-settable connector resource ID. * Must start with a letter. * Must contain between 4-63 characters from &#x60;/a-z-/&#x60;. * Must end with a number or a letter.
    :type connector_id: str
    :param request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param validate_only: Optional. If set, validates request by executing a dry-run which would not alter the resource in any way.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Connector.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_projects_locations_connectors_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """beyondcorp_projects_locations_connectors_list

    Lists Connectors in a given project and location.

    :param parent: Required. The resource name of the connector location using the form: &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param filter: Optional. A filter specifying constraints of a list operation.
    :type filter: str
    :param order_by: Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.
    :type order_by: str
    :param page_size: Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous ListConnectorsRequest, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_connectors_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, request_id=None, update_mask=None, validate_only=None, body=None) -> web.Response:
    """beyondcorp_projects_locations_connectors_patch

    Updates the parameters of a single Connector.

    :param name: Required. Unique resource name of the connector. The name is ignored when creating a connector.
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
    :param request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param update_mask: Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include these fields from [BeyondCorp.Connector]: * &#x60;labels&#x60; * &#x60;display_name&#x60;
    :type update_mask: str
    :param validate_only: Optional. If set, validates request by executing a dry-run which would not alter the resource in any way.
    :type validate_only: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Connector.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_projects_locations_connectors_report_status(request: web.Request, connector, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """beyondcorp_projects_locations_connectors_report_status

    Report status for a given connector.

    :param connector: Required. BeyondCorp Connector name using the form: &#x60;projects/{project_id}/locations/{location_id}/connectors/{connector}&#x60;
    :type connector: str
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
    body = ReportStatusRequest.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_projects_locations_connectors_resolve_instance_config(request: web.Request, connector, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """beyondcorp_projects_locations_connectors_resolve_instance_config

    Gets instance configuration for a given connector. An internal method called by a connector to get its container config.

    :param connector: Required. BeyondCorp Connector name using the form: &#x60;projects/{project_id}/locations/{location_id}/connectors/{connector}&#x60;
    :type connector: str
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


async def beyondcorp_projects_locations_insights_configured_insight(request: web.Request, insight, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, aggregation=None, custom_grouping_field_filter=None, custom_grouping_group_fields=None, end_time=None, field_filter=None, group=None, page_size=None, page_token=None, start_time=None) -> web.Response:
    """beyondcorp_projects_locations_insights_configured_insight

    Gets the value for a selected particular insight based on the provided filters. Use the organization level path for fetching at org level and project level path for fetching the insight value specific to a particular project.

    :param insight: Required. The resource name of the insight using the form: &#x60;organizations/{organization_id}/locations/{location_id}/insights/{insight_id}&#x60; &#x60;projects/{project_id}/locations/{location_id}/insights/{insight_id}&#x60;.
    :type insight: str
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
    :param aggregation: Required. Aggregation type. Available aggregation could be fetched by calling insight list and get APIs in &#x60;BASIC&#x60; view.
    :type aggregation: str
    :param custom_grouping_field_filter: Optional. Filterable parameters to be added to the grouping clause. Available fields could be fetched by calling insight list and get APIs in &#x60;BASIC&#x60; view. &#x60;&#x3D;&#x60; is the only comparison operator supported. &#x60;AND&#x60; is the only logical operator supported. Usage: field_filter&#x3D;\&quot;fieldName1&#x3D;fieldVal1 AND fieldName2&#x3D;fieldVal2\&quot;. NOTE: Only &#x60;AND&#x60; conditions are allowed. NOTE: Use the &#x60;filter_alias&#x60; from &#x60;Insight.Metadata.Field&#x60; message for the filtering the corresponding fields in this filter field. (These expressions are based on the filter language described at https://google.aip.dev/160).
    :type custom_grouping_field_filter: str
    :param custom_grouping_group_fields: Required. Fields to be used for grouping. NOTE: Use the &#x60;filter_alias&#x60; from &#x60;Insight.Metadata.Field&#x60; message for declaring the fields to be grouped-by here.
    :type custom_grouping_group_fields: List[str]
    :param end_time: Required. Ending time for the duration for which insight is to be pulled.
    :type end_time: str
    :param field_filter: Optional. Other filterable/configurable parameters as applicable to the selected insight. Available fields could be fetched by calling insight list and get APIs in &#x60;BASIC&#x60; view. &#x60;&#x3D;&#x60; is the only comparison operator supported. &#x60;AND&#x60; is the only logical operator supported. Usage: field_filter&#x3D;\&quot;fieldName1&#x3D;fieldVal1 AND fieldName2&#x3D;fieldVal2\&quot;. NOTE: Only &#x60;AND&#x60; conditions are allowed. NOTE: Use the &#x60;filter_alias&#x60; from &#x60;Insight.Metadata.Field&#x60; message for the filtering the corresponding fields in this filter field. (These expressions are based on the filter language described at https://google.aip.dev/160).
    :type field_filter: str
    :param group: Optional. Group id of the available groupings for the insight. Available groupings could be fetched by calling insight list and get APIs in &#x60;BASIC&#x60; view.
    :type group: str
    :param page_size: Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.
    :type page_size: int
    :param page_token: Optional. Used to fetch the page represented by the token. Fetches the first page when not set.
    :type page_token: str
    :param start_time: Required. Starting time for the duration for which insight is to be pulled.
    :type start_time: str

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_insights_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, view=None) -> web.Response:
    """beyondcorp_projects_locations_insights_list

    Lists for all the available insights that could be fetched from the system. Allows to filter using category. Setting the &#x60;view&#x60; to &#x60;BASIC&#x60; will let you iterate over the list of insight metadatas.

    :param parent: Required. The resource name of InsightMetadata using the form: &#x60;organizations/{organization_id}/locations/{location}&#x60; &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param filter: Optional. Filter expression to restrict the insights returned. Supported filter fields: * &#x60;type&#x60; * &#x60;category&#x60; * &#x60;subCategory&#x60; Examples: * \&quot;category &#x3D; application AND type &#x3D; count\&quot; * \&quot;category &#x3D; application AND subCategory &#x3D; iap\&quot; * \&quot;type &#x3D; status\&quot; Allowed values: * type: [count, latency, status, list] * category: [application, device, request, security] * subCategory: [iap, webprotect] NOTE: Only equality based comparison is allowed. Only &#x60;AND&#x60; conjunction is allowed. NOTE: The &#39;AND&#39; in the filter field needs to be in capital letters only. NOTE: Just filtering on &#x60;subCategory&#x60; is not allowed. It should be passed in with the parent &#x60;category&#x60; too. (These expressions are based on the filter language described at https://google.aip.dev/160).
    :type filter: str
    :param order_by: Optional. Hint for how to order the results. This is currently ignored.
    :type order_by: str
    :param page_size: Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. NOTE: Default page size is 50.
    :type page_size: int
    :param page_token: Optional. A token identifying a page of results the server should return.
    :type page_token: str
    :param view: Required. List only metadata or full data.
    :type view: str

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """beyondcorp_projects_locations_list

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


async def beyondcorp_projects_locations_net_connections_get_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, options_requested_policy_version=None) -> web.Response:
    """beyondcorp_projects_locations_net_connections_get_iam_policy

    Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

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
    :param options_requested_policy_version: Optional. The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).
    :type options_requested_policy_version: int

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_net_connections_set_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """beyondcorp_projects_locations_net_connections_set_iam_policy

    Sets the access control policy on the specified resource. Replaces any existing policy. Can return &#x60;NOT_FOUND&#x60;, &#x60;INVALID_ARGUMENT&#x60;, and &#x60;PERMISSION_DENIED&#x60; errors.

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
    body = GoogleIamV1SetIamPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_projects_locations_net_connections_test_iam_permissions(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """beyondcorp_projects_locations_net_connections_test_iam_permissions

    Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a &#x60;NOT_FOUND&#x60; error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may \&quot;fail open\&quot; without warning.

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
    body = GoogleIamV1TestIamPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def beyondcorp_projects_locations_operations_cancel(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """beyondcorp_projects_locations_operations_cancel

    Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn&#39;t support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to &#x60;Code.CANCELLED&#x60;.

    :param name: The name of the operation resource to be cancelled.
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
    :type body: 

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_operations_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, request_id=None, validate_only=None) -> web.Response:
    """beyondcorp_projects_locations_operations_delete

    Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn&#39;t support this method, it returns &#x60;google.rpc.Code.UNIMPLEMENTED&#x60;.

    :param name: The name of the operation resource to be deleted.
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
    :param request_id: Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    :type request_id: str
    :param validate_only: Optional. If set, validates request by executing a dry-run which would not alter the resource in any way.
    :type validate_only: bool

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_operations_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, view=None) -> web.Response:
    """beyondcorp_projects_locations_operations_get

    Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

    :param name: The name of the operation resource.
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
    :param view: Required. Metadata only or full data view.
    :type view: str

    """
    return web.Response(status=200)


async def beyondcorp_projects_locations_operations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """beyondcorp_projects_locations_operations_list

    Lists operations that match the specified filter in the request. If the server doesn&#39;t support this method, it returns &#x60;UNIMPLEMENTED&#x60;.

    :param name: The name of the operation&#39;s parent resource.
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
    :param filter: The standard list filter.
    :type filter: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str

    """
    return web.Response(status=200)
