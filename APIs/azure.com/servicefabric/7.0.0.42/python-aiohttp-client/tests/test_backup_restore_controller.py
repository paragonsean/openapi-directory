# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.backup_partition_description import BackupPartitionDescription
from openapi_server.models.backup_policy_description import BackupPolicyDescription
from openapi_server.models.backup_progress_info import BackupProgressInfo
from openapi_server.models.disable_backup_description import DisableBackupDescription
from openapi_server.models.enable_backup_description import EnableBackupDescription
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.get_backup_by_storage_query_description import GetBackupByStorageQueryDescription
from openapi_server.models.paged_backup_configuration_info_list import PagedBackupConfigurationInfoList
from openapi_server.models.paged_backup_entity_list import PagedBackupEntityList
from openapi_server.models.paged_backup_info_list import PagedBackupInfoList
from openapi_server.models.paged_backup_policy_description_list import PagedBackupPolicyDescriptionList
from openapi_server.models.partition_backup_configuration_info import PartitionBackupConfigurationInfo
from openapi_server.models.restore_partition_description import RestorePartitionDescription
from openapi_server.models.restore_progress_info import RestoreProgressInfo


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_backup_partition(client):
    """Test case for backup_partition

    Triggers backup of the partition's state.
    """
    backup_partition_description = openapi_server.BackupPartitionDescription()
    params = [('BackupTimeout', 10),
                    ('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/Backup'.format(partition_id='partition_id_example'),
        headers=headers,
        json=backup_partition_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_backup_policy(client):
    """Test case for create_backup_policy

    Creates a backup policy.
    """
    backup_policy_description = openapi_server.BackupPolicyDescription()
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/BackupRestore/BackupPolicies/$/Create',
        headers=headers,
        json=backup_policy_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_backup_policy(client):
    """Test case for delete_backup_policy

    Deletes the backup policy.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/BackupRestore/BackupPolicies/{backup_policy_name}/$/Delete'.format(backup_policy_name='backup_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_disable_application_backup(client):
    """Test case for disable_application_backup

    Disables periodic backup of Service Fabric application.
    """
    disable_backup_description = openapi_server.DisableBackupDescription()
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_id}/$/DisableBackup'.format(application_id='application_id_example'),
        headers=headers,
        json=disable_backup_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_disable_partition_backup(client):
    """Test case for disable_partition_backup

    Disables periodic backup of Service Fabric partition which was previously enabled.
    """
    disable_backup_description = openapi_server.DisableBackupDescription()
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/DisableBackup'.format(partition_id='partition_id_example'),
        headers=headers,
        json=disable_backup_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_disable_service_backup(client):
    """Test case for disable_service_backup

    Disables periodic backup of Service Fabric service which was previously enabled.
    """
    disable_backup_description = openapi_server.DisableBackupDescription()
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/{service_id}/$/DisableBackup'.format(service_id='service_id_example'),
        headers=headers,
        json=disable_backup_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_enable_application_backup(client):
    """Test case for enable_application_backup

    Enables periodic backup of stateful partitions under this Service Fabric application.
    """
    enable_backup_description = openapi_server.EnableBackupDescription()
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_id}/$/EnableBackup'.format(application_id='application_id_example'),
        headers=headers,
        json=enable_backup_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_enable_partition_backup(client):
    """Test case for enable_partition_backup

    Enables periodic backup of the stateful persisted partition.
    """
    enable_backup_description = openapi_server.EnableBackupDescription()
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/EnableBackup'.format(partition_id='partition_id_example'),
        headers=headers,
        json=enable_backup_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_enable_service_backup(client):
    """Test case for enable_service_backup

    Enables periodic backup of stateful partitions under this Service Fabric service.
    """
    enable_backup_description = openapi_server.EnableBackupDescription()
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/{service_id}/$/EnableBackup'.format(service_id='service_id_example'),
        headers=headers,
        json=enable_backup_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_entities_backed_up_by_policy(client):
    """Test case for get_all_entities_backed_up_by_policy

    Gets the list of backup entities that are associated with this policy.
    """
    params = [('api-version', 6.4),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('MaxResults', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/BackupRestore/BackupPolicies/{backup_policy_name}/$/GetBackupEnabledEntities'.format(backup_policy_name='backup_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_backup_configuration_info(client):
    """Test case for get_application_backup_configuration_info

    Gets the Service Fabric application backup configuration information.
    """
    params = [('api-version', 6.4),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('MaxResults', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_id}/$/GetBackupConfigurationInfo'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_backup_list(client):
    """Test case for get_application_backup_list

    Gets the list of backups available for every partition in this application.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60),
                    ('Latest', False),
                    ('StartDateTimeFilter', '2013-10-20T19:20:30+01:00'),
                    ('EndDateTimeFilter', '2013-10-20T19:20:30+01:00'),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('MaxResults', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Applications/{application_id}/$/GetBackups'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_backup_policy_by_name(client):
    """Test case for get_backup_policy_by_name

    Gets a particular backup policy by name.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/BackupRestore/BackupPolicies/{backup_policy_name}'.format(backup_policy_name='backup_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_backup_policy_list(client):
    """Test case for get_backup_policy_list

    Gets all the backup policies configured.
    """
    params = [('api-version', 6.4),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('MaxResults', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/BackupRestore/BackupPolicies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_backups_from_backup_location(client):
    """Test case for get_backups_from_backup_location

    Gets the list of backups available for the specified backed up entity at the specified backup location.
    """
    get_backup_by_storage_query_description = openapi_server.GetBackupByStorageQueryDescription()
    params = [('api-version', 6.4),
                    ('timeout', 60),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('MaxResults', 0)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/BackupRestore/$/GetBackups',
        headers=headers,
        json=get_backup_by_storage_query_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partition_backup_configuration_info(client):
    """Test case for get_partition_backup_configuration_info

    Gets the partition backup configuration information
    """
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetBackupConfigurationInfo'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partition_backup_list(client):
    """Test case for get_partition_backup_list

    Gets the list of backups available for the specified partition.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60),
                    ('Latest', False),
                    ('StartDateTimeFilter', '2013-10-20T19:20:30+01:00'),
                    ('EndDateTimeFilter', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetBackups'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partition_backup_progress(client):
    """Test case for get_partition_backup_progress

    Gets details for the latest backup triggered for this partition.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetBackupProgress'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_partition_restore_progress(client):
    """Test case for get_partition_restore_progress

    Gets details for the latest restore operation triggered for this partition.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Partitions/{partition_id}/$/GetRestoreProgress'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_backup_configuration_info(client):
    """Test case for get_service_backup_configuration_info

    Gets the Service Fabric service backup configuration information.
    """
    params = [('api-version', 6.4),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('MaxResults', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Services/{service_id}/$/GetBackupConfigurationInfo'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_backup_list(client):
    """Test case for get_service_backup_list

    Gets the list of backups available for every partition in this service.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60),
                    ('Latest', False),
                    ('StartDateTimeFilter', '2013-10-20T19:20:30+01:00'),
                    ('EndDateTimeFilter', '2013-10-20T19:20:30+01:00'),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('MaxResults', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Services/{service_id}/$/GetBackups'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_restore_partition(client):
    """Test case for restore_partition

    Triggers restore of the state of the partition using the specified restore partition description.
    """
    restore_partition_description = openapi_server.RestorePartitionDescription()
    params = [('RestoreTimeout', 10),
                    ('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/Restore'.format(partition_id='partition_id_example'),
        headers=headers,
        json=restore_partition_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resume_application_backup(client):
    """Test case for resume_application_backup

    Resumes periodic backup of a Service Fabric application which was previously suspended.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_id}/$/ResumeBackup'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resume_partition_backup(client):
    """Test case for resume_partition_backup

    Resumes periodic backup of partition which was previously suspended.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/ResumeBackup'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resume_service_backup(client):
    """Test case for resume_service_backup

    Resumes periodic backup of a Service Fabric service which was previously suspended.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/{service_id}/$/ResumeBackup'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suspend_application_backup(client):
    """Test case for suspend_application_backup

    Suspends periodic backup for the specified Service Fabric application.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Applications/{application_id}/$/SuspendBackup'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suspend_partition_backup(client):
    """Test case for suspend_partition_backup

    Suspends periodic backup for the specified partition.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Partitions/{partition_id}/$/SuspendBackup'.format(partition_id='partition_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suspend_service_backup(client):
    """Test case for suspend_service_backup

    Suspends periodic backup for the specified Service Fabric service.
    """
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Services/{service_id}/$/SuspendBackup'.format(service_id='service_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_backup_policy(client):
    """Test case for update_backup_policy

    Updates the backup policy.
    """
    backup_policy_description = openapi_server.BackupPolicyDescription()
    params = [('api-version', 6.4),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/BackupRestore/BackupPolicies/{backup_policy_name}/$/Update'.format(backup_policy_name='backup_policy_name_example'),
        headers=headers,
        json=backup_policy_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

