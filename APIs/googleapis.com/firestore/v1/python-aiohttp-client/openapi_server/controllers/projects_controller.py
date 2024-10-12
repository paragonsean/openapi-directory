from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_get_documents_request import BatchGetDocumentsRequest
from openapi_server.models.batch_get_documents_response import BatchGetDocumentsResponse
from openapi_server.models.batch_write_request import BatchWriteRequest
from openapi_server.models.batch_write_response import BatchWriteResponse
from openapi_server.models.begin_transaction_request import BeginTransactionRequest
from openapi_server.models.begin_transaction_response import BeginTransactionResponse
from openapi_server.models.commit_request import CommitRequest
from openapi_server.models.commit_response import CommitResponse
from openapi_server.models.document import Document
from openapi_server.models.google_firestore_admin_v1_backup import GoogleFirestoreAdminV1Backup
from openapi_server.models.google_firestore_admin_v1_backup_schedule import GoogleFirestoreAdminV1BackupSchedule
from openapi_server.models.google_firestore_admin_v1_database import GoogleFirestoreAdminV1Database
from openapi_server.models.google_firestore_admin_v1_export_documents_request import GoogleFirestoreAdminV1ExportDocumentsRequest
from openapi_server.models.google_firestore_admin_v1_import_documents_request import GoogleFirestoreAdminV1ImportDocumentsRequest
from openapi_server.models.google_firestore_admin_v1_index import GoogleFirestoreAdminV1Index
from openapi_server.models.google_firestore_admin_v1_list_backup_schedules_response import GoogleFirestoreAdminV1ListBackupSchedulesResponse
from openapi_server.models.google_firestore_admin_v1_list_backups_response import GoogleFirestoreAdminV1ListBackupsResponse
from openapi_server.models.google_firestore_admin_v1_list_databases_response import GoogleFirestoreAdminV1ListDatabasesResponse
from openapi_server.models.google_firestore_admin_v1_list_fields_response import GoogleFirestoreAdminV1ListFieldsResponse
from openapi_server.models.google_firestore_admin_v1_list_indexes_response import GoogleFirestoreAdminV1ListIndexesResponse
from openapi_server.models.google_firestore_admin_v1_restore_database_request import GoogleFirestoreAdminV1RestoreDatabaseRequest
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server.models.list_collection_ids_request import ListCollectionIdsRequest
from openapi_server.models.list_collection_ids_response import ListCollectionIdsResponse
from openapi_server.models.list_documents_response import ListDocumentsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.listen_request import ListenRequest
from openapi_server.models.listen_response import ListenResponse
from openapi_server.models.partition_query_request import PartitionQueryRequest
from openapi_server.models.partition_query_response import PartitionQueryResponse
from openapi_server.models.rollback_request import RollbackRequest
from openapi_server.models.run_aggregation_query_request import RunAggregationQueryRequest
from openapi_server.models.run_aggregation_query_response import RunAggregationQueryResponse
from openapi_server.models.run_query_request import RunQueryRequest
from openapi_server.models.run_query_response import RunQueryResponse
from openapi_server.models.write_request import WriteRequest
from openapi_server.models.write_response import WriteResponse
from openapi_server import util


async def firestore_projects_databases_backup_schedules_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_backup_schedules_create

    Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule with retention up to 7 days and one weekly backup schedule with retention up to 14 weeks.

    :param parent: Required. The parent database. Format &#x60;projects/{project}/databases/{database}&#x60;
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
    body = GoogleFirestoreAdminV1BackupSchedule.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_backup_schedules_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """firestore_projects_databases_backup_schedules_list

    List backup schedules.

    :param parent: Required. The parent database. Format is &#x60;projects/{project}/databases/{database}&#x60;.
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

    """
    return web.Response(status=200)


async def firestore_projects_databases_collection_groups_fields_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """firestore_projects_databases_collection_groups_fields_list

    Lists the field configuration and metadata for this database. Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to &#x60;indexConfig.usesAncestorConfig:false&#x60; or &#x60;ttlConfig:*&#x60;.

    :param parent: Required. A parent name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}&#x60;
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
    :param filter: The filter to apply to list results. Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with a filter that includes &#x60;indexConfig.usesAncestorConfig:false&#x60; .
    :type filter: str
    :param page_size: The number of results to return.
    :type page_size: int
    :param page_token: A page token, returned from a previous call to FirestoreAdmin.ListFields, that may be used to get the next page of results.
    :type page_token: str

    """
    return web.Response(status=200)


