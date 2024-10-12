from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_lf_tags_to_resource_request import AddLFTagsToResourceRequest
from openapi_server.models.add_lf_tags_to_resource_response import AddLFTagsToResourceResponse
from openapi_server.models.assume_decorated_role_with_saml_request import AssumeDecoratedRoleWithSAMLRequest
from openapi_server.models.assume_decorated_role_with_saml_response import AssumeDecoratedRoleWithSAMLResponse
from openapi_server.models.batch_grant_permissions_request import BatchGrantPermissionsRequest
from openapi_server.models.batch_grant_permissions_response import BatchGrantPermissionsResponse
from openapi_server.models.batch_revoke_permissions_request import BatchRevokePermissionsRequest
from openapi_server.models.batch_revoke_permissions_response import BatchRevokePermissionsResponse
from openapi_server.models.cancel_transaction_request import CancelTransactionRequest
from openapi_server.models.commit_transaction_request import CommitTransactionRequest
from openapi_server.models.commit_transaction_response import CommitTransactionResponse
from openapi_server.models.create_data_cells_filter_request import CreateDataCellsFilterRequest
from openapi_server.models.create_lf_tag_request import CreateLFTagRequest
from openapi_server.models.delete_data_cells_filter_request import DeleteDataCellsFilterRequest
from openapi_server.models.delete_lf_tag_request import DeleteLFTagRequest
from openapi_server.models.delete_objects_on_cancel_request import DeleteObjectsOnCancelRequest
from openapi_server.models.deregister_resource_request import DeregisterResourceRequest
from openapi_server.models.describe_resource_request import DescribeResourceRequest
from openapi_server.models.describe_resource_response import DescribeResourceResponse
from openapi_server.models.describe_transaction_request import DescribeTransactionRequest
from openapi_server.models.describe_transaction_response import DescribeTransactionResponse
from openapi_server.models.extend_transaction_request import ExtendTransactionRequest
from openapi_server.models.get_data_cells_filter_request import GetDataCellsFilterRequest
from openapi_server.models.get_data_cells_filter_response import GetDataCellsFilterResponse
from openapi_server.models.get_data_lake_settings_request import GetDataLakeSettingsRequest
from openapi_server.models.get_data_lake_settings_response import GetDataLakeSettingsResponse
from openapi_server.models.get_effective_permissions_for_path_request import GetEffectivePermissionsForPathRequest
from openapi_server.models.get_effective_permissions_for_path_response import GetEffectivePermissionsForPathResponse
from openapi_server.models.get_lf_tag_request import GetLFTagRequest
from openapi_server.models.get_lf_tag_response import GetLFTagResponse
from openapi_server.models.get_query_state_request import GetQueryStateRequest
from openapi_server.models.get_query_state_response import GetQueryStateResponse
from openapi_server.models.get_query_statistics_response import GetQueryStatisticsResponse
from openapi_server.models.get_resource_lf_tags_request import GetResourceLFTagsRequest
from openapi_server.models.get_resource_lf_tags_response import GetResourceLFTagsResponse
from openapi_server.models.get_table_objects_request import GetTableObjectsRequest
from openapi_server.models.get_table_objects_response import GetTableObjectsResponse
from openapi_server.models.get_temporary_glue_partition_credentials_request import GetTemporaryGluePartitionCredentialsRequest
from openapi_server.models.get_temporary_glue_partition_credentials_response import GetTemporaryGluePartitionCredentialsResponse
from openapi_server.models.get_temporary_glue_table_credentials_request import GetTemporaryGlueTableCredentialsRequest
from openapi_server.models.get_temporary_glue_table_credentials_response import GetTemporaryGlueTableCredentialsResponse
from openapi_server.models.get_work_unit_results_request import GetWorkUnitResultsRequest
from openapi_server.models.get_work_unit_results_response import GetWorkUnitResultsResponse
from openapi_server.models.get_work_units_request import GetWorkUnitsRequest
from openapi_server.models.get_work_units_response import GetWorkUnitsResponse
from openapi_server.models.grant_permissions_request import GrantPermissionsRequest
from openapi_server.models.list_data_cells_filter_request import ListDataCellsFilterRequest
from openapi_server.models.list_data_cells_filter_response import ListDataCellsFilterResponse
from openapi_server.models.list_lf_tags_request import ListLFTagsRequest
from openapi_server.models.list_lf_tags_response import ListLFTagsResponse
from openapi_server.models.list_permissions_request import ListPermissionsRequest
from openapi_server.models.list_permissions_response import ListPermissionsResponse
from openapi_server.models.list_resources_request import ListResourcesRequest
from openapi_server.models.list_resources_response import ListResourcesResponse
from openapi_server.models.list_table_storage_optimizers_request import ListTableStorageOptimizersRequest
from openapi_server.models.list_table_storage_optimizers_response import ListTableStorageOptimizersResponse
from openapi_server.models.list_transactions_request import ListTransactionsRequest
from openapi_server.models.list_transactions_response import ListTransactionsResponse
from openapi_server.models.put_data_lake_settings_request import PutDataLakeSettingsRequest
from openapi_server.models.register_resource_request import RegisterResourceRequest
from openapi_server.models.remove_lf_tags_from_resource_request import RemoveLFTagsFromResourceRequest
from openapi_server.models.remove_lf_tags_from_resource_response import RemoveLFTagsFromResourceResponse
from openapi_server.models.revoke_permissions_request import RevokePermissionsRequest
from openapi_server.models.search_databases_by_lf_tags_request import SearchDatabasesByLFTagsRequest
from openapi_server.models.search_databases_by_lf_tags_response import SearchDatabasesByLFTagsResponse
from openapi_server.models.search_tables_by_lf_tags_request import SearchTablesByLFTagsRequest
from openapi_server.models.search_tables_by_lf_tags_response import SearchTablesByLFTagsResponse
from openapi_server.models.start_query_planning_request import StartQueryPlanningRequest
from openapi_server.models.start_query_planning_response import StartQueryPlanningResponse
from openapi_server.models.start_transaction_request import StartTransactionRequest
from openapi_server.models.start_transaction_response import StartTransactionResponse
from openapi_server.models.update_lf_tag_request import UpdateLFTagRequest
from openapi_server.models.update_resource_request import UpdateResourceRequest
from openapi_server.models.update_table_objects_request import UpdateTableObjectsRequest
from openapi_server.models.update_table_storage_optimizer_request import UpdateTableStorageOptimizerRequest
from openapi_server.models.update_table_storage_optimizer_response import UpdateTableStorageOptimizerResponse
from openapi_server import util


