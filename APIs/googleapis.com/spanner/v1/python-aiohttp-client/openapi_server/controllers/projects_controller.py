from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup import Backup
from openapi_server.models.batch_create_sessions_request import BatchCreateSessionsRequest
from openapi_server.models.batch_create_sessions_response import BatchCreateSessionsResponse
from openapi_server.models.batch_write_request import BatchWriteRequest
from openapi_server.models.batch_write_response import BatchWriteResponse
from openapi_server.models.begin_transaction_request import BeginTransactionRequest
from openapi_server.models.commit_request import CommitRequest
from openapi_server.models.commit_response import CommitResponse
from openapi_server.models.copy_backup_request import CopyBackupRequest
from openapi_server.models.create_database_request import CreateDatabaseRequest
from openapi_server.models.create_instance_config_request import CreateInstanceConfigRequest
from openapi_server.models.create_instance_request import CreateInstanceRequest
from openapi_server.models.create_session_request import CreateSessionRequest
from openapi_server.models.database import Database
from openapi_server.models.execute_batch_dml_request import ExecuteBatchDmlRequest
from openapi_server.models.execute_batch_dml_response import ExecuteBatchDmlResponse
from openapi_server.models.execute_sql_request import ExecuteSqlRequest
from openapi_server.models.get_database_ddl_response import GetDatabaseDdlResponse
from openapi_server.models.get_iam_policy_request import GetIamPolicyRequest
from openapi_server.models.list_backup_operations_response import ListBackupOperationsResponse
from openapi_server.models.list_backups_response import ListBackupsResponse
from openapi_server.models.list_database_operations_response import ListDatabaseOperationsResponse
from openapi_server.models.list_database_roles_response import ListDatabaseRolesResponse
from openapi_server.models.list_databases_response import ListDatabasesResponse
from openapi_server.models.list_instance_config_operations_response import ListInstanceConfigOperationsResponse
from openapi_server.models.list_instance_configs_response import ListInstanceConfigsResponse
from openapi_server.models.list_instances_response import ListInstancesResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_sessions_response import ListSessionsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.partial_result_set import PartialResultSet
from openapi_server.models.partition_query_request import PartitionQueryRequest
from openapi_server.models.partition_read_request import PartitionReadRequest
from openapi_server.models.partition_response import PartitionResponse
from openapi_server.models.policy import Policy
from openapi_server.models.read_request import ReadRequest
from openapi_server.models.restore_database_request import RestoreDatabaseRequest
from openapi_server.models.result_set import ResultSet
from openapi_server.models.rollback_request import RollbackRequest
from openapi_server.models.scan import Scan
from openapi_server.models.session import Session
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.transaction import Transaction
from openapi_server.models.update_database_ddl_request import UpdateDatabaseDdlRequest
from openapi_server import util


async def spanner_projects_instance_config_operations_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """spanner_projects_instance_config_operations_list

    Lists the user-managed instance config long-running operations in the given project. An instance config operation has a name of the form &#x60;projects//instanceConfigs//operations/&#x60;. The long-running operation metadata field type &#x60;metadata.type_url&#x60; describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations. Operations returned are ordered by &#x60;operation.metadata.value.start_time&#x60; in descending order starting from the most recently started operation.

    :param parent: Required. The project of the instance config operations. Values are of the form &#x60;projects/&#x60;.
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
    :param filter: An expression that filters the list of returned operations. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&#x3D;&#x60;, or &#x60;:&#x60;. Colon &#x60;:&#x60; is the contains operator. Filter rules are not case sensitive. The following fields in the Operation are eligible for filtering: * &#x60;name&#x60; - The name of the long-running operation * &#x60;done&#x60; - False if the operation is in progress, else true. * &#x60;metadata.@type&#x60; - the type of metadata. For example, the type string for CreateInstanceConfigMetadata is &#x60;type.googleapis.com/google.spanner.admin.instance.v1.CreateInstanceConfigMetadata&#x60;. * &#x60;metadata.&#x60; - any field in metadata.value. &#x60;metadata.@type&#x60; must be specified first, if filtering on metadata fields. * &#x60;error&#x60; - Error associated with the long-running operation. * &#x60;response.@type&#x60; - the type of response. * &#x60;response.&#x60; - any field in response.value. You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic. However, you can specify AND, OR, and NOT logic explicitly. Here are a few examples: * &#x60;done:true&#x60; - The operation is complete. * &#x60;(metadata.@type&#x3D;&#x60; \\ &#x60;type.googleapis.com/google.spanner.admin.instance.v1.CreateInstanceConfigMetadata) AND&#x60; \\ &#x60;(metadata.instance_config.name:custom-config) AND&#x60; \\ &#x60;(metadata.progress.start_time &lt; \\\&quot;2021-03-28T14:50:00Z\\\&quot;) AND&#x60; \\ &#x60;(error:*)&#x60; - Return operations where: * The operation&#39;s metadata type is CreateInstanceConfigMetadata. * The instance config name contains \&quot;custom-config\&quot;. * The operation started before 2021-03-28T14:50:00Z. * The operation resulted in an error.
    :type filter: str
    :param page_size: Number of operations to be returned in the response. If 0 or less, defaults to the server&#39;s maximum allowed page size.
    :type page_size: int
    :param page_token: If non-empty, &#x60;page_token&#x60; should contain a next_page_token from a previous ListInstanceConfigOperationsResponse to the same &#x60;parent&#x60; and with the same &#x60;filter&#x60;.
    :type page_token: str

    """
    return web.Response(status=200)


