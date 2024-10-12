from typing import List, Dict
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
from openapi_server import util


async def associate_file_system_aliases(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_file_system_aliases

    &lt;p&gt;Use this action to associate one or more Domain Name Server (DNS) aliases with an existing Amazon FSx for Windows File Server file system. A file system can have a maximum of 50 DNS aliases associated with it at any one time. If you try to associate a DNS alias that is already associated with the file system, FSx takes no action on that alias in the request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html\&quot;&gt;Working with DNS Aliases&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/WindowsGuide/walkthrough05-file-system-custom-CNAME.html\&quot;&gt;Walkthrough 5: Using DNS aliases to access your file system&lt;/a&gt;, including additional steps you must take to be able to access your file system using a DNS alias.&lt;/p&gt; &lt;p&gt;The system response shows the DNS aliases that Amazon FSx is attempting to associate with the file system. Use the API operation to monitor the status of the aliases Amazon FSx is associating with the file system.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = AssociateFileSystemAliasesRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_data_repository_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_data_repository_task

    &lt;p&gt;Cancels an existing Amazon FSx for Lustre data repository task if that task is in either the &lt;code&gt;PENDING&lt;/code&gt; or &lt;code&gt;EXECUTING&lt;/code&gt; state. When you cancel a task, Amazon FSx does the following.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Any files that FSx has already exported are not reverted.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;FSx continues to export any files that are \&quot;in-flight\&quot; when the cancel operation is received.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;FSx does not export any files that have not yet been exported.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CancelDataRepositoryTaskRequest.from_dict(body)
    return web.Response(status=200)


async def copy_backup(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """copy_backup

    &lt;p&gt;Copies an existing backup within the same Amazon Web Services account to another Amazon Web Services Region (cross-Region copy) or within the same Amazon Web Services Region (in-Region copy). You can have up to five backup copy requests in progress to a single destination Region per account.&lt;/p&gt; &lt;p&gt;You can use cross-Region backup copies for cross-Region disaster recovery. You can periodically take backups and copy them to another Region so that in the event of a disaster in the primary Region, you can restore from backup and recover availability quickly in the other Region. You can make cross-Region copies only within your Amazon Web Services partition. A partition is a grouping of Regions. Amazon Web Services currently has three partitions: &lt;code&gt;aws&lt;/code&gt; (Standard Regions), &lt;code&gt;aws-cn&lt;/code&gt; (China Regions), and &lt;code&gt;aws-us-gov&lt;/code&gt; (Amazon Web Services GovCloud [US] Regions).&lt;/p&gt; &lt;p&gt;You can also use backup copies to clone your file dataset to another Region or within the same Region.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;SourceRegion&lt;/code&gt; parameter to specify the Amazon Web Services Region from which the backup will be copied. For example, if you make the call from the &lt;code&gt;us-west-1&lt;/code&gt; Region and want to copy a backup from the &lt;code&gt;us-east-2&lt;/code&gt; Region, you specify &lt;code&gt;us-east-2&lt;/code&gt; in the &lt;code&gt;SourceRegion&lt;/code&gt; parameter to make a cross-Region copy. If you don&#39;t specify a Region, the backup copy is created in the same Region where the request is sent from (in-Region copy).&lt;/p&gt; &lt;p&gt;For more information about creating backup copies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html#copy-backups\&quot;&gt; Copying backups&lt;/a&gt; in the &lt;i&gt;Amazon FSx for Windows User Guide&lt;/i&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-backups-fsx.html#copy-backups\&quot;&gt;Copying backups&lt;/a&gt; in the &lt;i&gt;Amazon FSx for Lustre User Guide&lt;/i&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/using-backups.html#copy-backups\&quot;&gt;Copying backups&lt;/a&gt; in the &lt;i&gt;Amazon FSx for OpenZFS User Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CopyBackupRequest.from_dict(body)
    return web.Response(status=200)


async def create_backup(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_backup

    &lt;p&gt;Creates a backup of an existing Amazon FSx for Windows File Server file system, Amazon FSx for Lustre file system, Amazon FSx for NetApp ONTAP volume, or Amazon FSx for OpenZFS file system. We recommend creating regular backups so that you can restore a file system or volume from a backup if an issue arises with the original file system or volume.&lt;/p&gt; &lt;p&gt;For Amazon FSx for Lustre file systems, you can create a backup only for file systems that have the following configuration:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A Persistent deployment type&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Are &lt;i&gt;not&lt;/i&gt; linked to a data repository&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about backups, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For Amazon FSx for Lustre, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-backups-fsx.html\&quot;&gt;Working with FSx for Lustre backups&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For Amazon FSx for Windows, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html\&quot;&gt;Working with FSx for Windows backups&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For Amazon FSx for NetApp ONTAP, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/using-backups.html\&quot;&gt;Working with FSx for NetApp ONTAP backups&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For Amazon FSx for OpenZFS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/using-backups.html\&quot;&gt;Working with FSx for OpenZFS backups&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If a backup with the specified client request token exists and the parameters match, this operation returns the description of the existing backup. If a backup with the specified client request token exists and the parameters don&#39;t match, this operation returns &lt;code&gt;IncompatibleParameterError&lt;/code&gt;. If a backup with the specified client request token doesn&#39;t exist, &lt;code&gt;CreateBackup&lt;/code&gt; does the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Creates a new Amazon FSx backup with an assigned ID, and an initial lifecycle state of &lt;code&gt;CREATING&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Returns the description of the backup.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;By using the idempotent operation, you can retry a &lt;code&gt;CreateBackup&lt;/code&gt; operation without the risk of creating an extra backup. This approach can be useful when an initial call fails in a way that makes it unclear whether a backup was created. If you use the same client request token and the initial call created a backup, the operation returns a successful result because all the parameters are the same.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;CreateBackup&lt;/code&gt; operation returns while the backup&#39;s lifecycle state is still &lt;code&gt;CREATING&lt;/code&gt;. You can check the backup creation status by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeBackups.html\&quot;&gt;DescribeBackups&lt;/a&gt; operation, which returns the backup state along with other information.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateBackupRequest.from_dict(body)
    return web.Response(status=200)


async def create_data_repository_association(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_data_repository_association

    &lt;p&gt;Creates an Amazon FSx for Lustre data repository association (DRA). A data repository association is a link between a directory on the file system and an Amazon S3 bucket or prefix. You can have a maximum of 8 data repository associations on a file system. Data repository associations are supported on all FSx for Lustre 2.12 and newer file systems, excluding &lt;code&gt;scratch_1&lt;/code&gt; deployment type.&lt;/p&gt; &lt;p&gt;Each data repository association must have a unique Amazon FSx file system directory and a unique S3 bucket or prefix associated with it. You can configure a data repository association for automatic import only, for automatic export only, or for both. To learn more about linking a data repository to your file system, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-dra-linked-data-repo.html\&quot;&gt;Linking your file system to an S3 bucket&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;CreateDataRepositoryAssociation&lt;/code&gt; isn&#39;t supported on Amazon File Cache resources. To create a DRA on Amazon File Cache, use the &lt;code&gt;CreateFileCache&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateDataRepositoryAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def create_data_repository_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_data_repository_task

    Creates an Amazon FSx for Lustre data repository task. You use data repository tasks to perform bulk operations between your Amazon FSx file system and its linked data repositories. An example of a data repository task is exporting any data and metadata changes, including POSIX metadata, to files, directories, and symbolic links (symlinks) from your FSx file system to a linked data repository. A &lt;code&gt;CreateDataRepositoryTask&lt;/code&gt; operation will fail if a data repository is not linked to the FSx file system. To learn more about data repository tasks, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-repository-tasks.html\&quot;&gt;Data Repository Tasks&lt;/a&gt;. To learn more about linking a data repository to your file system, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-dra-linked-data-repo.html\&quot;&gt;Linking your file system to an S3 bucket&lt;/a&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateDataRepositoryTaskRequest.from_dict(body)
    return web.Response(status=200)


async def create_file_cache(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_file_cache

    &lt;p&gt;Creates a new Amazon File Cache resource.&lt;/p&gt; &lt;p&gt;You can use this operation with a client request token in the request that Amazon File Cache uses to ensure idempotent creation. If a cache with the specified client request token exists and the parameters match, &lt;code&gt;CreateFileCache&lt;/code&gt; returns the description of the existing cache. If a cache with the specified client request token exists and the parameters don&#39;t match, this call returns &lt;code&gt;IncompatibleParameterError&lt;/code&gt;. If a file cache with the specified client request token doesn&#39;t exist, &lt;code&gt;CreateFileCache&lt;/code&gt; does the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Creates a new, empty Amazon File Cache resourcewith an assigned ID, and an initial lifecycle state of &lt;code&gt;CREATING&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Returns the description of the cache in JSON format.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;CreateFileCache&lt;/code&gt; call returns while the cache&#39;s lifecycle state is still &lt;code&gt;CREATING&lt;/code&gt;. You can check the cache creation status by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileCaches.html\&quot;&gt;DescribeFileCaches&lt;/a&gt; operation, which returns the cache state along with other information.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateFileCacheRequest.from_dict(body)
    return web.Response(status=200)


async def create_file_system(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_file_system

    &lt;p&gt;Creates a new, empty Amazon FSx file system. You can create the following supported Amazon FSx file systems using the &lt;code&gt;CreateFileSystem&lt;/code&gt; API operation:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Amazon FSx for Lustre&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon FSx for NetApp ONTAP&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon FSx for OpenZFS&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon FSx for Windows File Server&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation requires a client request token in the request that Amazon FSx uses to ensure idempotent creation. This means that calling the operation multiple times with the same client request token has no effect. By using the idempotent operation, you can retry a &lt;code&gt;CreateFileSystem&lt;/code&gt; operation without the risk of creating an extra file system. This approach can be useful when an initial call fails in a way that makes it unclear whether a file system was created. Examples are if a transport level timeout occurred, or your connection was reset. If you use the same client request token and the initial call created a file system, the client receives success as long as the parameters are the same.&lt;/p&gt; &lt;p&gt;If a file system with the specified client request token exists and the parameters match, &lt;code&gt;CreateFileSystem&lt;/code&gt; returns the description of the existing file system. If a file system with the specified client request token exists and the parameters don&#39;t match, this call returns &lt;code&gt;IncompatibleParameterError&lt;/code&gt;. If a file system with the specified client request token doesn&#39;t exist, &lt;code&gt;CreateFileSystem&lt;/code&gt; does the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Creates a new, empty Amazon FSx file system with an assigned ID, and an initial lifecycle state of &lt;code&gt;CREATING&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Returns the description of the file system in JSON format.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;CreateFileSystem&lt;/code&gt; call returns while the file system&#39;s lifecycle state is still &lt;code&gt;CREATING&lt;/code&gt;. You can check the file-system creation status by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html\&quot;&gt;DescribeFileSystems&lt;/a&gt; operation, which returns the file system state along with other information.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateFileSystemRequest.from_dict(body)
    return web.Response(status=200)


async def create_file_system_from_backup(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_file_system_from_backup

    &lt;p&gt;Creates a new Amazon FSx for Lustre, Amazon FSx for Windows File Server, or Amazon FSx for OpenZFS file system from an existing Amazon FSx backup.&lt;/p&gt; &lt;p&gt;If a file system with the specified client request token exists and the parameters match, this operation returns the description of the file system. If a file system with the specified client request token exists but the parameters don&#39;t match, this call returns &lt;code&gt;IncompatibleParameterError&lt;/code&gt;. If a file system with the specified client request token doesn&#39;t exist, this operation does the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Creates a new Amazon FSx file system from backup with an assigned ID, and an initial lifecycle state of &lt;code&gt;CREATING&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Returns the description of the file system.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Parameters like the Active Directory, default share name, automatic backup, and backup settings default to the parameters of the file system that was backed up, unless overridden. You can explicitly supply other settings.&lt;/p&gt; &lt;p&gt;By using the idempotent operation, you can retry a &lt;code&gt;CreateFileSystemFromBackup&lt;/code&gt; call without the risk of creating an extra file system. This approach can be useful when an initial call fails in a way that makes it unclear whether a file system was created. Examples are if a transport level timeout occurred, or your connection was reset. If you use the same client request token and the initial call created a file system, the client receives a success message as long as the parameters are the same.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;CreateFileSystemFromBackup&lt;/code&gt; call returns while the file system&#39;s lifecycle state is still &lt;code&gt;CREATING&lt;/code&gt;. You can check the file-system creation status by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html\&quot;&gt; DescribeFileSystems&lt;/a&gt; operation, which returns the file system state along with other information.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateFileSystemFromBackupRequest.from_dict(body)
    return web.Response(status=200)


async def create_snapshot(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_snapshot

    &lt;p&gt;Creates a snapshot of an existing Amazon FSx for OpenZFS volume. With snapshots, you can easily undo file changes and compare file versions by restoring the volume to a previous version.&lt;/p&gt; &lt;p&gt;If a snapshot with the specified client request token exists, and the parameters match, this operation returns the description of the existing snapshot. If a snapshot with the specified client request token exists, and the parameters don&#39;t match, this operation returns &lt;code&gt;IncompatibleParameterError&lt;/code&gt;. If a snapshot with the specified client request token doesn&#39;t exist, &lt;code&gt;CreateSnapshot&lt;/code&gt; does the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Creates a new OpenZFS snapshot with an assigned ID, and an initial lifecycle state of &lt;code&gt;CREATING&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Returns the description of the snapshot.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;By using the idempotent operation, you can retry a &lt;code&gt;CreateSnapshot&lt;/code&gt; operation without the risk of creating an extra snapshot. This approach can be useful when an initial call fails in a way that makes it unclear whether a snapshot was created. If you use the same client request token and the initial call created a snapshot, the operation returns a successful result because all the parameters are the same.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;CreateSnapshot&lt;/code&gt; operation returns while the snapshot&#39;s lifecycle state is still &lt;code&gt;CREATING&lt;/code&gt;. You can check the snapshot creation status by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeSnapshots.html\&quot;&gt;DescribeSnapshots&lt;/a&gt; operation, which returns the snapshot state along with other information.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def create_storage_virtual_machine(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_storage_virtual_machine

    Creates a storage virtual machine (SVM) for an Amazon FSx for ONTAP file system.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateStorageVirtualMachineRequest.from_dict(body)
    return web.Response(status=200)


async def create_volume(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_volume

    Creates an FSx for ONTAP or Amazon FSx for OpenZFS storage volume.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateVolumeRequest.from_dict(body)
    return web.Response(status=200)


async def create_volume_from_backup(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_volume_from_backup

    Creates a new Amazon FSx for NetApp ONTAP volume from an existing Amazon FSx volume backup.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = CreateVolumeFromBackupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_backup(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_backup

    &lt;p&gt;Deletes an Amazon FSx backup. After deletion, the backup no longer exists, and its data is gone.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;DeleteBackup&lt;/code&gt; call returns instantly. The backup won&#39;t show up in later &lt;code&gt;DescribeBackups&lt;/code&gt; calls.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The data in a deleted backup is also deleted and can&#39;t be recovered by any means.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteBackupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_data_repository_association(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_data_repository_association

    Deletes a data repository association on an Amazon FSx for Lustre file system. Deleting the data repository association unlinks the file system from the Amazon S3 bucket. When deleting a data repository association, you have the option of deleting the data in the file system that corresponds to the data repository association. Data repository associations are supported on all FSx for Lustre 2.12 and newer file systems, excluding &lt;code&gt;scratch_1&lt;/code&gt; deployment type.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteDataRepositoryAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_file_cache(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_file_cache

    &lt;p&gt;Deletes an Amazon File Cache resource. After deletion, the cache no longer exists, and its data is gone.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;DeleteFileCache&lt;/code&gt; operation returns while the cache has the &lt;code&gt;DELETING&lt;/code&gt; status. You can check the cache deletion status by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileCaches.html\&quot;&gt;DescribeFileCaches&lt;/a&gt; operation, which returns a list of caches in your account. If you pass the cache ID for a deleted cache, the &lt;code&gt;DescribeFileCaches&lt;/code&gt; operation returns a &lt;code&gt;FileCacheNotFound&lt;/code&gt; error.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The data in a deleted cache is also deleted and can&#39;t be recovered by any means.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteFileCacheRequest.from_dict(body)
    return web.Response(status=200)


async def delete_file_system(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_file_system

    &lt;p&gt;Deletes a file system. After deletion, the file system no longer exists, and its data is gone. Any existing automatic backups and snapshots are also deleted.&lt;/p&gt; &lt;p&gt;To delete an Amazon FSx for NetApp ONTAP file system, first delete all the volumes and storage virtual machines (SVMs) on the file system. Then provide a &lt;code&gt;FileSystemId&lt;/code&gt; value to the &lt;code&gt;DeleFileSystem&lt;/code&gt; operation.&lt;/p&gt; &lt;p&gt;By default, when you delete an Amazon FSx for Windows File Server file system, a final backup is created upon deletion. This final backup isn&#39;t subject to the file system&#39;s retention policy, and must be manually deleted.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;DeleteFileSystem&lt;/code&gt; operation returns while the file system has the &lt;code&gt;DELETING&lt;/code&gt; status. You can check the file system deletion status by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystems.html\&quot;&gt;DescribeFileSystems&lt;/a&gt; operation, which returns a list of file systems in your account. If you pass the file system ID for a deleted file system, the &lt;code&gt;DescribeFileSystems&lt;/code&gt; operation returns a &lt;code&gt;FileSystemNotFound&lt;/code&gt; error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If a data repository task is in a &lt;code&gt;PENDING&lt;/code&gt; or &lt;code&gt;EXECUTING&lt;/code&gt; state, deleting an Amazon FSx for Lustre file system will fail with an HTTP status code 400 (Bad Request).&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;The data in a deleted file system is also deleted and can&#39;t be recovered by any means.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteFileSystemRequest.from_dict(body)
    return web.Response(status=200)


async def delete_snapshot(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_snapshot

    &lt;p&gt;Deletes an Amazon FSx for OpenZFS snapshot. After deletion, the snapshot no longer exists, and its data is gone. Deleting a snapshot doesn&#39;t affect snapshots stored in a file system backup. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;DeleteSnapshot&lt;/code&gt; operation returns instantly. The snapshot appears with the lifecycle status of &lt;code&gt;DELETING&lt;/code&gt; until the deletion is complete.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def delete_storage_virtual_machine(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_storage_virtual_machine

    Deletes an existing Amazon FSx for ONTAP storage virtual machine (SVM). Prior to deleting an SVM, you must delete all non-root volumes in the SVM, otherwise the operation will fail.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteStorageVirtualMachineRequest.from_dict(body)
    return web.Response(status=200)


async def delete_volume(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_volume

    Deletes an Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS volume.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DeleteVolumeRequest.from_dict(body)
    return web.Response(status=200)


async def describe_backups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_backups

    &lt;p&gt;Returns the description of a specific Amazon FSx backup, if a &lt;code&gt;BackupIds&lt;/code&gt; value is provided for that backup. Otherwise, it returns all backups owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that you&#39;re calling.&lt;/p&gt; &lt;p&gt;When retrieving all backups, you can optionally specify the &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of backups in a response. If more backups remain, Amazon FSx returns a &lt;code&gt;NextToken&lt;/code&gt; value in the response. In this case, send a later request with the &lt;code&gt;NextToken&lt;/code&gt; request parameter set to the value of the &lt;code&gt;NextToken&lt;/code&gt; value from the last response.&lt;/p&gt; &lt;p&gt;This operation is used in an iterative process to retrieve a list of your backups. &lt;code&gt;DescribeBackups&lt;/code&gt; is called first without a &lt;code&gt;NextToken&lt;/code&gt; value. Then the operation continues to be called with the &lt;code&gt;NextToken&lt;/code&gt; parameter set to the value of the last &lt;code&gt;NextToken&lt;/code&gt; value until a response has no &lt;code&gt;NextToken&lt;/code&gt; value.&lt;/p&gt; &lt;p&gt;When using this operation, keep the following in mind:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The operation might return fewer than the &lt;code&gt;MaxResults&lt;/code&gt; value of backup descriptions while still including a &lt;code&gt;NextToken&lt;/code&gt; value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The order of the backups returned in the response of one &lt;code&gt;DescribeBackups&lt;/code&gt; call and the order of the backups returned across the responses of a multi-call iteration is unspecified.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeBackupsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_data_repository_associations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_data_repository_associations

    &lt;p&gt;Returns the description of specific Amazon FSx for Lustre or Amazon File Cache data repository associations, if one or more &lt;code&gt;AssociationIds&lt;/code&gt; values are provided in the request, or if filters are used in the request. Data repository associations are supported on Amazon File Cache resources and all FSx for Lustre 2.12 and newer file systems, excluding &lt;code&gt;scratch_1&lt;/code&gt; deployment type.&lt;/p&gt; &lt;p&gt;You can use filters to narrow the response to include just data repository associations for specific file systems (use the &lt;code&gt;file-system-id&lt;/code&gt; filter with the ID of the file system) or caches (use the &lt;code&gt;file-cache-id&lt;/code&gt; filter with the ID of the cache), or data repository associations for a specific repository type (use the &lt;code&gt;data-repository-type&lt;/code&gt; filter with a value of &lt;code&gt;S3&lt;/code&gt; or &lt;code&gt;NFS&lt;/code&gt;). If you don&#39;t use filters, the response returns all data repository associations owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that you&#39;re calling.&lt;/p&gt; &lt;p&gt;When retrieving all data repository associations, you can paginate the response by using the optional &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of data repository associations returned in a response. If more data repository associations remain, a &lt;code&gt;NextToken&lt;/code&gt; value is returned in the response. In this case, send a later request with the &lt;code&gt;NextToken&lt;/code&gt; request parameter set to the value of &lt;code&gt;NextToken&lt;/code&gt; from the last response.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeDataRepositoryAssociationsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_data_repository_tasks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_data_repository_tasks

    &lt;p&gt;Returns the description of specific Amazon FSx for Lustre or Amazon File Cache data repository tasks, if one or more &lt;code&gt;TaskIds&lt;/code&gt; values are provided in the request, or if filters are used in the request. You can use filters to narrow the response to include just tasks for specific file systems or caches, or tasks in a specific lifecycle state. Otherwise, it returns all data repository tasks owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that you&#39;re calling.&lt;/p&gt; &lt;p&gt;When retrieving all tasks, you can paginate the response by using the optional &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of tasks returned in a response. If more tasks remain, a &lt;code&gt;NextToken&lt;/code&gt; value is returned in the response. In this case, send a later request with the &lt;code&gt;NextToken&lt;/code&gt; request parameter set to the value of &lt;code&gt;NextToken&lt;/code&gt; from the last response.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeDataRepositoryTasksRequest.from_dict(body)
    return web.Response(status=200)


async def describe_file_caches(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_file_caches

    &lt;p&gt;Returns the description of a specific Amazon File Cache resource, if a &lt;code&gt;FileCacheIds&lt;/code&gt; value is provided for that cache. Otherwise, it returns descriptions of all caches owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that you&#39;re calling.&lt;/p&gt; &lt;p&gt;When retrieving all cache descriptions, you can optionally specify the &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of descriptions in a response. If more cache descriptions remain, the operation returns a &lt;code&gt;NextToken&lt;/code&gt; value in the response. In this case, send a later request with the &lt;code&gt;NextToken&lt;/code&gt; request parameter set to the value of &lt;code&gt;NextToken&lt;/code&gt; from the last response.&lt;/p&gt; &lt;p&gt;This operation is used in an iterative process to retrieve a list of your cache descriptions. &lt;code&gt;DescribeFileCaches&lt;/code&gt; is called first without a &lt;code&gt;NextToken&lt;/code&gt;value. Then the operation continues to be called with the &lt;code&gt;NextToken&lt;/code&gt; parameter set to the value of the last &lt;code&gt;NextToken&lt;/code&gt; value until a response has no &lt;code&gt;NextToken&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;When using this operation, keep the following in mind:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The implementation might return fewer than &lt;code&gt;MaxResults&lt;/code&gt; cache descriptions while still including a &lt;code&gt;NextToken&lt;/code&gt; value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The order of caches returned in the response of one &lt;code&gt;DescribeFileCaches&lt;/code&gt; call and the order of caches returned across the responses of a multicall iteration is unspecified.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeFileCachesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_file_system_aliases(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_file_system_aliases

    Returns the DNS aliases that are associated with the specified Amazon FSx for Windows File Server file system. A history of all DNS aliases that have been associated with and disassociated from the file system is available in the list of &lt;a&gt;AdministrativeAction&lt;/a&gt; provided in the &lt;a&gt;DescribeFileSystems&lt;/a&gt; operation response.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeFileSystemAliasesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_file_systems(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_file_systems

    &lt;p&gt;Returns the description of specific Amazon FSx file systems, if a &lt;code&gt;FileSystemIds&lt;/code&gt; value is provided for that file system. Otherwise, it returns descriptions of all file systems owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that you&#39;re calling.&lt;/p&gt; &lt;p&gt;When retrieving all file system descriptions, you can optionally specify the &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of descriptions in a response. If more file system descriptions remain, Amazon FSx returns a &lt;code&gt;NextToken&lt;/code&gt; value in the response. In this case, send a later request with the &lt;code&gt;NextToken&lt;/code&gt; request parameter set to the value of &lt;code&gt;NextToken&lt;/code&gt; from the last response.&lt;/p&gt; &lt;p&gt;This operation is used in an iterative process to retrieve a list of your file system descriptions. &lt;code&gt;DescribeFileSystems&lt;/code&gt; is called first without a &lt;code&gt;NextToken&lt;/code&gt;value. Then the operation continues to be called with the &lt;code&gt;NextToken&lt;/code&gt; parameter set to the value of the last &lt;code&gt;NextToken&lt;/code&gt; value until a response has no &lt;code&gt;NextToken&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;When using this operation, keep the following in mind:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The implementation might return fewer than &lt;code&gt;MaxResults&lt;/code&gt; file system descriptions while still including a &lt;code&gt;NextToken&lt;/code&gt; value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The order of file systems returned in the response of one &lt;code&gt;DescribeFileSystems&lt;/code&gt; call and the order of file systems returned across the responses of a multicall iteration is unspecified.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeFileSystemsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_snapshots(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_snapshots

    &lt;p&gt;Returns the description of specific Amazon FSx for OpenZFS snapshots, if a &lt;code&gt;SnapshotIds&lt;/code&gt; value is provided. Otherwise, this operation returns all snapshots owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that you&#39;re calling.&lt;/p&gt; &lt;p&gt;When retrieving all snapshots, you can optionally specify the &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of snapshots in a response. If more backups remain, Amazon FSx returns a &lt;code&gt;NextToken&lt;/code&gt; value in the response. In this case, send a later request with the &lt;code&gt;NextToken&lt;/code&gt; request parameter set to the value of &lt;code&gt;NextToken&lt;/code&gt; from the last response. &lt;/p&gt; &lt;p&gt;Use this operation in an iterative process to retrieve a list of your snapshots. &lt;code&gt;DescribeSnapshots&lt;/code&gt; is called first without a &lt;code&gt;NextToken&lt;/code&gt; value. Then the operation continues to be called with the &lt;code&gt;NextToken&lt;/code&gt; parameter set to the value of the last &lt;code&gt;NextToken&lt;/code&gt; value until a response has no &lt;code&gt;NextToken&lt;/code&gt; value.&lt;/p&gt; &lt;p&gt;When using this operation, keep the following in mind:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The operation might return fewer than the &lt;code&gt;MaxResults&lt;/code&gt; value of snapshot descriptions while still including a &lt;code&gt;NextToken&lt;/code&gt; value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The order of snapshots returned in the response of one &lt;code&gt;DescribeSnapshots&lt;/code&gt; call and the order of backups returned across the responses of a multi-call iteration is unspecified. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeSnapshotsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_storage_virtual_machines(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_storage_virtual_machines

    Describes one or more Amazon FSx for NetApp ONTAP storage virtual machines (SVMs).

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeStorageVirtualMachinesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_volumes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_volumes

    Describes one or more Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS volumes.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DescribeVolumesRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_file_system_aliases(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_file_system_aliases

    &lt;p&gt;Use this action to disassociate, or remove, one or more Domain Name Service (DNS) aliases from an Amazon FSx for Windows File Server file system. If you attempt to disassociate a DNS alias that is not associated with the file system, Amazon FSx responds with a 400 Bad Request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html\&quot;&gt;Working with DNS Aliases&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The system generated response showing the DNS aliases that Amazon FSx is attempting to disassociate from the file system. Use the API operation to monitor the status of the aliases Amazon FSx is disassociating with the file system.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = DisassociateFileSystemAliasesRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Lists tags for Amazon FSx resources.&lt;/p&gt; &lt;p&gt;When retrieving all tags, you can optionally specify the &lt;code&gt;MaxResults&lt;/code&gt; parameter to limit the number of tags in a response. If more tags remain, Amazon FSx returns a &lt;code&gt;NextToken&lt;/code&gt; value in the response. In this case, send a later request with the &lt;code&gt;NextToken&lt;/code&gt; request parameter set to the value of &lt;code&gt;NextToken&lt;/code&gt; from the last response.&lt;/p&gt; &lt;p&gt;This action is used in an iterative process to retrieve a list of your tags. &lt;code&gt;ListTagsForResource&lt;/code&gt; is called first without a &lt;code&gt;NextToken&lt;/code&gt;value. Then the action continues to be called with the &lt;code&gt;NextToken&lt;/code&gt; parameter set to the value of the last &lt;code&gt;NextToken&lt;/code&gt; value until a response has no &lt;code&gt;NextToken&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;When using this action, keep the following in mind:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The implementation might return fewer than &lt;code&gt;MaxResults&lt;/code&gt; file system descriptions while still including a &lt;code&gt;NextToken&lt;/code&gt; value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The order of tags returned in the response of one &lt;code&gt;ListTagsForResource&lt;/code&gt; call and the order of tags returned across the responses of a multi-call iteration is unspecified.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def release_file_system_nfs_v3_locks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """release_file_system_nfs_v3_locks

    Releases the file system lock from an Amazon FSx for OpenZFS file system.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = ReleaseFileSystemNfsV3LocksRequest.from_dict(body)
    return web.Response(status=200)


async def restore_volume_from_snapshot(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """restore_volume_from_snapshot

    Returns an Amazon FSx for OpenZFS volume to the state saved by the specified snapshot.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = RestoreVolumeFromSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Tags an Amazon FSx resource.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    This action removes a tag from an Amazon FSx resource.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_data_repository_association(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_data_repository_association

    Updates the configuration of an existing data repository association on an Amazon FSx for Lustre file system. Data repository associations are supported on all FSx for Lustre 2.12 and newer file systems, excluding &lt;code&gt;scratch_1&lt;/code&gt; deployment type.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateDataRepositoryAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def update_file_cache(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_file_cache

    Updates the configuration of an existing Amazon File Cache resource. You can update multiple properties in a single request.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateFileCacheRequest.from_dict(body)
    return web.Response(status=200)


async def update_file_system(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_file_system

    &lt;p&gt;Use this operation to update the configuration of an existing Amazon FSx file system. You can update multiple properties in a single request.&lt;/p&gt; &lt;p&gt;For FSx for Windows File Server file systems, you can update the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AuditLogConfiguration&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AutomaticBackupRetentionDays&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DailyAutomaticBackupStartTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SelfManagedActiveDirectoryConfiguration&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;StorageCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ThroughputCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WeeklyMaintenanceStartTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For FSx for Lustre file systems, you can update the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AutoImportPolicy&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AutomaticBackupRetentionDays&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DailyAutomaticBackupStartTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DataCompressionType&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LogConfiguration&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LustreRootSquashConfiguration&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;StorageCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WeeklyMaintenanceStartTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For FSx for ONTAP file systems, you can update the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AddRouteTableIds&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AutomaticBackupRetentionDays&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DailyAutomaticBackupStartTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DiskIopsConfiguration&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FsxAdminPassword&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RemoveRouteTableIds&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;StorageCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ThroughputCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WeeklyMaintenanceStartTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For FSx for OpenZFS file systems, you can update the following properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AutomaticBackupRetentionDays&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CopyTagsToBackups&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CopyTagsToVolumes&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DailyAutomaticBackupStartTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DiskIopsConfiguration&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;StorageCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ThroughputCapacity&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WeeklyMaintenanceStartTime&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateFileSystemRequest.from_dict(body)
    return web.Response(status=200)


async def update_snapshot(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_snapshot

    Updates the name of an Amazon FSx for OpenZFS snapshot.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def update_storage_virtual_machine(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_storage_virtual_machine

    Updates an FSx for ONTAP storage virtual machine (SVM).

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateStorageVirtualMachineRequest.from_dict(body)
    return web.Response(status=200)


async def update_volume(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_volume

    Updates the configuration of an Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS volume.

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = UpdateVolumeRequest.from_dict(body)
    return web.Response(status=200)
