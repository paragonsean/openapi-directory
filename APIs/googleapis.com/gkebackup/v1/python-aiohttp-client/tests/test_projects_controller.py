# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup import Backup
from openapi_server.models.backup_plan import BackupPlan
from openapi_server.models.google_longrunning_list_operations_response import GoogleLongrunningListOperationsResponse
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server.models.list_backup_plans_response import ListBackupPlansResponse
from openapi_server.models.list_backups_response import ListBackupsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_restore_plans_response import ListRestorePlansResponse
from openapi_server.models.list_restores_response import ListRestoresResponse
from openapi_server.models.list_volume_backups_response import ListVolumeBackupsResponse
from openapi_server.models.list_volume_restores_response import ListVolumeRestoresResponse
from openapi_server.models.policy import Policy
from openapi_server.models.restore import Restore
from openapi_server.models.restore_plan import RestorePlan
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.volume_restore import VolumeRestore


pytestmark = pytest.mark.asyncio

async def test_gkebackup_projects_locations_backup_plans_backups_create(client):
    """Test case for gkebackup_projects_locations_backup_plans_backups_create

    
    """
    body = {"deleteLockDays":0,"description":"description","encryptionKey":{"gcpKmsEncryptionKey":"gcpKmsEncryptionKey"},"configBackupSizeBytes":"configBackupSizeBytes","manual":True,"stateReason":"stateReason","deleteLockExpireTime":"deleteLockExpireTime","uid":"uid","allNamespaces":True,"volumeCount":5,"state":"STATE_UNSPECIFIED","containsVolumeData":True,"selectedNamespaces":{"namespaces":["namespaces","namespaces"]},"retainDays":5,"completeTime":"completeTime","containsSecrets":True,"podCount":6,"updateTime":"updateTime","retainExpireTime":"retainExpireTime","labels":{"key":"labels"},"sizeBytes":"sizeBytes","createTime":"createTime","resourceCount":1,"name":"name","selectedApplications":{"namespacedNames":[{"name":"name","namespace":"namespace"},{"name":"name","namespace":"namespace"}]},"etag":"etag","clusterMetadata":{"anthosVersion":"anthosVersion","cluster":"cluster","backupCrdVersions":{"key":"backupCrdVersions"},"gkeVersion":"gkeVersion","k8sVersion":"k8sVersion"}}
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
                    ('backupId', 'backup_id_example')]
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