async def spanner_projects_instance_configs_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instance_configs_create

    Creates an instance config and begins preparing it to be used. The returned long-running operation can be used to track the progress of preparing the new instance config. The instance config name is assigned by the caller. If the named instance config already exists, &#x60;CreateInstanceConfig&#x60; returns &#x60;ALREADY_EXISTS&#x60;. Immediately after the request returns: * The instance config is readable via the API, with all requested attributes. The instance config&#39;s reconciling field is set to true. Its state is &#x60;CREATING&#x60;. While the operation is pending: * Cancelling the operation renders the instance config immediately unreadable via the API. * Except for deleting the creating resource, all other attempts to modify the instance config are rejected. Upon completion of the returned operation: * Instances can be created using the instance configuration. * The instance config&#39;s reconciling field becomes false. Its state becomes &#x60;READY&#x60;. The returned long-running operation will have a name of the format &#x60;/operations/&#x60; and can be used to track creation of the instance config. The metadata field type is CreateInstanceConfigMetadata. The response field type is InstanceConfig, if successful. Authorization requires &#x60;spanner.instanceConfigs.create&#x60; permission on the resource parent.

    :param parent: Required. The name of the project in which to create the instance config. Values are of the form &#x60;projects/&#x60;.
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
    body = CreateInstanceConfigRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instance_configs_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """spanner_projects_instance_configs_list

    Lists the supported instance configurations for a given project.

    :param parent: Required. The name of the project for which a list of supported instance configurations is requested. Values are of the form &#x60;projects/&#x60;.
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
    :param page_size: Number of instance configurations to be returned in the response. If 0 or less, defaults to the server&#39;s maximum allowed page size.
    :type page_size: int
    :param page_token: If non-empty, &#x60;page_token&#x60; should contain a next_page_token from a previous ListInstanceConfigsResponse.
    :type page_token: str

    """
    return web.Response(status=200)


async def spanner_projects_instances_backup_operations_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """spanner_projects_instances_backup_operations_list

    Lists the backup long-running operations in the given instance. A backup operation has a name of the form &#x60;projects//instances//backups//operations/&#x60;. The long-running operation metadata field type &#x60;metadata.type_url&#x60; describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations. Operations returned are ordered by &#x60;operation.metadata.value.progress.start_time&#x60; in descending order starting from the most recently started operation.

    :param parent: Required. The instance of the backup operations. Values are of the form &#x60;projects//instances/&#x60;.
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
    :param filter: An expression that filters the list of returned backup operations. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&#x3D;&#x60;, or &#x60;:&#x60;. Colon &#x60;:&#x60; is the contains operator. Filter rules are not case sensitive. The following fields in the operation are eligible for filtering: * &#x60;name&#x60; - The name of the long-running operation * &#x60;done&#x60; - False if the operation is in progress, else true. * &#x60;metadata.@type&#x60; - the type of metadata. For example, the type string for CreateBackupMetadata is &#x60;type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata&#x60;. * &#x60;metadata.&#x60; - any field in metadata.value. &#x60;metadata.@type&#x60; must be specified first if filtering on metadata fields. * &#x60;error&#x60; - Error associated with the long-running operation. * &#x60;response.@type&#x60; - the type of response. * &#x60;response.&#x60; - any field in response.value. You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic, but you can specify AND, OR, and NOT logic explicitly. Here are a few examples: * &#x60;done:true&#x60; - The operation is complete. * &#x60;(metadata.@type&#x3D;type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND&#x60; \\ &#x60;metadata.database:prod&#x60; - Returns operations where: * The operation&#39;s metadata type is CreateBackupMetadata. * The source database name of backup contains the string \&quot;prod\&quot;. * &#x60;(metadata.@type&#x3D;type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND&#x60; \\ &#x60;(metadata.name:howl) AND&#x60; \\ &#x60;(metadata.progress.start_time &lt; \\\&quot;2018-03-28T14:50:00Z\\\&quot;) AND&#x60; \\ &#x60;(error:*)&#x60; - Returns operations where: * The operation&#39;s metadata type is CreateBackupMetadata. * The backup name contains the string \&quot;howl\&quot;. * The operation started before 2018-03-28T14:50:00Z. * The operation resulted in an error. * &#x60;(metadata.@type&#x3D;type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND&#x60; \\ &#x60;(metadata.source_backup:test) AND&#x60; \\ &#x60;(metadata.progress.start_time &lt; \\\&quot;2022-01-18T14:50:00Z\\\&quot;) AND&#x60; \\ &#x60;(error:*)&#x60; - Returns operations where: * The operation&#39;s metadata type is CopyBackupMetadata. * The source backup name contains the string \&quot;test\&quot;. * The operation started before 2022-01-18T14:50:00Z. * The operation resulted in an error. * &#x60;((metadata.@type&#x3D;type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND&#x60; \\ &#x60;(metadata.database:test_db)) OR&#x60; \\ &#x60;((metadata.@type&#x3D;type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND&#x60; \\ &#x60;(metadata.source_backup:test_bkp)) AND&#x60; \\ &#x60;(error:*)&#x60; - Returns operations where: * The operation&#39;s metadata matches either of criteria: * The operation&#39;s metadata type is CreateBackupMetadata AND the source database name of the backup contains the string \&quot;test_db\&quot; * The operation&#39;s metadata type is CopyBackupMetadata AND the source backup name contains the string \&quot;test_bkp\&quot; * The operation resulted in an error.
    :type filter: str
    :param page_size: Number of operations to be returned in the response. If 0 or less, defaults to the server&#39;s maximum allowed page size.
    :type page_size: int
    :param page_token: If non-empty, &#x60;page_token&#x60; should contain a next_page_token from a previous ListBackupOperationsResponse to the same &#x60;parent&#x60; and with the same &#x60;filter&#x60;.
    :type page_token: str

    """
    return web.Response(status=200)


