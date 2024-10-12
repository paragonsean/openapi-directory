from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.base_on_demand_snapshot_config import BaseOnDemandSnapshotConfig
from openapi_server.models.batch_async_request_status import BatchAsyncRequestStatus
from openapi_server.models.batch_mount_snapshot_job_config import BatchMountSnapshotJobConfig
from openapi_server.models.batch_vm_snapshot_summaries import BatchVmSnapshotSummaries
from openapi_server.models.batch_vmware_cdp_live_info import BatchVmwareCdpLiveInfo
from openapi_server.models.batch_vmware_cdp_state_info import BatchVmwareCdpStateInfo
from openapi_server.models.batch_vmware_vm_missed_recoverable_ranges import BatchVmwareVmMissedRecoverableRanges
from openapi_server.models.batch_vmware_vm_missed_recoverable_ranges_request import BatchVmwareVmMissedRecoverableRangesRequest
from openapi_server.models.batch_vmware_vm_recoverable_ranges import BatchVmwareVmRecoverableRanges
from openapi_server.models.batch_vmware_vm_recoverable_ranges_request import BatchVmwareVmRecoverableRangesRequest
from openapi_server.models.browse_response_list_response import BrowseResponseListResponse
from openapi_server.models.bulk_on_demand_snapshot_job_config import BulkOnDemandSnapshotJobConfig
from openapi_server.models.download_file_job_config import DownloadFileJobConfig
from openapi_server.models.export_snapshot_job_config_v1 import ExportSnapshotJobConfigV1
from openapi_server.models.instant_recovery_job_config import InstantRecoveryJobConfig
from openapi_server.models.missed_snapshot_list_response import MissedSnapshotListResponse
from openapi_server.models.mount_snapshot_job_config_v1 import MountSnapshotJobConfigV1
from openapi_server.models.relocate_mount_config import RelocateMountConfig
from openapi_server.models.restore_file_job_config import RestoreFileJobConfig
from openapi_server.models.search_response_list_response import SearchResponseListResponse
from openapi_server.models.update_mount_config import UpdateMountConfig
from openapi_server.models.virtual_disk_detail import VirtualDiskDetail
from openapi_server.models.virtual_disk_update import VirtualDiskUpdate
from openapi_server.models.virtual_machine_detail import VirtualMachineDetail
from openapi_server.models.virtual_machine_summary_list_response import VirtualMachineSummaryListResponse
from openapi_server.models.virtual_machine_update_with_secret import VirtualMachineUpdateWithSecret
from openapi_server.models.vm_force_full_request import VmForceFullRequest
from openapi_server.models.vm_force_full_response import VmForceFullResponse
from openapi_server.models.vm_guest_script_run_config import VmGuestScriptRunConfig
from openapi_server.models.vm_snapshot_detail import VmSnapshotDetail
from openapi_server.models.vm_snapshot_summary_list_response import VmSnapshotSummaryListResponse
from openapi_server.models.vmware_recoverable_range_list_response import VmwareRecoverableRangeListResponse
from openapi_server.models.vmware_vm_mount_detail_v1 import VmwareVmMountDetailV1
from openapi_server.models.vmware_vm_mount_summary_v1_list_response import VmwareVmMountSummaryV1ListResponse
from openapi_server import util


async def batch_mount_snapshot(request: web.Request, body) -> web.Response:
    """Live mount a snapshot each from a set of virtual machines

    

    :param body: Configuration object containing an array of virtual machine IDs, a way to indicate the snapshot to be chosen and mount configs.
    :type body: dict | bytes

    """
    body = BatchMountSnapshotJobConfig.from_dict(body)
    return web.Response(status=200)


async def browse_vmware_snapshot(request: web.Request, id, path, offset=None, limit=None) -> web.Response:
    """List files in VM snapshot

    For a virtual machine snapshot, list the directories and files that are beneath a specified file system path.

    :param id: ID of snapshot.
    :type id: str
    :param path: The absolute path of the starting point for the directory listing.
    :type path: str
    :param offset: Starting position in the list of path entries contained in the query results, sorted by lexicographical order. The response includes the specified numbered entry and all higher numbered entries.
    :type offset: int
    :param limit: Maximum number of entries in the response.
    :type limit: int

    """
    return web.Response(status=200)


