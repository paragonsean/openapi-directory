# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_batch_mount_snapshot(client):
    """Test case for batch_mount_snapshot

    Live mount a snapshot each from a set of virtual machines
    """
    body = {"snapshots":[{"snapshotBeforeDate":"2000-01-23T04:56:07.000+00:00","snapshotId":"snapshotId","vmId":"vmId","snapshotAfterDate":"2000-01-23T04:56:07.000+00:00","config":{"vmName":"vmName","keepMacAddresses":True,"disableNetwork":True,"powerOn":True,"vlan":0,"dataStoreName":"dataStoreName","hostId":"hostId","removeNetworkDevices":True,"createDatastoreOnly":True,"shouldRecoverTags":True}},{"snapshotBeforeDate":"2000-01-23T04:56:07.000+00:00","snapshotId":"snapshotId","vmId":"vmId","snapshotAfterDate":"2000-01-23T04:56:07.000+00:00","config":{"vmName":"vmName","keepMacAddresses":True,"disableNetwork":True,"powerOn":True,"vlan":0,"dataStoreName":"dataStoreName","hostId":"hostId","removeNetworkDevices":True,"createDatastoreOnly":True,"shouldRecoverTags":True}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/batch_mount',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_browse_vmware_snapshot(client):
    """Test case for browse_vmware_snapshot

    List files in VM snapshot
    """
    params = [('path', 'path_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vm/snapshot/{id}/browse'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_create_on_demand_backup(client):
    """Test case for bulk_create_on_demand_backup

    Take an on-demand snapshot of multiple virtual machines
    """
    body = {"slaId":"slaId","vms":["vms","vms"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/snapshot/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_download_file_job(client):
    """Test case for create_download_file_job

    Download file from VM snapshot
    """
    body = {"path":"path","legalHoldDownloadConfig":{"isLegalHoldDownload":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/snapshot/{id}/download_file'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_download_snapshot_from_cloud(client):
    """Test case for create_download_snapshot_from_cloud

    Download snapshot from archive
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/snapshot/{id}/download'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_export_v1(client):
    """Test case for create_export_v1

    Export VM snapshot
    """
    body = {"vmName":"vmName","keepMacAddresses":True,"unregisterVm":True,"disableNetwork":True,"powerOn":True,"hostId":"hostId","removeNetworkDevices":True,"datastoreId":"datastoreId","shouldRecoverTags":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/snapshot/{id}/export'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_export_with_download_from_cloud_v1(client):
    """Test case for create_export_with_download_from_cloud_v1

    Download a snapshot from an archival location, then export a virtual machine using the downloaded snapshot
    """
    body = {"vmName":"vmName","keepMacAddresses":True,"unregisterVm":True,"disableNetwork":True,"powerOn":True,"hostId":"hostId","removeNetworkDevices":True,"datastoreId":"datastoreId","shouldRecoverTags":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/snapshot/{id}/export_with_download'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_instant_recovery(client):
    """Test case for create_instant_recovery

    Instantly recover a VM
    """
    body = {"vmName":"vmName","keepMacAddresses":True,"disableNetwork":True,"powerOn":True,"vlan":0,"hostId":"hostId","removeNetworkDevices":True,"preserveMoid":False,"shouldRecoverTags":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/snapshot/{id}/instant_recover'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_mount_v1(client):
    """Test case for create_mount_v1

    Live mount a VM from a snapshot
    """
    body = {"vmName":"vmName","keepMacAddresses":True,"disableNetwork":True,"powerOn":True,"vlan":0,"dataStoreName":"dataStoreName","hostId":"hostId","removeNetworkDevices":True,"createDatastoreOnly":True,"shouldRecoverTags":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/snapshot/{id}/mount'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_on_demand_backup(client):
    """Test case for create_on_demand_backup

    Create an on-demand snapshot for a VM
    """
    body = {"slaId":"slaId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_restore_file_job(client):
    """Test case for create_restore_file_job

    Restore file from VM snapshot
    """
    body = {"path":"path","password":"password","shouldRestoreXAttrs":True,"domainName":"domainName","restorePath":"restorePath","ignoreErrors":False,"shouldSaveCredentials":True,"shouldUseAgent":True,"username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/snapshot/{id}/restore_file'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_unmount(client):
    """Test case for create_unmount

    Delete a Live Mount VM
    """
    params = [('force', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/vmware/vm/snapshot/mount/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vmware_snapshot(client):
    """Test case for delete_vmware_snapshot

    Delete VM snapshot
    """
    params = [('location', 'location_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/vmware/vm/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vmware_snapshots(client):
    """Test case for delete_vmware_snapshots

    Delete all snapshots of VM
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/vmware/vm/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_async_request_status(client):
    """Test case for get_async_request_status

    Get asynchronous request details for VM
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vm/request/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mount_v1(client):
    """Test case for get_mount_v1

    Get information for a Live Mount
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vm/snapshot/mount/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_snapshot(client):
    """Test case for get_snapshot

    Get VM snapshot details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vm/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_virtual_disk(client):
    """Test case for get_virtual_disk

    Details about the specific Virtual Disk
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vm/virtual_disk/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vm(client):
    """Test case for get_vm

    Get VM details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vm/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vm_force_full_spec(client):
    """Test case for get_vm_force_full_spec

    Retrieve the configuration for forcing a full snapshot of a VMware virtual machine
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vm/{id}/request/force_full_snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vmware_cdp_live_info(client):
    """Test case for get_vmware_cdp_live_info

    Returns the live CDP info for a set of CDP-enabled virtual machines
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/cdp',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vmware_cdp_state_info(client):
    """Test case for get_vmware_cdp_state_info

    Returns CDP state info for a set of virtual machines
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/cdp_state',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vmware_missed_recoverable_ranges(client):
    """Test case for get_vmware_missed_recoverable_ranges

    Get missed time ranges for point in time recovery
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
        path='/api/v1/vmware/vm/{id}/missed_recoverable_range'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vmware_recoverable_ranges(client):
    """Test case for get_vmware_recoverable_ranges

    Get available time ranges for point in time recovery
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
        path='/api/v1/vmware/vm/{id}/recoverable_range'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vmware_vm_missed_recoverable_ranges_in_batch(client):
    """Test case for get_vmware_vm_missed_recoverable_ranges_in_batch

    Returns the recoverable ranges that were missed for a set of CDP-enabled virtual machines
    """
    body = {"before_time":"2000-01-23T04:56:07.000+00:00","vmIds":["vmIds","vmIds"],"after_time":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/missed_recoverable_range',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vmware_vm_recoverable_ranges_in_batch(client):
    """Test case for get_vmware_vm_recoverable_ranges_in_batch

    Returns the recoverable ranges for a set of CDP-enabled virtual machines
    """
    body = {"before_time":"2000-01-23T04:56:07.000+00:00","vmIds":["vmIds","vmIds"],"after_time":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/recoverable_range',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_missed_snapshots(client):
    """Test case for missed_snapshots

    Get details about missed snapshots for a VM
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vm/{id}/missed_snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_mount_v1(client):
    """Test case for query_mount_v1

    Get Live Mount information
    """
    params = [('vm_id', 'vm_id_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vm/snapshot/mount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_snapshot(client):
    """Test case for query_snapshot

    Get list of snapshots of VM
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vm/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_snapshots_for_vms(client):
    """Test case for query_snapshots_for_vms

    Get snapshot information for a list of virtual machines
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/snapshots',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_vm(client):
    """Test case for query_vm

    Get list of VMs
    """
    params = [('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('is_relic', True),
                    ('name', 'name_example'),
                    ('moid', 'moid_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('guest_os_name', 'guest_os_name_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vm',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_relocate_mount(client):
    """Test case for relocate_mount

    Relocate a virtual machine to another datastore
    """
    body = {"datastoreId":"datastoreId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/snapshot/mount/{id}/relocate'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_vm_force_full_snapshot(client):
    """Test case for request_vm_force_full_snapshot

    Request a full snapshot for the next backup job of a VMware virtual machine
    """
    body = {"virtualDiskInfos":[{"shouldDedupe":True,"virtualDiskId":"virtualDiskId"},{"shouldDedupe":True,"virtualDiskId":"virtualDiskId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/{id}/request/force_full_snapshot'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_guest_os_script(client):
    """Test case for run_guest_os_script

    Run guest OS script
    """
    body = {"phase":"PreBackup"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/{id}/guest_script/run'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_vm(client):
    """Test case for search_vm

    Search for a file from a VM
    """
    params = [('path', 'path_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vmware/vm/{id}/search'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_mount(client):
    """Test case for update_mount

    Power a Live Mount on and off
    """
    body = {"powerStatus":True,"shouldForce":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/vmware/vm/snapshot/mount/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_virtual_disk(client):
    """Test case for update_virtual_disk

    Update a specific Virtual Disk
    """
    body = {"excludeFromSnapshots":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/vmware/vm/virtual_disk/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_vm(client):
    """Test case for update_vm

    Update VM
    """
    body = {"cloudInstantiationSpec":{"imageRetentionInSeconds":6},"postSnapScript":{"scriptPath":"scriptPath","failureHandling":"abort","timeoutMs":5},"isVmPaused":True,"shouldRefreshCacheAfterUpdate":True,"postBackupScript":{"scriptPath":"scriptPath","failureHandling":"abort","timeoutMs":5},"guestCredential":{"password":"password","username":"username"},"isArrayIntegrationEnabled":True,"preBackupScript":{"scriptPath":"scriptPath","failureHandling":"abort","timeoutMs":5},"maxNestedVsphereSnapshots":0,"configuredSlaDomainId":"configuredSlaDomainId","throttlingSettings":{"datastoreIoLatencyThreshold":2,"cpuUtilizationThreshold":5,"ioLatencyThreshold":7},"snapshotConsistencyMandate":"UNKNOWN"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/vmware/vm/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vm_make_primary(client):
    """Test case for vm_make_primary

    Make this cluster the primary for agents on a set of VMs
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/make_primary',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vm_register_agent(client):
    """Test case for vm_register_agent

    Register Rubrik Backup Service
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vmware/vm/{id}/register_agent'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