async def firestore_projects_databases_collection_groups_indexes_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_collection_groups_indexes_create

    Creates a composite index. This returns a google.longrunning.Operation which may be used to track the status of the creation. The metadata for the operation will be the type IndexOperationMetadata.

    :param parent: Required. A parent name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}&#x60;
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
    body = GoogleFirestoreAdminV1Index.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_collection_groups_indexes_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """firestore_projects_databases_collection_groups_indexes_list

    Lists composite indexes.

    :param parent: Required. A parent name of the form &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}&#x60;
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
    :param filter: The filter to apply to list results.
    :type filter: str
    :param page_size: The number of results to return.
    :type page_size: int
    :param page_token: A page token, returned from a previous call to FirestoreAdmin.ListIndexes, that may be used to get the next page of results.
    :type page_token: str

    """
    return web.Response(status=200)


async def firestore_projects_databases_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, database_id=None, body=None) -> web.Response:
    """firestore_projects_databases_create

    Create a database.

    :param parent: Required. A parent name of the form &#x60;projects/{project_id}&#x60;
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
    :param database_id: Required. The ID to use for the database, which will become the final component of the database&#39;s resource name. This value should be 4-63 characters. Valid characters are /a-z-/ with first character a letter and the last a letter or a number. Must not be UUID-like /[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}/. \&quot;(default)\&quot; database id is also valid.
    :type database_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleFirestoreAdminV1Database.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_batch_get(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_batch_get

    Gets multiple documents. Documents returned by this method are not guaranteed to be returned in the same order that they were requested.

    :param database: Required. The database name. In the format: &#x60;projects/{project_id}/databases/{database_id}&#x60;.
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
    body = BatchGetDocumentsRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_batch_write(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_batch_write

    Applies a batch of write operations. The BatchWrite method does not apply the write operations atomically and can apply them out of order. Method does not allow more than one write per document. Each write succeeds or fails independently. See the BatchWriteResponse for the success status of each write. If you require an atomically applied set of writes, use Commit instead.

    :param database: Required. The database name. In the format: &#x60;projects/{project_id}/databases/{database_id}&#x60;.
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
    body = BatchWriteRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_begin_transaction(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_begin_transaction

    Starts a new transaction.

    :param database: Required. The database name. In the format: &#x60;projects/{project_id}/databases/{database_id}&#x60;.
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
    body = BeginTransactionRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_commit(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_commit

    Commits a transaction, while optionally updating documents.

    :param database: Required. The database name. In the format: &#x60;projects/{project_id}/databases/{database_id}&#x60;.
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
    body = CommitRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_create_document(request: web.Request, parent, collection_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, document_id=None, mask_field_paths=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_create_document

    Creates a new document.

    :param parent: Required. The parent resource. For example: &#x60;projects/{project_id}/databases/{database_id}/documents&#x60; or &#x60;projects/{project_id}/databases/{database_id}/documents/chatrooms/{chatroom_id}&#x60;
    :type parent: str
    :param collection_id: Required. The collection ID, relative to &#x60;parent&#x60;, to list. For example: &#x60;chatrooms&#x60;.
    :type collection_id: str
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
    :param document_id: The client-assigned document ID to use for this document. Optional. If not specified, an ID will be assigned by the service.
    :type document_id: str
    :param mask_field_paths: The list of field paths in the mask. See Document.fields for a field path syntax reference.
    :type mask_field_paths: List[str]
    :param body: 
    :type body: dict | bytes

    """
    body = Document.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_list_collection_ids(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_list_collection_ids

    Lists all the collection IDs underneath a document.

    :param parent: Required. The parent document. In the format: &#x60;projects/{project_id}/databases/{database_id}/documents/{document_path}&#x60;. For example: &#x60;projects/my-project/databases/my-database/documents/chatrooms/my-chatroom&#x60;
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
    body = ListCollectionIdsRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_list_documents(request: web.Request, parent, collection_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, mask_field_paths=None, order_by=None, page_size=None, page_token=None, read_time=None, show_missing=None, transaction=None) -> web.Response:
    """firestore_projects_databases_documents_list_documents

    Lists documents.

    :param parent: Required. The parent resource name. In the format: &#x60;projects/{project_id}/databases/{database_id}/documents&#x60; or &#x60;projects/{project_id}/databases/{database_id}/documents/{document_path}&#x60;. For example: &#x60;projects/my-project/databases/my-database/documents&#x60; or &#x60;projects/my-project/databases/my-database/documents/chatrooms/my-chatroom&#x60;
    :type parent: str
    :param collection_id: Optional. The collection ID, relative to &#x60;parent&#x60;, to list. For example: &#x60;chatrooms&#x60; or &#x60;messages&#x60;. This is optional, and when not provided, Firestore will list documents from all collections under the provided &#x60;parent&#x60;.
    :type collection_id: str
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
    :param mask_field_paths: The list of field paths in the mask. See Document.fields for a field path syntax reference.
    :type mask_field_paths: List[str]
    :param order_by: Optional. The optional ordering of the documents to return. For example: &#x60;priority desc, __name__ desc&#x60;. This mirrors the &#x60;ORDER BY&#x60; used in Firestore queries but in a string representation. When absent, documents are ordered based on &#x60;__name__ ASC&#x60;.
    :type order_by: str
    :param page_size: Optional. The maximum number of documents to return in a single response. Firestore may return fewer than this value.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous &#x60;ListDocuments&#x60; response. Provide this to retrieve the subsequent page. When paginating, all other parameters (with the exception of &#x60;page_size&#x60;) must match the values set in the request that generated the page token.
    :type page_token: str
    :param read_time: Perform the read at the provided time. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days.
    :type read_time: str
    :param show_missing: If the list should show missing documents. A document is missing if it does not exist, but there are sub-documents nested underneath it. When true, such missing documents will be returned with a key but will not have fields, &#x60;create_time&#x60;, or &#x60;update_time&#x60; set. Requests with &#x60;show_missing&#x60; may not specify &#x60;where&#x60; or &#x60;order_by&#x60;.
    :type show_missing: bool
    :param transaction: Perform the read as part of an already active transaction.
    :type transaction: str

    """
    return web.Response(status=200)


async def firestore_projects_databases_documents_listen(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_listen

    Listens to changes. This method is only available via gRPC or WebChannel (not REST).

    :param database: Required. The database name. In the format: &#x60;projects/{project_id}/databases/{database_id}&#x60;.
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
    body = ListenRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_partition_query(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_partition_query

    Partitions a query by returning partition cursors that can be used to run the query in parallel. The returned partition cursors are split points that can be used by RunQuery as starting/end points for the query results.

    :param parent: Required. The parent resource name. In the format: &#x60;projects/{project_id}/databases/{database_id}/documents&#x60;. Document resource names are not supported; only database resource names can be specified.
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
    body = PartitionQueryRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, current_document_exists=None, current_document_update_time=None, mask_field_paths=None, update_mask_field_paths=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_patch

    Updates or inserts a document.

    :param name: The resource name of the document, for example &#x60;projects/{project_id}/databases/{database_id}/documents/{document_path}&#x60;.
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
    :param current_document_exists: When set to &#x60;true&#x60;, the target document must exist. When set to &#x60;false&#x60;, the target document must not exist.
    :type current_document_exists: bool
    :param current_document_update_time: When set, the target document must exist and have been last updated at that time. Timestamp must be microsecond aligned.
    :type current_document_update_time: str
    :param mask_field_paths: The list of field paths in the mask. See Document.fields for a field path syntax reference.
    :type mask_field_paths: List[str]
    :param update_mask_field_paths: The list of field paths in the mask. See Document.fields for a field path syntax reference.
    :type update_mask_field_paths: List[str]
    :param body: 
    :type body: dict | bytes

    """
    body = Document.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_rollback(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_rollback

    Rolls back a transaction.

    :param database: Required. The database name. In the format: &#x60;projects/{project_id}/databases/{database_id}&#x60;.
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
    body = RollbackRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_run_aggregation_query(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_run_aggregation_query

    Runs an aggregation query. Rather than producing Document results like Firestore.RunQuery, this API allows running an aggregation to produce a series of AggregationResult server-side. High-Level Example: &#x60;&#x60;&#x60; -- Return the number of documents in table given a filter. SELECT COUNT(*) FROM ( SELECT * FROM k where a &#x3D; true ); &#x60;&#x60;&#x60;

    :param parent: Required. The parent resource name. In the format: &#x60;projects/{project_id}/databases/{database_id}/documents&#x60; or &#x60;projects/{project_id}/databases/{database_id}/documents/{document_path}&#x60;. For example: &#x60;projects/my-project/databases/my-database/documents&#x60; or &#x60;projects/my-project/databases/my-database/documents/chatrooms/my-chatroom&#x60;
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
    body = RunAggregationQueryRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_run_query(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_run_query

    Runs a query.

    :param parent: Required. The parent resource name. In the format: &#x60;projects/{project_id}/databases/{database_id}/documents&#x60; or &#x60;projects/{project_id}/databases/{database_id}/documents/{document_path}&#x60;. For example: &#x60;projects/my-project/databases/my-database/documents&#x60; or &#x60;projects/my-project/databases/my-database/documents/chatrooms/my-chatroom&#x60;
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
    body = RunQueryRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_documents_write(request: web.Request, database, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_documents_write

    Streams batches of document updates and deletes, in order. This method is only available via gRPC or WebChannel (not REST).

    :param database: Required. The database name. In the format: &#x60;projects/{project_id}/databases/{database_id}&#x60;. This is only required in the first message.
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
    body = WriteRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_export_documents(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_export_documents

    Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage. For more details on export behavior and output format, refer to: https://cloud.google.com/firestore/docs/manage-data/export-import

    :param name: Required. Database to export. Should be of the form: &#x60;projects/{project_id}/databases/{database_id}&#x60;.
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
    body = GoogleFirestoreAdminV1ExportDocumentsRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_import_documents(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_import_documents

    Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore.

    :param name: Required. Database to import into. Should be of the form: &#x60;projects/{project_id}/databases/{database_id}&#x60;.
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
    body = GoogleFirestoreAdminV1ImportDocumentsRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_databases_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """firestore_projects_databases_list

    List all the databases in the project.

    :param parent: Required. A parent name of the form &#x60;projects/{project_id}&#x60;
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

    """
    return web.Response(status=200)


async def firestore_projects_databases_operations_cancel(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_operations_cancel

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


async def firestore_projects_databases_operations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """firestore_projects_databases_operations_list

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


async def firestore_projects_databases_restore(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firestore_projects_databases_restore

    Creates a new database by restoring from an existing backup. The new database must be in the same cloud region or multi-region location as the existing backup. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing backup. The long-running operation can be used to track the progress of the restore, with the Operation&#39;s metadata field type being the RestoreDatabaseMetadata. The response type is the Database if the restore was successful. The new database is not readable or writeable until the LRO has completed.

    :param parent: Required. The project to restore the database in. Format is &#x60;projects/{project_id}&#x60;.
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
    body = GoogleFirestoreAdminV1RestoreDatabaseRequest.from_dict(body)
    return web.Response(status=200)


async def firestore_projects_locations_backups_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, current_document_exists=None, current_document_update_time=None) -> web.Response:
    """firestore_projects_locations_backups_delete

    Deletes a backup.

    :param name: Required. Name of the backup to delete. format is &#x60;projects/{project}/locations/{location}/backups/{backup}&#x60;.
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
    :param current_document_exists: When set to &#x60;true&#x60;, the target document must exist. When set to &#x60;false&#x60;, the target document must not exist.
    :type current_document_exists: bool
    :param current_document_update_time: When set, the target document must exist and have been last updated at that time. Timestamp must be microsecond aligned.
    :type current_document_update_time: str

    """
    return web.Response(status=200)


async def firestore_projects_locations_backups_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, mask_field_paths=None, read_time=None, transaction=None) -> web.Response:
    """firestore_projects_locations_backups_get

    Gets information about a backup.

    :param name: Required. Name of the backup to fetch. Format is &#x60;projects/{project}/locations/{location}/backups/{backup}&#x60;.
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
    :param mask_field_paths: The list of field paths in the mask. See Document.fields for a field path syntax reference.
    :type mask_field_paths: List[str]
    :param read_time: Reads the version of the document at the given time. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days.
    :type read_time: str
    :param transaction: Reads the document in a transaction.
    :type transaction: str

    """
    return web.Response(status=200)


async def firestore_projects_locations_backups_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """firestore_projects_locations_backups_list

    Lists all the backups.

    :param parent: Required. The location to list backups from. Format is &#x60;projects/{project}/locations/{location}&#x60;. Use &#x60;{location} &#x3D; &#39;-&#39;&#x60; to list backups from all locations for the given project. This allows listing backups from a single location or from all locations.
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

    """
    return web.Response(status=200)


async def firestore_projects_locations_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """firestore_projects_locations_list

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
