from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_privacy_dlp_v2_create_deidentify_template_request import GooglePrivacyDlpV2CreateDeidentifyTemplateRequest
from openapi_server.models.google_privacy_dlp_v2_create_discovery_config_request import GooglePrivacyDlpV2CreateDiscoveryConfigRequest
from openapi_server.models.google_privacy_dlp_v2_create_dlp_job_request import GooglePrivacyDlpV2CreateDlpJobRequest
from openapi_server.models.google_privacy_dlp_v2_create_inspect_template_request import GooglePrivacyDlpV2CreateInspectTemplateRequest
from openapi_server.models.google_privacy_dlp_v2_create_job_trigger_request import GooglePrivacyDlpV2CreateJobTriggerRequest
from openapi_server.models.google_privacy_dlp_v2_create_stored_info_type_request import GooglePrivacyDlpV2CreateStoredInfoTypeRequest
from openapi_server.models.google_privacy_dlp_v2_deidentify_content_request import GooglePrivacyDlpV2DeidentifyContentRequest
from openapi_server.models.google_privacy_dlp_v2_deidentify_content_response import GooglePrivacyDlpV2DeidentifyContentResponse
from openapi_server.models.google_privacy_dlp_v2_deidentify_template import GooglePrivacyDlpV2DeidentifyTemplate
from openapi_server.models.google_privacy_dlp_v2_discovery_config import GooglePrivacyDlpV2DiscoveryConfig
from openapi_server.models.google_privacy_dlp_v2_dlp_job import GooglePrivacyDlpV2DlpJob
from openapi_server.models.google_privacy_dlp_v2_hybrid_inspect_job_trigger_request import GooglePrivacyDlpV2HybridInspectJobTriggerRequest
from openapi_server.models.google_privacy_dlp_v2_inspect_content_request import GooglePrivacyDlpV2InspectContentRequest
from openapi_server.models.google_privacy_dlp_v2_inspect_content_response import GooglePrivacyDlpV2InspectContentResponse
from openapi_server.models.google_privacy_dlp_v2_inspect_template import GooglePrivacyDlpV2InspectTemplate
from openapi_server.models.google_privacy_dlp_v2_job_trigger import GooglePrivacyDlpV2JobTrigger
from openapi_server.models.google_privacy_dlp_v2_list_column_data_profiles_response import GooglePrivacyDlpV2ListColumnDataProfilesResponse
from openapi_server.models.google_privacy_dlp_v2_list_deidentify_templates_response import GooglePrivacyDlpV2ListDeidentifyTemplatesResponse
from openapi_server.models.google_privacy_dlp_v2_list_discovery_configs_response import GooglePrivacyDlpV2ListDiscoveryConfigsResponse
from openapi_server.models.google_privacy_dlp_v2_list_dlp_jobs_response import GooglePrivacyDlpV2ListDlpJobsResponse
from openapi_server.models.google_privacy_dlp_v2_list_inspect_templates_response import GooglePrivacyDlpV2ListInspectTemplatesResponse
from openapi_server.models.google_privacy_dlp_v2_list_job_triggers_response import GooglePrivacyDlpV2ListJobTriggersResponse
from openapi_server.models.google_privacy_dlp_v2_list_project_data_profiles_response import GooglePrivacyDlpV2ListProjectDataProfilesResponse
from openapi_server.models.google_privacy_dlp_v2_list_stored_info_types_response import GooglePrivacyDlpV2ListStoredInfoTypesResponse
from openapi_server.models.google_privacy_dlp_v2_list_table_data_profiles_response import GooglePrivacyDlpV2ListTableDataProfilesResponse
from openapi_server.models.google_privacy_dlp_v2_redact_image_request import GooglePrivacyDlpV2RedactImageRequest
from openapi_server.models.google_privacy_dlp_v2_redact_image_response import GooglePrivacyDlpV2RedactImageResponse
from openapi_server.models.google_privacy_dlp_v2_reidentify_content_request import GooglePrivacyDlpV2ReidentifyContentRequest
from openapi_server.models.google_privacy_dlp_v2_reidentify_content_response import GooglePrivacyDlpV2ReidentifyContentResponse
from openapi_server.models.google_privacy_dlp_v2_stored_info_type import GooglePrivacyDlpV2StoredInfoType
from openapi_server.models.google_privacy_dlp_v2_update_stored_info_type_request import GooglePrivacyDlpV2UpdateStoredInfoTypeRequest
from openapi_server import util