async def bulk_create_on_demand_backup(request: web.Request, body) -> web.Response:
    """Take an on-demand snapshot of multiple virtual machines

    Bulk operation of taking on-demand snapshot for given virtual machines.

    :param body: The IDs of the virtual machines for which to take an on-demand snapshot and the ID of the SLA Domain to assign to the resulting snapshot.
    :type body: dict | bytes

    """
    body = BulkOnDemandSnapshotJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_download_file_job(request: web.Request, id, body) -> web.Response:
    """Download file from VM snapshot

    Create a request to download a file from a virtual machine snapshot.

    :param id: ID of a snapshot.
    :type id: str
    :param body: Configuration for the file download request.
    :type body: dict | bytes

    """
    body = DownloadFileJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_download_snapshot_from_cloud(request: web.Request, id) -> web.Response:
    """Download snapshot from archive

    Provides a method for retrieving a snapshot, that is not available locally, from an archival location.

    :param id: ID of snapshot.
    :type id: str

    """
    return web.Response(status=200)


async def create_export_v1(request: web.Request, id, body) -> web.Response:
    """Export VM snapshot

    Export a virtual machine from a snapshot, using a specified hypervisor host as the datastore.

    :param id: ID of a snapshot.
    :type id: str
    :param body: Configuration for the export request.
    :type body: dict | bytes

    """
    body = ExportSnapshotJobConfigV1.from_dict(body)
    return web.Response(status=200)


async def create_export_with_download_from_cloud_v1(request: web.Request, id, body) -> web.Response:
    """Download a snapshot from an archival location, then export a virtual machine using the downloaded snapshot

    Download a snapshot from an archival location and then export a virtual machine using the downloaded snapshot.

    :param id: ID of a snapshot.
    :type id: str
    :param body: Configuration for the export request.
    :type body: dict | bytes

    """
    body = ExportSnapshotJobConfigV1.from_dict(body)
    return web.Response(status=200)


async def create_instant_recovery(request: web.Request, id, body) -> web.Response:
    """Instantly recover a VM

    Instantly recovery a virtual machine from a snapshot. The Instant Recovery request starts the virtual machine with networking enabled and renames and powers off the source virtual machine, if it still exists.

    :param id: ID of Snapshot.
    :type id: str
    :param body: Configuration for the Instant Recovery request.
    :type body: dict | bytes

    """
    body = InstantRecoveryJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_mount_v1(request: web.Request, id, body=None) -> web.Response:
    """Live mount a VM from a snapshot

    Create a request to Live Mount a virtual machine from a snapshot using a specified configuration.

    :param id: ID of a snapshot.
    :type id: str
    :param body: Configuration for the Live Mount request.
    :type body: dict | bytes

    """
    body = MountSnapshotJobConfigV1.from_dict(body)
    return web.Response(status=200)


async def create_on_demand_backup(request: web.Request, id, body=None) -> web.Response:
    """Create an on-demand snapshot for a VM

    Use the ID of a virtual machine to create an on-demand snapshot.

    :param id: ID of the virtual machine.
    :type id: str
    :param body: Configuration for the on-demand snapshot.
    :type body: dict | bytes

    """
    body = BaseOnDemandSnapshotConfig.from_dict(body)
    return web.Response(status=200)


async def create_restore_file_job(request: web.Request, id, body) -> web.Response:
    """Restore file from VM snapshot

    Create a request to restore a file or folder to the source virtual machine.

    :param id: ID of a snapshot.
    :type id: str
    :param body: Configuration for the restore request.
    :type body: dict | bytes

    """
    body = RestoreFileJobConfig.from_dict(body)
    return web.Response(status=200)


