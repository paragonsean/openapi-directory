# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instance_config_operations_list(client):
    """Test case for spanner_projects_instance_config_operations_list

    
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
        path='/v1/{parent}/instanceConfigOperations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instance_configs_create(client):
    """Test case for spanner_projects_instance_configs_create

    
    """
    body = {"validateOnly":True,"instanceConfig":{"displayName":"displayName","replicas":[{"defaultLeaderLocation":True,"location":"location","type":"TYPE_UNSPECIFIED"},{"defaultLeaderLocation":True,"location":"location","type":"TYPE_UNSPECIFIED"}],"reconciling":True,"optionalReplicas":[{"defaultLeaderLocation":True,"location":"location","type":"TYPE_UNSPECIFIED"},{"defaultLeaderLocation":True,"location":"location","type":"TYPE_UNSPECIFIED"}],"configType":"TYPE_UNSPECIFIED","leaderOptions":["leaderOptions","leaderOptions"],"labels":{"key":"labels"},"freeInstanceAvailability":"FREE_INSTANCE_AVAILABILITY_UNSPECIFIED","name":"name","etag":"etag","state":"STATE_UNSPECIFIED","storageLimitPerProcessingUnit":"storageLimitPerProcessingUnit","baseConfig":"baseConfig"},"instanceConfigId":"instanceConfigId"}
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
        path='/v1/{parent}/instanceConfigs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instance_configs_list(client):
    """Test case for spanner_projects_instance_configs_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/instanceConfigs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_backup_operations_list(client):
    """Test case for spanner_projects_instances_backup_operations_list

    
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
        path='/v1/{parent}/backupOperations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_backups_copy(client):
    """Test case for spanner_projects_instances_backups_copy

    
    """
    body = {"encryptionConfig":{"encryptionType":"ENCRYPTION_TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"expireTime":"expireTime","backupId":"backupId","sourceBackup":"sourceBackup"}
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
        path='/v1/{parent}/backups:copy'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_backups_create(client):
    """Test case for spanner_projects_instances_backups_create

    
    """
    body = {"encryptionInfo":{"encryptionStatus":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"encryptionType":"TYPE_UNSPECIFIED","kmsKeyVersion":"kmsKeyVersion"},"database":"database","expireTime":"expireTime","referencingBackups":["referencingBackups","referencingBackups"],"createTime":"createTime","referencingDatabases":["referencingDatabases","referencingDatabases"],"versionTime":"versionTime","name":"name","databaseDialect":"DATABASE_DIALECT_UNSPECIFIED","state":"STATE_UNSPECIFIED","maxExpireTime":"maxExpireTime","sizeBytes":"sizeBytes"}
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
                    ('backupId', 'backup_id_example'),
                    ('encryptionConfig.encryptionType', 'encryption_config_encryption_type_example'),
                    ('encryptionConfig.kmsKeyName', 'encryption_config_kms_key_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/backups'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_backups_list(client):
    """Test case for spanner_projects_instances_backups_list

    
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
        path='/v1/{parent}/backups'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_create(client):
    """Test case for spanner_projects_instances_create

    
    """
    body = {"instance":{"freeInstanceMetadata":{"expireTime":"expireTime","upgradeTime":"upgradeTime","expireBehavior":"EXPIRE_BEHAVIOR_UNSPECIFIED"},"displayName":"displayName","instanceType":"INSTANCE_TYPE_UNSPECIFIED","updateTime":"updateTime","labels":{"key":"labels"},"endpointUris":["endpointUris","endpointUris"],"autoscalingConfig":{"autoscalingLimits":{"minProcessingUnits":5,"maxNodes":0,"maxProcessingUnits":6,"minNodes":1},"autoscalingTargets":{"highPriorityCpuUtilizationPercent":5,"storageUtilizationPercent":2}},"processingUnits":9,"createTime":"createTime","name":"name","nodeCount":7,"state":"STATE_UNSPECIFIED","config":"config"},"instanceId":"instanceId"}
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
        path='/v1/{parent}/instances'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_database_operations_list(client):
    """Test case for spanner_projects_instances_database_operations_list

    
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
        path='/v1/{parent}/databaseOperations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_create(client):
    """Test case for spanner_projects_instances_databases_create

    
    """
    body = {"createStatement":"createStatement","encryptionConfig":{"kmsKeyName":"kmsKeyName"},"protoDescriptors":"protoDescriptors","databaseDialect":"DATABASE_DIALECT_UNSPECIFIED","extraStatements":["extraStatements","extraStatements"]}
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
        path='/v1/{parent}/databases'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_database_roles_list(client):
    """Test case for spanner_projects_instances_databases_database_roles_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/databaseRoles'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_database_roles_test_iam_permissions(client):
    """Test case for spanner_projects_instances_databases_database_roles_test_iam_permissions

    
    """
    body = {"permissions":["permissions","permissions"]}
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
        path='/v1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_drop_database(client):
    """Test case for spanner_projects_instances_databases_drop_database

    
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
        method='DELETE',
        path='/v1/{database}'.format(database='database_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_get_ddl(client):
    """Test case for spanner_projects_instances_databases_get_ddl

    
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
        path='/v1/{database}/ddl'.format(database='database_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_get_iam_policy(client):
    """Test case for spanner_projects_instances_databases_get_iam_policy

    
    """
    body = {"options":{"requestedPolicyVersion":0}}
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
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_get_scans(client):
    """Test case for spanner_projects_instances_databases_get_scans

    
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
                    ('endTime', 'end_time_example'),
                    ('startTime', 'start_time_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}/scans'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_list(client):
    """Test case for spanner_projects_instances_databases_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
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

async def test_spanner_projects_instances_databases_patch(client):
    """Test case for spanner_projects_instances_databases_patch

    
    """
    body = {"encryptionConfig":{"kmsKeyName":"kmsKeyName"},"encryptionInfo":[{"encryptionStatus":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"encryptionType":"TYPE_UNSPECIFIED","kmsKeyVersion":"kmsKeyVersion"},{"encryptionStatus":{"code":0,"details":[{"key":""},{"key":""}],"message":"message"},"encryptionType":"TYPE_UNSPECIFIED","kmsKeyVersion":"kmsKeyVersion"}],"versionRetentionPeriod":"versionRetentionPeriod","createTime":"createTime","earliestVersionTime":"earliestVersionTime","defaultLeader":"defaultLeader","name":"name","reconciling":True,"restoreInfo":{"sourceType":"TYPE_UNSPECIFIED","backupInfo":{"backup":"backup","createTime":"createTime","sourceDatabase":"sourceDatabase","versionTime":"versionTime"}},"databaseDialect":"DATABASE_DIALECT_UNSPECIFIED","state":"STATE_UNSPECIFIED","enableDropProtection":True}
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
                    ('updateMask', 'update_mask_example')]
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

