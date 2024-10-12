from typing import List, Dict
from aiohttp import web

from openapi_server.models.activate_gateway_input import ActivateGatewayInput
from openapi_server.models.activate_gateway_output import ActivateGatewayOutput
from openapi_server.models.add_cache_input import AddCacheInput
from openapi_server.models.add_cache_output import AddCacheOutput
from openapi_server.models.add_tags_to_resource_input import AddTagsToResourceInput
from openapi_server.models.add_tags_to_resource_output import AddTagsToResourceOutput
from openapi_server.models.add_upload_buffer_input import AddUploadBufferInput
from openapi_server.models.add_upload_buffer_output import AddUploadBufferOutput
from openapi_server.models.add_working_storage_input import AddWorkingStorageInput
from openapi_server.models.add_working_storage_output import AddWorkingStorageOutput
from openapi_server.models.assign_tape_pool_input import AssignTapePoolInput
from openapi_server.models.assign_tape_pool_output import AssignTapePoolOutput
from openapi_server.models.associate_file_system_input import AssociateFileSystemInput
from openapi_server.models.associate_file_system_output import AssociateFileSystemOutput
from openapi_server.models.attach_volume_input import AttachVolumeInput
from openapi_server.models.attach_volume_output import AttachVolumeOutput
from openapi_server.models.cancel_archival_input import CancelArchivalInput
from openapi_server.models.cancel_archival_output import CancelArchivalOutput
from openapi_server.models.cancel_retrieval_input import CancelRetrievalInput
from openapi_server.models.cancel_retrieval_output import CancelRetrievalOutput
from openapi_server.models.create_cachedi_scsi_volume_input import CreateCachediSCSIVolumeInput
from openapi_server.models.create_cachedi_scsi_volume_output import CreateCachediSCSIVolumeOutput
from openapi_server.models.create_nfs_file_share_input import CreateNFSFileShareInput
from openapi_server.models.create_nfs_file_share_output import CreateNFSFileShareOutput
from openapi_server.models.create_smb_file_share_input import CreateSMBFileShareInput
from openapi_server.models.create_smb_file_share_output import CreateSMBFileShareOutput
from openapi_server.models.create_snapshot_from_volume_recovery_point_input import CreateSnapshotFromVolumeRecoveryPointInput
from openapi_server.models.create_snapshot_from_volume_recovery_point_output import CreateSnapshotFromVolumeRecoveryPointOutput
from openapi_server.models.create_snapshot_input import CreateSnapshotInput
from openapi_server.models.create_snapshot_output import CreateSnapshotOutput
from openapi_server.models.create_storedi_scsi_volume_input import CreateStorediSCSIVolumeInput
from openapi_server.models.create_storedi_scsi_volume_output import CreateStorediSCSIVolumeOutput
from openapi_server.models.create_tape_pool_input import CreateTapePoolInput
from openapi_server.models.create_tape_pool_output import CreateTapePoolOutput
from openapi_server.models.create_tape_with_barcode_input import CreateTapeWithBarcodeInput
from openapi_server.models.create_tape_with_barcode_output import CreateTapeWithBarcodeOutput
from openapi_server.models.create_tapes_input import CreateTapesInput
from openapi_server.models.create_tapes_output import CreateTapesOutput
from openapi_server.models.delete_automatic_tape_creation_policy_input import DeleteAutomaticTapeCreationPolicyInput
from openapi_server.models.delete_automatic_tape_creation_policy_output import DeleteAutomaticTapeCreationPolicyOutput
from openapi_server.models.delete_bandwidth_rate_limit_input import DeleteBandwidthRateLimitInput
from openapi_server.models.delete_bandwidth_rate_limit_output import DeleteBandwidthRateLimitOutput
from openapi_server.models.delete_chap_credentials_input import DeleteChapCredentialsInput
from openapi_server.models.delete_chap_credentials_output import DeleteChapCredentialsOutput
from openapi_server.models.delete_file_share_input import DeleteFileShareInput
from openapi_server.models.delete_file_share_output import DeleteFileShareOutput
from openapi_server.models.delete_gateway_input import DeleteGatewayInput
from openapi_server.models.delete_gateway_output import DeleteGatewayOutput
from openapi_server.models.delete_snapshot_schedule_input import DeleteSnapshotScheduleInput
from openapi_server.models.delete_snapshot_schedule_output import DeleteSnapshotScheduleOutput
from openapi_server.models.delete_tape_archive_input import DeleteTapeArchiveInput
from openapi_server.models.delete_tape_archive_output import DeleteTapeArchiveOutput
from openapi_server.models.delete_tape_input import DeleteTapeInput
from openapi_server.models.delete_tape_output import DeleteTapeOutput
from openapi_server.models.delete_tape_pool_input import DeleteTapePoolInput
from openapi_server.models.delete_tape_pool_output import DeleteTapePoolOutput
from openapi_server.models.delete_volume_input import DeleteVolumeInput
from openapi_server.models.delete_volume_output import DeleteVolumeOutput
from openapi_server.models.describe_availability_monitor_test_input import DescribeAvailabilityMonitorTestInput
from openapi_server.models.describe_availability_monitor_test_output import DescribeAvailabilityMonitorTestOutput
from openapi_server.models.describe_bandwidth_rate_limit_input import DescribeBandwidthRateLimitInput
from openapi_server.models.describe_bandwidth_rate_limit_output import DescribeBandwidthRateLimitOutput
from openapi_server.models.describe_bandwidth_rate_limit_schedule_input import DescribeBandwidthRateLimitScheduleInput
from openapi_server.models.describe_bandwidth_rate_limit_schedule_output import DescribeBandwidthRateLimitScheduleOutput
from openapi_server.models.describe_cache_input import DescribeCacheInput
from openapi_server.models.describe_cache_output import DescribeCacheOutput
from openapi_server.models.describe_cachedi_scsi_volumes_input import DescribeCachediSCSIVolumesInput
from openapi_server.models.describe_cachedi_scsi_volumes_output import DescribeCachediSCSIVolumesOutput
from openapi_server.models.describe_chap_credentials_input import DescribeChapCredentialsInput
from openapi_server.models.describe_chap_credentials_output import DescribeChapCredentialsOutput
from openapi_server.models.describe_file_system_associations_input import DescribeFileSystemAssociationsInput
from openapi_server.models.describe_file_system_associations_output import DescribeFileSystemAssociationsOutput
from openapi_server.models.describe_gateway_information_input import DescribeGatewayInformationInput
from openapi_server.models.describe_gateway_information_output import DescribeGatewayInformationOutput
from openapi_server.models.describe_maintenance_start_time_input import DescribeMaintenanceStartTimeInput
from openapi_server.models.describe_maintenance_start_time_output import DescribeMaintenanceStartTimeOutput
from openapi_server.models.describe_nfs_file_shares_input import DescribeNFSFileSharesInput
from openapi_server.models.describe_nfs_file_shares_output import DescribeNFSFileSharesOutput
from openapi_server.models.describe_smb_file_shares_input import DescribeSMBFileSharesInput
from openapi_server.models.describe_smb_file_shares_output import DescribeSMBFileSharesOutput
from openapi_server.models.describe_smb_settings_input import DescribeSMBSettingsInput
from openapi_server.models.describe_smb_settings_output import DescribeSMBSettingsOutput
from openapi_server.models.describe_snapshot_schedule_input import DescribeSnapshotScheduleInput
from openapi_server.models.describe_snapshot_schedule_output import DescribeSnapshotScheduleOutput
from openapi_server.models.describe_storedi_scsi_volumes_input import DescribeStorediSCSIVolumesInput
from openapi_server.models.describe_storedi_scsi_volumes_output import DescribeStorediSCSIVolumesOutput
from openapi_server.models.describe_tape_archives_input import DescribeTapeArchivesInput
from openapi_server.models.describe_tape_archives_output import DescribeTapeArchivesOutput
from openapi_server.models.describe_tape_recovery_points_input import DescribeTapeRecoveryPointsInput
from openapi_server.models.describe_tape_recovery_points_output import DescribeTapeRecoveryPointsOutput
from openapi_server.models.describe_tapes_input import DescribeTapesInput
from openapi_server.models.describe_tapes_output import DescribeTapesOutput
from openapi_server.models.describe_upload_buffer_input import DescribeUploadBufferInput
from openapi_server.models.describe_upload_buffer_output import DescribeUploadBufferOutput
from openapi_server.models.describe_vtl_devices_input import DescribeVTLDevicesInput
from openapi_server.models.describe_vtl_devices_output import DescribeVTLDevicesOutput
from openapi_server.models.describe_working_storage_input import DescribeWorkingStorageInput
from openapi_server.models.describe_working_storage_output import DescribeWorkingStorageOutput
from openapi_server.models.detach_volume_input import DetachVolumeInput
from openapi_server.models.detach_volume_output import DetachVolumeOutput
from openapi_server.models.disable_gateway_input import DisableGatewayInput
from openapi_server.models.disable_gateway_output import DisableGatewayOutput
from openapi_server.models.disassociate_file_system_input import DisassociateFileSystemInput
from openapi_server.models.disassociate_file_system_output import DisassociateFileSystemOutput
from openapi_server.models.join_domain_input import JoinDomainInput
from openapi_server.models.join_domain_output import JoinDomainOutput
from openapi_server.models.list_automatic_tape_creation_policies_input import ListAutomaticTapeCreationPoliciesInput
from openapi_server.models.list_automatic_tape_creation_policies_output import ListAutomaticTapeCreationPoliciesOutput
from openapi_server.models.list_file_shares_input import ListFileSharesInput
from openapi_server.models.list_file_shares_output import ListFileSharesOutput
from openapi_server.models.list_file_system_associations_input import ListFileSystemAssociationsInput
from openapi_server.models.list_file_system_associations_output import ListFileSystemAssociationsOutput
from openapi_server.models.list_gateways_input import ListGatewaysInput
from openapi_server.models.list_gateways_output import ListGatewaysOutput
from openapi_server.models.list_local_disks_input import ListLocalDisksInput
from openapi_server.models.list_local_disks_output import ListLocalDisksOutput
from openapi_server.models.list_tags_for_resource_input import ListTagsForResourceInput
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.list_tape_pools_input import ListTapePoolsInput
from openapi_server.models.list_tape_pools_output import ListTapePoolsOutput
from openapi_server.models.list_tapes_input import ListTapesInput
from openapi_server.models.list_tapes_output import ListTapesOutput
from openapi_server.models.list_volume_initiators_input import ListVolumeInitiatorsInput
from openapi_server.models.list_volume_initiators_output import ListVolumeInitiatorsOutput
from openapi_server.models.list_volume_recovery_points_input import ListVolumeRecoveryPointsInput
from openapi_server.models.list_volume_recovery_points_output import ListVolumeRecoveryPointsOutput
from openapi_server.models.list_volumes_input import ListVolumesInput
from openapi_server.models.list_volumes_output import ListVolumesOutput
from openapi_server.models.notify_when_uploaded_input import NotifyWhenUploadedInput
from openapi_server.models.notify_when_uploaded_output import NotifyWhenUploadedOutput
from openapi_server.models.refresh_cache_input import RefreshCacheInput
from openapi_server.models.refresh_cache_output import RefreshCacheOutput
from openapi_server.models.remove_tags_from_resource_input import RemoveTagsFromResourceInput
from openapi_server.models.remove_tags_from_resource_output import RemoveTagsFromResourceOutput
from openapi_server.models.reset_cache_input import ResetCacheInput
from openapi_server.models.reset_cache_output import ResetCacheOutput
from openapi_server.models.retrieve_tape_archive_input import RetrieveTapeArchiveInput
from openapi_server.models.retrieve_tape_archive_output import RetrieveTapeArchiveOutput
from openapi_server.models.retrieve_tape_recovery_point_input import RetrieveTapeRecoveryPointInput
from openapi_server.models.retrieve_tape_recovery_point_output import RetrieveTapeRecoveryPointOutput
from openapi_server.models.set_local_console_password_input import SetLocalConsolePasswordInput
from openapi_server.models.set_local_console_password_output import SetLocalConsolePasswordOutput
from openapi_server.models.set_smb_guest_password_input import SetSMBGuestPasswordInput
from openapi_server.models.set_smb_guest_password_output import SetSMBGuestPasswordOutput
from openapi_server.models.shutdown_gateway_input import ShutdownGatewayInput
from openapi_server.models.shutdown_gateway_output import ShutdownGatewayOutput
from openapi_server.models.start_availability_monitor_test_input import StartAvailabilityMonitorTestInput
from openapi_server.models.start_availability_monitor_test_output import StartAvailabilityMonitorTestOutput
from openapi_server.models.start_gateway_input import StartGatewayInput
from openapi_server.models.start_gateway_output import StartGatewayOutput
from openapi_server.models.update_automatic_tape_creation_policy_input import UpdateAutomaticTapeCreationPolicyInput
from openapi_server.models.update_automatic_tape_creation_policy_output import UpdateAutomaticTapeCreationPolicyOutput
from openapi_server.models.update_bandwidth_rate_limit_input import UpdateBandwidthRateLimitInput
from openapi_server.models.update_bandwidth_rate_limit_output import UpdateBandwidthRateLimitOutput
from openapi_server.models.update_bandwidth_rate_limit_schedule_input import UpdateBandwidthRateLimitScheduleInput
from openapi_server.models.update_bandwidth_rate_limit_schedule_output import UpdateBandwidthRateLimitScheduleOutput
from openapi_server.models.update_chap_credentials_input import UpdateChapCredentialsInput
from openapi_server.models.update_chap_credentials_output import UpdateChapCredentialsOutput
from openapi_server.models.update_file_system_association_input import UpdateFileSystemAssociationInput
from openapi_server.models.update_file_system_association_output import UpdateFileSystemAssociationOutput
from openapi_server.models.update_gateway_information_input import UpdateGatewayInformationInput
from openapi_server.models.update_gateway_information_output import UpdateGatewayInformationOutput
from openapi_server.models.update_gateway_software_now_input import UpdateGatewaySoftwareNowInput
from openapi_server.models.update_gateway_software_now_output import UpdateGatewaySoftwareNowOutput
from openapi_server.models.update_maintenance_start_time_input import UpdateMaintenanceStartTimeInput
from openapi_server.models.update_maintenance_start_time_output import UpdateMaintenanceStartTimeOutput
from openapi_server.models.update_nfs_file_share_input import UpdateNFSFileShareInput
from openapi_server.models.update_nfs_file_share_output import UpdateNFSFileShareOutput
from openapi_server.models.update_smb_file_share_input import UpdateSMBFileShareInput
from openapi_server.models.update_smb_file_share_output import UpdateSMBFileShareOutput
from openapi_server.models.update_smb_file_share_visibility_input import UpdateSMBFileShareVisibilityInput
from openapi_server.models.update_smb_file_share_visibility_output import UpdateSMBFileShareVisibilityOutput
from openapi_server.models.update_smb_local_groups_input import UpdateSMBLocalGroupsInput
from openapi_server.models.update_smb_local_groups_output import UpdateSMBLocalGroupsOutput
from openapi_server.models.update_smb_security_strategy_input import UpdateSMBSecurityStrategyInput
from openapi_server.models.update_smb_security_strategy_output import UpdateSMBSecurityStrategyOutput
from openapi_server.models.update_snapshot_schedule_input import UpdateSnapshotScheduleInput
from openapi_server.models.update_snapshot_schedule_output import UpdateSnapshotScheduleOutput
from openapi_server.models.update_vtl_device_type_input import UpdateVTLDeviceTypeInput
from openapi_server.models.update_vtl_device_type_output import UpdateVTLDeviceTypeOutput
from openapi_server import util