async def add_lf_tags_to_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_lf_tags_to_resource

    Attaches one or more LF-tags to an existing resource.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AddLFTagsToResourceRequest.from_dict(body)
    return web.Response(status=200)


async def assume_decorated_role_with_saml(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """assume_decorated_role_with_saml

    &lt;p&gt;Allows a caller to assume an IAM role decorated as the SAML user specified in the SAML assertion included in the request. This decoration allows Lake Formation to enforce access policies against the SAML users and groups. This API operation requires SAML federation setup in the caller’s account as it can only be called with valid SAML assertions. Lake Formation does not scope down the permission of the assumed role. All permissions attached to the role via the SAML federation setup will be included in the role session. &lt;/p&gt; &lt;p&gt; This decorated role is expected to access data in Amazon S3 by getting temporary access from Lake Formation which is authorized via the virtual API &lt;code&gt;GetDataAccess&lt;/code&gt;. Therefore, all SAML roles that can be assumed via &lt;code&gt;AssumeDecoratedRoleWithSAML&lt;/code&gt; must at a minimum include &lt;code&gt;lakeformation:GetDataAccess&lt;/code&gt; in their role policies. A typical IAM policy attached to such a role would look as follows: &lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssumeDecoratedRoleWithSAMLRequest.from_dict(body)
    return web.Response(status=200)


async def batch_grant_permissions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_grant_permissions

    Batch operation to grant permissions to the principal.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchGrantPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def batch_revoke_permissions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_revoke_permissions

    Batch operation to revoke permissions from the principal.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchRevokePermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_transaction(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_transaction

    Attempts to cancel the specified transaction. Returns an exception if the transaction was previously committed.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CancelTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def commit_transaction(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """commit_transaction

    Attempts to commit the specified transaction. Returns an exception if the transaction was previously aborted. This API action is idempotent if called multiple times for the same transaction.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CommitTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def create_data_cells_filter(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_data_cells_filter

    Creates a data cell filter to allow one to grant access to certain columns on certain rows.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateDataCellsFilterRequest.from_dict(body)
    return web.Response(status=200)


async def create_lf_tag(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_lf_tag

    Creates an LF-tag with the specified name and values.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateLFTagRequest.from_dict(body)
    return web.Response(status=200)


async def delete_data_cells_filter(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_data_cells_filter

    Deletes a data cell filter.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteDataCellsFilterRequest.from_dict(body)
    return web.Response(status=200)


async def delete_lf_tag(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_lf_tag

    Deletes the specified LF-tag given a key name. If the input parameter tag key was not found, then the operation will throw an exception. When you delete an LF-tag, the &lt;code&gt;LFTagPolicy&lt;/code&gt; attached to the LF-tag becomes invalid. If the deleted LF-tag was still assigned to any resource, the tag policy attach to the deleted LF-tag will no longer be applied to the resource.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteLFTagRequest.from_dict(body)
    return web.Response(status=200)


async def delete_objects_on_cancel(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_objects_on_cancel

    &lt;p&gt;For a specific governed table, provides a list of Amazon S3 objects that will be written during the current transaction and that can be automatically deleted if the transaction is canceled. Without this call, no Amazon S3 objects are automatically deleted when a transaction cancels. &lt;/p&gt; &lt;p&gt; The Glue ETL library function &lt;code&gt;write_dynamic_frame.from_catalog()&lt;/code&gt; includes an option to automatically call &lt;code&gt;DeleteObjectsOnCancel&lt;/code&gt; before writes. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lake-formation/latest/dg/transactions-data-operations.html#rolling-back-writes\&quot;&gt;Rolling Back Amazon S3 Writes&lt;/a&gt;. &lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteObjectsOnCancelRequest.from_dict(body)
    return web.Response(status=200)


async def deregister_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_resource

    &lt;p&gt;Deregisters the resource as managed by the Data Catalog.&lt;/p&gt; &lt;p&gt;When you deregister a path, Lake Formation removes the path from the inline policy attached to your service-linked role.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeregisterResourceRequest.from_dict(body)
    return web.Response(status=200)


async def describe_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_resource

    Retrieves the current data access role for the given resource registered in Lake Formation.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeResourceRequest.from_dict(body)
    return web.Response(status=200)


async def describe_transaction(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_transaction

    Returns the details of a single transaction.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def extend_transaction(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """extend_transaction

    &lt;p&gt;Indicates to the service that the specified transaction is still active and should not be treated as idle and aborted.&lt;/p&gt; &lt;p&gt;Write transactions that remain idle for a long period are automatically aborted unless explicitly extended.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ExtendTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def get_data_cells_filter(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_data_cells_filter

    Returns a data cells filter.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetDataCellsFilterRequest.from_dict(body)
    return web.Response(status=200)


async def get_data_lake_settings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_data_lake_settings

    Retrieves the list of the data lake administrators of a Lake Formation-managed data lake. 

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetDataLakeSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def get_effective_permissions_for_path(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_effective_permissions_for_path

    Returns the Lake Formation permissions for a specified table or database resource located at a path in Amazon S3. &lt;code&gt;GetEffectivePermissionsForPath&lt;/code&gt; will not return databases and tables if the catalog is encrypted.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = GetEffectivePermissionsForPathRequest.from_dict(body)
    return web.Response(status=200)


async def get_lf_tag(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_lf_tag

    Returns an LF-tag definition.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetLFTagRequest.from_dict(body)
    return web.Response(status=200)


async def get_query_state(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_query_state

    Returns the state of a query previously submitted. Clients are expected to poll &lt;code&gt;GetQueryState&lt;/code&gt; to monitor the current state of the planning before retrieving the work units. A query state is only visible to the principal that made the initial call to &lt;code&gt;StartQueryPlanning&lt;/code&gt;.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetQueryStateRequest.from_dict(body)
    return web.Response(status=200)


async def get_query_statistics(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_query_statistics

    Retrieves statistics on the planning and execution of a query.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetQueryStateRequest.from_dict(body)
    return web.Response(status=200)


async def get_resource_lf_tags(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_resource_lf_tags

    Returns the LF-tags applied to a resource.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetResourceLFTagsRequest.from_dict(body)
    return web.Response(status=200)


async def get_table_objects(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_table_objects

    Returns the set of Amazon S3 objects that make up the specified governed table. A transaction ID or timestamp can be specified for time-travel queries.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = GetTableObjectsRequest.from_dict(body)
    return web.Response(status=200)


async def get_temporary_glue_partition_credentials(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_temporary_glue_partition_credentials

    This API is identical to &lt;code&gt;GetTemporaryTableCredentials&lt;/code&gt; except that this is used when the target Data Catalog resource is of type Partition. Lake Formation restricts the permission of the vended credentials with the same scope down policy which restricts access to a single Amazon S3 prefix.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetTemporaryGluePartitionCredentialsRequest.from_dict(body)
    return web.Response(status=200)


async def get_temporary_glue_table_credentials(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_temporary_glue_table_credentials

    Allows a caller in a secure environment to assume a role with permission to access Amazon S3. In order to vend such credentials, Lake Formation assumes the role associated with a registered location, for example an Amazon S3 bucket, with a scope down policy which restricts the access to a single prefix.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetTemporaryGlueTableCredentialsRequest.from_dict(body)
    return web.Response(status=200)


async def get_work_unit_results(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_work_unit_results

    Returns the work units resulting from the query. Work units can be executed in any order and in parallel. 

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetWorkUnitResultsRequest.from_dict(body)
    return web.Response(status=200)


async def get_work_units(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, page_size=None, next_token=None) -> web.Response:
    """get_work_units

    Retrieves the work units generated by the &lt;code&gt;StartQueryPlanning&lt;/code&gt; operation.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param page_size: Pagination limit
    :type page_size: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = GetWorkUnitsRequest.from_dict(body)
    return web.Response(status=200)


async def grant_permissions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """grant_permissions

    &lt;p&gt;Grants permissions to the principal to access metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3.&lt;/p&gt; &lt;p&gt;For information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html\&quot;&gt;Security and Access Control to Metadata and Data&lt;/a&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GrantPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_data_cells_filter(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_data_cells_filter

    Lists all the data cell filters on a table.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListDataCellsFilterRequest.from_dict(body)
    return web.Response(status=200)


async def list_lf_tags(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_lf_tags

    Lists LF-tags that the requester has permission to view. 

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListLFTagsRequest.from_dict(body)
    return web.Response(status=200)


async def list_permissions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_permissions

    &lt;p&gt;Returns a list of the principal permissions on the resource, filtered by the permissions of the caller. For example, if you are granted an ALTER permission, you are able to see only the principal permissions for ALTER.&lt;/p&gt; &lt;p&gt;This operation returns only those permissions that have been explicitly granted.&lt;/p&gt; &lt;p&gt;For information about permissions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html\&quot;&gt;Security and Access Control to Metadata and Data&lt;/a&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_resources(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_resources

    Lists the resources registered to be managed by the Data Catalog.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def list_table_storage_optimizers(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_table_storage_optimizers

    Returns the configuration of all storage optimizers associated with a specified table.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTableStorageOptimizersRequest.from_dict(body)
    return web.Response(status=200)


async def list_transactions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_transactions

    &lt;p&gt;Returns metadata about transactions and their status. To prevent the response from growing indefinitely, only uncommitted transactions and those available for time-travel queries are returned.&lt;/p&gt; &lt;p&gt;This operation can help you identify uncommitted transactions or to get information about transactions.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTransactionsRequest.from_dict(body)
    return web.Response(status=200)


async def put_data_lake_settings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_data_lake_settings

    &lt;p&gt;Sets the list of data lake administrators who have admin privileges on all resources managed by Lake Formation. For more information on admin privileges, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lake-formation/latest/dg/lake-formation-permissions.html\&quot;&gt;Granting Lake Formation Permissions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This API replaces the current list of data lake admins with the new list being passed. To add an admin, fetch the current list and add the new admin to that list and pass that list in this API.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutDataLakeSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def register_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_resource

    &lt;p&gt;Registers the resource as managed by the Data Catalog.&lt;/p&gt; &lt;p&gt;To add or update data, Lake Formation needs read/write access to the chosen Amazon S3 path. Choose a role that you know has permission to do this, or choose the AWSServiceRoleForLakeFormationDataAccess service-linked role. When you register the first Amazon S3 path, the service-linked role and a new inline policy are created on your behalf. Lake Formation adds the first path to the inline policy and attaches it to the service-linked role. When you register subsequent paths, Lake Formation adds the path to the existing policy.&lt;/p&gt; &lt;p&gt;The following request registers a new location and gives Lake Formation permission to use the service-linked role to access that location.&lt;/p&gt; &lt;p&gt; &lt;code&gt;ResourceArn &#x3D; arn:aws:s3:::my-bucket UseServiceLinkedRole &#x3D; true&lt;/code&gt; &lt;/p&gt; &lt;p&gt;If &lt;code&gt;UseServiceLinkedRole&lt;/code&gt; is not set to true, you must provide or set the &lt;code&gt;RoleArn&lt;/code&gt;:&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:aws:iam::12345:role/my-data-access-role&lt;/code&gt; &lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RegisterResourceRequest.from_dict(body)
    return web.Response(status=200)


async def remove_lf_tags_from_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_lf_tags_from_resource

    Removes an LF-tag from the resource. Only database, table, or tableWithColumns resource are allowed. To tag columns, use the column inclusion list in &lt;code&gt;tableWithColumns&lt;/code&gt; to specify column input.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RemoveLFTagsFromResourceRequest.from_dict(body)
    return web.Response(status=200)


async def revoke_permissions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """revoke_permissions

    Revokes permissions to the principal to access metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RevokePermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def search_databases_by_lf_tags(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_databases_by_lf_tags

    This operation allows a search on &lt;code&gt;DATABASE&lt;/code&gt; resources by &lt;code&gt;TagCondition&lt;/code&gt;. This operation is used by admins who want to grant user permissions on certain &lt;code&gt;TagConditions&lt;/code&gt;. Before making a grant, the admin can use &lt;code&gt;SearchDatabasesByTags&lt;/code&gt; to find all resources where the given &lt;code&gt;TagConditions&lt;/code&gt; are valid to verify whether the returned resources can be shared.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = SearchDatabasesByLFTagsRequest.from_dict(body)
    return web.Response(status=200)


async def search_tables_by_lf_tags(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """search_tables_by_lf_tags

    This operation allows a search on &lt;code&gt;TABLE&lt;/code&gt; resources by &lt;code&gt;LFTag&lt;/code&gt;s. This will be used by admins who want to grant user permissions on certain LF-tags. Before making a grant, the admin can use &lt;code&gt;SearchTablesByLFTags&lt;/code&gt; to find all resources where the given &lt;code&gt;LFTag&lt;/code&gt;s are valid to verify whether the returned resources can be shared.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = SearchTablesByLFTagsRequest.from_dict(body)
    return web.Response(status=200)


async def start_query_planning(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_query_planning

    &lt;p&gt;Submits a request to process a query statement.&lt;/p&gt; &lt;p&gt;This operation generates work units that can be retrieved with the &lt;code&gt;GetWorkUnits&lt;/code&gt; operation as soon as the query state is WORKUNITS_AVAILABLE or FINISHED.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartQueryPlanningRequest.from_dict(body)
    return web.Response(status=200)


async def start_transaction(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_transaction

    Starts a new transaction and returns its transaction ID. Transaction IDs are opaque objects that you can use to identify a transaction.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def update_data_cells_filter(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_data_cells_filter

    Updates a data cell filter.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateDataCellsFilterRequest.from_dict(body)
    return web.Response(status=200)


async def update_lf_tag(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_lf_tag

    Updates the list of possible values for the specified LF-tag key. If the LF-tag does not exist, the operation throws an EntityNotFoundException. The values in the delete key values will be deleted from list of possible values. If any value in the delete key values is attached to a resource, then API errors out with a 400 Exception - \&quot;Update not allowed\&quot;. Untag the attribute before deleting the LF-tag key&#39;s value. 

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateLFTagRequest.from_dict(body)
    return web.Response(status=200)


async def update_resource(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_resource

    Updates the data access role used for vending access to the given (registered) resource in Lake Formation. 

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_table_objects(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_table_objects

    Updates the manifest of Amazon S3 objects that make up the specified governed table.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateTableObjectsRequest.from_dict(body)
    return web.Response(status=200)


async def update_table_storage_optimizer(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_table_storage_optimizer

    Updates the configuration of the storage optimizers for a table.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateTableStorageOptimizerRequest.from_dict(body)
    return web.Response(status=200)