async def spanner_projects_instances_backups_copy(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_backups_copy

    Starts copying a Cloud Spanner Backup. The returned backup long-running operation will have a name of the format &#x60;projects//instances//backups//operations/&#x60; and can be used to track copying of the backup. The operation is associated with the destination backup. The metadata field type is CopyBackupMetadata. The response field type is Backup, if successful. Cancelling the returned operation will stop the copying and delete the destination backup. Concurrent CopyBackup requests can run on the same source backup.

    :param parent: Required. The name of the destination instance that will contain the backup copy. Values are of the form: &#x60;projects//instances/&#x60;.
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
    body = CopyBackupRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_backups_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, backup_id=None, encryption_config_encryption_type=None, encryption_config_kms_key_name=None, body=None) -> web.Response:
    """spanner_projects_instances_backups_create

    Starts creating a new Cloud Spanner Backup. The returned backup long-running operation will have a name of the format &#x60;projects//instances//backups//operations/&#x60; and can be used to track creation of the backup. The metadata field type is CreateBackupMetadata. The response field type is Backup, if successful. Cancelling the returned operation will stop the creation and delete the backup. There can be only one pending backup creation per database. Backup creation of different databases can run concurrently.

    :param parent: Required. The name of the instance in which the backup will be created. This must be the same instance that contains the database the backup will be created from. The backup will be stored in the location(s) specified in the instance configuration of this instance. Values are of the form &#x60;projects//instances/&#x60;.
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
    :param backup_id: Required. The id of the backup to be created. The &#x60;backup_id&#x60; appended to &#x60;parent&#x60; forms the full backup name of the form &#x60;projects//instances//backups/&#x60;.
    :type backup_id: str
    :param encryption_config_encryption_type: Required. The encryption type of the backup.
    :type encryption_config_encryption_type: str
    :param encryption_config_kms_key_name: Optional. The Cloud KMS key that will be used to protect the backup. This field should be set only when encryption_type is &#x60;CUSTOMER_MANAGED_ENCRYPTION&#x60;. Values are of the form &#x60;projects//locations//keyRings//cryptoKeys/&#x60;.
    :type encryption_config_kms_key_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = Backup.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_backups_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """spanner_projects_instances_backups_list

    Lists completed and pending backups. Backups returned are ordered by &#x60;create_time&#x60; in descending order, starting from the most recent &#x60;create_time&#x60;.

    :param parent: Required. The instance to list backups from. Values are of the form &#x60;projects//instances/&#x60;.
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
    :param filter: An expression that filters the list of returned backups. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&#x3D;&#x60;, or &#x60;:&#x60;. Colon &#x60;:&#x60; is the contains operator. Filter rules are not case sensitive. The following fields in the Backup are eligible for filtering: * &#x60;name&#x60; * &#x60;database&#x60; * &#x60;state&#x60; * &#x60;create_time&#x60; (and values are of the format YYYY-MM-DDTHH:MM:SSZ) * &#x60;expire_time&#x60; (and values are of the format YYYY-MM-DDTHH:MM:SSZ) * &#x60;version_time&#x60; (and values are of the format YYYY-MM-DDTHH:MM:SSZ) * &#x60;size_bytes&#x60; You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic, but you can specify AND, OR, and NOT logic explicitly. Here are a few examples: * &#x60;name:Howl&#x60; - The backup&#39;s name contains the string \&quot;howl\&quot;. * &#x60;database:prod&#x60; - The database&#39;s name contains the string \&quot;prod\&quot;. * &#x60;state:CREATING&#x60; - The backup is pending creation. * &#x60;state:READY&#x60; - The backup is fully created and ready for use. * &#x60;(name:howl) AND (create_time &lt; \\\&quot;2018-03-28T14:50:00Z\\\&quot;)&#x60; - The backup name contains the string \&quot;howl\&quot; and &#x60;create_time&#x60; of the backup is before 2018-03-28T14:50:00Z. * &#x60;expire_time &lt; \\\&quot;2018-03-28T14:50:00Z\\\&quot;&#x60; - The backup &#x60;expire_time&#x60; is before 2018-03-28T14:50:00Z. * &#x60;size_bytes &gt; 10000000000&#x60; - The backup&#39;s size is greater than 10GB
    :type filter: str
    :param page_size: Number of backups to be returned in the response. If 0 or less, defaults to the server&#39;s maximum allowed page size.
    :type page_size: int
    :param page_token: If non-empty, &#x60;page_token&#x60; should contain a next_page_token from a previous ListBackupsResponse to the same &#x60;parent&#x60; and with the same &#x60;filter&#x60;.
    :type page_token: str

    """
    return web.Response(status=200)


async def spanner_projects_instances_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_create

    Creates an instance and begins preparing it to begin serving. The returned long-running operation can be used to track the progress of preparing the new instance. The instance name is assigned by the caller. If the named instance already exists, &#x60;CreateInstance&#x60; returns &#x60;ALREADY_EXISTS&#x60;. Immediately upon completion of this request: * The instance is readable via the API, with all requested attributes but no allocated resources. Its state is &#x60;CREATING&#x60;. Until completion of the returned operation: * Cancelling the operation renders the instance immediately unreadable via the API. * The instance can be deleted. * All other attempts to modify the instance are rejected. Upon completion of the returned operation: * Billing for all successfully-allocated resources begins (some types may have lower than the requested levels). * Databases can be created in the instance. * The instance&#39;s allocated resource levels are readable via the API. * The instance&#39;s state becomes &#x60;READY&#x60;. The returned long-running operation will have a name of the format &#x60;/operations/&#x60; and can be used to track creation of the instance. The metadata field type is CreateInstanceMetadata. The response field type is Instance, if successful.

    :param parent: Required. The name of the project in which to create the instance. Values are of the form &#x60;projects/&#x60;.
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
    body = CreateInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_database_operations_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """spanner_projects_instances_database_operations_list

    Lists database longrunning-operations. A database operation has a name of the form &#x60;projects//instances//databases//operations/&#x60;. The long-running operation metadata field type &#x60;metadata.type_url&#x60; describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations.

    :param parent: Required. The instance of the database operations. Values are of the form &#x60;projects//instances/&#x60;.
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
    :param filter: An expression that filters the list of returned operations. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&#x3D;&#x60;, or &#x60;:&#x60;. Colon &#x60;:&#x60; is the contains operator. Filter rules are not case sensitive. The following fields in the Operation are eligible for filtering: * &#x60;name&#x60; - The name of the long-running operation * &#x60;done&#x60; - False if the operation is in progress, else true. * &#x60;metadata.@type&#x60; - the type of metadata. For example, the type string for RestoreDatabaseMetadata is &#x60;type.googleapis.com/google.spanner.admin.database.v1.RestoreDatabaseMetadata&#x60;. * &#x60;metadata.&#x60; - any field in metadata.value. &#x60;metadata.@type&#x60; must be specified first, if filtering on metadata fields. * &#x60;error&#x60; - Error associated with the long-running operation. * &#x60;response.@type&#x60; - the type of response. * &#x60;response.&#x60; - any field in response.value. You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic. However, you can specify AND, OR, and NOT logic explicitly. Here are a few examples: * &#x60;done:true&#x60; - The operation is complete. * &#x60;(metadata.@type&#x3D;type.googleapis.com/google.spanner.admin.database.v1.RestoreDatabaseMetadata) AND&#x60; \\ &#x60;(metadata.source_type:BACKUP) AND&#x60; \\ &#x60;(metadata.backup_info.backup:backup_howl) AND&#x60; \\ &#x60;(metadata.name:restored_howl) AND&#x60; \\ &#x60;(metadata.progress.start_time &lt; \\\&quot;2018-03-28T14:50:00Z\\\&quot;) AND&#x60; \\ &#x60;(error:*)&#x60; - Return operations where: * The operation&#39;s metadata type is RestoreDatabaseMetadata. * The database is restored from a backup. * The backup name contains \&quot;backup_howl\&quot;. * The restored database&#39;s name contains \&quot;restored_howl\&quot;. * The operation started before 2018-03-28T14:50:00Z. * The operation resulted in an error.
    :type filter: str
    :param page_size: Number of operations to be returned in the response. If 0 or less, defaults to the server&#39;s maximum allowed page size.
    :type page_size: int
    :param page_token: If non-empty, &#x60;page_token&#x60; should contain a next_page_token from a previous ListDatabaseOperationsResponse to the same &#x60;parent&#x60; and with the same &#x60;filter&#x60;.
    :type page_token: str

    """
    return web.Response(status=200)


async def spanner_projects_instances_databases_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_create

    Creates a new Cloud Spanner database and starts to prepare it for serving. The returned long-running operation will have a name of the format &#x60;/operations/&#x60; and can be used to track preparation of the database. The metadata field type is CreateDatabaseMetadata. The response field type is Database, if successful.

    :param parent: Required. The name of the instance that will serve the new database. Values are of the form &#x60;projects//instances/&#x60;.
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
    body = CreateDatabaseRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_database_roles_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """spanner_projects_instances_databases_database_roles_list

    Lists Cloud Spanner database roles.

    :param parent: Required. The database whose roles should be listed. Values are of the form &#x60;projects//instances//databases/&#x60;.
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
    :param page_size: Number of database roles to be returned in the response. If 0 or less, defaults to the server&#39;s maximum allowed page size.
    :type page_size: int
    :param page_token: If non-empty, &#x60;page_token&#x60; should contain a next_page_token from a previous ListDatabaseRolesResponse.
    :type page_token: str

    """
    return web.Response(status=200)


async def spanner_projects_instances_databases_database_roles_test_iam_permissions(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_database_roles_test_iam_permissions

    Returns permissions that the caller has on the specified database or backup resource. Attempting this RPC on a non-existent Cloud Spanner database will result in a NOT_FOUND error if the user has &#x60;spanner.databases.list&#x60; permission on the containing Cloud Spanner instance. Otherwise returns an empty set of permissions. Calling this method on a backup that does not exist will result in a NOT_FOUND error if the user has &#x60;spanner.backups.list&#x60; permission on the containing instance.

    :param resource: REQUIRED: The Cloud Spanner resource for which permissions are being tested. The format is &#x60;projects//instances/&#x60; for instance resources and &#x60;projects//instances//databases/&#x60; for database resources.
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


async def spanner_projects_instances_databases_drop_database(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """spanner_projects_instances_databases_drop_database

    Drops (aka deletes) a Cloud Spanner database. Completed backups for the database will be retained according to their &#x60;expire_time&#x60;. Note: Cloud Spanner might continue to accept requests for a few seconds after the database has been deleted.

    :param database: Required. The database to be dropped.
    :type database: str
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


