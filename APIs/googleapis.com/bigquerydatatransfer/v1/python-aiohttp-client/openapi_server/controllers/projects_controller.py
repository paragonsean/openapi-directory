from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_valid_creds_response import CheckValidCredsResponse
from openapi_server.models.enroll_data_sources_request import EnrollDataSourcesRequest
from openapi_server.models.list_data_sources_response import ListDataSourcesResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_transfer_configs_response import ListTransferConfigsResponse
from openapi_server.models.list_transfer_logs_response import ListTransferLogsResponse
from openapi_server.models.list_transfer_runs_response import ListTransferRunsResponse
from openapi_server.models.schedule_transfer_runs_request import ScheduleTransferRunsRequest
from openapi_server.models.schedule_transfer_runs_response import ScheduleTransferRunsResponse
from openapi_server.models.start_manual_transfer_runs_request import StartManualTransferRunsRequest
from openapi_server.models.start_manual_transfer_runs_response import StartManualTransferRunsResponse
from openapi_server.models.transfer_config import TransferConfig
from openapi_server.models.transfer_run import TransferRun
from openapi_server.models.unenroll_data_sources_request import UnenrollDataSourcesRequest
from openapi_server import util


async def bigquerydatatransfer_projects_locations_data_sources_check_valid_creds(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """bigquerydatatransfer_projects_locations_data_sources_check_valid_creds

    Returns true if valid credentials exist for the given data source and requesting user.

    :param name: Required. The data source in the form: &#x60;projects/{project_id}/dataSources/{data_source_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}&#x60;.
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


async def bigquerydatatransfer_projects_locations_data_sources_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """bigquerydatatransfer_projects_locations_data_sources_list

    Lists supported data sources and returns their settings.

    :param parent: Required. The BigQuery project id for which data sources should be returned. Must be in the form: &#x60;projects/{project_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param page_size: Page size. The default page size is the maximum value of 1000 results.
    :type page_size: int
    :param page_token: Pagination token, which can be used to request a specific page of &#x60;ListDataSourcesRequest&#x60; list results. For multiple-page results, &#x60;ListDataSourcesResponse&#x60; outputs a &#x60;next_page&#x60; token, which can be used as the &#x60;page_token&#x60; value to request the next page of list results.
    :type page_token: str

    """
    return web.Response(status=200)


async def bigquerydatatransfer_projects_locations_enroll_data_sources(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """bigquerydatatransfer_projects_locations_enroll_data_sources

    Enroll data sources in a user project. This allows users to create transfer configurations for these data sources. They will also appear in the ListDataSources RPC and as such, will appear in the [BigQuery UI](https://console.cloud.google.com/bigquery), and the documents can be found in the public guide for [BigQuery Web UI](https://cloud.google.com/bigquery/bigquery-web-ui) and [Data Transfer Service](https://cloud.google.com/bigquery/docs/working-with-transfers).

    :param name: The name of the project resource in the form: &#x60;projects/{project_id}&#x60;
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
    body = EnrollDataSourcesRequest.from_dict(body)
    return web.Response(status=200)


async def bigquerydatatransfer_projects_locations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """bigquerydatatransfer_projects_locations_list

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


async def bigquerydatatransfer_projects_locations_unenroll_data_sources(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """bigquerydatatransfer_projects_locations_unenroll_data_sources

    Unenroll data sources in a user project. This allows users to remove transfer configurations for these data sources. They will no longer appear in the ListDataSources RPC and will also no longer appear in the [BigQuery UI](https://console.cloud.google.com/bigquery). Data transfers configurations of unenrolled data sources will not be scheduled.

    :param name: The name of the project resource in the form: &#x60;projects/{project_id}&#x60;
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
    body = UnenrollDataSourcesRequest.from_dict(body)
    return web.Response(status=200)


async def bigquerydatatransfer_projects_transfer_configs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, authorization_code=None, service_account_name=None, version_info=None, body=None) -> web.Response:
    """bigquerydatatransfer_projects_transfer_configs_create

    Creates a new data transfer configuration.

    :param parent: Required. The BigQuery project id where the transfer configuration should be created. Must be in the format projects/{project_id}/locations/{location_id} or projects/{project_id}. If specified location and location of the destination bigquery dataset do not match - the request will fail.
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
    :param authorization_code: Optional OAuth2 authorization code to use with this transfer configuration. This is required only if &#x60;transferConfig.dataSourceId&#x60; is &#39;youtube_channel&#39; and new credentials are needed, as indicated by &#x60;CheckValidCreds&#x60;. In order to obtain authorization_code, make a request to the following URL: https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?redirect_uri&#x3D;urn:ietf:wg:oauth:2.0:oob&amp;response_type&#x3D;authorization_code&amp;client_id&#x3D;client_id&amp;scope&#x3D;data_source_scopes * The client_id is the OAuth client_id of the a data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when &#x60;service_account_name&#x60; is used to create the transfer config.
    :type authorization_code: str
    :param service_account_name: Optional service account email. If this field is set, the transfer config will be created with this service account&#39;s credentials. It requires that the requesting user calling this API has permissions to act as this service account. Note that not all data sources support service account credentials when creating a transfer config. For the latest list of data sources, read about [using service accounts](https://cloud.google.com/bigquery-transfer/docs/use-service-accounts).
    :type service_account_name: str
    :param version_info: Optional version info. This is required only if &#x60;transferConfig.dataSourceId&#x60; is not &#39;youtube_channel&#39; and new credentials are needed, as indicated by &#x60;CheckValidCreds&#x60;. In order to obtain version info, make a request to the following URL: https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?redirect_uri&#x3D;urn:ietf:wg:oauth:2.0:oob&amp;response_type&#x3D;version_info&amp;client_id&#x3D;client_id&amp;scope&#x3D;data_source_scopes * The client_id is the OAuth client_id of the a data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when &#x60;service_account_name&#x60; is used to create the transfer config.
    :type version_info: str
    :param body: 
    :type body: dict | bytes

    """
    body = TransferConfig.from_dict(body)
    return web.Response(status=200)


async def bigquerydatatransfer_projects_transfer_configs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, data_source_ids=None, page_size=None, page_token=None) -> web.Response:
    """bigquerydatatransfer_projects_transfer_configs_list

    Returns information about all transfer configs owned by a project in the specified location.

    :param parent: Required. The BigQuery project id for which transfer configs should be returned: &#x60;projects/{project_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}&#x60;
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
    :param data_source_ids: When specified, only configurations of requested data sources are returned.
    :type data_source_ids: List[str]
    :param page_size: Page size. The default page size is the maximum value of 1000 results.
    :type page_size: int
    :param page_token: Pagination token, which can be used to request a specific page of &#x60;ListTransfersRequest&#x60; list results. For multiple-page results, &#x60;ListTransfersResponse&#x60; outputs a &#x60;next_page&#x60; token, which can be used as the &#x60;page_token&#x60; value to request the next page of list results.
    :type page_token: str

    """
    return web.Response(status=200)


async def bigquerydatatransfer_projects_transfer_configs_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, authorization_code=None, service_account_name=None, update_mask=None, version_info=None, body=None) -> web.Response:
    """bigquerydatatransfer_projects_transfer_configs_patch

    Updates a data transfer configuration. All fields must be set, even if they are not updated.

    :param name: The resource name of the transfer config. Transfer config names have the form either &#x60;projects/{project_id}/locations/{region}/transferConfigs/{config_id}&#x60; or &#x60;projects/{project_id}/transferConfigs/{config_id}&#x60;, where &#x60;config_id&#x60; is usually a UUID, even though it is not guaranteed or required. The name is ignored when creating a transfer config.
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
    :param authorization_code: Optional OAuth2 authorization code to use with this transfer configuration. This is required only if &#x60;transferConfig.dataSourceId&#x60; is &#39;youtube_channel&#39; and new credentials are needed, as indicated by &#x60;CheckValidCreds&#x60;. In order to obtain authorization_code, make a request to the following URL: https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?redirect_uri&#x3D;urn:ietf:wg:oauth:2.0:oob&amp;response_type&#x3D;authorization_code&amp;client_id&#x3D;client_id&amp;scope&#x3D;data_source_scopes * The client_id is the OAuth client_id of the a data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when &#x60;service_account_name&#x60; is used to update the transfer config.
    :type authorization_code: str
    :param service_account_name: Optional service account email. If this field is set, the transfer config will be created with this service account&#39;s credentials. It requires that the requesting user calling this API has permissions to act as this service account. Note that not all data sources support service account credentials when creating a transfer config. For the latest list of data sources, read about [using service accounts](https://cloud.google.com/bigquery-transfer/docs/use-service-accounts).
    :type service_account_name: str
    :param update_mask: Required. Required list of fields to be updated in this request.
    :type update_mask: str
    :param version_info: Optional version info. This is required only if &#x60;transferConfig.dataSourceId&#x60; is not &#39;youtube_channel&#39; and new credentials are needed, as indicated by &#x60;CheckValidCreds&#x60;. In order to obtain version info, make a request to the following URL: https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?redirect_uri&#x3D;urn:ietf:wg:oauth:2.0:oob&amp;response_type&#x3D;version_info&amp;client_id&#x3D;client_id&amp;scope&#x3D;data_source_scopes * The client_id is the OAuth client_id of the a data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when &#x60;service_account_name&#x60; is used to update the transfer config.
    :type version_info: str
    :param body: 
    :type body: dict | bytes

    """
    body = TransferConfig.from_dict(body)
    return web.Response(status=200)