async def create_unmount(request: web.Request, id, force=None) -> web.Response:
    """Delete a Live Mount VM

    Create a request to delete a Live Mount virtual machine.

    :param id: ID of a Live Mount.
    :type id: str
    :param force: Force unmount to remove metadata when the datastore of the Live Mount virtual machine was moved off of the Rubrik cluster.
    :type force: bool

    """
    return web.Response(status=200)


async def delete_vmware_snapshot(request: web.Request, id, location) -> web.Response:
    """Delete VM snapshot

    Designate a snapshot as expired and available for garbage collection. The snapshot must be an on-demand snapshot or a snapshot from a virtual machine that is not assigned to an SLA Domain.

    :param id: ID of snapshot.
    :type id: str
    :param location: Location of the snapshot. Use **_local_** to delete only the local copy of the snapshot. Or use **_all_** to delete the snapshot locally, on a replication target, and at an archival location.
    :type location: str

    """
    return web.Response(status=200)


async def delete_vmware_snapshots(request: web.Request, id) -> web.Response:
    """Delete all snapshots of VM

    Delete all of the snapshots from a virtual machine.

    :param id: Virtual machine ID.
    :type id: str

    """
    return web.Response(status=200)


async def get_async_request_status(request: web.Request, id) -> web.Response:
    """Get asynchronous request details for VM

    Get the details of an asynchronous request that involves a VMware virtual machine.

    :param id: ID of an asynchronous request.
    :type id: str

    """
    return web.Response(status=200)


async def get_mount_v1(request: web.Request, id) -> web.Response:
    """Get information for a Live Mount

    Retrieve detailed information for a specified Live Mount.

    :param id: ID of a Live Mount.
    :type id: str

    """
    return web.Response(status=200)


async def get_snapshot(request: web.Request, id) -> web.Response:
    """Get VM snapshot details

    Retrieve detailed information about a virtual machine snapshot.

    :param id: ID of a snapshot.
    :type id: str

    """
    return web.Response(status=200)


async def get_virtual_disk(request: web.Request, id) -> web.Response:
    """Details about the specific Virtual Disk

    Detailed about the specific Virtual Disk.

    :param id: ID of the Virtual Disk.
    :type id: str

    """
    return web.Response(status=200)


async def get_vm(request: web.Request, id) -> web.Response:
    """Get VM details

    Retrieve details for a virtual machine.

    :param id: ID of the virtual machine.
    :type id: str

    """
    return web.Response(status=200)


async def get_vm_force_full_spec(request: web.Request, id) -> web.Response:
    """Retrieve the configuration for forcing a full snapshot of a VMware virtual machine

    Retrieve the configuration that has been set for forcing a full snapshot for a VMware virtual machine.

    :param id: ID of the VMware virtual machine.
    :type id: str

    """
    return web.Response(status=200)


async def get_vmware_cdp_live_info(request: web.Request, body) -> web.Response:
    """Returns the live CDP info for a set of CDP-enabled virtual machines

    

    :param body: The ID of each CDP-enabled virtual machine for which live info is being retrieved.
    :type body: List[str]

    """
    return web.Response(status=200)


async def get_vmware_cdp_state_info(request: web.Request, body) -> web.Response:
    """Returns CDP state info for a set of virtual machines

    

    :param body: The ID of each virtual machine for which CDP state info is being retrieved.
    :type body: List[str]

    """
    return web.Response(status=200)