async def spanner_projects_instances_databases_get_ddl(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """spanner_projects_instances_databases_get_ddl

    Returns the schema of a Cloud Spanner database as a list of formatted DDL statements. This method does not show pending schema updates, those may be queried using the Operations API.

    :param database: Required. The database whose schema we wish to get. Values are of the form &#x60;projects//instances//databases/&#x60;
    :type database: str
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


async def spanner_projects_instances_databases_get_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_get_iam_policy

    Gets the access control policy for a database or backup resource. Returns an empty policy if a database or backup exists but does not have a policy set. Authorization requires &#x60;spanner.databases.getIamPolicy&#x60; permission on resource. For backups, authorization requires &#x60;spanner.backups.getIamPolicy&#x60; permission on resource.

    :param resource: REQUIRED: The Cloud Spanner resource for which the policy is being retrieved. The format is &#x60;projects//instances/&#x60; for instance resources and &#x60;projects//instances//databases/&#x60; for database resources.
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


async def spanner_projects_instances_databases_get_scans(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, end_time=None, start_time=None, view=None) -> web.Response:
    """spanner_projects_instances_databases_get_scans

    Request a specific scan with Database-specific data for Cloud Key Visualizer.

    :param name: Required. The unique name of the scan containing the requested information, specific to the Database service implementing this interface.
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
    :param end_time: The upper bound for the time range to retrieve Scan data for.
    :type end_time: str
    :param start_time: These fields restrict the Database-specific information returned in the &#x60;Scan.data&#x60; field. If a &#x60;View&#x60; is provided that does not include the &#x60;Scan.data&#x60; field, these are ignored. This range of time must be entirely contained within the defined time range of the targeted scan. The lower bound for the time range to retrieve Scan data for.
    :type start_time: str
    :param view: Specifies which parts of the Scan should be returned in the response. Note, if left unspecified, the FULL view is assumed.
    :type view: str

    """
    return web.Response(status=200)


async def spanner_projects_instances_databases_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """spanner_projects_instances_databases_list

    Lists Cloud Spanner databases.

    :param parent: Required. The instance whose databases should be listed. Values are of the form &#x60;projects//instances/&#x60;.
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
    :param page_size: Number of databases to be returned in the response. If 0 or less, defaults to the server&#39;s maximum allowed page size.
    :type page_size: int
    :param page_token: If non-empty, &#x60;page_token&#x60; should contain a next_page_token from a previous ListDatabasesResponse.
    :type page_token: str

    """
    return web.Response(status=200)


async def spanner_projects_instances_databases_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_patch

    Updates a Cloud Spanner database. The returned long-running operation can be used to track the progress of updating the database. If the named database does not exist, returns &#x60;NOT_FOUND&#x60;. While the operation is pending: * The database&#39;s reconciling field is set to true. * Cancelling the operation is best-effort. If the cancellation succeeds, the operation metadata&#39;s cancel_time is set, the updates are reverted, and the operation terminates with a &#x60;CANCELLED&#x60; status. * New UpdateDatabase requests will return a &#x60;FAILED_PRECONDITION&#x60; error until the pending operation is done (returns successfully or with error). * Reading the database via the API continues to give the pre-request values. Upon completion of the returned operation: * The new values are in effect and readable via the API. * The database&#39;s reconciling field becomes false. The returned long-running operation will have a name of the format &#x60;projects//instances//databases//operations/&#x60; and can be used to track the database modification. The metadata field type is UpdateDatabaseMetadata. The response field type is Database, if successful.

    :param name: Required. The name of the database. Values are of the form &#x60;projects//instances//databases/&#x60;, where &#x60;&#x60; is as specified in the &#x60;CREATE DATABASE&#x60; statement. This name can be passed to other API methods to identify the database.
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
    :param update_mask: Required. The list of fields to update. Currently, only &#x60;enable_drop_protection&#x60; field can be updated.
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Database.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_restore(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_restore

    Create a new database by restoring from a completed backup. The new database must be in the same project and in an instance with the same instance configuration as the instance containing the backup. The returned database long-running operation has a name of the format &#x60;projects//instances//databases//operations/&#x60;, and can be used to track the progress of the operation, and to cancel it. The metadata field type is RestoreDatabaseMetadata. The response type is Database, if successful. Cancelling the returned operation will stop the restore and delete the database. There can be only one database being restored into an instance at a time. Once the restore operation completes, a new restore operation can be initiated, without waiting for the optimize operation associated with the first restore to complete.

    :param parent: Required. The name of the instance in which to create the restored database. This instance must be in the same project and have the same instance configuration as the instance containing the source backup. Values are of the form &#x60;projects//instances/&#x60;.
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
    body = RestoreDatabaseRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_batch_create(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_batch_create

    Creates multiple new sessions. This API can be used to initialize a session cache on the clients. See https://goo.gl/TgSFN2 for best practices on session cache management.

    :param database: Required. The database in which the new sessions are created.
    :type database: str
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
    body = BatchCreateSessionsRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_batch_write(request: web.Request, session, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_batch_write

    Batches the supplied mutation groups in a collection of efficient transactions. All mutations in a group are committed atomically. However, mutations across groups can be committed non-atomically in an unspecified order and thus, they must be independent of each other. Partial failure is possible, i.e., some groups may have been committed successfully, while some may have failed. The results of individual batches are streamed into the response as the batches are applied. BatchWrite requests are not replay protected, meaning that each mutation group may be applied more than once. Replays of non-idempotent mutations may have undesirable effects. For example, replays of an insert mutation may produce an already exists error or if you use generated or commit timestamp-based keys, it may result in additional rows being added to the mutation&#39;s table. We recommend structuring your mutation groups to be idempotent to avoid this issue.

    :param session: Required. The session in which the batch request is to be run.
    :type session: str
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
    body = BatchWriteRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_begin_transaction(request: web.Request, session, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_begin_transaction

    Begins a new transaction. This step can often be skipped: Read, ExecuteSql and Commit can begin a new transaction as a side-effect.

    :param session: Required. The session in which the transaction runs.
    :type session: str
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
    body = BeginTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_commit(request: web.Request, session, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_commit

    Commits a transaction. The request includes the mutations to be applied to rows in the database. &#x60;Commit&#x60; might return an &#x60;ABORTED&#x60; error. This can occur at any time; commonly, the cause is conflicts with concurrent transactions. However, it can also happen for a variety of other reasons. If &#x60;Commit&#x60; returns &#x60;ABORTED&#x60;, the caller should re-attempt the transaction from the beginning, re-using the same session. On very rare occasions, &#x60;Commit&#x60; might return &#x60;UNKNOWN&#x60;. This can happen, for example, if the client job experiences a 1+ hour networking failure. At that point, Cloud Spanner has lost track of the transaction outcome and we recommend that you perform another read from the database to see the state of things as they are now.

    :param session: Required. The session in which the transaction to be committed is running.
    :type session: str
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
    body = CommitRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_create(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_create

    Creates a new session. A session can be used to perform transactions that read and/or modify data in a Cloud Spanner database. Sessions are meant to be reused for many consecutive transactions. Sessions can only execute one transaction at a time. To execute multiple concurrent read-write/write-only transactions, create multiple sessions. Note that standalone reads and queries use a transaction internally, and count toward the one transaction limit. Active sessions use additional server resources, so it is a good idea to delete idle and unneeded sessions. Aside from explicit deletes, Cloud Spanner may delete sessions for which no operations are sent for more than an hour. If a session is deleted, requests to it return &#x60;NOT_FOUND&#x60;. Idle sessions can be kept alive by sending a trivial SQL query periodically, e.g., &#x60;\&quot;SELECT 1\&quot;&#x60;.

    :param database: Required. The database in which the new session is created.
    :type database: str
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
    body = CreateSessionRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_execute_batch_dml(request: web.Request, session, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_execute_batch_dml

    Executes a batch of SQL DML statements. This method allows many statements to be run with lower latency than submitting them sequentially with ExecuteSql. Statements are executed in sequential order. A request can succeed even if a statement fails. The ExecuteBatchDmlResponse.status field in the response provides information about the statement that failed. Clients must inspect this field to determine whether an error occurred. Execution stops after the first failed statement; the remaining statements are not executed.

    :param session: Required. The session in which the DML statements should be performed.
    :type session: str
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
    body = ExecuteBatchDmlRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_execute_sql(request: web.Request, session, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_execute_sql

    Executes an SQL statement, returning all results in a single reply. This method cannot be used to return a result set larger than 10 MiB; if the query yields more data than that, the query fails with a &#x60;FAILED_PRECONDITION&#x60; error. Operations inside read-write transactions might return &#x60;ABORTED&#x60;. If this occurs, the application should restart the transaction from the beginning. See Transaction for more details. Larger result sets can be fetched in streaming fashion by calling ExecuteStreamingSql instead.

    :param session: Required. The session in which the SQL query should be performed.
    :type session: str
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
    body = ExecuteSqlRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_execute_streaming_sql(request: web.Request, session, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_execute_streaming_sql

    Like ExecuteSql, except returns the result set as a stream. Unlike ExecuteSql, there is no limit on the size of the returned result set. However, no individual row in the result set can exceed 100 MiB, and no column value can exceed 10 MiB.

    :param session: Required. The session in which the SQL query should be performed.
    :type session: str
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
    body = ExecuteSqlRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_list(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_list

    Lists all sessions in a given database.

    :param database: Required. The database in which to list sessions.
    :type database: str
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
    :param filter: An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are: * &#x60;labels.key&#x60; where key is the name of a label Some examples of using filters are: * &#x60;labels.env:*&#x60; --&gt; The session has the label \&quot;env\&quot;. * &#x60;labels.env:dev&#x60; --&gt; The session has the label \&quot;env\&quot; and the value of the label contains the string \&quot;dev\&quot;.
    :type filter: str
    :param page_size: Number of sessions to be returned in the response. If 0 or less, defaults to the server&#39;s maximum allowed page size.
    :type page_size: int
    :param page_token: If non-empty, &#x60;page_token&#x60; should contain a next_page_token from a previous ListSessionsResponse.
    :type page_token: str

    """
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_partition_query(request: web.Request, session, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_partition_query

    Creates a set of partition tokens that can be used to execute a query operation in parallel. Each of the returned partition tokens can be used by ExecuteStreamingSql to specify a subset of the query result to read. The same session and read-only transaction must be used by the PartitionQueryRequest used to create the partition tokens and the ExecuteSqlRequests that use the partition tokens. Partition tokens become invalid when the session used to create them is deleted, is idle for too long, begins a new transaction, or becomes too old. When any of these happen, it is not possible to resume the query, and the whole operation must be restarted from the beginning.

    :param session: Required. The session used to create the partitions.
    :type session: str
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
    body = PartitionQueryRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_partition_read(request: web.Request, session, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_partition_read

    Creates a set of partition tokens that can be used to execute a read operation in parallel. Each of the returned partition tokens can be used by StreamingRead to specify a subset of the read result to read. The same session and read-only transaction must be used by the PartitionReadRequest used to create the partition tokens and the ReadRequests that use the partition tokens. There are no ordering guarantees on rows returned among the returned partition tokens, or even within each individual StreamingRead call issued with a partition_token. Partition tokens become invalid when the session used to create them is deleted, is idle for too long, begins a new transaction, or becomes too old. When any of these happen, it is not possible to resume the read, and the whole operation must be restarted from the beginning.

    :param session: Required. The session used to create the partitions.
    :type session: str
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
    body = PartitionReadRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_read(request: web.Request, session, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_read

    Reads rows from the database using key lookups and scans, as a simple key/value style alternative to ExecuteSql. This method cannot be used to return a result set larger than 10 MiB; if the read matches more data than that, the read fails with a &#x60;FAILED_PRECONDITION&#x60; error. Reads inside read-write transactions might return &#x60;ABORTED&#x60;. If this occurs, the application should restart the transaction from the beginning. See Transaction for more details. Larger result sets can be yielded in streaming fashion by calling StreamingRead instead.

    :param session: Required. The session in which the read should be performed.
    :type session: str
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
    body = ReadRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_rollback(request: web.Request, session, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_rollback

    Rolls back a transaction, releasing any locks it holds. It is a good idea to call this for any transaction that includes one or more Read or ExecuteSql requests and ultimately decides not to commit. &#x60;Rollback&#x60; returns &#x60;OK&#x60; if it successfully aborts the transaction, the transaction was already aborted, or the transaction is not found. &#x60;Rollback&#x60; never returns &#x60;ABORTED&#x60;.

    :param session: Required. The session in which the transaction to roll back is running.
    :type session: str
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
    body = RollbackRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_sessions_streaming_read(request: web.Request, session, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_sessions_streaming_read

    Like Read, except returns the result set as a stream. Unlike Read, there is no limit on the size of the returned result set. However, no individual row in the result set can exceed 100 MiB, and no column value can exceed 10 MiB.

    :param session: Required. The session in which the read should be performed.
    :type session: str
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
    body = ReadRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_databases_set_iam_policy(request: web.Request, resource, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_set_iam_policy

    Sets the access control policy on a database or backup resource. Replaces any existing policy. Authorization requires &#x60;spanner.databases.setIamPolicy&#x60; permission on resource. For backups, authorization requires &#x60;spanner.backups.setIamPolicy&#x60; permission on resource.

    :param resource: REQUIRED: The Cloud Spanner resource for which the policy is being set. The format is &#x60;projects//instances/&#x60; for instance resources and &#x60;projects//instances//databases/&#x60; for databases resources.
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


async def spanner_projects_instances_databases_update_ddl(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """spanner_projects_instances_databases_update_ddl

    Updates the schema of a Cloud Spanner database by creating/altering/dropping tables, columns, indexes, etc. The returned long-running operation will have a name of the format &#x60;/operations/&#x60; and can be used to track execution of the schema change(s). The metadata field type is UpdateDatabaseDdlMetadata. The operation has no response.

    :param database: Required. The database to update.
    :type database: str
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
    body = UpdateDatabaseDdlRequest.from_dict(body)
    return web.Response(status=200)


async def spanner_projects_instances_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, instance_deadline=None, page_size=None, page_token=None) -> web.Response:
    """spanner_projects_instances_list

    Lists all instances in the given project.

    :param parent: Required. The name of the project for which a list of instances is requested. Values are of the form &#x60;projects/&#x60;.
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
    :param filter: An expression for filtering the results of the request. Filter rules are case insensitive. The fields eligible for filtering are: * &#x60;name&#x60; * &#x60;display_name&#x60; * &#x60;labels.key&#x60; where key is the name of a label Some examples of using filters are: * &#x60;name:*&#x60; --&gt; The instance has a name. * &#x60;name:Howl&#x60; --&gt; The instance&#39;s name contains the string \&quot;howl\&quot;. * &#x60;name:HOWL&#x60; --&gt; Equivalent to above. * &#x60;NAME:howl&#x60; --&gt; Equivalent to above. * &#x60;labels.env:*&#x60; --&gt; The instance has the label \&quot;env\&quot;. * &#x60;labels.env:dev&#x60; --&gt; The instance has the label \&quot;env\&quot; and the value of the label contains the string \&quot;dev\&quot;. * &#x60;name:howl labels.env:dev&#x60; --&gt; The instance&#39;s name contains \&quot;howl\&quot; and it has the label \&quot;env\&quot; with its value containing \&quot;dev\&quot;.
    :type filter: str
    :param instance_deadline: Deadline used while retrieving metadata for instances. Instances whose metadata cannot be retrieved within this deadline will be added to unreachable in ListInstancesResponse.
    :type instance_deadline: str
    :param page_size: Number of instances to be returned in the response. If 0 or less, defaults to the server&#39;s maximum allowed page size.
    :type page_size: int
    :param page_token: If non-empty, &#x60;page_token&#x60; should contain a next_page_token from a previous ListInstancesResponse.
    :type page_token: str

    """
    return web.Response(status=200)


async def spanner_projects_instances_operations_cancel(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """spanner_projects_instances_operations_cancel

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

    """
    return web.Response(status=200)


async def spanner_projects_instances_operations_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, etag=None, validate_only=None) -> web.Response:
    """spanner_projects_instances_operations_delete

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
    :param etag: Used for optimistic concurrency control as a way to help prevent simultaneous deletes of an instance config from overwriting each other. If not empty, the API only deletes the instance config when the etag provided matches the current status of the requested instance config. Otherwise, deletes the instance config without checking the current status of the requested instance config.
    :type etag: str
    :param validate_only: An option to validate, but not actually execute, a request, and provide the same response.
    :type validate_only: bool

    """
    return web.Response(status=200)


async def spanner_projects_instances_operations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """spanner_projects_instances_operations_list

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