async def test_gkebackup_projects_locations_backup_plans_backups_list(client):
    """Test case for gkebackup_projects_locations_backup_plans_backups_list

    
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
                    ('orderBy', 'order_by_example'),
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

async def test_gkebackup_projects_locations_backup_plans_backups_volume_backups_list(client):
    """Test case for gkebackup_projects_locations_backup_plans_backups_volume_backups_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/volumeBackups'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkebackup_projects_locations_backup_plans_create(client):
    """Test case for gkebackup_projects_locations_backup_plans_create

    
    """
    body = {"backupSchedule":{"paused":True,"cronSchedule":"cronSchedule"},"cluster":"cluster","protectedPodCount":0,"description":"description","updateTime":"updateTime","stateReason":"stateReason","deactivated":True,"labels":{"key":"labels"},"uid":"uid","createTime":"createTime","backupConfig":{"allNamespaces":True,"selectedNamespaces":{"namespaces":["namespaces","namespaces"]},"includeSecrets":True,"includeVolumeData":True,"selectedApplications":{"namespacedNames":[{"name":"name","namespace":"namespace"},{"name":"name","namespace":"namespace"}]},"encryptionKey":{"gcpKmsEncryptionKey":"gcpKmsEncryptionKey"}},"name":"name","etag":"etag","retentionPolicy":{"backupRetainDays":1,"backupDeleteLockDays":6,"locked":True},"state":"STATE_UNSPECIFIED"}
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
                    ('backupPlanId', 'backup_plan_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/backupPlans'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkebackup_projects_locations_backup_plans_list(client):
    """Test case for gkebackup_projects_locations_backup_plans_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/backupPlans'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkebackup_projects_locations_list(client):
    """Test case for gkebackup_projects_locations_list

    
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


pytestmark = pytest.mark.asyncio

async def test_gkebackup_projects_locations_operations_cancel(client):
    """Test case for gkebackup_projects_locations_operations_cancel

    
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

async def test_gkebackup_projects_locations_operations_list(client):
    """Test case for gkebackup_projects_locations_operations_list

    
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

async def test_gkebackup_projects_locations_restore_plans_create(client):
    """Test case for gkebackup_projects_locations_restore_plans_create

    
    """
    body = {"cluster":"cluster","uid":"uid","createTime":"createTime","name":"name","description":"description","backupPlan":"backupPlan","etag":"etag","updateTime":"updateTime","state":"STATE_UNSPECIFIED","stateReason":"stateReason","restoreConfig":{"clusterResourceConflictPolicy":"CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED","namespacedResourceRestoreMode":"NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED","allNamespaces":True,"selectedNamespaces":{"namespaces":["namespaces","namespaces"]},"selectedApplications":{"namespacedNames":[{"name":"name","namespace":"namespace"},{"name":"name","namespace":"namespace"}]},"excludedNamespaces":{"namespaces":["namespaces","namespaces"]},"transformationRules":[{"description":"description","resourceFilter":{"groupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"jsonPath":"jsonPath","namespaces":["namespaces","namespaces"]},"fieldActions":[{"fromPath":"fromPath","op":"OP_UNSPECIFIED","path":"path","value":"value"},{"fromPath":"fromPath","op":"OP_UNSPECIFIED","path":"path","value":"value"}]},{"description":"description","resourceFilter":{"groupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"jsonPath":"jsonPath","namespaces":["namespaces","namespaces"]},"fieldActions":[{"fromPath":"fromPath","op":"OP_UNSPECIFIED","path":"path","value":"value"},{"fromPath":"fromPath","op":"OP_UNSPECIFIED","path":"path","value":"value"}]}],"volumeDataRestorePolicy":"VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED","substitutionRules":[{"newValue":"newValue","targetGroupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"originalValuePattern":"originalValuePattern","targetNamespaces":["targetNamespaces","targetNamespaces"],"targetJsonPath":"targetJsonPath"},{"newValue":"newValue","targetGroupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"originalValuePattern":"originalValuePattern","targetNamespaces":["targetNamespaces","targetNamespaces"],"targetJsonPath":"targetJsonPath"}],"noNamespaces":True,"clusterResourceRestoreScope":{"noGroupKinds":True,"allGroupKinds":True,"selectedGroupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"excludedGroupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}]}},"labels":{"key":"labels"}}
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
                    ('restorePlanId', 'restore_plan_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/restorePlans'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkebackup_projects_locations_restore_plans_list(client):
    """Test case for gkebackup_projects_locations_restore_plans_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/restorePlans'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkebackup_projects_locations_restore_plans_restores_create(client):
    """Test case for gkebackup_projects_locations_restore_plans_restores_create

    
    """
    body = {"cluster":"cluster","backup":"backup","resourcesExcludedCount":0,"resourcesFailedCount":6,"completeTime":"completeTime","description":"description","updateTime":"updateTime","stateReason":"stateReason","restoreConfig":{"clusterResourceConflictPolicy":"CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED","namespacedResourceRestoreMode":"NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED","allNamespaces":True,"selectedNamespaces":{"namespaces":["namespaces","namespaces"]},"selectedApplications":{"namespacedNames":[{"name":"name","namespace":"namespace"},{"name":"name","namespace":"namespace"}]},"excludedNamespaces":{"namespaces":["namespaces","namespaces"]},"transformationRules":[{"description":"description","resourceFilter":{"groupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"jsonPath":"jsonPath","namespaces":["namespaces","namespaces"]},"fieldActions":[{"fromPath":"fromPath","op":"OP_UNSPECIFIED","path":"path","value":"value"},{"fromPath":"fromPath","op":"OP_UNSPECIFIED","path":"path","value":"value"}]},{"description":"description","resourceFilter":{"groupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"jsonPath":"jsonPath","namespaces":["namespaces","namespaces"]},"fieldActions":[{"fromPath":"fromPath","op":"OP_UNSPECIFIED","path":"path","value":"value"},{"fromPath":"fromPath","op":"OP_UNSPECIFIED","path":"path","value":"value"}]}],"volumeDataRestorePolicy":"VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED","substitutionRules":[{"newValue":"newValue","targetGroupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"originalValuePattern":"originalValuePattern","targetNamespaces":["targetNamespaces","targetNamespaces"],"targetJsonPath":"targetJsonPath"},{"newValue":"newValue","targetGroupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"originalValuePattern":"originalValuePattern","targetNamespaces":["targetNamespaces","targetNamespaces"],"targetJsonPath":"targetJsonPath"}],"noNamespaces":True,"clusterResourceRestoreScope":{"noGroupKinds":True,"allGroupKinds":True,"selectedGroupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"excludedGroupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}]}},"labels":{"key":"labels"},"uid":"uid","createTime":"createTime","volumesRestoredCount":5,"name":"name","etag":"etag","state":"STATE_UNSPECIFIED","resourcesRestoredCount":1}
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
                    ('restoreId', 'restore_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/restores'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkebackup_projects_locations_restore_plans_restores_delete(client):
    """Test case for gkebackup_projects_locations_restore_plans_restores_delete

    
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
                    ('force', True)]
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

