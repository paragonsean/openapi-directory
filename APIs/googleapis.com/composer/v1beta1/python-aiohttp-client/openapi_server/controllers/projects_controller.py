from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_upgrade_request import CheckUpgradeRequest
from openapi_server.models.environment import Environment
from openapi_server.models.execute_airflow_command_request import ExecuteAirflowCommandRequest
from openapi_server.models.execute_airflow_command_response import ExecuteAirflowCommandResponse
from openapi_server.models.fetch_database_properties_response import FetchDatabasePropertiesResponse
from openapi_server.models.list_environments_response import ListEnvironmentsResponse
from openapi_server.models.list_image_versions_response import ListImageVersionsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_user_workloads_config_maps_response import ListUserWorkloadsConfigMapsResponse
from openapi_server.models.list_user_workloads_secrets_response import ListUserWorkloadsSecretsResponse
from openapi_server.models.list_workloads_response import ListWorkloadsResponse
from openapi_server.models.load_snapshot_request import LoadSnapshotRequest
from openapi_server.models.operation import Operation
from openapi_server.models.poll_airflow_command_request import PollAirflowCommandRequest
from openapi_server.models.poll_airflow_command_response import PollAirflowCommandResponse
from openapi_server.models.save_snapshot_request import SaveSnapshotRequest
from openapi_server.models.stop_airflow_command_request import StopAirflowCommandRequest
from openapi_server.models.stop_airflow_command_response import StopAirflowCommandResponse
from openapi_server.models.user_workloads_config_map import UserWorkloadsConfigMap
from openapi_server.models.user_workloads_secret import UserWorkloadsSecret
from openapi_server import util