async def get_vmware_missed_recoverable_ranges(request: web.Request, id, after_time=None, before_time=None) -> web.Response:
    """Get missed time ranges for point in time recovery

    Gets a list of time ranges to which a CDP-enabled virtual machine cannot perform a point-in-time recovery. The time ranges are indicated by start and end timestamps listed as date-time strings.

    :param id: The virtual machine ID.
    :type id: str
    :param after_time: Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;.
    :type after_time: str
    :param before_time: Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;.
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def get_vmware_recoverable_ranges(request: web.Request, id, after_time=None, before_time=None) -> web.Response:
    """Get available time ranges for point in time recovery

    Gets time ranges available for point-in-time recovery. The time ranges are indicated by start and end date-time strings.

    :param id: The virtual machine ID.
    :type id: str
    :param after_time: Filter ranges to end after this time. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;.
    :type after_time: str
    :param before_time: Filter ranges to start before this time. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;.
    :type before_time: str

    """
    after_time = util.deserialize_datetime(after_time)
    before_time = util.deserialize_datetime(before_time)
    return web.Response(status=200)


async def get_vmware_vm_missed_recoverable_ranges_in_batch(request: web.Request, body) -> web.Response:
    """Returns the recoverable ranges that were missed for a set of CDP-enabled virtual machines

    

    :param body: The batch request and the date ranges (optional) as a filter. The batch request includes the ID of each CDP-enabled virtual machine for which missed recoverable ranges are being retrieved.
    :type body: dict | bytes

    """
    body = BatchVmwareVmMissedRecoverableRangesRequest.from_dict(body)
    return web.Response(status=200)


async def get_vmware_vm_recoverable_ranges_in_batch(request: web.Request, body) -> web.Response:
    """Returns the recoverable ranges for a set of CDP-enabled virtual machines

    

    :param body: The batch request, which includes the ID of each CDP-enabled virtual machine for which recoverable ranges are being retrieved, and optionally the date ranges as a filter.
    :type body: dict | bytes

    """
    body = BatchVmwareVmRecoverableRangesRequest.from_dict(body)
    return web.Response(status=200)


async def missed_snapshots(request: web.Request, id) -> web.Response:
    """Get details about missed snapshots for a VM

    Retrieve details about the missed snapshots for a virtual machine.

    :param id: ID of a virtual machine.
    :type id: str

    """
    return web.Response(status=200)


async def query_mount_v1(request: web.Request, vm_id=None, offset=None, limit=None) -> web.Response:
    """Get Live Mount information

    Retrieve summary information about Live Mount activity.

    :param vm_id: Filters information by virtual machine ID.
    :type vm_id: str
    :param offset: Starting position in the list of Live Mount entries contained in the response. The summary information includes the specified numbered entry and all higher numbered entries. Use with **_limit_** to retrieve the summary information as smaller groups of entries, e.g. for paging of the results.
    :type offset: int
    :param limit: Limit the summary information to a specified maximum number of entries. Optionally, use with **_offset_** to start the count at a specified point. Default is 25.
    :type limit: int

    """
    return web.Response(status=200)


async def query_snapshot(request: web.Request, id) -> web.Response:
    """Get list of snapshots of VM

    Retrieve summary information for the snapshots of a virtual machine.

    :param id: ID of the virtual machine.
    :type id: str

    """
    return web.Response(status=200)


async def query_snapshots_for_vms(request: web.Request, body) -> web.Response:
    """Get snapshot information for a list of virtual machines

    Retrieve snapshot summaries for a list of virtual machines.

    :param body: IDs of the virtual machines.
    :type body: List[str]

    """
    return web.Response(status=200)


async def query_vm(request: web.Request, effective_sla_domain_id=None, primary_cluster_id=None, limit=None, offset=None, is_relic=None, name=None, moid=None, sla_assignment=None, guest_os_name=None, sort_by=None, sort_order=None) -> web.Response:
    """Get list of VMs

    Get summary of all the VMs.

    :param effective_sla_domain_id: Filter by ID of effective SLA Domain.
    :type effective_sla_domain_id: str
    :param primary_cluster_id: Filter by primary cluster ID, or **local**.
    :type primary_cluster_id: str
    :param limit: Limit the number of matches returned.
    :type limit: int
    :param offset: Ignore these many matches in the beginning.
    :type offset: int
    :param is_relic: Filter by the isRelic field of the virtual machine. When this parameter is not set, return both relic and non-relic virtual machines.
    :type is_relic: bool
    :param name: Search by using a virtual machine name.
    :type name: str
    :param moid: Search by using a virtual machine managed object ID.
    :type moid: str
    :param sla_assignment: Filter by SLA Domain assignment type.
    :type sla_assignment: str
    :param guest_os_name: Filters by the name of operating system using infix search.
    :type guest_os_name: str
    :param sort_by: Sort results based on the specified attribute.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str

    """
    return web.Response(status=200)


async def relocate_mount(request: web.Request, id, body) -> web.Response:
    """Relocate a virtual machine to another datastore

    Run storage VMotion to relocate a specified Live Mount into another data store.

    :param id: ID of the live mount.
    :type id: str
    :param body: Configuration for the RelocateMount request to another data store.
    :type body: dict | bytes

    """
    body = RelocateMountConfig.from_dict(body)
    return web.Response(status=200)


async def request_vm_force_full_snapshot(request: web.Request, id, body) -> web.Response:
    """Request a full snapshot for the next backup job of a VMware virtual machine

    Request a full snapshot to be taken for the next backup job of a VMware virtual machine.

    :param id: ID of the VMware virtual machine.
    :type id: str
    :param body: Configuration for forcing a full snapshot on the VMware virtual machine.
    :type body: dict | bytes

    """
    body = VmForceFullRequest.from_dict(body)
    return web.Response(status=200)


async def run_guest_os_script(request: web.Request, id, body) -> web.Response:
    """Run guest OS script

    Run the specified preBackup, postSnap, or postBackup script in the guest OS of a virtual machine. The script must exist and meet requirements.

    :param id: ID of the virtual machine.
    :type id: str
    :param body: Configuration used to run the specified preBackup, postSnap, or postBackup guest OS script.
    :type body: dict | bytes

    """
    body = VmGuestScriptRunConfig.from_dict(body)
    return web.Response(status=200)


async def search_vm(request: web.Request, id, path, limit=None, cursor=None) -> web.Response:
    """Search for a file from a VM

    Search for a file in the snapshots of a a virtual machine. Specify the file by full path prefix or filename prefix.

    :param id: ID of the virtual machine.
    :type id: str
    :param path: The path query. Use either a path prefix or a filename prefix.
    :type path: str
    :param limit: Maximum number of entries in the response.
    :type limit: int
    :param cursor: Pagination cursor returned by the previous request.
    :type cursor: str

    """
    return web.Response(status=200)


async def update_mount(request: web.Request, id, body) -> web.Response:
    """Power a Live Mount on and off

    Power a specified Live Mount virtual machine on or off. Pass **_true_** to power the virtual machine on and pass **_false_** to power the virtual machine off.

    :param id: ID of a Live Mount.
    :type id: str
    :param body: Power state configuration.
    :type body: dict | bytes

    """
    body = UpdateMountConfig.from_dict(body)
    return web.Response(status=200)


async def update_virtual_disk(request: web.Request, id, body) -> web.Response:
    """Update a specific Virtual Disk

    Update a specific Virtual Disk.

    :param id: ID of the Virtual Disk.
    :type id: str
    :param body: Virtual Disk update information.
    :type body: dict | bytes

    """
    body = VirtualDiskUpdate.from_dict(body)
    return web.Response(status=200)


async def update_vm(request: web.Request, id, body) -> web.Response:
    """Update VM

    Update a virtual machine with specified properties. Use the guestCredential field to update the guest credential for a specified virtual machine.

    :param id: ID of virtual machine.
    :type id: str
    :param body: Properties to update.
    :type body: dict | bytes

    """
    body = VirtualMachineUpdateWithSecret.from_dict(body)
    return web.Response(status=200)


async def vm_make_primary(request: web.Request, body) -> web.Response:
    """Make this cluster the primary for agents on a set of VMs

    Migrate the primary cluster with which the agent is able to communicate. For disaster recovery when migrating everything over from another cluster, the /host/make_primary endpoint can be used with the oldPrimaryClusterUuid parameter.

    :param body: IDs of hosts to migrate.
    :type body: List[str]

    """
    return web.Response(status=200)


async def vm_register_agent(request: web.Request, id) -> web.Response:
    """Register Rubrik Backup Service

    Register the Rubrik Backup Service that is running on a specified host with the specified Rubrik cluster.

    :param id: ID assigned to a virtual machine object.
    :type id: str

    """
    return web.Response(status=200)
