# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.count_response import CountResponse
from openapi_server.models.download_mssql_backup_files_by_id_job_config import DownloadMssqlBackupFilesByIdJobConfig
from openapi_server.models.export_mssql_db_job_config import ExportMssqlDbJobConfig
from openapi_server.models.internal_job_instance_detail import InternalJobInstanceDetail
from openapi_server.models.job_scheduled_response import JobScheduledResponse
from openapi_server.models.missed_snapshot_list_response import MissedSnapshotListResponse
from openapi_server.models.mount_mssql_db_config import MountMssqlDbConfig
from openapi_server.models.mssql_availability_group_detail import MssqlAvailabilityGroupDetail
from openapi_server.models.mssql_availability_group_summary_list_response import MssqlAvailabilityGroupSummaryListResponse
from openapi_server.models.mssql_availability_group_update import MssqlAvailabilityGroupUpdate
from openapi_server.models.mssql_backup_job_config import MssqlBackupJobConfig
from openapi_server.models.mssql_backup_selection import MssqlBackupSelection
from openapi_server.models.mssql_backups import MssqlBackups
from openapi_server.models.mssql_batch_backup_job_config import MssqlBatchBackupJobConfig
from openapi_server.models.mssql_batch_backup_summary import MssqlBatchBackupSummary
from openapi_server.models.mssql_db_defaults import MssqlDbDefaults
from openapi_server.models.mssql_db_defaults_update import MssqlDbDefaultsUpdate
from openapi_server.models.mssql_db_detail import MssqlDbDetail
from openapi_server.models.mssql_db_snapshot_detail import MssqlDbSnapshotDetail
from openapi_server.models.mssql_db_snapshot_summary_list_response import MssqlDbSnapshotSummaryListResponse
from openapi_server.models.mssql_db_summary_list_response import MssqlDbSummaryListResponse
from openapi_server.models.mssql_db_update import MssqlDbUpdate
from openapi_server.models.mssql_db_update_id import MssqlDbUpdateId
from openapi_server.models.mssql_download_from_archive_config import MssqlDownloadFromArchiveConfig
from openapi_server.models.mssql_hierarchy_object_summary import MssqlHierarchyObjectSummary
from openapi_server.models.mssql_hierarchy_object_summary_list_response import MssqlHierarchyObjectSummaryListResponse
from openapi_server.models.mssql_host_configuration import MssqlHostConfiguration
from openapi_server.models.mssql_host_configuration_with_host_id import MssqlHostConfigurationWithHostId
from openapi_server.models.mssql_host_configuration_with_host_id_list_response import MssqlHostConfigurationWithHostIdListResponse
from openapi_server.models.mssql_instance_detail import MssqlInstanceDetail
from openapi_server.models.mssql_instance_summary_list_response import MssqlInstanceSummaryListResponse
from openapi_server.models.mssql_instance_update import MssqlInstanceUpdate
from openapi_server.models.mssql_log_shipping_create_config import MssqlLogShippingCreateConfig
from openapi_server.models.mssql_log_shipping_detail import MssqlLogShippingDetail
from openapi_server.models.mssql_log_shipping_reseed_config import MssqlLogShippingReseedConfig
from openapi_server.models.mssql_log_shipping_summary_list_response import MssqlLogShippingSummaryListResponse
from openapi_server.models.mssql_log_shipping_update import MssqlLogShippingUpdate
from openapi_server.models.mssql_missed_recoverable_range_list_response import MssqlMissedRecoverableRangeListResponse
from openapi_server.models.mssql_mount_detail import MssqlMountDetail
from openapi_server.models.mssql_mount_summary_list_response import MssqlMountSummaryListResponse
from openapi_server.models.mssql_recoverable_range_list_response import MssqlRecoverableRangeListResponse
from openapi_server.models.mssql_restore_estimate_result import MssqlRestoreEstimateResult
from openapi_server.models.mssql_restore_file import MssqlRestoreFile
from openapi_server.models.mssql_sla_domain_assign_info import MssqlSlaDomainAssignInfo
from openapi_server.models.mssql_snappable_id import MssqlSnappableId
from openapi_server.models.protected_objects_count import ProtectedObjectsCount
from openapi_server.models.restore_mssql_db_job_config import RestoreMssqlDbJobConfig


pytestmark = pytest.mark.asyncio

