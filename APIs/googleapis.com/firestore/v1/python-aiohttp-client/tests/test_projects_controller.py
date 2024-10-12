# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_backup_schedules_create(client):
    """Test case for firestore_projects_databases_backup_schedules_create

    
    """
    body = {"dailyRecurrence":"{}","createTime":"createTime","name":"name","updateTime":"updateTime","retention":"retention","weeklyRecurrence":{"day":"DAY_OF_WEEK_UNSPECIFIED"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/backupSchedules'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_backup_schedules_list(client):
    """Test case for firestore_projects_databases_backup_schedules_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/backupSchedules'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_collection_groups_fields_list(client):
    """Test case for firestore_projects_databases_collection_groups_fields_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/fields'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_collection_groups_indexes_create(client):
    """Test case for firestore_projects_databases_collection_groups_indexes_create

    
    """
    body = {"apiScope":"ANY_API","queryScope":"QUERY_SCOPE_UNSPECIFIED","name":"name","state":"STATE_UNSPECIFIED","fields":[{"arrayConfig":"ARRAY_CONFIG_UNSPECIFIED","vectorConfig":{"flat":"{}","dimension":0},"fieldPath":"fieldPath","order":"ORDER_UNSPECIFIED"},{"arrayConfig":"ARRAY_CONFIG_UNSPECIFIED","vectorConfig":{"flat":"{}","dimension":0},"fieldPath":"fieldPath","order":"ORDER_UNSPECIFIED"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/indexes'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_collection_groups_indexes_list(client):
    """Test case for firestore_projects_databases_collection_groups_indexes_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/indexes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_create(client):
    """Test case for firestore_projects_databases_create

    
    """
    body = {"pointInTimeRecoveryEnablement":"POINT_IN_TIME_RECOVERY_ENABLEMENT_UNSPECIFIED","updateTime":"updateTime","deleteProtectionState":"DELETE_PROTECTION_STATE_UNSPECIFIED","type":"DATABASE_TYPE_UNSPECIFIED","keyPrefix":"keyPrefix","concurrencyMode":"CONCURRENCY_MODE_UNSPECIFIED","uid":"uid","versionRetentionPeriod":"versionRetentionPeriod","createTime":"createTime","earliestVersionTime":"earliestVersionTime","locationId":"locationId","name":"name","etag":"etag","appEngineIntegrationMode":"APP_ENGINE_INTEGRATION_MODE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('databaseId', 'database_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/databases'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_batch_get(client):
    """Test case for firestore_projects_databases_documents_batch_get

    
    """
    body = {"newTransaction":{"readWrite":{"retryTransaction":"retryTransaction"},"readOnly":{"readTime":"readTime"}},"documents":["documents","documents"],"readTime":"readTime","transaction":"transaction","mask":{"fieldPaths":["fieldPaths","fieldPaths"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{database}/documents:batchGet'.format(database='database_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_batch_write(client):
    """Test case for firestore_projects_databases_documents_batch_write

    
    """
    body = {"writes":[{"transform":{"document":"document","fieldTransforms":[{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}]},"update":{"createTime":"createTime","name":"name","updateTime":"updateTime","fields":{"key":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}},"currentDocument":{"exists":True,"updateTime":"updateTime"},"updateTransforms":[{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}],"updateMask":{"fieldPaths":["fieldPaths","fieldPaths"]},"delete":"delete"},{"transform":{"document":"document","fieldTransforms":[{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}]},"update":{"createTime":"createTime","name":"name","updateTime":"updateTime","fields":{"key":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}},"currentDocument":{"exists":True,"updateTime":"updateTime"},"updateTransforms":[{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}],"updateMask":{"fieldPaths":["fieldPaths","fieldPaths"]},"delete":"delete"}],"labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{database}/documents:batchWrite'.format(database='database_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_begin_transaction(client):
    """Test case for firestore_projects_databases_documents_begin_transaction

    
    """
    body = {"options":{"readWrite":{"retryTransaction":"retryTransaction"},"readOnly":{"readTime":"readTime"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{database}/documents:beginTransaction'.format(database='database_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_commit(client):
    """Test case for firestore_projects_databases_documents_commit

    
    """
    body = {"writes":[{"transform":{"document":"document","fieldTransforms":[{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}]},"update":{"createTime":"createTime","name":"name","updateTime":"updateTime","fields":{"key":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}},"currentDocument":{"exists":True,"updateTime":"updateTime"},"updateTransforms":[{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}],"updateMask":{"fieldPaths":["fieldPaths","fieldPaths"]},"delete":"delete"},{"transform":{"document":"document","fieldTransforms":[{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}]},"update":{"createTime":"createTime","name":"name","updateTime":"updateTime","fields":{"key":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}},"currentDocument":{"exists":True,"updateTime":"updateTime"},"updateTransforms":[{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}],"updateMask":{"fieldPaths":["fieldPaths","fieldPaths"]},"delete":"delete"}],"transaction":"transaction"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{database}/documents:commit'.format(database='database_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_create_document(client):
    """Test case for firestore_projects_databases_documents_create_document

    
    """
    body = {"createTime":"createTime","name":"name","updateTime":"updateTime","fields":{"key":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('documentId', 'document_id_example'),
                    ('mask.fieldPaths', ['mask_field_paths_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/{collection_id}'.format(parent='parent_example', collection_id='collection_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_list_collection_ids(client):
    """Test case for firestore_projects_databases_documents_list_collection_ids

    
    """
    body = {"pageSize":0,"readTime":"readTime","pageToken":"pageToken"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parentlist_collection_id}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_list_documents(client):
    """Test case for firestore_projects_databases_documents_list_documents

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('mask.fieldPaths', ['mask_field_paths_example']),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('readTime', 'read_time_example'),
                    ('showMissing', True),
                    ('transaction', 'transaction_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/{collection_id}'.format(parent='parent_example', collection_id='collection_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_listen(client):
    """Test case for firestore_projects_databases_documents_listen

    
    """
    body = {"addTarget":{"resumeToken":"resumeToken","targetId":5,"documents":{"documents":["documents","documents"]},"once":True,"query":{"parent":"parent","structuredQuery":{"select":{"fields":[{"fieldPath":"fieldPath"},{"fieldPath":"fieldPath"}]},"offset":1,"limit":6,"orderBy":[{"field":{"fieldPath":"fieldPath"},"direction":"DIRECTION_UNSPECIFIED"},{"field":{"fieldPath":"fieldPath"},"direction":"DIRECTION_UNSPECIFIED"}],"from":[{"allDescendants":True,"collectionId":"collectionId"},{"allDescendants":True,"collectionId":"collectionId"}],"where":{"compositeFilter":{"op":"OPERATOR_UNSPECIFIED","filters":[null,null]},"fieldFilter":{"op":"OPERATOR_UNSPECIFIED","field":{"fieldPath":"fieldPath"},"value":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},"unaryFilter":{"op":"OPERATOR_UNSPECIFIED","field":{"fieldPath":"fieldPath"}}},"endAt":{"before":True,"values":[{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}]},"startAt":{"before":True,"values":[{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}]}}},"readTime":"readTime","expectedCount":0},"labels":{"key":"labels"},"removeTarget":5}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{database}/documents:listen'.format(database='database_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_partition_query(client):
    """Test case for firestore_projects_databases_documents_partition_query

    
    """
    body = {"partitionCount":"partitionCount","structuredQuery":{"select":{"fields":[{"fieldPath":"fieldPath"},{"fieldPath":"fieldPath"}]},"offset":1,"limit":6,"orderBy":[{"field":{"fieldPath":"fieldPath"},"direction":"DIRECTION_UNSPECIFIED"},{"field":{"fieldPath":"fieldPath"},"direction":"DIRECTION_UNSPECIFIED"}],"from":[{"allDescendants":True,"collectionId":"collectionId"},{"allDescendants":True,"collectionId":"collectionId"}],"where":{"compositeFilter":{"op":"OPERATOR_UNSPECIFIED","filters":[null,null]},"fieldFilter":{"op":"OPERATOR_UNSPECIFIED","field":{"fieldPath":"fieldPath"},"value":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},"unaryFilter":{"op":"OPERATOR_UNSPECIFIED","field":{"fieldPath":"fieldPath"}}},"endAt":{"before":True,"values":[{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}]},"startAt":{"before":True,"values":[{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}]}},"pageSize":0,"readTime":"readTime","pageToken":"pageToken"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parentpartition_quer}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_patch(client):
    """Test case for firestore_projects_databases_documents_patch

    
    """
    body = {"createTime":"createTime","name":"name","updateTime":"updateTime","fields":{"key":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('currentDocument.exists', True),
                    ('currentDocument.updateTime', 'current_document_update_time_example'),
                    ('mask.fieldPaths', ['mask_field_paths_example']),
                    ('updateMask.fieldPaths', ['update_mask_field_paths_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_rollback(client):
    """Test case for firestore_projects_databases_documents_rollback

    
    """
    body = {"transaction":"transaction"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{database}/documents:rollback'.format(database='database_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_run_aggregation_query(client):
    """Test case for firestore_projects_databases_documents_run_aggregation_query

    
    """
    body = {"newTransaction":{"readWrite":{"retryTransaction":"retryTransaction"},"readOnly":{"readTime":"readTime"}},"readTime":"readTime","structuredAggregationQuery":{"structuredQuery":{"select":{"fields":[{"fieldPath":"fieldPath"},{"fieldPath":"fieldPath"}]},"offset":1,"limit":6,"orderBy":[{"field":{"fieldPath":"fieldPath"},"direction":"DIRECTION_UNSPECIFIED"},{"field":{"fieldPath":"fieldPath"},"direction":"DIRECTION_UNSPECIFIED"}],"from":[{"allDescendants":True,"collectionId":"collectionId"},{"allDescendants":True,"collectionId":"collectionId"}],"where":{"compositeFilter":{"op":"OPERATOR_UNSPECIFIED","filters":[null,null]},"fieldFilter":{"op":"OPERATOR_UNSPECIFIED","field":{"fieldPath":"fieldPath"},"value":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},"unaryFilter":{"op":"OPERATOR_UNSPECIFIED","field":{"fieldPath":"fieldPath"}}},"endAt":{"before":True,"values":[{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}]},"startAt":{"before":True,"values":[{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}]}},"aggregations":[{"avg":{"field":{"fieldPath":"fieldPath"}},"count":{"upTo":"upTo"},"alias":"alias","sum":{"field":{"fieldPath":"fieldPath"}}},{"avg":{"field":{"fieldPath":"fieldPath"}},"count":{"upTo":"upTo"},"alias":"alias","sum":{"field":{"fieldPath":"fieldPath"}}}]},"transaction":"transaction"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parentrun_aggregation_quer}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_run_query(client):
    """Test case for firestore_projects_databases_documents_run_query

    
    """
    body = {"newTransaction":{"readWrite":{"retryTransaction":"retryTransaction"},"readOnly":{"readTime":"readTime"}},"structuredQuery":{"select":{"fields":[{"fieldPath":"fieldPath"},{"fieldPath":"fieldPath"}]},"offset":1,"limit":6,"orderBy":[{"field":{"fieldPath":"fieldPath"},"direction":"DIRECTION_UNSPECIFIED"},{"field":{"fieldPath":"fieldPath"},"direction":"DIRECTION_UNSPECIFIED"}],"from":[{"allDescendants":True,"collectionId":"collectionId"},{"allDescendants":True,"collectionId":"collectionId"}],"where":{"compositeFilter":{"op":"OPERATOR_UNSPECIFIED","filters":[null,null]},"fieldFilter":{"op":"OPERATOR_UNSPECIFIED","field":{"fieldPath":"fieldPath"},"value":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},"unaryFilter":{"op":"OPERATOR_UNSPECIFIED","field":{"fieldPath":"fieldPath"}}},"endAt":{"before":True,"values":[{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}]},"startAt":{"before":True,"values":[{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}]}},"readTime":"readTime","transaction":"transaction"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parentrun_quer}'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_documents_write(client):
    """Test case for firestore_projects_databases_documents_write

    
    """
    body = {"streamId":"streamId","writes":[{"transform":{"document":"document","fieldTransforms":[{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}]},"update":{"createTime":"createTime","name":"name","updateTime":"updateTime","fields":{"key":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}},"currentDocument":{"exists":True,"updateTime":"updateTime"},"updateTransforms":[{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}],"updateMask":{"fieldPaths":["fieldPaths","fieldPaths"]},"delete":"delete"},{"transform":{"document":"document","fieldTransforms":[{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}]},"update":{"createTime":"createTime","name":"name","updateTime":"updateTime","fields":{"key":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}},"currentDocument":{"exists":True,"updateTime":"updateTime"},"updateTransforms":[{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}},{"appendMissingElements":{"values":[null,null]},"removeAllFromArray":{"values":[null,null]},"setToServerValue":"SERVER_VALUE_UNSPECIFIED","fieldPath":"fieldPath","increment":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"maximum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"},"minimum":{"mapValue":{"fields":{}},"stringValue":"stringValue","timestampValue":"timestampValue","geoPointValue":{"latitude":6.027456183070403,"longitude":1.4658129805029452},"booleanValue":True,"integerValue":"integerValue","arrayValue":{"values":[null,null]},"doubleValue":0.8008281904610115,"bytesValue":"bytesValue","nullValue":"NULL_VALUE","referenceValue":"referenceValue"}}],"updateMask":{"fieldPaths":["fieldPaths","fieldPaths"]},"delete":"delete"}],"streamToken":"streamToken","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{database}/documents:write'.format(database='database_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_export_documents(client):
    """Test case for firestore_projects_databases_export_documents

    
    """
    body = {"collectionIds":["collectionIds","collectionIds"],"namespaceIds":["namespaceIds","namespaceIds"],"outputUriPrefix":"outputUriPrefix","snapshotTime":"snapshotTime"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameexport_document}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_import_documents(client):
    """Test case for firestore_projects_databases_import_documents

    
    """
    body = {"inputUriPrefix":"inputUriPrefix","collectionIds":["collectionIds","collectionIds"],"namespaceIds":["namespaceIds","namespaceIds"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameimport_document}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_list(client):
    """Test case for firestore_projects_databases_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/databases'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_operations_cancel(client):
    """Test case for firestore_projects_databases_operations_cancel

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_operations_list(client):
    """Test case for firestore_projects_databases_operations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_databases_restore(client):
    """Test case for firestore_projects_databases_restore

    
    """
    body = {"databaseSnapshot":{"database":"database","snapshotTime":"snapshotTime"},"backup":"backup","databaseId":"databaseId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/databases:restore'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_locations_backups_delete(client):
    """Test case for firestore_projects_locations_backups_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('currentDocument.exists', True),
                    ('currentDocument.updateTime', 'current_document_update_time_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_locations_backups_get(client):
    """Test case for firestore_projects_locations_backups_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('mask.fieldPaths', ['mask_field_paths_example']),
                    ('readTime', 'read_time_example'),
                    ('transaction', 'transaction_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_locations_backups_list(client):
    """Test case for firestore_projects_locations_backups_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/backups'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firestore_projects_locations_list(client):
    """Test case for firestore_projects_locations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