async def dlp_projects_locations_column_data_profiles_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """dlp_projects_locations_column_data_profiles_list

    Lists data profiles for an organization.

    :param parent: Required. Resource name of the organization or project, for example &#x60;organizations/433245324/locations/europe&#x60; or projects/project-id/locations/asia.
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
    :param filter: Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * Supported fields/values: - &#x60;table_data_profile_name&#x60; - The name of the related table data profile. - &#x60;project_id&#x60; - The Google Cloud project ID. (REQUIRED) - &#x60;dataset_id&#x60; - The BigQuery dataset ID. (REQUIRED) - &#x60;table_id&#x60; - The BigQuery table ID. (REQUIRED) - &#x60;field_id&#x60; - The ID of the BigQuery field. - &#x60;info_type&#x60; - The infotype detected in the resource. - &#x60;sensitivity_level&#x60; - HIGH|MEDIUM|LOW - &#x60;data_risk_level&#x60;: How much risk is associated with this data. - &#x60;status_code&#x60; - an RPC status code as defined in https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto * The operator must be &#x60;&#x3D;&#x60; for project_id, dataset_id, and table_id. Other filters also support &#x60;!&#x3D;&#x60;. Examples: * project_id &#x3D; 12345 AND status_code &#x3D; 1 * project_id &#x3D; 12345 AND sensitivity_level &#x3D; HIGH * project_id &#x3D; 12345 AND info_type &#x3D; STREET_ADDRESS The length of this field should be no more than 500 characters.
    :type filter: str
    :param order_by: Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed. Examples: * &#x60;project_id asc&#x60; * &#x60;table_id&#x60; * &#x60;sensitivity_level desc&#x60; Supported fields are: - &#x60;project_id&#x60;: The Google Cloud project ID. - &#x60;dataset_id&#x60;: The ID of a BigQuery dataset. - &#x60;table_id&#x60;: The ID of a BigQuery table. - &#x60;sensitivity_level&#x60;: How sensitive the data in a column is, at most. - &#x60;data_risk_level&#x60;: How much risk is associated with this data. - &#x60;profile_last_generated&#x60;: When the profile was last updated in epoch seconds.
    :type order_by: str
    :param page_size: Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.
    :type page_size: int
    :param page_token: Page token to continue retrieval.
    :type page_token: str

    """
    return web.Response(status=200)