async def test_assign_mssql_sla_properties(client):
    """Test case for assign_mssql_sla_properties

    Assign SLA properties to SQL Server objects
    """
    body = {"logRetentionHours":6,"copyOnly":True,"useConfiguredDefaultLogRetention":True,"ids":["ids","ids"],"configuredSlaDomainId":"configuredSlaDomainId","existingSnapshotRetention":"RetainSnapshots","logBackupFrequencyInSeconds":0}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/sla_domain/assign',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_browse_mssql_backup_files(client):
    """Test case for browse_mssql_backup_files

    List snapshots and logs from a Microsoft SQL database
    """
    body = {"endPoint":{"date":"2000-01-23T04:56:07.000+00:00","lsnPoint":{"lsn":"lsn","recoveryForkGuid":"recoveryForkGuid"},"timestampMs":0},"legalHoldDownloadConfig":{"isLegalHoldDownload":True},"startPoint":{"date":"2000-01-23T04:56:07.000+00:00","lsnPoint":{"lsn":"lsn","recoveryForkGuid":"recoveryForkGuid"},"timestampMs":0},"recoveryPoint":{"date":"2000-01-23T04:56:07.000+00:00","lsnPoint":{"lsn":"lsn","recoveryForkGuid":"recoveryForkGuid"},"timestampMs":0},"backupType":"Snapshot"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/db/{id}/browse'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_update_mssql_db_v1(client):
    """Test case for bulk_update_mssql_db_v1

    Update multiple Microsoft SQL databases
    """
    body = {"updateProperties":{"isPaused":True,"shouldForceFull":True,"logRetentionHours":6,"copyOnly":True,"postBackupScript":{"scriptPath":"scriptPath","scriptErrorAction":"abort","timeoutMs":7},"useConfiguredDefaultLogRetention":True,"preBackupScript":{"scriptPath":"scriptPath","scriptErrorAction":"abort","timeoutMs":7},"configuredSlaDomainId":"configuredSlaDomainId","maxDataStreams":1,"logBackupFrequencyInSeconds":0},"databaseId":"databaseId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/mssql/db/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_count_mssql_db_v1(client):
    """Test case for count_mssql_db_v1

    Returns a count of Microsoft SQL databases
    """
    params = [('root_id', 'root_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_count_mssql_instance_v1(client):
    """Test case for count_mssql_instance_v1

    Returns a count of Microsoft SQL instances
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/instance/count',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_download_mssql_backup_files(client):
    """Test case for create_download_mssql_backup_files

    Download snapshots and logs backups from a Microsoft SQL Database
    """
    body = {"endPoint":{"date":"2000-01-23T04:56:07.000+00:00","lsnPoint":{"lsn":"lsn","recoveryForkGuid":"recoveryForkGuid"},"timestampMs":0},"legalHoldDownloadConfig":{"isLegalHoldDownload":True},"startPoint":{"date":"2000-01-23T04:56:07.000+00:00","lsnPoint":{"lsn":"lsn","recoveryForkGuid":"recoveryForkGuid"},"timestampMs":0},"recoveryPoint":{"date":"2000-01-23T04:56:07.000+00:00","lsnPoint":{"lsn":"lsn","recoveryForkGuid":"recoveryForkGuid"},"timestampMs":0},"backupType":"Snapshot"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/db/{id}/download_files'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_download_mssql_backup_files_by_id(client):
    """Test case for create_download_mssql_backup_files_by_id

    Downloads a list of snapshot and log backups from a Microsoft SQL database
    """
    body = {"legalHoldDownloadConfig":{"isLegalHoldDownload":True},"items":["items","items"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/db/{id}/download_files_by_id'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_export_mssql_db(client):
    """Test case for create_export_mssql_db

    Export a Microsoft SQL database to a new location
    """
    body = {"targetLogFilePath":"targetLogFilePath","targetInstanceId":"targetInstanceId","targetDatabaseName":"targetDatabaseName","allowOverwrite":False,"finishRecovery":True,"targetFilePaths":[{"logicalName":"logicalName","newFilename":"newFilename","exportPath":"exportPath","newLogicalName":"newLogicalName"},{"logicalName":"logicalName","newFilename":"newFilename","exportPath":"exportPath","newLogicalName":"newLogicalName"}],"maxDataStreams":0,"recoveryPoint":{"date":"2000-01-23T04:56:07.000+00:00","lsnPoint":{"lsn":"lsn","recoveryForkGuid":"recoveryForkGuid"},"timestampMs":0},"targetDataFilePath":"targetDataFilePath"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/db/{id}/export'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_log_shipping_configuration(client):
    """Test case for create_log_shipping_configuration

    Create a log shipping configuration
    """
    body = {"targetLogFilePath":"targetLogFilePath","targetInstanceId":"targetInstanceId","targetDatabaseName":"targetDatabaseName","shouldDisconnectStandbyUsers":True,"targetFilePaths":[{"logicalName":"logicalName","newFilename":"newFilename","exportPath":"exportPath","newLogicalName":"newLogicalName"},{"logicalName":"logicalName","newFilename":"newFilename","exportPath":"exportPath","newLogicalName":"newLogicalName"}],"state":"RESTORING","maxDataStreams":0,"targetDataFilePath":"targetDataFilePath"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/db/{id}/log_shipping'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_mssql_host_config(client):
    """Test case for create_mssql_host_config

    Create a SQL Server host configuration
    """
    body = {"throttlePhysicalHostMaxRefCount":7,"physicalHostLogBackupThrottleMaxRefCount":2,"fileRestoreReadParallelism":0,"enableDatabaseBatchSnapshots":"Enabled","hostId":"hostId","fileRestoreWriteParallelism":6,"physicalHostDatabaseRestoreThrottleMaxRefCount":5,"fileTransferParallelism":1,"mssqlDefaultMaxDataStreamsPerDatabase":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/host/configuration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_mssql_mount(client):
    """Test case for create_mssql_mount

    Live Mount SQL Server database from a point in time copy
    """
    body = {"targetInstanceId":"targetInstanceId","recoveryModel":"SIMPLE","mountedDatabaseName":"mountedDatabaseName","recoveryPoint":{"date":"2000-01-23T04:56:07.000+00:00","lsnPoint":{"lsn":"lsn","recoveryForkGuid":"recoveryForkGuid"},"timestampMs":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/db/{id}/mount'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_mssql_unmount(client):
    """Test case for create_mssql_unmount

    Delete a Live Mount of a SQL Server database
    """
    params = [('force', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/mssql/db/mount/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_on_demand_mssql_backup(client):
    """Test case for create_on_demand_mssql_backup

    Take an on-demand backup of a Microsoft SQL database
    """
    body = {"slaId":"slaId","forceFullSnapshot":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/db/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_on_demand_mssql_batch_backup_v1(client):
    """Test case for create_on_demand_mssql_batch_backup_v1

    Take an on-demand backup of multiple Microsoft SQL databases
    """
    body = {"availabilityGroupIds":["availabilityGroupIds","availabilityGroupIds"],"slaId":"slaId","instanceIds":["instanceIds","instanceIds"],"databaseIds":["databaseIds","databaseIds"],"windowsClusterIds":["windowsClusterIds","windowsClusterIds"],"forceFullSnapshot":True,"hostIds":["hostIds","hostIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/db/bulk/snapshot',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_on_demand_mssql_log_backup(client):
    """Test case for create_on_demand_mssql_log_backup

    Take an on-demand log backup for a Microsoft SQL database
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/db/{id}/log_backup'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_restore_mssql_db(client):
    """Test case for create_restore_mssql_db

    Restore a Microsoft SQL database
    """
    body = {"finishRecovery":True,"maxDataStreams":0,"recoveryPoint":{"date":"2000-01-23T04:56:07.000+00:00","lsnPoint":{"lsn":"lsn","recoveryForkGuid":"recoveryForkGuid"},"timestampMs":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/db/{id}/restore'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_downloaded_mssql_db_recoverable_ranges_v1(client):
    """Test case for delete_downloaded_mssql_db_recoverable_ranges_v1

    Delete downloaded recoverable ranges of a Microsoft SQL database
    """
    params = [('after_time', '2013-10-20T19:20:30+01:00'),
                    ('before_time', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/mssql/db/{id}/recoverable_range/download'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_log_shipping_configuration(client):
    """Test case for delete_log_shipping_configuration

    Delete a specified log shipping configuration
    """
    params = [('delete_secondary_database', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/mssql/db/log_shipping/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_mssql_db_snapshots(client):
    """Test case for delete_mssql_db_snapshots

    Delete all snapshots of a Microsoft SQL database
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/mssql/db/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_mssql_host_config(client):
    """Test case for delete_mssql_host_config

    Delete the SQL Server host configuration
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/mssql/host/configuration/{host_id}'.format(host_id='host_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_from_archive(client):
    """Test case for download_from_archive

    Download snapshots and log backups from archival
    """
    body = {"recoveryPoint":{"date":"2000-01-23T04:56:07.000+00:00","lsnPoint":{"lsn":"lsn","recoveryForkGuid":"recoveryForkGuid"},"timestampMs":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/db/{id}/download'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_compatible_mssql_instances_v1(client):
    """Test case for get_compatible_mssql_instances_v1

    Get compatible instances for the recovery of a Microsoft SQL database
    """
    params = [('recovery_time', '2013-10-20T19:20:30+01:00'),
                    ('recovery_type', 'recovery_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/{id}/compatible_instance'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default_db_properties_v1(client):
    """Test case for get_default_db_properties_v1

    Returns the current default properties for Microsoft SQL databases
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/defaults',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_delete_mssql_db_recoverable_ranges_status_v1(client):
    """Test case for get_delete_mssql_db_recoverable_ranges_status_v1

    Get the deletion status of downloaded recoverable ranges
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/recoverable_range/download/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_log_shipping_configuration(client):
    """Test case for get_log_shipping_configuration

    Get a log shipping configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/log_shipping/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_missed_mssql_db_snapshots(client):
    """Test case for get_missed_mssql_db_snapshots

    Get summary information for missed snapshots of a SQL database
    """
    params = [('after_time', '2013-10-20T19:20:30+01:00'),
                    ('before_time', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/{id}/missed_snapshot'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mssql_async_request_status(client):
    """Test case for get_mssql_async_request_status

    Get details for an async request
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/request/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mssql_availability_group_v1(client):
    """Test case for get_mssql_availability_group_v1

    Returns detailed information for a Microsoft SQL availability group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/availability_group/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mssql_db(client):
    """Test case for get_mssql_db

    Get detailed information for a Microsoft SQL database
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mssql_db_missed_recoverable_ranges(client):
    """Test case for get_mssql_db_missed_recoverable_ranges

    Get missed recoverable ranges of a Microsoft SQL database
    """
    params = [('after_time', '2013-10-20T19:20:30+01:00'),
                    ('before_time', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/{id}/missed_recoverable_range'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mssql_db_recoverable_ranges(client):
    """Test case for get_mssql_db_recoverable_ranges

    Get recoverable ranges of a Microsoft SQL database
    """
    params = [('after_time', '2013-10-20T19:20:30+01:00'),
                    ('before_time', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/{id}/recoverable_range'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mssql_db_snapshot(client):
    """Test case for get_mssql_db_snapshot

    Get details information about a Microsoft SQL database snapshot
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mssql_hierarchy_children(client):
    """Test case for get_mssql_hierarchy_children

    Get list of immediate descendant objects
    """
    params = [('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('object_type', ['object_type_example']),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example'),
                    ('is_relic', True),
                    ('is_live_mount', True),
                    ('is_log_shipping_secondary', True),
                    ('is_clustered', True),
                    ('has_instances', True),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('snappable_status', 'snappable_status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/hierarchy/{id}/children'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mssql_hierarchy_descendants(client):
    """Test case for get_mssql_hierarchy_descendants

    Get list of descendant objects
    """
    params = [('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('object_type', ['object_type_example']),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example'),
                    ('is_relic', True),
                    ('is_live_mount', True),
                    ('is_log_shipping_secondary', True),
                    ('is_clustered', True),
                    ('has_instances', True),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('snappable_status', 'snappable_status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/hierarchy/{id}/descendants'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mssql_hierarchy_object(client):
    """Test case for get_mssql_hierarchy_object

    Get summary of a SQL Server hierarchy object
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/hierarchy/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mssql_host_config(client):
    """Test case for get_mssql_host_config

    Get the configuration for a specific host
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/host/configuration/{host_id}'.format(host_id='host_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mssql_instance(client):
    """Test case for get_mssql_instance

    Get detailed information for a Microsoft SQL instance
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/instance/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mssql_mount(client):
    """Test case for get_mssql_mount

    Get detailed information for a Live Mount of a SQL Server database
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/mount/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_on_demand_mssql_batch_backup_result_v1(client):
    """Test case for get_on_demand_mssql_batch_backup_result_v1

    Returns details for an on-demand backup of multiple Microsoft SQL databases
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/bulk/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mssql_get_restore_files_v1(client):
    """Test case for mssql_get_restore_files_v1

    Returns a list all database files to be restored
    """
    params = [('time', '2013-10-20T19:20:30+01:00'),
                    ('lsn', 'lsn_example'),
                    ('recovery_fork_guid', 'recovery_fork_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/{id}/restore_files'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mssql_get_snappable_id_v1(client):
    """Test case for mssql_get_snappable_id_v1

    Returns the snappableId for a Microsoft SQL database
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/{id}/snappable_id'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mssql_restore_estimate_v1(client):
    """Test case for mssql_restore_estimate_v1

    Returns a size estimate for a restore or export
    """
    params = [('time', '2013-10-20T19:20:30+01:00'),
                    ('lsn', 'lsn_example'),
                    ('recovery_fork_guid', 'recovery_fork_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/{id}/restore_estimate'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_log_shipping_configurations(client):
    """Test case for query_log_shipping_configurations

    Get log shipping configurations
    """
    params = [('primary_database_id', 'primary_database_id_example'),
                    ('primary_database_name', 'primary_database_name_example'),
                    ('secondary_database_name', 'secondary_database_name_example'),
                    ('location', 'location_example'),
                    ('status', 'status_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/log_shipping',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_mssql_availability_group_v1(client):
    """Test case for query_mssql_availability_group_v1

    Returns summary information for Microsoft SQL availability groups
    """
    params = [('primary_cluster_id', 'primary_cluster_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/availability_group',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_mssql_db(client):
    """Test case for query_mssql_db

    Get summary information for SQL Server databases
    """
    params = [('instance_id', 'instance_id_example'),
                    ('availability_group_id', 'availability_group_id_example'),
                    ('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('name', 'name_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('is_relic', True),
                    ('is_live_mount', True),
                    ('is_log_shipping_secondary', True),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('include_backup_task_info', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_mssql_db_snapshot(client):
    """Test case for query_mssql_db_snapshot

    Get summary information for snapshots of a Microsoft SQL database
    """
    params = [('after_time', '2013-10-20T19:20:30+01:00'),
                    ('before_time', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_mssql_host_config(client):
    """Test case for query_mssql_host_config

    Get the summary of SQL Server host configurations
    """
    params = [('host_id', ['host_id_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/host/configuration',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_mssql_instance(client):
    """Test case for query_mssql_instance

    Get summary information for Microsoft SQL instances
    """
    params = [('root_id', 'root_id_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('snappable_status', 'snappable_status_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/instance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_mssql_mount(client):
    """Test case for query_mssql_mount

    Get summary information for all Live Mounts SQL Server databases
    """
    params = [('source_database_id', 'source_database_id_example'),
                    ('source_database_name', 'source_database_name_example'),
                    ('target_instance_id', 'target_instance_id_example'),
                    ('mounted_database_name', 'mounted_database_name_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mssql/db/mount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reseed_secondary(client):
    """Test case for reseed_secondary

    Reseed a secondary database
    """
    body = {"shouldDisconnectStandbyUsers":True,"state":"RESTORING"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/mssql/db/log_shipping/{id}/reseed'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_default_db_properties_v1(client):
    """Test case for update_default_db_properties_v1

    Update the default properties for Microsoft SQL databases
    """
    body = {"logRetentionTimeInHours":6,"cbtStatus":True,"logBackupFrequencyInSeconds":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/mssql/db/defaults',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_log_shipping_configuration(client):
    """Test case for update_log_shipping_configuration

    Update a specified log shipping configuration
    """
    body = {"shouldDisconnectStandbyUsers":True,"state":"RESTORING"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/mssql/db/log_shipping/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_mssql_availability_group_v1(client):
    """Test case for update_mssql_availability_group_v1

    Update a Microsoft SQL availability group
    """
    body = {"logRetentionHours":6,"copyOnly":True,"useConfiguredDefaultLogRetention":True,"configuredSlaDomainId":"configuredSlaDomainId","logBackupFrequencyInSeconds":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/mssql/availability_group/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_mssql_db(client):
    """Test case for update_mssql_db

    Update a Microsoft SQL database
    """
    body = {"isPaused":True,"shouldForceFull":True,"logRetentionHours":6,"copyOnly":True,"postBackupScript":{"scriptPath":"scriptPath","scriptErrorAction":"abort","timeoutMs":7},"useConfiguredDefaultLogRetention":True,"preBackupScript":{"scriptPath":"scriptPath","scriptErrorAction":"abort","timeoutMs":7},"configuredSlaDomainId":"configuredSlaDomainId","maxDataStreams":1,"logBackupFrequencyInSeconds":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/mssql/db/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_mssql_host_config(client):
    """Test case for update_mssql_host_config

    Update host configuration
    """
    body = {"throttlePhysicalHostMaxRefCount":7,"physicalHostLogBackupThrottleMaxRefCount":2,"fileRestoreReadParallelism":0,"enableDatabaseBatchSnapshots":"Enabled","fileRestoreWriteParallelism":6,"physicalHostDatabaseRestoreThrottleMaxRefCount":5,"fileTransferParallelism":1,"mssqlDefaultMaxDataStreamsPerDatabase":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/mssql/host/configuration/{host_id}'.format(host_id='host_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_mssql_instance(client):
    """Test case for update_mssql_instance

    Update a Microsoft SQL instance
    """
    body = {"logRetentionHours":6,"copyOnly":True,"useConfiguredDefaultLogRetention":True,"configuredSlaDomainId":"configuredSlaDomainId","logBackupFrequencyInSeconds":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/mssql/instance/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