async def bigquerydatatransfer_projects_transfer_configs_runs_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """bigquerydatatransfer_projects_transfer_configs_runs_delete

    Deletes the specified transfer run.

    :param name: Required. The field will contain name of the resource requested, for example: &#x60;projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}&#x60;
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


async def bigquerydatatransfer_projects_transfer_configs_runs_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """bigquerydatatransfer_projects_transfer_configs_runs_get

    Returns information about the particular transfer run.

    :param name: Required. The field will contain name of the resource requested, for example: &#x60;projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}&#x60;
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


async def bigquerydatatransfer_projects_transfer_configs_runs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, run_attempt=None, states=None) -> web.Response:
    """bigquerydatatransfer_projects_transfer_configs_runs_list

    Returns information about running and completed transfer runs.

    :param parent: Required. Name of transfer configuration for which transfer runs should be retrieved. Format of transfer configuration resource name is: &#x60;projects/{project_id}/transferConfigs/{config_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}&#x60;.
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
    :param page_size: Page size. The default page size is the maximum value of 1000 results.
    :type page_size: int
    :param page_token: Pagination token, which can be used to request a specific page of &#x60;ListTransferRunsRequest&#x60; list results. For multiple-page results, &#x60;ListTransferRunsResponse&#x60; outputs a &#x60;next_page&#x60; token, which can be used as the &#x60;page_token&#x60; value to request the next page of list results.
    :type page_token: str
    :param run_attempt: Indicates how run attempts are to be pulled.
    :type run_attempt: str
    :param states: When specified, only transfer runs with requested states are returned.
    :type states: List[str]

    """
    return web.Response(status=200)