async def composer_projects_locations_environments_check_upgrade(request: web.Request, environment, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """composer_projects_locations_environments_check_upgrade

    Check if an upgrade operation on the environment will succeed. In case of problems detailed info can be found in the returned Operation.

    :param environment: The resource name of the environment to check upgrade for, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
    :type environment: str
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
    body = CheckUpgradeRequest.from_dict(body)
    return web.Response(status=200)


async def composer_projects_locations_environments_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """composer_projects_locations_environments_create

    Create a new environment.

    :param parent: The parent must be of the form \&quot;projects/{projectId}/locations/{locationId}\&quot;.
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
    body = Environment.from_dict(body)
    return web.Response(status=200)


async def composer_projects_locations_environments_database_failover(request: web.Request, environment, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """composer_projects_locations_environments_database_failover

    Triggers database failover (only for highly resilient environments).

    :param environment: Target environment: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
    :type environment: str
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


async def composer_projects_locations_environments_execute_airflow_command(request: web.Request, environment, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """composer_projects_locations_environments_execute_airflow_command

    Executes Airflow CLI command.

    :param environment: The resource name of the environment in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;.
    :type environment: str
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
    body = ExecuteAirflowCommandRequest.from_dict(body)
    return web.Response(status=200)


async def composer_projects_locations_environments_fetch_database_properties(request: web.Request, environment, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """composer_projects_locations_environments_fetch_database_properties

    Fetches database properties.

    :param environment: Required. The resource name of the environment, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
    :type environment: str
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


async def composer_projects_locations_environments_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """composer_projects_locations_environments_list

    List environments.

    :param parent: List environments in the given project and location, in the form: \&quot;projects/{projectId}/locations/{locationId}\&quot;
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
    :param page_size: The maximum number of environments to return.
    :type page_size: int
    :param page_token: The next_page_token value returned from a previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def composer_projects_locations_environments_load_snapshot(request: web.Request, environment, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """composer_projects_locations_environments_load_snapshot

    Loads a snapshot of a Cloud Composer environment. As a result of this operation, a snapshot of environment&#39;s specified in LoadSnapshotRequest is loaded into the environment.

    :param environment: The resource name of the target environment in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
    :type environment: str
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
    body = LoadSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def composer_projects_locations_environments_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """composer_projects_locations_environments_patch

    Update an environment.

    :param name: The relative resource name of the environment to update, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
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
    :param update_mask: Required. A comma-separated list of paths, relative to &#x60;Environment&#x60;, of fields to update. For example, to set the version of scikit-learn to install in the environment to 0.19.0 and to remove an existing installation of argparse, the &#x60;updateMask&#x60; parameter would include the following two &#x60;paths&#x60; values: \&quot;config.softwareConfig.pypiPackages.scikit-learn\&quot; and \&quot;config.softwareConfig.pypiPackages.argparse\&quot;. The included patch environment would specify the scikit-learn version as follows: { \&quot;config\&quot;:{ \&quot;softwareConfig\&quot;:{ \&quot;pypiPackages\&quot;:{ \&quot;scikit-learn\&quot;:\&quot;&#x3D;&#x3D;0.19.0\&quot; } } } } Note that in the above example, any existing PyPI packages other than scikit-learn and argparse will be unaffected. Only one update type may be included in a single request&#39;s &#x60;updateMask&#x60;. For example, one cannot update both the PyPI packages and labels in the same request. However, it is possible to update multiple members of a map field simultaneously in the same request. For example, to set the labels \&quot;label1\&quot; and \&quot;label2\&quot; while clearing \&quot;label3\&quot; (assuming it already exists), one can provide the paths \&quot;labels.label1\&quot;, \&quot;labels.label2\&quot;, and \&quot;labels.label3\&quot; and populate the patch environment as follows: { \&quot;labels\&quot;:{ \&quot;label1\&quot;:\&quot;new-label1-value\&quot; \&quot;label2\&quot;:\&quot;new-label2-value\&quot; } } Note that in the above example, any existing labels that are not included in the &#x60;updateMask&#x60; will be unaffected. It is also possible to replace an entire map field by providing the map field&#39;s path in the &#x60;updateMask&#x60;. The new value of the field will be that which is provided in the patch environment. For example, to delete all pre-existing user-specified PyPI packages and install botocore at version 1.7.14, the &#x60;updateMask&#x60; would contain the path \&quot;config.softwareConfig.pypiPackages\&quot;, and the patch environment would be the following: { \&quot;config\&quot;:{ \&quot;softwareConfig\&quot;:{ \&quot;pypiPackages\&quot;:{ \&quot;botocore\&quot;:\&quot;&#x3D;&#x3D;1.7.14\&quot; } } } } **Note:** Only the following fields can be updated: * &#x60;config.softwareConfig.pypiPackages&#x60; * Replace all custom custom PyPI packages. If a replacement package map is not included in &#x60;environment&#x60;, all custom PyPI packages are cleared. It is an error to provide both this mask and a mask specifying an individual package. * &#x60;config.softwareConfig.pypiPackages.&#x60;packagename * Update the custom PyPI package *packagename*, preserving other packages. To delete the package, include it in &#x60;updateMask&#x60;, and omit the mapping for it in &#x60;environment.config.softwareConfig.pypiPackages&#x60;. It is an error to provide both a mask of this form and the &#x60;config.softwareConfig.pypiPackages&#x60; mask. * &#x60;labels&#x60; * Replace all environment labels. If a replacement labels map is not included in &#x60;environment&#x60;, all labels are cleared. It is an error to provide both this mask and a mask specifying one or more individual labels. * &#x60;labels.&#x60;labelName * Set the label named *labelName*, while preserving other labels. To delete the label, include it in &#x60;updateMask&#x60; and omit its mapping in &#x60;environment.labels&#x60;. It is an error to provide both a mask of this form and the &#x60;labels&#x60; mask. * &#x60;config.nodeCount&#x60; * Horizontally scale the number of nodes in the environment. An integer greater than or equal to 3 must be provided in the &#x60;config.nodeCount&#x60; field. Supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. * &#x60;config.webServerNetworkAccessControl&#x60; * Replace the environment&#39;s current WebServerNetworkAccessControl. * &#x60;config.softwareConfig.airflowConfigOverrides&#x60; * Replace all Apache Airflow config overrides. If a replacement config overrides map is not included in &#x60;environment&#x60;, all config overrides are cleared. It is an error to provide both this mask and a mask specifying one or more individual config overrides. * &#x60;config.softwareConfig.airflowConfigOverrides.&#x60;section-name * Override the Apache Airflow config property *name* in the section named *section*, preserving other properties. To delete the property override, include it in &#x60;updateMask&#x60; and omit its mapping in &#x60;environment.config.softwareConfig.airflowConfigOverrides&#x60;. It is an error to provide both a mask of this form and the &#x60;config.softwareConfig.airflowConfigOverrides&#x60; mask. * &#x60;config.softwareConfig.envVariables&#x60; * Replace all environment variables. If a replacement environment variable map is not included in &#x60;environment&#x60;, all custom environment variables are cleared. * &#x60;config.softwareConfig.imageVersion&#x60; * Upgrade the version of the environment in-place. Refer to &#x60;SoftwareConfig.image_version&#x60; for information on how to format the new image version. Additionally, the new image version cannot effect a version downgrade, and must match the current image version&#39;s Composer and Airflow major versions. Consult the [Cloud Composer version list](/composer/docs/concepts/versioning/composer-versions) for valid values. * &#x60;config.softwareConfig.schedulerCount&#x60; * Horizontally scale the number of schedulers in Airflow. A positive integer not greater than the number of nodes must be provided in the &#x60;config.softwareConfig.schedulerCount&#x60; field. Supported for Cloud Composer environments in versions composer-1.*.*-airflow-2.*.*. * &#x60;config.softwareConfig.cloudDataLineageIntegration&#x60; * Configuration for Cloud Data Lineage integration. * &#x60;config.databaseConfig.machineType&#x60; * Cloud SQL machine type used by Airflow database. It has to be one of: db-n1-standard-2, db-n1-standard-4, db-n1-standard-8 or db-n1-standard-16. Supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. * &#x60;config.webServerConfig.machineType&#x60; * Machine type on which Airflow web server is running. It has to be one of: composer-n1-webserver-2, composer-n1-webserver-4 or composer-n1-webserver-8. Supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. * &#x60;config.maintenanceWindow&#x60; * Maintenance window during which Cloud Composer components may be under maintenance. * &#x60;config.workloadsConfig&#x60; * The workloads configuration settings for the GKE cluster associated with the Cloud Composer environment. Supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer. * &#x60;config.environmentSize&#x60; * The size of the Cloud Composer environment. Supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Environment.from_dict(body)
    return web.Response(status=200)


async def composer_projects_locations_environments_poll_airflow_command(request: web.Request, environment, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """composer_projects_locations_environments_poll_airflow_command

    Polls Airflow CLI command execution and fetches logs.

    :param environment: The resource name of the environment in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
    :type environment: str
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
    body = PollAirflowCommandRequest.from_dict(body)
    return web.Response(status=200)


async def composer_projects_locations_environments_restart_web_server(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """composer_projects_locations_environments_restart_web_server

    Restart Airflow web server.

    :param name: The resource name of the environment to restart the web server for, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
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


async def composer_projects_locations_environments_save_snapshot(request: web.Request, environment, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """composer_projects_locations_environments_save_snapshot

    Creates a snapshots of a Cloud Composer environment. As a result of this operation, snapshot of environment&#39;s state is stored in a location specified in the SaveSnapshotRequest.

    :param environment: The resource name of the source environment in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
    :type environment: str
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
    body = SaveSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def composer_projects_locations_environments_stop_airflow_command(request: web.Request, environment, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """composer_projects_locations_environments_stop_airflow_command

    Stops Airflow CLI command execution.

    :param environment: The resource name of the environment in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;.
    :type environment: str
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
    body = StopAirflowCommandRequest.from_dict(body)
    return web.Response(status=200)


async def composer_projects_locations_environments_user_workloads_config_maps_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """composer_projects_locations_environments_user_workloads_config_maps_create

    Creates a user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

    :param parent: Required. The environment name to create a ConfigMap for, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
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
    body = UserWorkloadsConfigMap.from_dict(body)
    return web.Response(status=200)


async def composer_projects_locations_environments_user_workloads_config_maps_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """composer_projects_locations_environments_user_workloads_config_maps_list

    Lists user workloads ConfigMaps. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

    :param parent: Required. List ConfigMaps in the given environment, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
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
    :param page_size: Optional. The maximum number of ConfigMaps to return.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def composer_projects_locations_environments_user_workloads_secrets_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """composer_projects_locations_environments_user_workloads_secrets_create

    Creates a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

    :param parent: Required. The environment name to create a Secret for, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
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
    body = UserWorkloadsSecret.from_dict(body)
    return web.Response(status=200)


async def composer_projects_locations_environments_user_workloads_secrets_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """composer_projects_locations_environments_user_workloads_secrets_list

    Lists user workloads Secrets. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

    :param parent: Required. List Secrets in the given environment, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
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
    :param page_size: Optional. The maximum number of Secrets to return.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def composer_projects_locations_environments_user_workloads_secrets_update(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """composer_projects_locations_environments_user_workloads_secrets_update

    Updates a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

    :param name: Identifier. The resource name of the Secret, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}\&quot;
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
    body = UserWorkloadsSecret.from_dict(body)
    return web.Response(status=200)


async def composer_projects_locations_environments_workloads_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """composer_projects_locations_environments_workloads_list

    Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

    :param parent: Required. The environment name to get workloads for, in the form: \&quot;projects/{projectId}/locations/{locationId}/environments/{environmentId}\&quot;
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
    :param filter: Optional. The list filter. Currently only supports equality on the type field. The value of a field specified in the filter expression must be one ComposerWorkloadType enum option. It&#39;s possible to get multiple types using \&quot;OR\&quot; operator, e.g.: \&quot;type&#x3D;SCHEDULER OR type&#x3D;CELERY_WORKER\&quot;. If not specified, all items are returned.
    :type filter: str
    :param page_size: Optional. The maximum number of environments to return.
    :type page_size: int
    :param page_token: Optional. The next_page_token value returned from a previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def composer_projects_locations_image_versions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_past_releases=None, page_size=None, page_token=None) -> web.Response:
    """composer_projects_locations_image_versions_list

    List ImageVersions for provided location.

    :param parent: List ImageVersions in the given project and location, in the form: \&quot;projects/{projectId}/locations/{locationId}\&quot;
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
    :param include_past_releases: Whether or not image versions from old releases should be included.
    :type include_past_releases: bool
    :param page_size: The maximum number of image_versions to return.
    :type page_size: int
    :param page_token: The next_page_token value returned from a previous List request, if any.
    :type page_token: str

    """
    return web.Response(status=200)


async def composer_projects_locations_operations_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """composer_projects_locations_operations_delete

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

    """
    return web.Response(status=200)


async def composer_projects_locations_operations_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """composer_projects_locations_operations_get

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

    """
    return web.Response(status=200)


async def composer_projects_locations_operations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """composer_projects_locations_operations_list

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
