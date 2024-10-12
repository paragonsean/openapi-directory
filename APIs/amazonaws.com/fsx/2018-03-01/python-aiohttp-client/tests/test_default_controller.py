# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.associate_file_system_aliases_request import AssociateFileSystemAliasesRequest
from openapi_server.models.associate_file_system_aliases_response import AssociateFileSystemAliasesResponse
from openapi_server.models.cancel_data_repository_task_request import CancelDataRepositoryTaskRequest
from openapi_server.models.cancel_data_repository_task_response import CancelDataRepositoryTaskResponse
from openapi_server.models.copy_backup_request import CopyBackupRequest
from openapi_server.models.copy_backup_response import CopyBackupResponse
from openapi_server.models.create_backup_request import CreateBackupRequest
from openapi_server.models.create_backup_response import CreateBackupResponse
from openapi_server.models.create_data_repository_association_request import CreateDataRepositoryAssociationRequest
from openapi_server.models.create_data_repository_association_response import CreateDataRepositoryAssociationResponse
from openapi_server.models.create_data_repository_task_request import CreateDataRepositoryTaskRequest
from openapi_server.models.create_data_repository_task_response import CreateDataRepositoryTaskResponse
from openapi_server.models.create_file_cache_request import CreateFileCacheRequest
from openapi_server.models.create_file_cache_response import CreateFileCacheResponse
from openapi_server.models.create_file_system_from_backup_request import CreateFileSystemFromBackupRequest
from openapi_server.models.create_file_system_from_backup_response import CreateFileSystemFromBackupResponse
from openapi_server.models.create_file_system_request import CreateFileSystemRequest
from openapi_server.models.create_file_system_response import CreateFileSystemResponse
from openapi_server.models.create_snapshot_request import CreateSnapshotRequest
from openapi_server.models.create_snapshot_response import CreateSnapshotResponse
from openapi_server.models.create_storage_virtual_machine_request import CreateStorageVirtualMachineRequest
from openapi_server.models.create_storage_virtual_machine_response import CreateStorageVirtualMachineResponse
from openapi_server.models.create_volume_from_backup_request import CreateVolumeFromBackupRequest
from openapi_server.models.create_volume_from_backup_response import CreateVolumeFromBackupResponse
from openapi_server.models.create_volume_request import CreateVolumeRequest
from openapi_server.models.create_volume_response import CreateVolumeResponse
from openapi_server.models.delete_backup_request import DeleteBackupRequest
from openapi_server.models.delete_backup_response import DeleteBackupResponse
from openapi_server.models.delete_data_repository_association_request import DeleteDataRepositoryAssociationRequest
from openapi_server.models.delete_data_repository_association_response import DeleteDataRepositoryAssociationResponse
from openapi_server.models.delete_file_cache_request import DeleteFileCacheRequest
from openapi_server.models.delete_file_cache_response import DeleteFileCacheResponse
from openapi_server.models.delete_file_system_request import DeleteFileSystemRequest
from openapi_server.models.delete_file_system_response import DeleteFileSystemResponse
from openapi_server.models.delete_snapshot_request import DeleteSnapshotRequest
from openapi_server.models.delete_snapshot_response import DeleteSnapshotResponse
from openapi_server.models.delete_storage_virtual_machine_request import DeleteStorageVirtualMachineRequest
from openapi_server.models.delete_storage_virtual_machine_response import DeleteStorageVirtualMachineResponse
from openapi_server.models.delete_volume_request import DeleteVolumeRequest
from openapi_server.models.delete_volume_response import DeleteVolumeResponse
from openapi_server.models.describe_backups_request import DescribeBackupsRequest
from openapi_server.models.describe_backups_response import DescribeBackupsResponse
from openapi_server.models.describe_data_repository_associations_request import DescribeDataRepositoryAssociationsRequest
from openapi_server.models.describe_data_repository_associations_response import DescribeDataRepositoryAssociationsResponse
from openapi_server.models.describe_data_repository_tasks_request import DescribeDataRepositoryTasksRequest
from openapi_server.models.describe_data_repository_tasks_response import DescribeDataRepositoryTasksResponse
from openapi_server.models.describe_file_caches_request import DescribeFileCachesRequest
from openapi_server.models.describe_file_caches_response import DescribeFileCachesResponse
from openapi_server.models.describe_file_system_aliases_request import DescribeFileSystemAliasesRequest
from openapi_server.models.describe_file_system_aliases_response import DescribeFileSystemAliasesResponse
from openapi_server.models.describe_file_systems_request import DescribeFileSystemsRequest
from openapi_server.models.describe_file_systems_response import DescribeFileSystemsResponse
from openapi_server.models.describe_snapshots_request import DescribeSnapshotsRequest
from openapi_server.models.describe_snapshots_response import DescribeSnapshotsResponse
from openapi_server.models.describe_storage_virtual_machines_request import DescribeStorageVirtualMachinesRequest
from openapi_server.models.describe_storage_virtual_machines_response import DescribeStorageVirtualMachinesResponse
from openapi_server.models.describe_volumes_request import DescribeVolumesRequest
from openapi_server.models.describe_volumes_response import DescribeVolumesResponse
from openapi_server.models.disassociate_file_system_aliases_request import DisassociateFileSystemAliasesRequest
from openapi_server.models.disassociate_file_system_aliases_response import DisassociateFileSystemAliasesResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.release_file_system_nfs_v3_locks_request import ReleaseFileSystemNfsV3LocksRequest
from openapi_server.models.release_file_system_nfs_v3_locks_response import ReleaseFileSystemNfsV3LocksResponse
from openapi_server.models.restore_volume_from_snapshot_request import RestoreVolumeFromSnapshotRequest
from openapi_server.models.restore_volume_from_snapshot_response import RestoreVolumeFromSnapshotResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_data_repository_association_request import UpdateDataRepositoryAssociationRequest
from openapi_server.models.update_data_repository_association_response import UpdateDataRepositoryAssociationResponse
from openapi_server.models.update_file_cache_request import UpdateFileCacheRequest
from openapi_server.models.update_file_cache_response import UpdateFileCacheResponse
from openapi_server.models.update_file_system_request import UpdateFileSystemRequest
from openapi_server.models.update_file_system_response import UpdateFileSystemResponse
from openapi_server.models.update_snapshot_request import UpdateSnapshotRequest
from openapi_server.models.update_snapshot_response import UpdateSnapshotResponse
from openapi_server.models.update_storage_virtual_machine_request import UpdateStorageVirtualMachineRequest
from openapi_server.models.update_storage_virtual_machine_response import UpdateStorageVirtualMachineResponse
from openapi_server.models.update_volume_request import UpdateVolumeRequest
from openapi_server.models.update_volume_response import UpdateVolumeResponse