async def bigquerydatatransfer_projects_transfer_configs_runs_transfer_logs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, message_types=None, page_size=None, page_token=None) -> web.Response:
    """bigquerydatatransfer_projects_transfer_configs_runs_transfer_logs_list

    Returns log messages for the transfer run.

    :param parent: Required. Transfer run name in the form: &#x60;projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}&#x60;
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
    :param message_types: Message types to return. If not populated - INFO, WARNING and ERROR messages are returned.
    :type message_types: List[str]
    :param page_size: Page size. The default page size is the maximum value of 1000 results.
    :type page_size: int
    :param page_token: Pagination token, which can be used to request a specific page of &#x60;ListTransferLogsRequest&#x60; list results. For multiple-page results, &#x60;ListTransferLogsResponse&#x60; outputs a &#x60;next_page&#x60; token, which can be used as the &#x60;page_token&#x60; value to request the next page of list results.
    :type page_token: str

    """
    return web.Response(status=200)


async def bigquerydatatransfer_projects_transfer_configs_schedule_runs(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """bigquerydatatransfer_projects_transfer_configs_schedule_runs

    Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead.

    :param parent: Required. Transfer configuration name in the form: &#x60;projects/{project_id}/transferConfigs/{config_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}&#x60;.
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
    :param body: 
    :type body: dict | bytes

    """
    body = ScheduleTransferRunsRequest.from_dict(body)
    return web.Response(status=200)


async def bigquerydatatransfer_projects_transfer_configs_start_manual_runs(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """bigquerydatatransfer_projects_transfer_configs_start_manual_runs

    Start manual transfer runs to be executed now with schedule_time equal to current time. The transfer runs can be created for a time range where the run_time is between start_time (inclusive) and end_time (exclusive), or for a specific run_time.

    :param parent: Transfer configuration name in the form: &#x60;projects/{project_id}/transferConfigs/{config_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}&#x60;.
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
    :param body: 
    :type body: dict | bytes

    """
    body = StartManualTransferRunsRequest.from_dict(body)
    return web.Response(status=200)