async def test_gkebackup_projects_locations_restore_plans_restores_list(client):
    """Test case for gkebackup_projects_locations_restore_plans_restores_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/restores'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkebackup_projects_locations_restore_plans_restores_patch(client):
    """Test case for gkebackup_projects_locations_restore_plans_restores_patch

    
    """
    body = {"cluster":"cluster","backup":"backup","resourcesExcludedCount":0,"resourcesFailedCount":6,"completeTime":"completeTime","description":"description","updateTime":"updateTime","stateReason":"stateReason","restoreConfig":{"clusterResourceConflictPolicy":"CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED","namespacedResourceRestoreMode":"NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED","allNamespaces":True,"selectedNamespaces":{"namespaces":["namespaces","namespaces"]},"selectedApplications":{"namespacedNames":[{"name":"name","namespace":"namespace"},{"name":"name","namespace":"namespace"}]},"excludedNamespaces":{"namespaces":["namespaces","namespaces"]},"transformationRules":[{"description":"description","resourceFilter":{"groupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"jsonPath":"jsonPath","namespaces":["namespaces","namespaces"]},"fieldActions":[{"fromPath":"fromPath","op":"OP_UNSPECIFIED","path":"path","value":"value"},{"fromPath":"fromPath","op":"OP_UNSPECIFIED","path":"path","value":"value"}]},{"description":"description","resourceFilter":{"groupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"jsonPath":"jsonPath","namespaces":["namespaces","namespaces"]},"fieldActions":[{"fromPath":"fromPath","op":"OP_UNSPECIFIED","path":"path","value":"value"},{"fromPath":"fromPath","op":"OP_UNSPECIFIED","path":"path","value":"value"}]}],"volumeDataRestorePolicy":"VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED","substitutionRules":[{"newValue":"newValue","targetGroupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"originalValuePattern":"originalValuePattern","targetNamespaces":["targetNamespaces","targetNamespaces"],"targetJsonPath":"targetJsonPath"},{"newValue":"newValue","targetGroupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"originalValuePattern":"originalValuePattern","targetNamespaces":["targetNamespaces","targetNamespaces"],"targetJsonPath":"targetJsonPath"}],"noNamespaces":True,"clusterResourceRestoreScope":{"noGroupKinds":True,"allGroupKinds":True,"selectedGroupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}],"excludedGroupKinds":[{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"},{"resourceKind":"resourceKind","resourceGroup":"resourceGroup"}]}},"labels":{"key":"labels"},"uid":"uid","createTime":"createTime","volumesRestoredCount":5,"name":"name","etag":"etag","state":"STATE_UNSPECIFIED","resourcesRestoredCount":1}
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

async def test_gkebackup_projects_locations_restore_plans_restores_volume_restores_get(client):
    """Test case for gkebackup_projects_locations_restore_plans_restores_volume_restores_get

    
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkebackup_projects_locations_restore_plans_restores_volume_restores_get_iam_policy(client):
    """Test case for gkebackup_projects_locations_restore_plans_restores_volume_restores_get_iam_policy

    
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
                    ('options.requestedPolicyVersion', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkebackup_projects_locations_restore_plans_restores_volume_restores_list(client):
    """Test case for gkebackup_projects_locations_restore_plans_restores_volume_restores_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/volumeRestores'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gkebackup_projects_locations_restore_plans_restores_volume_restores_set_iam_policy(client):
    """Test case for gkebackup_projects_locations_restore_plans_restores_volume_restores_set_iam_policy

    
    """
    body = {"updateMask":"updateMask","policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0,"auditConfigs":[{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"},{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"}]}}
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

async def test_gkebackup_projects_locations_restore_plans_restores_volume_restores_test_iam_permissions(client):
    """Test case for gkebackup_projects_locations_restore_plans_restores_volume_restores_test_iam_permissions

    
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