pytestmark = pytest.mark.asyncio

async def test_associate_file_system_aliases(client):
    """Test case for associate_file_system_aliases

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","FileSystemId":"","Aliases":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.AssociateFileSystemAliases',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_data_repository_task(client):
    """Test case for cancel_data_repository_task

    
    """
    body = {"TaskId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.CancelDataRepositoryTask',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_backup(client):
    """Test case for copy_backup

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","SourceBackupId":"","KmsKeyId":"KmsKeyId","SourceRegion":"","Tags":[{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""}],"CopyTags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.CopyBackup',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_backup(client):
    """Test case for create_backup

    
    """
    body = {"ClientRequestToken":"","VolumeId":"","FileSystemId":"","Tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.CreateBackup',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_data_repository_association(client):
    """Test case for create_data_repository_association

    
    """
    body = {"FileSystemPath":"","DataRepositoryPath":"","BatchImportMetaDataOnCreate":"","S3":{"AutoImportPolicy":{"Events":""},"AutoExportPolicy":{"Events":""}},"ClientRequestToken":"ClientRequestToken","FileSystemId":"FileSystemId","ImportedFileChunkSize":"","Tags":[{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.CreateDataRepositoryAssociation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_data_repository_task(client):
    """Test case for create_data_repository_task

    
    """
    body = {"CapacityToRelease":"","ClientRequestToken":"ClientRequestToken","Type":"","Report":{"Path":"","Format":"","Scope":"","Enabled":""},"FileSystemId":"FileSystemId","Paths":"","Tags":[{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.CreateDataRepositoryTask',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_file_cache(client):
    """Test case for create_file_cache

    
    """
    body = {"ClientRequestToken":"","DataRepositoryAssociations":"","StorageCapacity":"","KmsKeyId":"","CopyTagsToDataRepositoryAssociations":"","FileCacheTypeVersion":"","FileCacheType":"","LustreConfiguration":{"WeeklyMaintenanceStartTime":"WeeklyMaintenanceStartTime","MetadataConfiguration":{"StorageCapacity":""},"DeploymentType":"","PerUnitStorageThroughput":""},"SubnetIds":[null,null,null,null,null],"SecurityGroupIds":"","Tags":[{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.CreateFileCache',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_file_system(client):
    """Test case for create_file_system

    
    """
    body = {"StorageType":"","StorageCapacity":"","KmsKeyId":"KmsKeyId","LustreConfiguration":{"DriveCacheType":"","AutoImportPolicy":"","ImportedFileChunkSize":"","DeploymentType":"","LogConfiguration":{"Destination":"","Level":""},"DataCompressionType":"","WeeklyMaintenanceStartTime":"","ImportPath":"","RootSquashConfiguration":{"RootSquash":"","NoSquashNids":""},"DailyAutomaticBackupStartTime":"DailyAutomaticBackupStartTime","CopyTagsToBackups":"","ExportPath":"","PerUnitStorageThroughput":"","AutomaticBackupRetentionDays":""},"OntapConfiguration":{"FsxAdminPassword":"","RouteTableIds":"","WeeklyMaintenanceStartTime":"WeeklyMaintenanceStartTime","DiskIopsConfiguration":{"Mode":"","Iops":""},"DeploymentType":"","DailyAutomaticBackupStartTime":"DailyAutomaticBackupStartTime","ThroughputCapacity":"","AutomaticBackupRetentionDays":7,"EndpointIpAddressRange":"","PreferredSubnetId":""},"SubnetIds":"","SecurityGroupIds":"","WindowsConfiguration":{"SelfManagedActiveDirectoryConfiguration":{"FileSystemAdministratorsGroup":"","UserName":"","DomainName":"","OrganizationalUnitDistinguishedName":"","DnsIps":"","Password":""},"AuditLogConfiguration":{"FileAccessAuditLogLevel":"","FileShareAccessAuditLogLevel":"","AuditLogDestination":""},"WeeklyMaintenanceStartTime":"","ActiveDirectoryId":"","DeploymentType":"","Aliases":"","ThroughputCapacity":"","DailyAutomaticBackupStartTime":"","CopyTagsToBackups":"","AutomaticBackupRetentionDays":"","PreferredSubnetId":""},"FileSystemTypeVersion":"","OpenZFSConfiguration":{"WeeklyMaintenanceStartTime":"WeeklyMaintenanceStartTime","DiskIopsConfiguration":{"Mode":"","Iops":""},"CopyTagsToVolumes":"","DeploymentType":"","CopyTagsToBackups":"","DailyAutomaticBackupStartTime":"DailyAutomaticBackupStartTime","ThroughputCapacity":"","RootVolumeConfiguration":{"ReadOnly":"","DataCompressionType":"","NfsExports":"","CopyTagsToSnapshots":"","RecordSizeKiB":"","UserAndGroupQuotas":""},"AutomaticBackupRetentionDays":54},"ClientRequestToken":"","FileSystemType":"","Tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.CreateFileSystem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_file_system_from_backup(client):
    """Test case for create_file_system_from_backup

    
    """
    body = {"FileSystemTypeVersion":"","OpenZFSConfiguration":{"WeeklyMaintenanceStartTime":"WeeklyMaintenanceStartTime","DiskIopsConfiguration":{"Mode":"","Iops":""},"CopyTagsToVolumes":"","DeploymentType":"","CopyTagsToBackups":"","DailyAutomaticBackupStartTime":"DailyAutomaticBackupStartTime","ThroughputCapacity":"","RootVolumeConfiguration":{"ReadOnly":"","DataCompressionType":"","NfsExports":"","CopyTagsToSnapshots":"","RecordSizeKiB":"","UserAndGroupQuotas":""},"AutomaticBackupRetentionDays":7},"ClientRequestToken":"","StorageType":"","KmsKeyId":"KmsKeyId","StorageCapacity":"","LustreConfiguration":{"DriveCacheType":"","AutoImportPolicy":"","ImportedFileChunkSize":"","DeploymentType":"","LogConfiguration":{"Destination":"","Level":""},"DataCompressionType":"","WeeklyMaintenanceStartTime":"","ImportPath":"","RootSquashConfiguration":{"RootSquash":"","NoSquashNids":""},"DailyAutomaticBackupStartTime":"DailyAutomaticBackupStartTime","CopyTagsToBackups":"","ExportPath":"","PerUnitStorageThroughput":"","AutomaticBackupRetentionDays":""},"BackupId":"BackupId","SubnetIds":"","SecurityGroupIds":"","Tags":"","WindowsConfiguration":{"SelfManagedActiveDirectoryConfiguration":{"FileSystemAdministratorsGroup":"","UserName":"","DomainName":"","OrganizationalUnitDistinguishedName":"","DnsIps":"","Password":""},"AuditLogConfiguration":{"FileAccessAuditLogLevel":"","FileShareAccessAuditLogLevel":"","AuditLogDestination":""},"WeeklyMaintenanceStartTime":"","ActiveDirectoryId":"","DeploymentType":"","Aliases":"","ThroughputCapacity":"","DailyAutomaticBackupStartTime":"","CopyTagsToBackups":"","AutomaticBackupRetentionDays":"","PreferredSubnetId":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.CreateFileSystemFromBackup',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_snapshot(client):
    """Test case for create_snapshot

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","VolumeId":"","Tags":[{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""}],"Name":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.CreateSnapshot',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_storage_virtual_machine(client):
    """Test case for create_storage_virtual_machine

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","SvmAdminPassword":"","ActiveDirectoryConfiguration":{"SelfManagedActiveDirectoryConfiguration":{"FileSystemAdministratorsGroup":"","UserName":"","DomainName":"","OrganizationalUnitDistinguishedName":"","DnsIps":"","Password":""},"NetBiosName":""},"RootVolumeSecurityStyle":"","FileSystemId":"FileSystemId","Tags":[{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""}],"Name":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.CreateStorageVirtualMachine',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_volume(client):
    """Test case for create_volume

    
    """
    body = {"OpenZFSConfiguration":{"ReadOnly":"","DataCompressionType":"","NfsExports":"","StorageCapacityQuotaGiB":"","CopyTagsToSnapshots":"","ParentVolumeId":"","StorageCapacityReservationGiB":"","RecordSizeKiB":"","OriginSnapshot":{"CopyStrategy":"","SnapshotARN":"SnapshotARN"},"UserAndGroupQuotas":""},"ClientRequestToken":"ClientRequestToken","VolumeType":"","OntapConfiguration":{"JunctionPath":"","StorageVirtualMachineId":"","TieringPolicy":{"CoolingPeriod":"","Name":""},"SnapshotPolicy":"","StorageEfficiencyEnabled":"","SizeInMegabytes":"","SecurityStyle":"","CopyTagsToBackups":"","SnaplockConfiguration":{"AuditLogVolume":"","VolumeAppendModeEnabled":"","AutocommitPeriod":{"Type":"","Value":""},"RetentionPeriod":{"DefaultRetention":{"Type":"","Value":""},"MaximumRetention":{"Type":"","Value":""},"MinimumRetention":{"Type":"","Value":""}},"PrivilegedDelete":"","SnaplockType":""},"OntapVolumeType":""},"Tags":[{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""}],"Name":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.CreateVolume',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_volume_from_backup(client):
    """Test case for create_volume_from_backup

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","BackupId":"BackupId","OntapConfiguration":{"JunctionPath":"","StorageVirtualMachineId":"","TieringPolicy":{"CoolingPeriod":"","Name":""},"SnapshotPolicy":"","StorageEfficiencyEnabled":"","SizeInMegabytes":"","SecurityStyle":"","CopyTagsToBackups":"","SnaplockConfiguration":{"AuditLogVolume":"","VolumeAppendModeEnabled":"","AutocommitPeriod":{"Type":"","Value":""},"RetentionPeriod":{"DefaultRetention":{"Type":"","Value":""},"MaximumRetention":{"Type":"","Value":""},"MinimumRetention":{"Type":"","Value":""}},"PrivilegedDelete":"","SnaplockType":""},"OntapVolumeType":""},"Tags":[{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""}],"Name":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.CreateVolumeFromBackup',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_backup(client):
    """Test case for delete_backup

    
    """
    body = {"ClientRequestToken":"","BackupId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DeleteBackup',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_data_repository_association(client):
    """Test case for delete_data_repository_association

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","DeleteDataInFileSystem":"","AssociationId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DeleteDataRepositoryAssociation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_file_cache(client):
    """Test case for delete_file_cache

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","FileCacheId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DeleteFileCache',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_file_system(client):
    """Test case for delete_file_system

    
    """
    body = {"OpenZFSConfiguration":{"Options":"","FinalBackupTags":"","SkipFinalBackup":""},"ClientRequestToken":"","LustreConfiguration":{"FinalBackupTags":"","SkipFinalBackup":""},"FileSystemId":"","WindowsConfiguration":{"FinalBackupTags":"","SkipFinalBackup":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DeleteFileSystem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_snapshot(client):
    """Test case for delete_snapshot

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","SnapshotId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DeleteSnapshot',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_storage_virtual_machine(client):
    """Test case for delete_storage_virtual_machine

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","StorageVirtualMachineId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DeleteStorageVirtualMachine',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_volume(client):
    """Test case for delete_volume

    
    """
    body = {"OpenZFSConfiguration":{"Options":""},"ClientRequestToken":"ClientRequestToken","VolumeId":"","OntapConfiguration":{"FinalBackupTags":[{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""},{"Value":"","Key":""}],"BypassSnaplockEnterpriseRetention":"","SkipFinalBackup":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DeleteVolume',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_backups(client):
    """Test case for describe_backups

    
    """
    body = {"Filters":"","NextToken":"","MaxResults":"","BackupIds":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DescribeBackups',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_data_repository_associations(client):
    """Test case for describe_data_repository_associations

    
    """
    body = {"Filters":[{"Values":"","Name":""},{"Values":"","Name":""},{"Values":"","Name":""},{"Values":"","Name":""},{"Values":"","Name":""}],"NextToken":"NextToken","MaxResults":"","AssociationIds":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DescribeDataRepositoryAssociations',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_data_repository_tasks(client):
    """Test case for describe_data_repository_tasks

    
    """
    body = {"Filters":"","TaskIds":"","NextToken":"NextToken","MaxResults":171976545}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DescribeDataRepositoryTasks',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_file_caches(client):
    """Test case for describe_file_caches

    
    """
    body = {"NextToken":"NextToken","MaxResults":171976545,"FileCacheIds":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DescribeFileCaches',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_file_system_aliases(client):
    """Test case for describe_file_system_aliases

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","NextToken":"","MaxResults":"","FileSystemId":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DescribeFileSystemAliases',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_file_systems(client):
    """Test case for describe_file_systems

    
    """
    body = {"NextToken":"","MaxResults":"","FileSystemIds":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DescribeFileSystems',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_snapshots(client):
    """Test case for describe_snapshots

    
    """
    body = {"Filters":"","NextToken":"NextToken","MaxResults":171976545,"SnapshotIds":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DescribeSnapshots',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_storage_virtual_machines(client):
    """Test case for describe_storage_virtual_machines

    
    """
    body = {"StorageVirtualMachineIds":"","Filters":"","NextToken":"NextToken","MaxResults":171976545}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DescribeStorageVirtualMachines',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_volumes(client):
    """Test case for describe_volumes

    
    """
    body = {"Filters":"","NextToken":"NextToken","MaxResults":171976545,"VolumeIds":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DescribeVolumes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disassociate_file_system_aliases(client):
    """Test case for disassociate_file_system_aliases

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","FileSystemId":"","Aliases":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.DisassociateFileSystemAliases',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    body = {"ResourceARN":"","NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.ListTagsForResource',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_release_file_system_nfs_v3_locks(client):
    """Test case for release_file_system_nfs_v3_locks

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","FileSystemId":"FileSystemId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.ReleaseFileSystemNfsV3Locks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restore_volume_from_snapshot(client):
    """Test case for restore_volume_from_snapshot

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","SnapshotId":"","Options":"","VolumeId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.RestoreVolumeFromSnapshot',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"ResourceARN":"","Tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.TagResource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    body = {"ResourceARN":"","TagKeys":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.UntagResource',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_data_repository_association(client):
    """Test case for update_data_repository_association

    
    """
    body = {"S3":{"AutoImportPolicy":{"Events":""},"AutoExportPolicy":{"Events":""}},"ClientRequestToken":"ClientRequestToken","ImportedFileChunkSize":"","AssociationId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.UpdateDataRepositoryAssociation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_file_cache(client):
    """Test case for update_file_cache

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","FileCacheId":"","LustreConfiguration":{"WeeklyMaintenanceStartTime":"WeeklyMaintenanceStartTime"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.UpdateFileCache',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_file_system(client):
    """Test case for update_file_system

    
    """
    body = {"OpenZFSConfiguration":{"WeeklyMaintenanceStartTime":"WeeklyMaintenanceStartTime","DiskIopsConfiguration":{"Mode":"","Iops":""},"CopyTagsToVolumes":"","CopyTagsToBackups":"","DailyAutomaticBackupStartTime":"DailyAutomaticBackupStartTime","ThroughputCapacity":"","AutomaticBackupRetentionDays":54},"ClientRequestToken":"","StorageCapacity":"","LustreConfiguration":{"DataCompressionType":"","WeeklyMaintenanceStartTime":"","AutoImportPolicy":"","RootSquashConfiguration":{"RootSquash":"","NoSquashNids":""},"DailyAutomaticBackupStartTime":"DailyAutomaticBackupStartTime","LogConfiguration":{"Destination":"","Level":""},"AutomaticBackupRetentionDays":""},"FileSystemId":"","OntapConfiguration":{"FsxAdminPassword":"","RemoveRouteTableIds":"","WeeklyMaintenanceStartTime":"WeeklyMaintenanceStartTime","DiskIopsConfiguration":{"Mode":"","Iops":""},"AddRouteTableIds":"","DailyAutomaticBackupStartTime":"DailyAutomaticBackupStartTime","ThroughputCapacity":"","AutomaticBackupRetentionDays":7},"WindowsConfiguration":{"SelfManagedActiveDirectoryConfiguration":{"FileSystemAdministratorsGroup":"","UserName":"","DomainName":"","OrganizationalUnitDistinguishedName":"","DnsIps":"","Password":""},"AuditLogConfiguration":{"FileAccessAuditLogLevel":"","FileShareAccessAuditLogLevel":"","AuditLogDestination":""},"WeeklyMaintenanceStartTime":"","DailyAutomaticBackupStartTime":"","ThroughputCapacity":"","AutomaticBackupRetentionDays":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.UpdateFileSystem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_snapshot(client):
    """Test case for update_snapshot

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","SnapshotId":"","Name":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.UpdateSnapshot',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_storage_virtual_machine(client):
    """Test case for update_storage_virtual_machine

    
    """
    body = {"ClientRequestToken":"ClientRequestToken","SvmAdminPassword":"","StorageVirtualMachineId":"","ActiveDirectoryConfiguration":{"SelfManagedActiveDirectoryConfiguration":{"FileSystemAdministratorsGroup":"","UserName":"","DomainName":"","OrganizationalUnitDistinguishedName":"","DnsIps":"","Password":""},"NetBiosName":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.UpdateStorageVirtualMachine',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_volume(client):
    """Test case for update_volume

    
    """
    body = {"OpenZFSConfiguration":{"ReadOnly":"","DataCompressionType":"","NfsExports":"","StorageCapacityQuotaGiB":"","StorageCapacityReservationGiB":"","RecordSizeKiB":"","UserAndGroupQuotas":""},"ClientRequestToken":"ClientRequestToken","VolumeId":"","OntapConfiguration":{"JunctionPath":"","TieringPolicy":{"CoolingPeriod":"","Name":""},"SnapshotPolicy":"","StorageEfficiencyEnabled":"","SizeInMegabytes":"","SecurityStyle":"","CopyTagsToBackups":"","SnaplockConfiguration":{"AuditLogVolume":"","VolumeAppendModeEnabled":"","AutocommitPeriod":{"Type":"","Value":""},"RetentionPeriod":{"DefaultRetention":{"Type":"","Value":""},"MaximumRetention":{"Type":"","Value":""},"MinimumRetention":{"Type":"","Value":""}},"PrivilegedDelete":""}},"Name":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSSimbaAPIService_v20180301.UpdateVolume',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