async def dlp_projects_locations_content_deidentify(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_content_deidentify

    De-identifies potentially sensitive info from a ContentItem. This method has limits on input size and output size. See https://cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data to learn more. When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.

    :param parent: Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    body = GooglePrivacyDlpV2DeidentifyContentRequest.from_dict(body)
    return web.Response(status=200)


async def dlp_projects_locations_content_inspect(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_content_inspect

    Finds potentially sensitive info in content. This method has limits on input size, processing time, and output size. When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated. For how to guides, see https://cloud.google.com/sensitive-data-protection/docs/inspecting-images and https://cloud.google.com/sensitive-data-protection/docs/inspecting-text,

    :param parent: Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    body = GooglePrivacyDlpV2InspectContentRequest.from_dict(body)
    return web.Response(status=200)


async def dlp_projects_locations_content_reidentify(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_content_reidentify

    Re-identifies content that has been de-identified. See https://cloud.google.com/sensitive-data-protection/docs/pseudonymization#re-identification_in_free_text_code_example to learn more.

    :param parent: Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    body = GooglePrivacyDlpV2ReidentifyContentRequest.from_dict(body)
    return web.Response(status=200)


async def dlp_projects_locations_deidentify_templates_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_deidentify_templates_create

    Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more.

    :param parent: Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID + Organizations scope, location specified: &#x60;organizations/&#x60;ORG_ID&#x60;/locations/&#x60;LOCATION_ID + Organizations scope, no location specified (defaults to global): &#x60;organizations/&#x60;ORG_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    body = GooglePrivacyDlpV2CreateDeidentifyTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def dlp_projects_locations_deidentify_templates_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, location_id=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """dlp_projects_locations_deidentify_templates_list

    Lists DeidentifyTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more.

    :param parent: Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID + Organizations scope, location specified: &#x60;organizations/&#x60;ORG_ID&#x60;/locations/&#x60;LOCATION_ID + Organizations scope, no location specified (defaults to global): &#x60;organizations/&#x60;ORG_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    :param location_id: Deprecated. This field has no effect.
    :type location_id: str
    :param order_by: Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: &#x60;name asc,update_time, create_time desc&#x60; Supported fields are: - &#x60;create_time&#x60;: corresponds to the time the template was created. - &#x60;update_time&#x60;: corresponds to the time the template was last updated. - &#x60;name&#x60;: corresponds to the template&#39;s name. - &#x60;display_name&#x60;: corresponds to the template&#39;s display name.
    :type order_by: str
    :param page_size: Size of the page. This value can be limited by the server. If zero server returns a page of max size 100.
    :type page_size: int
    :param page_token: Page token to continue retrieval. Comes from the previous call to &#x60;ListDeidentifyTemplates&#x60;.
    :type page_token: str

    """
    return web.Response(status=200)


async def dlp_projects_locations_discovery_configs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_discovery_configs_create

    Creates a config for discovery to scan and profile storage.

    :param parent: Required. Parent resource name. The format of this value is as follows: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    body = GooglePrivacyDlpV2CreateDiscoveryConfigRequest.from_dict(body)
    return web.Response(status=200)


async def dlp_projects_locations_discovery_configs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """dlp_projects_locations_discovery_configs_list

    Lists discovery configurations.

    :param parent: Required. Parent resource name. The format of this value is as follows: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    :param order_by: Comma separated list of config fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: &#x60;name asc,update_time, create_time desc&#x60; Supported fields are: - &#x60;last_run_time&#x60;: corresponds to the last time the DiscoveryConfig ran. - &#x60;name&#x60;: corresponds to the DiscoveryConfig&#39;s name. - &#x60;status&#x60;: corresponds to DiscoveryConfig&#39;s status.
    :type order_by: str
    :param page_size: Size of the page. This value can be limited by a server.
    :type page_size: int
    :param page_token: Page token to continue retrieval. Comes from the previous call to ListDiscoveryConfigs. &#x60;order_by&#x60; field must not change for subsequent calls.
    :type page_token: str

    """
    return web.Response(status=200)


async def dlp_projects_locations_dlp_jobs_cancel(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_dlp_jobs_cancel

    Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more.

    :param name: Required. The name of the DlpJob resource to be cancelled.
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


async def dlp_projects_locations_dlp_jobs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_dlp_jobs_create

    Creates a new job to inspect storage or calculate risk metrics. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.

    :param parent: Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    body = GooglePrivacyDlpV2CreateDlpJobRequest.from_dict(body)
    return web.Response(status=200)


async def dlp_projects_locations_dlp_jobs_finish(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_dlp_jobs_finish

    Finish a running hybrid DlpJob. Triggers the finalization steps and running of any enabled actions that have not yet run.

    :param name: Required. The name of the DlpJob resource to be finished.
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


async def dlp_projects_locations_dlp_jobs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, location_id=None, order_by=None, page_size=None, page_token=None, type=None) -> web.Response:
    """dlp_projects_locations_dlp_jobs_list

    Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more.

    :param parent: Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    :param filter: Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * Supported fields/values for inspect jobs: - &#x60;state&#x60; - PENDING|RUNNING|CANCELED|FINISHED|FAILED - &#x60;inspected_storage&#x60; - DATASTORE|CLOUD_STORAGE|BIGQUERY - &#x60;trigger_name&#x60; - The name of the trigger that created the job. - &#39;end_time&#x60; - Corresponds to the time the job finished. - &#39;start_time&#x60; - Corresponds to the time the job finished. * Supported fields for risk analysis jobs: - &#x60;state&#x60; - RUNNING|CANCELED|FINISHED|FAILED - &#39;end_time&#x60; - Corresponds to the time the job finished. - &#39;start_time&#x60; - Corresponds to the time the job finished. * The operator must be &#x60;&#x3D;&#x60; or &#x60;!&#x3D;&#x60;. Examples: * inspected_storage &#x3D; cloud_storage AND state &#x3D; done * inspected_storage &#x3D; cloud_storage OR inspected_storage &#x3D; bigquery * inspected_storage &#x3D; cloud_storage AND (state &#x3D; done OR state &#x3D; canceled) * end_time &gt; \\\&quot;2017-12-12T00:00:00+00:00\\\&quot; The length of this field should be no more than 500 characters.
    :type filter: str
    :param location_id: Deprecated. This field has no effect.
    :type location_id: str
    :param order_by: Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: &#x60;name asc, end_time asc, create_time desc&#x60; Supported fields are: - &#x60;create_time&#x60;: corresponds to the time the job was created. - &#x60;end_time&#x60;: corresponds to the time the job ended. - &#x60;name&#x60;: corresponds to the job&#39;s name. - &#x60;state&#x60;: corresponds to &#x60;state&#x60;
    :type order_by: str
    :param page_size: The standard list page size.
    :type page_size: int
    :param page_token: The standard list page token.
    :type page_token: str
    :param type: The type of job. Defaults to &#x60;DlpJobType.INSPECT&#x60;
    :type type: str

    """
    return web.Response(status=200)


async def dlp_projects_locations_image_redact(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_image_redact

    Redacts potentially sensitive info from an image. This method has limits on input size, processing time, and output size. See https://cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images to learn more. When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.

    :param parent: Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    body = GooglePrivacyDlpV2RedactImageRequest.from_dict(body)
    return web.Response(status=200)


async def dlp_projects_locations_inspect_templates_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_inspect_templates_create

    Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more.

    :param parent: Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID + Organizations scope, location specified: &#x60;organizations/&#x60;ORG_ID&#x60;/locations/&#x60;LOCATION_ID + Organizations scope, no location specified (defaults to global): &#x60;organizations/&#x60;ORG_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    body = GooglePrivacyDlpV2CreateInspectTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def dlp_projects_locations_inspect_templates_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, location_id=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """dlp_projects_locations_inspect_templates_list

    Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more.

    :param parent: Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID + Organizations scope, location specified: &#x60;organizations/&#x60;ORG_ID&#x60;/locations/&#x60;LOCATION_ID + Organizations scope, no location specified (defaults to global): &#x60;organizations/&#x60;ORG_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    :param location_id: Deprecated. This field has no effect.
    :type location_id: str
    :param order_by: Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: &#x60;name asc,update_time, create_time desc&#x60; Supported fields are: - &#x60;create_time&#x60;: corresponds to the time the template was created. - &#x60;update_time&#x60;: corresponds to the time the template was last updated. - &#x60;name&#x60;: corresponds to the template&#39;s name. - &#x60;display_name&#x60;: corresponds to the template&#39;s display name.
    :type order_by: str
    :param page_size: Size of the page. This value can be limited by the server. If zero server returns a page of max size 100.
    :type page_size: int
    :param page_token: Page token to continue retrieval. Comes from the previous call to &#x60;ListInspectTemplates&#x60;.
    :type page_token: str

    """
    return web.Response(status=200)


async def dlp_projects_locations_job_triggers_activate(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_job_triggers_activate

    Activate a job trigger. Causes the immediate execute of a trigger instead of waiting on the trigger event to occur.

    :param name: Required. Resource name of the trigger to activate, for example &#x60;projects/dlp-test-project/jobTriggers/53234423&#x60;.
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


async def dlp_projects_locations_job_triggers_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_job_triggers_create

    Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more.

    :param parent: Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    body = GooglePrivacyDlpV2CreateJobTriggerRequest.from_dict(body)
    return web.Response(status=200)


async def dlp_projects_locations_job_triggers_hybrid_inspect(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_locations_job_triggers_hybrid_inspect

    Inspect hybrid content and store findings to a trigger. The inspection will be processed asynchronously. To review the findings monitor the jobs within the trigger.

    :param name: Required. Resource name of the trigger to execute a hybrid inspect on, for example &#x60;projects/dlp-test-project/jobTriggers/53234423&#x60;.
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
    body = GooglePrivacyDlpV2HybridInspectJobTriggerRequest.from_dict(body)
    return web.Response(status=200)


async def dlp_projects_locations_job_triggers_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, location_id=None, order_by=None, page_size=None, page_token=None, type=None) -> web.Response:
    """dlp_projects_locations_job_triggers_list

    Lists job triggers. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more.

    :param parent: Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    :param filter: Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * Supported fields/values for inspect triggers: - &#x60;status&#x60; - HEALTHY|PAUSED|CANCELLED - &#x60;inspected_storage&#x60; - DATASTORE|CLOUD_STORAGE|BIGQUERY - &#39;last_run_time&#x60; - RFC 3339 formatted timestamp, surrounded by quotation marks. Nanoseconds are ignored. - &#39;error_count&#39; - Number of errors that have occurred while running. * The operator must be &#x60;&#x3D;&#x60; or &#x60;!&#x3D;&#x60; for status and inspected_storage. Examples: * inspected_storage &#x3D; cloud_storage AND status &#x3D; HEALTHY * inspected_storage &#x3D; cloud_storage OR inspected_storage &#x3D; bigquery * inspected_storage &#x3D; cloud_storage AND (state &#x3D; PAUSED OR state &#x3D; HEALTHY) * last_run_time &gt; \\\&quot;2017-12-12T00:00:00+00:00\\\&quot; The length of this field should be no more than 500 characters.
    :type filter: str
    :param location_id: Deprecated. This field has no effect.
    :type location_id: str
    :param order_by: Comma separated list of triggeredJob fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: &#x60;name asc,update_time, create_time desc&#x60; Supported fields are: - &#x60;create_time&#x60;: corresponds to the time the JobTrigger was created. - &#x60;update_time&#x60;: corresponds to the time the JobTrigger was last updated. - &#x60;last_run_time&#x60;: corresponds to the last time the JobTrigger ran. - &#x60;name&#x60;: corresponds to the JobTrigger&#39;s name. - &#x60;display_name&#x60;: corresponds to the JobTrigger&#39;s display name. - &#x60;status&#x60;: corresponds to JobTrigger&#39;s status.
    :type order_by: str
    :param page_size: Size of the page. This value can be limited by a server.
    :type page_size: int
    :param page_token: Page token to continue retrieval. Comes from the previous call to ListJobTriggers. &#x60;order_by&#x60; field must not change for subsequent calls.
    :type page_token: str
    :param type: The type of jobs. Will use &#x60;DlpJobType.INSPECT&#x60; if not set.
    :type type: str

    """
    return web.Response(status=200)


async def dlp_projects_locations_project_data_profiles_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """dlp_projects_locations_project_data_profiles_list

    Lists data profiles for an organization.

    :param parent: Required. organizations/{org_id}/locations/{loc_id}
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
    :param filter: Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * Supported fields/values: - &#x60;sensitivity_level&#x60; - HIGH|MODERATE|LOW - &#x60;data_risk_level&#x60; - HIGH|MODERATE|LOW - &#x60;status_code&#x60; - an RPC status code as defined in https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto * The operator must be &#x60;&#x3D;&#x60; or &#x60;!&#x3D;&#x60;. Examples: * project_id &#x3D; 12345 AND status_code &#x3D; 1 * project_id &#x3D; 12345 AND sensitivity_level &#x3D; HIGH The length of this field should be no more than 500 characters.
    :type filter: str
    :param order_by: Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed. Examples: * &#x60;project_id&#x60; * &#x60;sensitivity_level desc&#x60; Supported fields are: - &#x60;project_id&#x60;: GCP project ID - &#x60;sensitivity_level&#x60;: How sensitive the data in a project is, at most. - &#x60;data_risk_level&#x60;: How much risk is associated with this data. - &#x60;profile_last_generated&#x60;: When the profile was last updated in epoch seconds.
    :type order_by: str
    :param page_size: Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.
    :type page_size: int
    :param page_token: Page token to continue retrieval.
    :type page_token: str

    """
    return web.Response(status=200)


async def dlp_projects_locations_table_data_profiles_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """dlp_projects_locations_table_data_profiles_list

    Lists data profiles for an organization.

    :param parent: Required. Resource name of the organization or project, for example &#x60;organizations/433245324/locations/europe&#x60; or &#x60;projects/project-id/locations/asia&#x60;.
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
    :param filter: Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * Supported fields/values: - &#x60;project_id&#x60; - The GCP project ID. - &#x60;dataset_id&#x60; - The BigQuery dataset ID. - &#x60;table_id&#x60; - The ID of the BigQuery table. - &#x60;sensitivity_level&#x60; - HIGH|MODERATE|LOW - &#x60;data_risk_level&#x60; - HIGH|MODERATE|LOW - &#x60;resource_visibility&#x60;: PUBLIC|RESTRICTED - &#x60;status_code&#x60; - an RPC status code as defined in https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto * The operator must be &#x60;&#x3D;&#x60; or &#x60;!&#x3D;&#x60;. Examples: * project_id &#x3D; 12345 AND status_code &#x3D; 1 * project_id &#x3D; 12345 AND sensitivity_level &#x3D; HIGH * project_id &#x3D; 12345 AND resource_visibility &#x3D; PUBLIC The length of this field should be no more than 500 characters.
    :type filter: str
    :param order_by: Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed. Examples: * &#x60;project_id asc&#x60; * &#x60;table_id&#x60; * &#x60;sensitivity_level desc&#x60; Supported fields are: - &#x60;project_id&#x60;: The GCP project ID. - &#x60;dataset_id&#x60;: The ID of a BigQuery dataset. - &#x60;table_id&#x60;: The ID of a BigQuery table. - &#x60;sensitivity_level&#x60;: How sensitive the data in a table is, at most. - &#x60;data_risk_level&#x60;: How much risk is associated with this data. - &#x60;profile_last_generated&#x60;: When the profile was last updated in epoch seconds. - &#x60;last_modified&#x60;: The last time the resource was modified. - &#x60;resource_visibility&#x60;: Visibility restriction for this resource. - &#x60;row_count&#x60;: Number of rows in this resource.
    :type order_by: str
    :param page_size: Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.
    :type page_size: int
    :param page_token: Page token to continue retrieval.
    :type page_token: str

    """
    return web.Response(status=200)


async def dlp_projects_stored_info_types_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_stored_info_types_create

    Creates a pre-built stored infoType to be used for inspection. See https://cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes to learn more.

    :param parent: Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID + Organizations scope, location specified: &#x60;organizations/&#x60;ORG_ID&#x60;/locations/&#x60;LOCATION_ID + Organizations scope, no location specified (defaults to global): &#x60;organizations/&#x60;ORG_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    body = GooglePrivacyDlpV2CreateStoredInfoTypeRequest.from_dict(body)
    return web.Response(status=200)


async def dlp_projects_stored_info_types_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """dlp_projects_stored_info_types_delete

    Deletes a stored infoType. See https://cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes to learn more.

    :param name: Required. Resource name of the organization and storedInfoType to be deleted, for example &#x60;organizations/433245324/storedInfoTypes/432452342&#x60; or projects/project-id/storedInfoTypes/432452342.
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


async def dlp_projects_stored_info_types_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """dlp_projects_stored_info_types_get

    Gets a stored infoType. See https://cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes to learn more.

    :param name: Required. Resource name of the organization and storedInfoType to be read, for example &#x60;organizations/433245324/storedInfoTypes/432452342&#x60; or projects/project-id/storedInfoTypes/432452342.
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


async def dlp_projects_stored_info_types_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, location_id=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """dlp_projects_stored_info_types_list

    Lists stored infoTypes. See https://cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes to learn more.

    :param parent: Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3
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
    :param location_id: Deprecated. This field has no effect.
    :type location_id: str
    :param order_by: Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: &#x60;name asc, display_name, create_time desc&#x60; Supported fields are: - &#x60;create_time&#x60;: corresponds to the time the most recent version of the resource was created. - &#x60;state&#x60;: corresponds to the state of the resource. - &#x60;name&#x60;: corresponds to resource name. - &#x60;display_name&#x60;: corresponds to info type&#39;s display name.
    :type order_by: str
    :param page_size: Size of the page. This value can be limited by the server. If zero server returns a page of max size 100.
    :type page_size: int
    :param page_token: Page token to continue retrieval. Comes from the previous call to &#x60;ListStoredInfoTypes&#x60;.
    :type page_token: str

    """
    return web.Response(status=200)


async def dlp_projects_stored_info_types_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """dlp_projects_stored_info_types_patch

    Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes to learn more.

    :param name: Required. Resource name of organization and storedInfoType to be updated, for example &#x60;organizations/433245324/storedInfoTypes/432452342&#x60; or projects/project-id/storedInfoTypes/432452342.
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
    body = GooglePrivacyDlpV2UpdateStoredInfoTypeRequest.from_dict(body)
    return web.Response(status=200)