async def test_spanner_projects_instances_databases_restore(client):
    """Test case for spanner_projects_instances_databases_restore

    
    """
    body = {"encryptionConfig":{"encryptionType":"ENCRYPTION_TYPE_UNSPECIFIED","kmsKeyName":"kmsKeyName"},"backup":"backup","databaseId":"databaseId"}
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

async def test_spanner_projects_instances_databases_sessions_batch_create(client):
    """Test case for spanner_projects_instances_databases_sessions_batch_create

    
    """
    body = {"sessionCount":0,"sessionTemplate":{"approximateLastUseTime":"approximateLastUseTime","creatorRole":"creatorRole","createTime":"createTime","name":"name","labels":{"key":"labels"}}}
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
        path='/v1/{database}/sessions:batchCreate'.format(database='database_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_batch_write(client):
    """Test case for spanner_projects_instances_databases_sessions_batch_write

    
    """
    body = {"requestOptions":{"transactionTag":"transactionTag","priority":"PRIORITY_UNSPECIFIED","requestTag":"requestTag"},"mutationGroups":[{"mutations":[{"replace":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"insert":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"update":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"delete":{"keySet":{"all":True,"ranges":[{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]},{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]}],"keys":[["",""],["",""]]},"table":"table"},"insertOrUpdate":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"}},{"replace":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"insert":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"update":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"delete":{"keySet":{"all":True,"ranges":[{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]},{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]}],"keys":[["",""],["",""]]},"table":"table"},"insertOrUpdate":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"}}]},{"mutations":[{"replace":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"insert":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"update":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"delete":{"keySet":{"all":True,"ranges":[{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]},{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]}],"keys":[["",""],["",""]]},"table":"table"},"insertOrUpdate":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"}},{"replace":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"insert":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"update":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"delete":{"keySet":{"all":True,"ranges":[{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]},{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]}],"keys":[["",""],["",""]]},"table":"table"},"insertOrUpdate":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"}}]}]}
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
        path='/v1/{sessionbatch_writ}'.format(session='session_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_begin_transaction(client):
    """Test case for spanner_projects_instances_databases_sessions_begin_transaction

    
    """
    body = {"options":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}},"requestOptions":{"transactionTag":"transactionTag","priority":"PRIORITY_UNSPECIFIED","requestTag":"requestTag"}}
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
        path='/v1/{sessionbegin_transactio}'.format(session='session_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_commit(client):
    """Test case for spanner_projects_instances_databases_sessions_commit

    
    """
    body = {"mutations":[{"replace":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"insert":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"update":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"delete":{"keySet":{"all":True,"ranges":[{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]},{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]}],"keys":[["",""],["",""]]},"table":"table"},"insertOrUpdate":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"}},{"replace":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"insert":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"update":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"},"delete":{"keySet":{"all":True,"ranges":[{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]},{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]}],"keys":[["",""],["",""]]},"table":"table"},"insertOrUpdate":{"columns":["columns","columns"],"values":[["",""],["",""]],"table":"table"}}],"maxCommitDelay":"maxCommitDelay","singleUseTransaction":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}},"requestOptions":{"transactionTag":"transactionTag","priority":"PRIORITY_UNSPECIFIED","requestTag":"requestTag"},"transactionId":"transactionId","returnCommitStats":True}
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
        path='/v1/{sessioncommi}'.format(session='session_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_create(client):
    """Test case for spanner_projects_instances_databases_sessions_create

    
    """
    body = {"session":{"approximateLastUseTime":"approximateLastUseTime","creatorRole":"creatorRole","createTime":"createTime","name":"name","labels":{"key":"labels"}}}
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
        path='/v1/{database}/sessions'.format(database='database_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_execute_batch_dml(client):
    """Test case for spanner_projects_instances_databases_sessions_execute_batch_dml

    
    """
    body = {"seqno":"seqno","statements":[{"paramTypes":{"key":{"code":"TYPE_CODE_UNSPECIFIED","protoTypeFqn":"protoTypeFqn","typeAnnotation":"TYPE_ANNOTATION_CODE_UNSPECIFIED"}},"params":{"key":""},"sql":"sql"},{"paramTypes":{"key":{"code":"TYPE_CODE_UNSPECIFIED","protoTypeFqn":"protoTypeFqn","typeAnnotation":"TYPE_ANNOTATION_CODE_UNSPECIFIED"}},"params":{"key":""},"sql":"sql"}],"requestOptions":{"transactionTag":"transactionTag","priority":"PRIORITY_UNSPECIFIED","requestTag":"requestTag"},"transaction":{"singleUse":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}},"id":"id","begin":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}}}}
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
        path='/v1/{sessionexecute_batch_dm}'.format(session='session_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_execute_sql(client):
    """Test case for spanner_projects_instances_databases_sessions_execute_sql

    
    """
    body = {"queryMode":"NORMAL","resumeToken":"resumeToken","directedReadOptions":{"includeReplicas":{"autoFailoverDisabled":True,"replicaSelections":[{"location":"location","type":"TYPE_UNSPECIFIED"},{"location":"location","type":"TYPE_UNSPECIFIED"}]},"excludeReplicas":{"replicaSelections":[{"location":"location","type":"TYPE_UNSPECIFIED"},{"location":"location","type":"TYPE_UNSPECIFIED"}]}},"seqno":"seqno","paramTypes":{"key":{"code":"TYPE_CODE_UNSPECIFIED","protoTypeFqn":"protoTypeFqn","typeAnnotation":"TYPE_ANNOTATION_CODE_UNSPECIFIED"}},"queryOptions":{"optimizerStatisticsPackage":"optimizerStatisticsPackage","optimizerVersion":"optimizerVersion"},"dataBoostEnabled":True,"params":{"key":""},"partitionToken":"partitionToken","requestOptions":{"transactionTag":"transactionTag","priority":"PRIORITY_UNSPECIFIED","requestTag":"requestTag"},"transaction":{"singleUse":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}},"id":"id","begin":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}}},"sql":"sql"}
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
        path='/v1/{sessionexecute_sq}'.format(session='session_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_execute_streaming_sql(client):
    """Test case for spanner_projects_instances_databases_sessions_execute_streaming_sql

    
    """
    body = {"queryMode":"NORMAL","resumeToken":"resumeToken","directedReadOptions":{"includeReplicas":{"autoFailoverDisabled":True,"replicaSelections":[{"location":"location","type":"TYPE_UNSPECIFIED"},{"location":"location","type":"TYPE_UNSPECIFIED"}]},"excludeReplicas":{"replicaSelections":[{"location":"location","type":"TYPE_UNSPECIFIED"},{"location":"location","type":"TYPE_UNSPECIFIED"}]}},"seqno":"seqno","paramTypes":{"key":{"code":"TYPE_CODE_UNSPECIFIED","protoTypeFqn":"protoTypeFqn","typeAnnotation":"TYPE_ANNOTATION_CODE_UNSPECIFIED"}},"queryOptions":{"optimizerStatisticsPackage":"optimizerStatisticsPackage","optimizerVersion":"optimizerVersion"},"dataBoostEnabled":True,"params":{"key":""},"partitionToken":"partitionToken","requestOptions":{"transactionTag":"transactionTag","priority":"PRIORITY_UNSPECIFIED","requestTag":"requestTag"},"transaction":{"singleUse":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}},"id":"id","begin":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}}},"sql":"sql"}
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
        path='/v1/{sessionexecute_streaming_sq}'.format(session='session_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_list(client):
    """Test case for spanner_projects_instances_databases_sessions_list

    
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
        path='/v1/{database}/sessions'.format(database='database_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_partition_query(client):
    """Test case for spanner_projects_instances_databases_sessions_partition_query

    
    """
    body = {"partitionOptions":{"partitionSizeBytes":"partitionSizeBytes","maxPartitions":"maxPartitions"},"paramTypes":{"key":{"code":"TYPE_CODE_UNSPECIFIED","protoTypeFqn":"protoTypeFqn","typeAnnotation":"TYPE_ANNOTATION_CODE_UNSPECIFIED"}},"params":{"key":""},"transaction":{"singleUse":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}},"id":"id","begin":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}}},"sql":"sql"}
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
        path='/v1/{sessionpartition_quer}'.format(session='session_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_partition_read(client):
    """Test case for spanner_projects_instances_databases_sessions_partition_read

    
    """
    body = {"partitionOptions":{"partitionSizeBytes":"partitionSizeBytes","maxPartitions":"maxPartitions"},"columns":["columns","columns"],"index":"index","keySet":{"all":True,"ranges":[{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]},{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]}],"keys":[["",""],["",""]]},"table":"table","transaction":{"singleUse":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}},"id":"id","begin":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}}}}
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
        path='/v1/{sessionpartition_rea}'.format(session='session_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_read(client):
    """Test case for spanner_projects_instances_databases_sessions_read

    
    """
    body = {"resumeToken":"resumeToken","directedReadOptions":{"includeReplicas":{"autoFailoverDisabled":True,"replicaSelections":[{"location":"location","type":"TYPE_UNSPECIFIED"},{"location":"location","type":"TYPE_UNSPECIFIED"}]},"excludeReplicas":{"replicaSelections":[{"location":"location","type":"TYPE_UNSPECIFIED"},{"location":"location","type":"TYPE_UNSPECIFIED"}]}},"columns":["columns","columns"],"dataBoostEnabled":True,"limit":"limit","index":"index","partitionToken":"partitionToken","requestOptions":{"transactionTag":"transactionTag","priority":"PRIORITY_UNSPECIFIED","requestTag":"requestTag"},"keySet":{"all":True,"ranges":[{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]},{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]}],"keys":[["",""],["",""]]},"table":"table","transaction":{"singleUse":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}},"id":"id","begin":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}}}}
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
        path='/v1/{sessionrea}'.format(session='session_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_rollback(client):
    """Test case for spanner_projects_instances_databases_sessions_rollback

    
    """
    body = {"transactionId":"transactionId"}
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
        path='/v1/{sessionrollbac}'.format(session='session_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_sessions_streaming_read(client):
    """Test case for spanner_projects_instances_databases_sessions_streaming_read

    
    """
    body = {"resumeToken":"resumeToken","directedReadOptions":{"includeReplicas":{"autoFailoverDisabled":True,"replicaSelections":[{"location":"location","type":"TYPE_UNSPECIFIED"},{"location":"location","type":"TYPE_UNSPECIFIED"}]},"excludeReplicas":{"replicaSelections":[{"location":"location","type":"TYPE_UNSPECIFIED"},{"location":"location","type":"TYPE_UNSPECIFIED"}]}},"columns":["columns","columns"],"dataBoostEnabled":True,"limit":"limit","index":"index","partitionToken":"partitionToken","requestOptions":{"transactionTag":"transactionTag","priority":"PRIORITY_UNSPECIFIED","requestTag":"requestTag"},"keySet":{"all":True,"ranges":[{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]},{"endOpen":["",""],"startClosed":["",""],"endClosed":["",""],"startOpen":["",""]}],"keys":[["",""],["",""]]},"table":"table","transaction":{"singleUse":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}},"id":"id","begin":{"partitionedDml":"{}","readWrite":{"readLockMode":"READ_LOCK_MODE_UNSPECIFIED"},"readOnly":{"readTimestamp":"readTimestamp","strong":True,"returnReadTimestamp":True,"minReadTimestamp":"minReadTimestamp","exactStaleness":"exactStaleness","maxStaleness":"maxStaleness"}}}}
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
        path='/v1/{sessionstreaming_rea}'.format(session='session_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_set_iam_policy(client):
    """Test case for spanner_projects_instances_databases_set_iam_policy

    
    """
    body = {"policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0}}
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
        path='/v1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_databases_update_ddl(client):
    """Test case for spanner_projects_instances_databases_update_ddl

    
    """
    body = {"operationId":"operationId","protoDescriptors":"protoDescriptors","statements":["statements","statements"]}
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
        method='PATCH',
        path='/v1/{database}/ddl'.format(database='database_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_list(client):
    """Test case for spanner_projects_instances_list

    
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
                    ('instanceDeadline', 'instance_deadline_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/instances'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_operations_cancel(client):
    """Test case for spanner_projects_instances_operations_cancel

    
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
        method='POST',
        path='/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spanner_projects_instances_operations_delete(client):
    """Test case for spanner_projects_instances_operations_delete

    
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
                    ('etag', 'etag_example'),
                    ('validateOnly', True)]
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

async def test_spanner_projects_instances_operations_list(client):
    """Test case for spanner_projects_instances_operations_list

    
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