async def activate_gateway(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """activate_gateway

    &lt;p&gt;Activates the gateway you previously deployed on your host. In the activation process, you specify information such as the Amazon Web Services Region that you want to use for storing snapshots or tapes, the time zone for scheduled snapshots the gateway snapshot schedule window, an activation key, and a name for your gateway. The activation process also associates your gateway with your account. For more information, see &lt;a&gt;UpdateGatewayInformation&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You must turn on the gateway VM before you can activate your gateway.&lt;/p&gt; &lt;/note&gt;

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
    body = ActivateGatewayInput.from_dict(body)
    return web.Response(status=200)


async def add_cache(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_cache

    &lt;p&gt;Configures one or more gateway local disks as cache for a gateway. This operation is only supported in the cached volume, tape, and file gateway type (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html\&quot;&gt;How Storage Gateway works (architecture)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add cache, and one or more disk IDs that you want to configure as cache.&lt;/p&gt;

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
    body = AddCacheInput.from_dict(body)
    return web.Response(status=200)


async def add_tags_to_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_tags_to_resource

    &lt;p&gt;Adds one or more tags to the specified resource. You use tags to add metadata to resources, which you can use to categorize these resources. For example, you can categorize resources by purpose, owner, environment, or team. Each tag consists of a key and a value, which you define. You can add tags to the following Storage Gateway resources:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Storage gateways of all types&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Storage volumes&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Virtual tapes&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;NFS and SMB file shares&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;File System associations&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can create a maximum of 50 tags for each resource. Virtual tapes and storage volumes that are recovered to a new gateway maintain their tags.&lt;/p&gt;

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
    body = AddTagsToResourceInput.from_dict(body)
    return web.Response(status=200)


async def add_upload_buffer(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_upload_buffer

    &lt;p&gt;Configures one or more gateway local disks as upload buffer for a specified gateway. This operation is supported for the stored volume, cached volume, and tape gateway types.&lt;/p&gt; &lt;p&gt;In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add upload buffer, and one or more disk IDs that you want to configure as upload buffer.&lt;/p&gt;

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
    body = AddUploadBufferInput.from_dict(body)
    return web.Response(status=200)


async def add_working_storage(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_working_storage

    &lt;p&gt;Configures one or more gateway local disks as working storage for a gateway. This operation is only supported in the stored volume gateway type. This operation is deprecated in cached volume API version 20120630. Use &lt;a&gt;AddUploadBuffer&lt;/a&gt; instead.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Working storage is also referred to as upload buffer. You can also use the &lt;a&gt;AddUploadBuffer&lt;/a&gt; operation to add upload buffer to a stored volume gateway.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add working storage, and one or more disk IDs that you want to configure as working storage.&lt;/p&gt;

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
    body = AddWorkingStorageInput.from_dict(body)
    return web.Response(status=200)


async def assign_tape_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """assign_tape_pool

    Assigns a tape to a tape pool for archiving. The tape assigned to a pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the S3 storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.

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
    body = AssignTapePoolInput.from_dict(body)
    return web.Response(status=200)


async def associate_file_system(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_file_system

    Associate an Amazon FSx file system with the FSx File Gateway. After the association process is complete, the file shares on the Amazon FSx file system are available for access through the gateway. This operation only supports the FSx File Gateway type.

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
    body = AssociateFileSystemInput.from_dict(body)
    return web.Response(status=200)


async def attach_volume(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """attach_volume

    Connects a volume to an iSCSI connection and then attaches the volume to the specified gateway. Detaching and attaching a volume enables you to recover your data from one gateway to a different gateway without creating a snapshot. It also makes it easier to move your volumes from an on-premises gateway to a gateway hosted on an Amazon EC2 instance.

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
    body = AttachVolumeInput.from_dict(body)
    return web.Response(status=200)


async def cancel_archival(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_archival

    Cancels archiving of a virtual tape to the virtual tape shelf (VTS) after the archiving process is initiated. This operation is only supported in the tape gateway type.

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
    body = CancelArchivalInput.from_dict(body)
    return web.Response(status=200)


async def cancel_retrieval(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_retrieval

    Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a gateway after the retrieval process is initiated. The virtual tape is returned to the VTS. This operation is only supported in the tape gateway type.

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
    body = CancelRetrievalInput.from_dict(body)
    return web.Response(status=200)


async def create_cachedi_scsi_volume(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cachedi_scsi_volume

    &lt;p&gt;Creates a cached volume on a specified cached volume gateway. This operation is only supported in the cached volume gateway type.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Cache storage must be allocated to the gateway before you can create a cached volume. Use the &lt;a&gt;AddCache&lt;/a&gt; operation to add cache storage to a gateway.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;In the request, you must specify the gateway, size of the volume in bytes, the iSCSI target name, an IP address on which to expose the target, and a unique client token. In response, the gateway creates the volume and returns information about it. This information includes the volume Amazon Resource Name (ARN), its size, and the iSCSI target ARN that initiators can use to connect to the volume target.&lt;/p&gt; &lt;p&gt;Optionally, you can provide the ARN for an existing volume as the &lt;code&gt;SourceVolumeARN&lt;/code&gt; for this cached volume, which creates an exact copy of the existing volume’s latest recovery point. The &lt;code&gt;VolumeSizeInBytes&lt;/code&gt; value must be equal to or larger than the size of the copied volume, in bytes.&lt;/p&gt;

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
    body = CreateCachediSCSIVolumeInput.from_dict(body)
    return web.Response(status=200)


async def create_nfs_file_share(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_nfs_file_share

    &lt;p&gt;Creates a Network File System (NFS) file share on an existing S3 File Gateway. In Storage Gateway, a file share is a file system mount point backed by Amazon S3 cloud storage. Storage Gateway exposes file shares using an NFS interface. This operation is only supported for S3 File Gateways.&lt;/p&gt; &lt;important&gt; &lt;p&gt;S3 File gateway requires Security Token Service (Amazon Web Services STS) to be activated to enable you to create a file share. Make sure Amazon Web Services STS is activated in the Amazon Web Services Region you are creating your S3 File Gateway in. If Amazon Web Services STS is not activated in the Amazon Web Services Region, activate it. For information about how to activate Amazon Web Services STS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html\&quot;&gt;Activating and deactivating Amazon Web Services STS in an Amazon Web Services Region&lt;/a&gt; in the &lt;i&gt;Identity and Access Management User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;S3 File Gateways do not support creating hard or symbolic links on a file share.&lt;/p&gt; &lt;/important&gt;

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
    body = CreateNFSFileShareInput.from_dict(body)
    return web.Response(status=200)


async def create_smb_file_share(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_smb_file_share

    &lt;p&gt;Creates a Server Message Block (SMB) file share on an existing S3 File Gateway. In Storage Gateway, a file share is a file system mount point backed by Amazon S3 cloud storage. Storage Gateway exposes file shares using an SMB interface. This operation is only supported for S3 File Gateways.&lt;/p&gt; &lt;important&gt; &lt;p&gt;S3 File Gateways require Security Token Service (Amazon Web Services STS) to be activated to enable you to create a file share. Make sure that Amazon Web Services STS is activated in the Amazon Web Services Region you are creating your S3 File Gateway in. If Amazon Web Services STS is not activated in this Amazon Web Services Region, activate it. For information about how to activate Amazon Web Services STS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html\&quot;&gt;Activating and deactivating Amazon Web Services STS in an Amazon Web Services Region&lt;/a&gt; in the &lt;i&gt;Identity and Access Management User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;File gateways don&#39;t support creating hard or symbolic links on a file share.&lt;/p&gt; &lt;/important&gt;

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
    body = CreateSMBFileShareInput.from_dict(body)
    return web.Response(status=200)


async def create_snapshot(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_snapshot

    &lt;p&gt;Initiates a snapshot of a volume.&lt;/p&gt; &lt;p&gt;Storage Gateway provides the ability to back up point-in-time snapshots of your data to Amazon Simple Storage (Amazon S3) for durable off-site recovery, and also import the data to an Amazon Elastic Block Store (EBS) volume in Amazon Elastic Compute Cloud (EC2). You can take snapshots of your gateway volume on a scheduled or ad hoc basis. This API enables you to take an ad hoc snapshot. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#SchedulingSnapshot\&quot;&gt;Editing a snapshot schedule&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;In the &lt;code&gt;CreateSnapshot&lt;/code&gt; request, you identify the volume by providing its Amazon Resource Name (ARN). You must also provide description for the snapshot. When Storage Gateway takes the snapshot of specified volume, the snapshot and description appears in the Storage Gateway console. In response, Storage Gateway returns you a snapshot ID. You can use this snapshot ID to check the snapshot progress or later use it when you want to create a volume from a snapshot. This operation is only supported in stored and cached volume gateway type.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To list or delete a snapshot, you must use the Amazon EC2 API. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html\&quot;&gt;DescribeSnapshots&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSnapshot.html\&quot;&gt;DeleteSnapshot&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud API Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;Volume and snapshot IDs are changing to a longer length ID format. For more information, see the important note on the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/APIReference/Welcome.html\&quot;&gt;Welcome&lt;/a&gt; page.&lt;/p&gt; &lt;/important&gt;

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
    body = CreateSnapshotInput.from_dict(body)
    return web.Response(status=200)


async def create_snapshot_from_volume_recovery_point(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_snapshot_from_volume_recovery_point

    &lt;p&gt;Initiates a snapshot of a gateway from a volume recovery point. This operation is only supported in the cached volume gateway type.&lt;/p&gt; &lt;p&gt;A volume recovery point is a point in time at which all data of the volume is consistent and from which you can create a snapshot. To get a list of volume recovery point for cached volume gateway, use &lt;a&gt;ListVolumeRecoveryPoints&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;In the &lt;code&gt;CreateSnapshotFromVolumeRecoveryPoint&lt;/code&gt; request, you identify the volume by providing its Amazon Resource Name (ARN). You must also provide a description for the snapshot. When the gateway takes a snapshot of the specified volume, the snapshot and its description appear in the Storage Gateway console. In response, the gateway returns you a snapshot ID. You can use this snapshot ID to check the snapshot progress or later use it when you want to create a volume from a snapshot.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To list or delete a snapshot, you must use the Amazon EC2 API. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html\&quot;&gt;DescribeSnapshots&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSnapshot.html\&quot;&gt;DeleteSnapshot&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud API Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateSnapshotFromVolumeRecoveryPointInput.from_dict(body)
    return web.Response(status=200)


async def create_storedi_scsi_volume(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_storedi_scsi_volume

    &lt;p&gt;Creates a volume on a specified gateway. This operation is only supported in the stored volume gateway type.&lt;/p&gt; &lt;p&gt;The size of the volume to create is inferred from the disk size. You can choose to preserve existing data on the disk, create volume from an existing snapshot, or create an empty volume. If you choose to create an empty gateway volume, then any existing data on the disk is erased.&lt;/p&gt; &lt;p&gt;In the request, you must specify the gateway and the disk information on which you are creating the volume. In response, the gateway creates the volume and returns volume information such as the volume Amazon Resource Name (ARN), its size, and the iSCSI target ARN that initiators can use to connect to the volume target.&lt;/p&gt;

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
    body = CreateStorediSCSIVolumeInput.from_dict(body)
    return web.Response(status=200)


async def create_tape_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_tape_pool

    Creates a new custom tape pool. You can use custom tape pool to enable tape retention lock on tapes that are archived in the custom pool.

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
    body = CreateTapePoolInput.from_dict(body)
    return web.Response(status=200)


async def create_tape_with_barcode(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_tape_with_barcode

    &lt;p&gt;Creates a virtual tape by using your own barcode. You write data to the virtual tape and then archive the tape. A barcode is unique and cannot be reused if it has already been used on a tape. This applies to barcodes used on deleted tapes. This operation is only supported in the tape gateway type.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Cache storage must be allocated to the gateway before you can create a virtual tape. Use the &lt;a&gt;AddCache&lt;/a&gt; operation to add cache storage to a gateway.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateTapeWithBarcodeInput.from_dict(body)
    return web.Response(status=200)


async def create_tapes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_tapes

    &lt;p&gt;Creates one or more virtual tapes. You write data to the virtual tapes and then archive the tapes. This operation is only supported in the tape gateway type.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Cache storage must be allocated to the gateway before you can create virtual tapes. Use the &lt;a&gt;AddCache&lt;/a&gt; operation to add cache storage to a gateway.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateTapesInput.from_dict(body)
    return web.Response(status=200)


async def delete_automatic_tape_creation_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_automatic_tape_creation_policy

    Deletes the automatic tape creation policy of a gateway. If you delete this policy, new virtual tapes must be created manually. Use the Amazon Resource Name (ARN) of the gateway in your request to remove the policy.

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
    body = DeleteAutomaticTapeCreationPolicyInput.from_dict(body)
    return web.Response(status=200)


async def delete_bandwidth_rate_limit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_bandwidth_rate_limit

    Deletes the bandwidth rate limits of a gateway. You can delete either the upload and download bandwidth rate limit, or you can delete both. If you delete only one of the limits, the other limit remains unchanged. To specify which gateway to work with, use the Amazon Resource Name (ARN) of the gateway in your request. This operation is supported only for the stored volume, cached volume, and tape gateway types.

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
    body = DeleteBandwidthRateLimitInput.from_dict(body)
    return web.Response(status=200)


async def delete_chap_credentials(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_chap_credentials

    Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target and initiator pair. This operation is supported in volume and tape gateway types.

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
    body = DeleteChapCredentialsInput.from_dict(body)
    return web.Response(status=200)


async def delete_file_share(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_file_share

    Deletes a file share from an S3 File Gateway. This operation is only supported for S3 File Gateways.

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
    body = DeleteFileShareInput.from_dict(body)
    return web.Response(status=200)


async def delete_gateway(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_gateway

    &lt;p&gt;Deletes a gateway. To specify which gateway to delete, use the Amazon Resource Name (ARN) of the gateway in your request. The operation deletes the gateway; however, it does not delete the gateway virtual machine (VM) from your host computer.&lt;/p&gt; &lt;p&gt;After you delete a gateway, you cannot reactivate it. Completed snapshots of the gateway volumes are not deleted upon deleting the gateway, however, pending snapshots will not complete. After you delete a gateway, your next step is to remove it from your environment.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You no longer pay software charges after the gateway is deleted; however, your existing Amazon EBS snapshots persist and you will continue to be billed for these snapshots. You can choose to remove all remaining Amazon EBS snapshots by canceling your Amazon EC2 subscription.  If you prefer not to cancel your Amazon EC2 subscription, you can delete your snapshots using the Amazon EC2 console. For more information, see the &lt;a href&#x3D;\&quot;http://aws.amazon.com/storagegateway\&quot;&gt;Storage Gateway detail page&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;

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
    body = DeleteGatewayInput.from_dict(body)
    return web.Response(status=200)


async def delete_snapshot_schedule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_snapshot_schedule

    &lt;p&gt;Deletes a snapshot of a volume.&lt;/p&gt; &lt;p&gt;You can take snapshots of your gateway volumes on a scheduled or ad hoc basis. This API action enables you to delete a snapshot schedule for a volume. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/userguide/backing-up-volumes.html\&quot;&gt;Backing up your volumes&lt;/a&gt;. In the &lt;code&gt;DeleteSnapshotSchedule&lt;/code&gt; request, you identify the volume by providing its Amazon Resource Name (ARN). This operation is only supported for cached volume gateway types.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To list or delete a snapshot, you must use the Amazon EC2 API. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html\&quot;&gt;DescribeSnapshots&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud API Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = DeleteSnapshotScheduleInput.from_dict(body)
    return web.Response(status=200)


async def delete_tape(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_tape

    Deletes the specified virtual tape. This operation is only supported in the tape gateway type.

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
    body = DeleteTapeInput.from_dict(body)
    return web.Response(status=200)


async def delete_tape_archive(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_tape_archive

    Deletes the specified virtual tape from the virtual tape shelf (VTS). This operation is only supported in the tape gateway type.

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
    body = DeleteTapeArchiveInput.from_dict(body)
    return web.Response(status=200)


async def delete_tape_pool(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_tape_pool

    Delete a custom tape pool. A custom tape pool can only be deleted if there are no tapes in the pool and if there are no automatic tape creation policies that reference the custom tape pool.

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
    body = DeleteTapePoolInput.from_dict(body)
    return web.Response(status=200)


async def delete_volume(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_volume

    &lt;p&gt;Deletes the specified storage volume that you previously created using the &lt;a&gt;CreateCachediSCSIVolume&lt;/a&gt; or &lt;a&gt;CreateStorediSCSIVolume&lt;/a&gt; API. This operation is only supported in the cached volume and stored volume types. For stored volume gateways, the local disk that was configured as the storage volume is not deleted. You can reuse the local disk to create another storage volume.&lt;/p&gt; &lt;p&gt;Before you delete a volume, make sure there are no iSCSI connections to the volume you are deleting. You should also make sure there is no snapshot in progress. You can use the Amazon Elastic Compute Cloud (Amazon EC2) API to query snapshots on the volume you are deleting and check the snapshot status. For more information, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSnapshots.html\&quot;&gt;DescribeSnapshots&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud API Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;In the request, you must provide the Amazon Resource Name (ARN) of the storage volume you want to delete.&lt;/p&gt;

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
    body = DeleteVolumeInput.from_dict(body)
    return web.Response(status=200)


async def describe_availability_monitor_test(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_availability_monitor_test

    Returns information about the most recent high availability monitoring test that was performed on the host in a cluster. If a test isn&#39;t performed, the status and start time in the response would be null.

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
    body = DescribeAvailabilityMonitorTestInput.from_dict(body)
    return web.Response(status=200)


async def describe_bandwidth_rate_limit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_bandwidth_rate_limit

    &lt;p&gt;Returns the bandwidth rate limits of a gateway. By default, these limits are not set, which means no bandwidth rate limiting is in effect. This operation is supported only for the stored volume, cached volume, and tape gateway types. To describe bandwidth rate limits for S3 file gateways, use &lt;a&gt;DescribeBandwidthRateLimitSchedule&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation returns a value for a bandwidth rate limit only if the limit is set. If no limits are set for the gateway, then this operation returns only the gateway ARN in the response body. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.&lt;/p&gt;

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
    body = DescribeBandwidthRateLimitInput.from_dict(body)
    return web.Response(status=200)


async def describe_bandwidth_rate_limit_schedule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_bandwidth_rate_limit_schedule

    &lt;p&gt; Returns information about the bandwidth rate limit schedule of a gateway. By default, gateways do not have bandwidth rate limit schedules, which means no bandwidth rate limiting is in effect. This operation is supported only for volume, tape and S3 file gateways. FSx file gateways do not support bandwidth rate limits.&lt;/p&gt; &lt;p&gt;This operation returns information about a gateway&#39;s bandwidth rate limit schedule. A bandwidth rate limit schedule consists of one or more bandwidth rate limit intervals. A bandwidth rate limit interval defines a period of time on one or more days of the week, during which bandwidth rate limits are specified for uploading, downloading, or both. &lt;/p&gt; &lt;p&gt; A bandwidth rate limit interval consists of one or more days of the week, a start hour and minute, an ending hour and minute, and bandwidth rate limits for uploading and downloading &lt;/p&gt; &lt;p&gt; If no bandwidth rate limit schedule intervals are set for the gateway, this operation returns an empty response. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.&lt;/p&gt;

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
    body = DescribeBandwidthRateLimitScheduleInput.from_dict(body)
    return web.Response(status=200)


async def describe_cache(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_cache

    &lt;p&gt;Returns information about the cache of a gateway. This operation is only supported in the cached volume, tape, and file gateway types.&lt;/p&gt; &lt;p&gt;The response includes disk IDs that are configured as cache, and it includes the amount of cache allocated and used.&lt;/p&gt;

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
    body = DescribeCacheInput.from_dict(body)
    return web.Response(status=200)


async def describe_cachedi_scsi_volumes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_cachedi_scsi_volumes

    &lt;p&gt;Returns a description of the gateway volumes specified in the request. This operation is only supported in the cached volume gateway types.&lt;/p&gt; &lt;p&gt;The list of gateway volumes in the request must be from one gateway. In the response, Storage Gateway returns volume information sorted by volume Amazon Resource Name (ARN).&lt;/p&gt;

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
    body = DescribeCachediSCSIVolumesInput.from_dict(body)
    return web.Response(status=200)


async def describe_chap_credentials(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_chap_credentials

    Returns an array of Challenge-Handshake Authentication Protocol (CHAP) credentials information for a specified iSCSI target, one for each target-initiator pair. This operation is supported in the volume and tape gateway types.

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
    body = DescribeChapCredentialsInput.from_dict(body)
    return web.Response(status=200)


async def describe_file_system_associations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_file_system_associations

    Gets the file system association information. This operation is only supported for FSx File Gateways.

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
    body = DescribeFileSystemAssociationsInput.from_dict(body)
    return web.Response(status=200)


async def describe_gateway_information(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_gateway_information

    Returns metadata about a gateway such as its name, network interfaces, configured time zone, and the state (whether the gateway is running or not). To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.

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
    body = DescribeGatewayInformationInput.from_dict(body)
    return web.Response(status=200)


async def describe_maintenance_start_time(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_maintenance_start_time

    Returns your gateway&#39;s weekly maintenance start time including the day and time of the week. Note that values are in terms of the gateway&#39;s time zone.

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
    body = DescribeMaintenanceStartTimeInput.from_dict(body)
    return web.Response(status=200)


async def describe_nfs_file_shares(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_nfs_file_shares

    Gets a description for one or more Network File System (NFS) file shares from an S3 File Gateway. This operation is only supported for S3 File Gateways.

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
    body = DescribeNFSFileSharesInput.from_dict(body)
    return web.Response(status=200)


async def describe_smb_file_shares(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_smb_file_shares

    Gets a description for one or more Server Message Block (SMB) file shares from a S3 File Gateway. This operation is only supported for S3 File Gateways.

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
    body = DescribeSMBFileSharesInput.from_dict(body)
    return web.Response(status=200)


async def describe_smb_settings(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_smb_settings

    Gets a description of a Server Message Block (SMB) file share settings from a file gateway. This operation is only supported for file gateways.

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
    body = DescribeSMBSettingsInput.from_dict(body)
    return web.Response(status=200)


async def describe_snapshot_schedule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_snapshot_schedule

    Describes the snapshot schedule for the specified gateway volume. The snapshot schedule information includes intervals at which snapshots are automatically initiated on the volume. This operation is only supported in the cached volume and stored volume types.

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
    body = DescribeSnapshotScheduleInput.from_dict(body)
    return web.Response(status=200)


async def describe_storedi_scsi_volumes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_storedi_scsi_volumes

    Returns the description of the gateway volumes specified in the request. The list of gateway volumes in the request must be from one gateway. In the response, Storage Gateway returns volume information sorted by volume ARNs. This operation is only supported in stored volume gateway type.

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
    body = DescribeStorediSCSIVolumesInput.from_dict(body)
    return web.Response(status=200)


async def describe_tape_archives(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, marker=None) -> web.Response:
    """describe_tape_archives

    &lt;p&gt;Returns a description of specified virtual tapes in the virtual tape shelf (VTS). This operation is only supported in the tape gateway type.&lt;/p&gt; &lt;p&gt;If a specific &lt;code&gt;TapeARN&lt;/code&gt; is not specified, Storage Gateway returns a description of all virtual tapes found in the VTS associated with your account.&lt;/p&gt;

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
    :param limit: Pagination limit
    :type limit: str
    :param marker: Pagination token
    :type marker: str

    """
    body = DescribeTapeArchivesInput.from_dict(body)
    return web.Response(status=200)


async def describe_tape_recovery_points(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, marker=None) -> web.Response:
    """describe_tape_recovery_points

    &lt;p&gt;Returns a list of virtual tape recovery points that are available for the specified tape gateway.&lt;/p&gt; &lt;p&gt;A recovery point is a point-in-time view of a virtual tape at which all the data on the virtual tape is consistent. If your gateway crashes, virtual tapes that have recovery points can be recovered to a new gateway. This operation is only supported in the tape gateway type.&lt;/p&gt;

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
    :param limit: Pagination limit
    :type limit: str
    :param marker: Pagination token
    :type marker: str

    """
    body = DescribeTapeRecoveryPointsInput.from_dict(body)
    return web.Response(status=200)


async def describe_tapes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, marker=None) -> web.Response:
    """describe_tapes

    Returns a description of the specified Amazon Resource Name (ARN) of virtual tapes. If a &lt;code&gt;TapeARN&lt;/code&gt; is not specified, returns a description of all virtual tapes associated with the specified gateway. This operation is only supported in the tape gateway type.

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
    :param limit: Pagination limit
    :type limit: str
    :param marker: Pagination token
    :type marker: str

    """
    body = DescribeTapesInput.from_dict(body)
    return web.Response(status=200)


async def describe_upload_buffer(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_upload_buffer

    &lt;p&gt;Returns information about the upload buffer of a gateway. This operation is supported for the stored volume, cached volume, and tape gateway types.&lt;/p&gt; &lt;p&gt;The response includes disk IDs that are configured as upload buffer space, and it includes the amount of upload buffer space allocated and used.&lt;/p&gt;

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
    body = DescribeUploadBufferInput.from_dict(body)
    return web.Response(status=200)


async def describe_vtl_devices(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, marker=None) -> web.Response:
    """describe_vtl_devices

    &lt;p&gt;Returns a description of virtual tape library (VTL) devices for the specified tape gateway. In the response, Storage Gateway returns VTL device information.&lt;/p&gt; &lt;p&gt;This operation is only supported in the tape gateway type.&lt;/p&gt;

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
    :param limit: Pagination limit
    :type limit: str
    :param marker: Pagination token
    :type marker: str

    """
    body = DescribeVTLDevicesInput.from_dict(body)
    return web.Response(status=200)


async def describe_working_storage(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_working_storage

    &lt;p&gt;Returns information about the working storage of a gateway. This operation is only supported in the stored volumes gateway type. This operation is deprecated in cached volumes API version (20120630). Use DescribeUploadBuffer instead.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Working storage is also referred to as upload buffer. You can also use the DescribeUploadBuffer operation to add upload buffer to a stored volume gateway.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The response includes disk IDs that are configured as working storage, and it includes the amount of working storage allocated and used.&lt;/p&gt;

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
    body = DescribeWorkingStorageInput.from_dict(body)
    return web.Response(status=200)


async def detach_volume(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """detach_volume

    Disconnects a volume from an iSCSI connection and then detaches the volume from the specified gateway. Detaching and attaching a volume enables you to recover your data from one gateway to a different gateway without creating a snapshot. It also makes it easier to move your volumes from an on-premises gateway to a gateway hosted on an Amazon EC2 instance. This operation is only supported in the volume gateway type.

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
    body = DetachVolumeInput.from_dict(body)
    return web.Response(status=200)


async def disable_gateway(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disable_gateway

    &lt;p&gt;Disables a tape gateway when the gateway is no longer functioning. For example, if your gateway VM is damaged, you can disable the gateway so you can recover virtual tapes.&lt;/p&gt; &lt;p&gt;Use this operation for a tape gateway that is not reachable or not functioning. This operation is only supported in the tape gateway type.&lt;/p&gt; &lt;important&gt; &lt;p&gt;After a gateway is disabled, it cannot be enabled.&lt;/p&gt; &lt;/important&gt;

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
    body = DisableGatewayInput.from_dict(body)
    return web.Response(status=200)


async def disassociate_file_system(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_file_system

    Disassociates an Amazon FSx file system from the specified gateway. After the disassociation process finishes, the gateway can no longer access the Amazon FSx file system. This operation is only supported in the FSx File Gateway type.

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
    body = DisassociateFileSystemInput.from_dict(body)
    return web.Response(status=200)


async def join_domain(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """join_domain

    Adds a file gateway to an Active Directory domain. This operation is only supported for file gateways that support the SMB file protocol.

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
    body = JoinDomainInput.from_dict(body)
    return web.Response(status=200)


async def list_automatic_tape_creation_policies(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_automatic_tape_creation_policies

    &lt;p&gt;Lists the automatic tape creation policies for a gateway. If there are no automatic tape creation policies for the gateway, it returns an empty list.&lt;/p&gt; &lt;p&gt;This operation is only supported for tape gateways.&lt;/p&gt;

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
    body = ListAutomaticTapeCreationPoliciesInput.from_dict(body)
    return web.Response(status=200)


async def list_file_shares(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, marker=None) -> web.Response:
    """list_file_shares

    Gets a list of the file shares for a specific S3 File Gateway, or the list of file shares that belong to the calling user account. This operation is only supported for S3 File Gateways.

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
    :param limit: Pagination limit
    :type limit: str
    :param marker: Pagination token
    :type marker: str

    """
    body = ListFileSharesInput.from_dict(body)
    return web.Response(status=200)


async def list_file_system_associations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, marker=None) -> web.Response:
    """list_file_system_associations

    Gets a list of &lt;code&gt;FileSystemAssociationSummary&lt;/code&gt; objects. Each object contains a summary of a file system association. This operation is only supported for FSx File Gateways.

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
    :param limit: Pagination limit
    :type limit: str
    :param marker: Pagination token
    :type marker: str

    """
    body = ListFileSystemAssociationsInput.from_dict(body)
    return web.Response(status=200)


async def list_gateways(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, marker=None) -> web.Response:
    """list_gateways

    &lt;p&gt;Lists gateways owned by an Amazon Web Services account in an Amazon Web Services Region specified in the request. The returned list is ordered by gateway Amazon Resource Name (ARN).&lt;/p&gt; &lt;p&gt;By default, the operation returns a maximum of 100 gateways. This operation supports pagination that allows you to optionally reduce the number of gateways returned in a response.&lt;/p&gt; &lt;p&gt;If you have more gateways than are returned in a response (that is, the response returns only a truncated list of your gateways), the response contains a marker that you can specify in your next request to fetch the next page of gateways.&lt;/p&gt;

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
    :param limit: Pagination limit
    :type limit: str
    :param marker: Pagination token
    :type marker: str

    """
    body = ListGatewaysInput.from_dict(body)
    return web.Response(status=200)


async def list_local_disks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_local_disks

    &lt;p&gt;Returns a list of the gateway&#39;s local disks. To specify which gateway to describe, you use the Amazon Resource Name (ARN) of the gateway in the body of the request.&lt;/p&gt; &lt;p&gt;The request returns a list of all disks, specifying which are configured as working storage, cache storage, or stored volume or not configured at all. The response includes a &lt;code&gt;DiskStatus&lt;/code&gt; field. This field can have a value of present (the disk is available to use), missing (the disk is no longer connected to the gateway), or mismatch (the disk node is occupied by a disk that has incorrect metadata or the disk content is corrupted).&lt;/p&gt;

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
    body = ListLocalDisksInput.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, marker=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags that have been added to the specified resource. This operation is supported in storage gateways of all types.

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
    :param limit: Pagination limit
    :type limit: str
    :param marker: Pagination token
    :type marker: str

    """
    body = ListTagsForResourceInput.from_dict(body)
    return web.Response(status=200)


async def list_tape_pools(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, marker=None) -> web.Response:
    """list_tape_pools

    &lt;p&gt;Lists custom tape pools. You specify custom tape pools to list by specifying one or more custom tape pool Amazon Resource Names (ARNs). If you don&#39;t specify a custom tape pool ARN, the operation lists all custom tape pools.&lt;/p&gt; &lt;p&gt;This operation supports pagination. You can optionally specify the &lt;code&gt;Limit&lt;/code&gt; parameter in the body to limit the number of tape pools in the response. If the number of tape pools returned in the response is truncated, the response includes a &lt;code&gt;Marker&lt;/code&gt; element that you can use in your subsequent request to retrieve the next set of tape pools.&lt;/p&gt;

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
    :param limit: Pagination limit
    :type limit: str
    :param marker: Pagination token
    :type marker: str

    """
    body = ListTapePoolsInput.from_dict(body)
    return web.Response(status=200)


async def list_tapes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, marker=None) -> web.Response:
    """list_tapes

    &lt;p&gt;Lists virtual tapes in your virtual tape library (VTL) and your virtual tape shelf (VTS). You specify the tapes to list by specifying one or more tape Amazon Resource Names (ARNs). If you don&#39;t specify a tape ARN, the operation lists all virtual tapes in both your VTL and VTS.&lt;/p&gt; &lt;p&gt;This operation supports pagination. By default, the operation returns a maximum of up to 100 tapes. You can optionally specify the &lt;code&gt;Limit&lt;/code&gt; parameter in the body to limit the number of tapes in the response. If the number of tapes returned in the response is truncated, the response includes a &lt;code&gt;Marker&lt;/code&gt; element that you can use in your subsequent request to retrieve the next set of tapes. This operation is only supported in the tape gateway type.&lt;/p&gt;

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
    :param limit: Pagination limit
    :type limit: str
    :param marker: Pagination token
    :type marker: str

    """
    body = ListTapesInput.from_dict(body)
    return web.Response(status=200)


async def list_volume_initiators(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_volume_initiators

    Lists iSCSI initiators that are connected to a volume. You can use this operation to determine whether a volume is being used or not. This operation is only supported in the cached volume and stored volume gateway types.

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
    body = ListVolumeInitiatorsInput.from_dict(body)
    return web.Response(status=200)


async def list_volume_recovery_points(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_volume_recovery_points

    &lt;p&gt;Lists the recovery points for a specified gateway. This operation is only supported in the cached volume gateway type.&lt;/p&gt; &lt;p&gt;Each cache volume has one recovery point. A volume recovery point is a point in time at which all data of the volume is consistent and from which you can create a snapshot or clone a new cached volume from a source volume. To create a snapshot from a volume recovery point use the &lt;a&gt;CreateSnapshotFromVolumeRecoveryPoint&lt;/a&gt; operation.&lt;/p&gt;

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
    body = ListVolumeRecoveryPointsInput.from_dict(body)
    return web.Response(status=200)


async def list_volumes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, limit=None, marker=None) -> web.Response:
    """list_volumes

    &lt;p&gt;Lists the iSCSI stored volumes of a gateway. Results are sorted by volume ARN. The response includes only the volume ARNs. If you want additional volume information, use the &lt;a&gt;DescribeStorediSCSIVolumes&lt;/a&gt; or the &lt;a&gt;DescribeCachediSCSIVolumes&lt;/a&gt; API.&lt;/p&gt; &lt;p&gt;The operation supports pagination. By default, the operation returns a maximum of up to 100 volumes. You can optionally specify the &lt;code&gt;Limit&lt;/code&gt; field in the body to limit the number of volumes in the response. If the number of volumes returned in the response is truncated, the response includes a Marker field. You can use this Marker value in your subsequent request to retrieve the next set of volumes. This operation is only supported in the cached volume and stored volume gateway types.&lt;/p&gt;

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
    :param limit: Pagination limit
    :type limit: str
    :param marker: Pagination token
    :type marker: str

    """
    body = ListVolumesInput.from_dict(body)
    return web.Response(status=200)


async def notify_when_uploaded(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """notify_when_uploaded

    &lt;p&gt;Sends you notification through CloudWatch Events when all files written to your file share have been uploaded to S3. Amazon S3.&lt;/p&gt; &lt;p&gt;Storage Gateway can send a notification through Amazon CloudWatch Events when all files written to your file share up to that point in time have been uploaded to Amazon S3. These files include files written to the file share up to the time that you make a request for notification. When the upload is done, Storage Gateway sends you notification through an Amazon CloudWatch Event. You can configure CloudWatch Events to send the notification through event targets such as Amazon SNS or Lambda function. This operation is only supported for S3 File Gateways.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/userguide/monitoring-file-gateway.html#get-upload-notification\&quot;&gt;Getting file upload notification&lt;/a&gt; in the &lt;i&gt;Storage Gateway User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = NotifyWhenUploadedInput.from_dict(body)
    return web.Response(status=200)


async def refresh_cache(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """refresh_cache

    &lt;p&gt;Refreshes the cached inventory of objects for the specified file share. This operation finds objects in the Amazon S3 bucket that were added, removed, or replaced since the gateway last listed the bucket&#39;s contents and cached the results. This operation does not import files into the S3 File Gateway cache storage. It only updates the cached inventory to reflect changes in the inventory of the objects in the S3 bucket. This operation is only supported in the S3 File Gateway types.&lt;/p&gt; &lt;p&gt;You can subscribe to be notified through an Amazon CloudWatch event when your &lt;code&gt;RefreshCache&lt;/code&gt; operation completes. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/userguide/monitoring-file-gateway.html#get-notification\&quot;&gt;Getting notified about file operations&lt;/a&gt; in the &lt;i&gt;Storage Gateway User Guide&lt;/i&gt;. This operation is Only supported for S3 File Gateways.&lt;/p&gt; &lt;p&gt;When this API is called, it only initiates the refresh operation. When the API call completes and returns a success code, it doesn&#39;t necessarily mean that the file refresh has completed. You should use the refresh-complete notification to determine that the operation has completed before you check for new files on the gateway file share. You can subscribe to be notified through a CloudWatch event when your &lt;code&gt;RefreshCache&lt;/code&gt; operation completes.&lt;/p&gt; &lt;p&gt;Throttle limit: This API is asynchronous, so the gateway will accept no more than two refreshes at any time. We recommend using the refresh-complete CloudWatch event notification before issuing additional requests. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/userguide/monitoring-file-gateway.html#get-notification\&quot;&gt;Getting notified about file operations&lt;/a&gt; in the &lt;i&gt;Storage Gateway User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Wait at least 60 seconds between consecutive RefreshCache API requests.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;RefreshCache does not evict cache entries if invoked consecutively within 60 seconds of a previous RefreshCache request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you invoke the RefreshCache API when two requests are already being processed, any new request will cause an &lt;code&gt;InvalidGatewayRequestException&lt;/code&gt; error because too many requests were sent to the server.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;The S3 bucket name does not need to be included when entering the list of folders in the FolderList parameter.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/userguide/monitoring-file-gateway.html#get-notification\&quot;&gt;Getting notified about file operations&lt;/a&gt; in the &lt;i&gt;Storage Gateway User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RefreshCacheInput.from_dict(body)
    return web.Response(status=200)


async def remove_tags_from_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_tags_from_resource

    Removes one or more tags from the specified resource. This operation is supported in storage gateways of all types.

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
    body = RemoveTagsFromResourceInput.from_dict(body)
    return web.Response(status=200)


async def reset_cache(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reset_cache

    &lt;p&gt;Resets all cache disks that have encountered an error and makes the disks available for reconfiguration as cache storage. If your cache disk encounters an error, the gateway prevents read and write operations on virtual tapes in the gateway. For example, an error can occur when a disk is corrupted or removed from the gateway. When a cache is reset, the gateway loses its cache storage. At this point, you can reconfigure the disks as cache disks. This operation is only supported in the cached volume and tape types.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the cache disk you are resetting contains data that has not been uploaded to Amazon S3 yet, that data can be lost. After you reset cache disks, there will be no configured cache disks left in the gateway, so you must configure at least one new cache disk for your gateway to function properly.&lt;/p&gt; &lt;/important&gt;

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
    body = ResetCacheInput.from_dict(body)
    return web.Response(status=200)


async def retrieve_tape_archive(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """retrieve_tape_archive

    &lt;p&gt;Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a tape gateway. Virtual tapes archived in the VTS are not associated with any gateway. However after a tape is retrieved, it is associated with a gateway, even though it is also listed in the VTS, that is, archive. This operation is only supported in the tape gateway type.&lt;/p&gt; &lt;p&gt;Once a tape is successfully retrieved to a gateway, it cannot be retrieved again to another gateway. You must archive the tape again before you can retrieve it to another gateway. This operation is only supported in the tape gateway type.&lt;/p&gt;

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
    body = RetrieveTapeArchiveInput.from_dict(body)
    return web.Response(status=200)


async def retrieve_tape_recovery_point(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """retrieve_tape_recovery_point

    &lt;p&gt;Retrieves the recovery point for the specified virtual tape. This operation is only supported in the tape gateway type.&lt;/p&gt; &lt;p&gt;A recovery point is a point in time view of a virtual tape at which all the data on the tape is consistent. If your gateway crashes, virtual tapes that have recovery points can be recovered to a new gateway.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The virtual tape can be retrieved to only one gateway. The retrieved tape is read-only. The virtual tape can be retrieved to only a tape gateway. There is no charge for retrieving recovery points.&lt;/p&gt; &lt;/note&gt;

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
    body = RetrieveTapeRecoveryPointInput.from_dict(body)
    return web.Response(status=200)


async def set_local_console_password(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_local_console_password

    Sets the password for your VM local console. When you log in to the local console for the first time, you log in to the VM with the default credentials. We recommend that you set a new password. You don&#39;t need to know the default password to set a new password.

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
    body = SetLocalConsolePasswordInput.from_dict(body)
    return web.Response(status=200)


async def set_smb_guest_password(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_smb_guest_password

    Sets the password for the guest user &lt;code&gt;smbguest&lt;/code&gt;. The &lt;code&gt;smbguest&lt;/code&gt; user is the user when the authentication method for the file share is set to &lt;code&gt;GuestAccess&lt;/code&gt;. This operation only supported for S3 File Gateways

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
    body = SetSMBGuestPasswordInput.from_dict(body)
    return web.Response(status=200)


async def shutdown_gateway(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """shutdown_gateway

    &lt;p&gt;Shuts down a gateway. To specify which gateway to shut down, use the Amazon Resource Name (ARN) of the gateway in the body of your request.&lt;/p&gt; &lt;p&gt;The operation shuts down the gateway service component running in the gateway&#39;s virtual machine (VM) and not the host VM.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you want to shut down the VM, it is recommended that you first shut down the gateway component in the VM to avoid unpredictable conditions.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;After the gateway is shutdown, you cannot call any other API except &lt;a&gt;StartGateway&lt;/a&gt;, &lt;a&gt;DescribeGatewayInformation&lt;/a&gt;, and &lt;a&gt;ListGateways&lt;/a&gt;. For more information, see &lt;a&gt;ActivateGateway&lt;/a&gt;. Your applications cannot read from or write to the gateway&#39;s storage volumes, and there are no snapshots taken.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you make a shutdown request, you will get a &lt;code&gt;200 OK&lt;/code&gt; success response immediately. However, it might take some time for the gateway to shut down. You can call the &lt;a&gt;DescribeGatewayInformation&lt;/a&gt; API to check the status. For more information, see &lt;a&gt;ActivateGateway&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;If do not intend to use the gateway again, you must delete the gateway (using &lt;a&gt;DeleteGateway&lt;/a&gt;) to no longer pay software charges associated with the gateway.&lt;/p&gt;

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
    body = ShutdownGatewayInput.from_dict(body)
    return web.Response(status=200)


async def start_availability_monitor_test(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_availability_monitor_test

    &lt;p&gt;Start a test that verifies that the specified gateway is configured for High Availability monitoring in your host environment. This request only initiates the test and that a successful response only indicates that the test was started. It doesn&#39;t indicate that the test passed. For the status of the test, invoke the &lt;code&gt;DescribeAvailabilityMonitorTest&lt;/code&gt; API.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Starting this test will cause your gateway to go offline for a brief period.&lt;/p&gt; &lt;/note&gt;

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
    body = StartAvailabilityMonitorTestInput.from_dict(body)
    return web.Response(status=200)


async def start_gateway(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_gateway

    &lt;p&gt;Starts a gateway that you previously shut down (see &lt;a&gt;ShutdownGateway&lt;/a&gt;). After the gateway starts, you can then make other API calls, your applications can read from or write to the gateway&#39;s storage volumes and you will be able to take snapshot backups.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you make a request, you will get a 200 OK success response immediately. However, it might take some time for the gateway to be ready. You should call &lt;a&gt;DescribeGatewayInformation&lt;/a&gt; and check the status before making any additional API calls. For more information, see &lt;a&gt;ActivateGateway&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;To specify which gateway to start, use the Amazon Resource Name (ARN) of the gateway in your request.&lt;/p&gt;

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
    body = StartGatewayInput.from_dict(body)
    return web.Response(status=200)


async def update_automatic_tape_creation_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_automatic_tape_creation_policy

    &lt;p&gt;Updates the automatic tape creation policy of a gateway. Use this to update the policy with a new set of automatic tape creation rules. This is only supported for tape gateways.&lt;/p&gt; &lt;p&gt;By default, there is no automatic tape creation policy.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A gateway can have only one automatic tape creation policy.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateAutomaticTapeCreationPolicyInput.from_dict(body)
    return web.Response(status=200)


async def update_bandwidth_rate_limit(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_bandwidth_rate_limit

    &lt;p&gt;Updates the bandwidth rate limits of a gateway. You can update both the upload and download bandwidth rate limit or specify only one of the two. If you don&#39;t set a bandwidth rate limit, the existing rate limit remains. This operation is supported only for the stored volume, cached volume, and tape gateway types. To update bandwidth rate limits for S3 file gateways, use &lt;a&gt;UpdateBandwidthRateLimitSchedule&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;By default, a gateway&#39;s bandwidth rate limits are not set. If you don&#39;t set any limit, the gateway does not have any limitations on its bandwidth usage and could potentially use the maximum available bandwidth.&lt;/p&gt; &lt;p&gt;To specify which gateway to update, use the Amazon Resource Name (ARN) of the gateway in your request.&lt;/p&gt;

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
    body = UpdateBandwidthRateLimitInput.from_dict(body)
    return web.Response(status=200)


async def update_bandwidth_rate_limit_schedule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_bandwidth_rate_limit_schedule

     Updates the bandwidth rate limit schedule for a specified gateway. By default, gateways do not have bandwidth rate limit schedules, which means no bandwidth rate limiting is in effect. Use this to initiate or update a gateway&#39;s bandwidth rate limit schedule. This operation is supported only for volume, tape and S3 file gateways. FSx file gateways do not support bandwidth rate limits.

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
    body = UpdateBandwidthRateLimitScheduleInput.from_dict(body)
    return web.Response(status=200)


async def update_chap_credentials(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_chap_credentials

    &lt;p&gt;Updates the Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target. By default, a gateway does not have CHAP enabled; however, for added security, you might use it. This operation is supported in the volume and tape gateway types.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When you update CHAP credentials, all existing connections on the target are closed and initiators must reconnect with the new credentials.&lt;/p&gt; &lt;/important&gt;

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
    body = UpdateChapCredentialsInput.from_dict(body)
    return web.Response(status=200)


async def update_file_system_association(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_file_system_association

    Updates a file system association. This operation is only supported in the FSx File Gateways.

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
    body = UpdateFileSystemAssociationInput.from_dict(body)
    return web.Response(status=200)


async def update_gateway_information(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_gateway_information

    &lt;p&gt;Updates a gateway&#39;s metadata, which includes the gateway&#39;s name and time zone. To specify which gateway to update, use the Amazon Resource Name (ARN) of the gateway in your request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For gateways activated after September 2, 2015, the gateway&#39;s ARN contains the gateway ID rather than the gateway name. However, changing the name of the gateway has no effect on the gateway&#39;s ARN.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateGatewayInformationInput.from_dict(body)
    return web.Response(status=200)


async def update_gateway_software_now(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_gateway_software_now

    &lt;p&gt;Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you make this request, you get a &lt;code&gt;200 OK&lt;/code&gt; success response immediately. However, it might take some time for the update to complete. You can call &lt;a&gt;DescribeGatewayInformation&lt;/a&gt; to verify the gateway is in the &lt;code&gt;STATE_RUNNING&lt;/code&gt; state.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;A software update forces a system restart of your gateway. You can minimize the chance of any disruption to your applications by increasing your iSCSI Initiators&#39; timeouts. For more information about increasing iSCSI Initiator timeouts for Windows and Linux, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/userguide/ConfiguringiSCSIClientInitiatorWindowsClient.html#CustomizeWindowsiSCSISettings\&quot;&gt;Customizing your Windows iSCSI settings&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/storagegateway/latest/userguide/ConfiguringiSCSIClientInitiatorRedHatClient.html#CustomizeLinuxiSCSISettings\&quot;&gt;Customizing your Linux iSCSI settings&lt;/a&gt;, respectively.&lt;/p&gt; &lt;/important&gt;

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
    body = UpdateGatewaySoftwareNowInput.from_dict(body)
    return web.Response(status=200)


async def update_maintenance_start_time(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_maintenance_start_time

    Updates a gateway&#39;s weekly maintenance start time information, including day and time of the week. The maintenance time is the time in your gateway&#39;s time zone.

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
    body = UpdateMaintenanceStartTimeInput.from_dict(body)
    return web.Response(status=200)


async def update_nfs_file_share(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_nfs_file_share

    &lt;p&gt;Updates a Network File System (NFS) file share. This operation is only supported in S3 File Gateways.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To leave a file share field unchanged, set the corresponding input field to null.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Updates the following file share settings:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Default storage class for your S3 bucket&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Metadata defaults for your S3 bucket&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Allowed NFS clients for your file share&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Squash settings&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Write status of your file share&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = UpdateNFSFileShareInput.from_dict(body)
    return web.Response(status=200)


async def update_smb_file_share(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_smb_file_share

    &lt;p&gt;Updates a Server Message Block (SMB) file share. This operation is only supported for S3 File Gateways.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To leave a file share field unchanged, set the corresponding input field to null.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;File gateways require Security Token Service (Amazon Web Services STS) to be activated to enable you to create a file share. Make sure that Amazon Web Services STS is activated in the Amazon Web Services Region you are creating your file gateway in. If Amazon Web Services STS is not activated in this Amazon Web Services Region, activate it. For information about how to activate Amazon Web Services STS, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html\&quot;&gt;Activating and deactivating Amazon Web Services STS in an Amazon Web Services Region&lt;/a&gt; in the &lt;i&gt;Identity and Access Management User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;File gateways don&#39;t support creating hard or symbolic links on a file share.&lt;/p&gt; &lt;/important&gt;

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
    body = UpdateSMBFileShareInput.from_dict(body)
    return web.Response(status=200)


async def update_smb_file_share_visibility(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_smb_file_share_visibility

    Controls whether the shares on an S3 File Gateway are visible in a net view or browse list. The operation is only supported for S3 File Gateways.

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
    body = UpdateSMBFileShareVisibilityInput.from_dict(body)
    return web.Response(status=200)


async def update_smb_local_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_smb_local_groups

    Updates the list of Active Directory users and groups that have special permissions for SMB file shares on the gateway.

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
    body = UpdateSMBLocalGroupsInput.from_dict(body)
    return web.Response(status=200)


async def update_smb_security_strategy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_smb_security_strategy

    &lt;p&gt;Updates the SMB security strategy on a file gateway. This action is only supported in file gateways.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is called Security level in the User Guide.&lt;/p&gt; &lt;p&gt;A higher security level can affect performance of the gateway.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateSMBSecurityStrategyInput.from_dict(body)
    return web.Response(status=200)


async def update_snapshot_schedule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_snapshot_schedule

    &lt;p&gt;Updates a snapshot schedule configured for a gateway volume. This operation is only supported in the cached volume and stored volume gateway types.&lt;/p&gt; &lt;p&gt;The default snapshot schedule for volume is once every 24 hours, starting at the creation time of the volume. You can use this API to change the snapshot schedule configured for the volume.&lt;/p&gt; &lt;p&gt;In the request you must identify the gateway volume whose snapshot schedule you want to update, and the schedule information, including when you want the snapshot to begin on a day and the frequency (in hours) of snapshots.&lt;/p&gt;

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
    body = UpdateSnapshotScheduleInput.from_dict(body)
    return web.Response(status=200)


async def update_vtl_device_type(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_vtl_device_type

    Updates the type of medium changer in a tape gateway. When you activate a tape gateway, you select a medium changer type for the tape gateway. This operation enables you to select a different type of medium changer after a tape gateway is activated. This operation is only supported in the tape gateway type.

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
    body = UpdateVTLDeviceTypeInput.from_dict(body)
    return web.Response(status=200)
