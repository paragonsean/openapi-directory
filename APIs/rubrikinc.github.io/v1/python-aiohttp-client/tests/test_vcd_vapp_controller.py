# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_search_response_list_response import AppSearchResponseListResponse
from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.base_on_demand_snapshot_config import BaseOnDemandSnapshotConfig
from openapi_server.models.missed_snapshot_list_response import MissedSnapshotListResponse
from openapi_server.models.vapp_export_options import VappExportOptions
from openapi_server.models.vapp_export_snapshot_job_config import VappExportSnapshotJobConfig
from openapi_server.models.vapp_instant_recovery_job_config import VappInstantRecoveryJobConfig
from openapi_server.models.vapp_instant_recovery_options import VappInstantRecoveryOptions
from openapi_server.models.vapp_template_export_job_config import VappTemplateExportJobConfig
from openapi_server.models.vapp_template_export_options_union import VappTemplateExportOptionsUnion
from openapi_server.models.vcd_vapp_detail import VcdVappDetail
from openapi_server.models.vcd_vapp_patch import VcdVappPatch
from openapi_server.models.vcd_vapp_snapshot_detail import VcdVappSnapshotDetail
from openapi_server.models.vcd_vapp_snapshot_summary_list_response import VcdVappSnapshotSummaryListResponse
from openapi_server.models.vcd_vapp_summary_list_response import VcdVappSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_create_on_demand_snapshot_v1(client):
    """Test case for create_on_demand_snapshot_v1

    Create an on-demand snapshot for a vApp
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
        path='/api/v1/vcd/vapp/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_vapp_export_v1(client):
    """Test case for create_vapp_export_v1

    Export vApp snapshot
    """
    body = {"exportMode":"ExportToNewVapp","shouldPowerOnVappAfterExport":False,"networksToRestore":[{"newName":"newName","isDeployed":True,"parentNetworkId":"parentNetworkId","name":"name"},{"newName":"newName","isDeployed":True,"parentNetworkId":"parentNetworkId","name":"name"}],"newVappParams":{"name":"name","orgVdcId":"orgVdcId"},"vmsToExport":[{"vcdMoid":"vcdMoid","networkConnections":[{"macAddress":"macAddress","addressingMode":"DHCP","networkAdapterType":"networkAdapterType","ipAddress":"ipAddress","isConnected":True,"vappNetworkName":"vappNetworkName","nicIndex":5},{"macAddress":"macAddress","addressingMode":"DHCP","networkAdapterType":"networkAdapterType","ipAddress":"ipAddress","isConnected":True,"vappNetworkName":"vappNetworkName","nicIndex":5}],"name":"name","storagePolicyId":"storagePolicyId"},{"vcdMoid":"vcdMoid","networkConnections":[{"macAddress":"macAddress","addressingMode":"DHCP","networkAdapterType":"networkAdapterType","ipAddress":"ipAddress","isConnected":True,"vappNetworkName":"vappNetworkName","nicIndex":5},{"macAddress":"macAddress","addressingMode":"DHCP","networkAdapterType":"networkAdapterType","ipAddress":"ipAddress","isConnected":True,"vappNetworkName":"vappNetworkName","nicIndex":5}],"name":"name","storagePolicyId":"storagePolicyId"}],"targetVappId":"targetVappId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vcd/vapp/snapshot/{snapshot_id}/export'.format(snapshot_id='snapshot_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_vapp_instant_recovery_v1(client):
    """Test case for create_vapp_instant_recovery_v1

    Instant Recovery of vApp virtual machines
    """
    body = {"shouldPowerOnVmsAfterRecovery":False,"vmsToRestore":[{"vcdMoid":"vcdMoid","networkConnections":[{"macAddress":"macAddress","addressingMode":"DHCP","networkAdapterType":"networkAdapterType","ipAddress":"ipAddress","isConnected":True,"vappNetworkName":"vappNetworkName","nicIndex":5},{"macAddress":"macAddress","addressingMode":"DHCP","networkAdapterType":"networkAdapterType","ipAddress":"ipAddress","isConnected":True,"vappNetworkName":"vappNetworkName","nicIndex":5}],"name":"name","storagePolicyId":"storagePolicyId"},{"vcdMoid":"vcdMoid","networkConnections":[{"macAddress":"macAddress","addressingMode":"DHCP","networkAdapterType":"networkAdapterType","ipAddress":"ipAddress","isConnected":True,"vappNetworkName":"vappNetworkName","nicIndex":5},{"macAddress":"macAddress","addressingMode":"DHCP","networkAdapterType":"networkAdapterType","ipAddress":"ipAddress","isConnected":True,"vappNetworkName":"vappNetworkName","nicIndex":5}],"name":"name","storagePolicyId":"storagePolicyId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vcd/vapp/snapshot/{snapshot_id}/instant_recover'.format(snapshot_id='snapshot_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_vapp_template_snapshot_export(client):
    """Test case for create_vapp_template_snapshot_export

    Export of a vApp template snapshot
    """
    body = {"catalogId":"catalogId","name":"name","orgVdcId":"orgVdcId","storagePolicyId":"storagePolicyId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vcd/vapp/template/snapshot/{snapshot_id}/export'.format(snapshot_id='snapshot_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_vcd_vapp_download_snapshot_from_cloud_v1(client):
    """Test case for create_vcd_vapp_download_snapshot_from_cloud_v1

    Download snapshot from archive
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vcd/vapp/snapshot/{id}/download'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vapp_snapshot_v1(client):
    """Test case for delete_vapp_snapshot_v1

    Delete a vApp snapshot
    """
    params = [('location', 'location_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/vcd/vapp/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vapp_snapshots_v1(client):
    """Test case for delete_vapp_snapshots_v1

    Delete all snapshots of vApp
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/vcd/vapp/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vapp_async_request_status_v1(client):
    """Test case for get_vapp_async_request_status_v1

    Get vApp job status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/vapp/request/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vapp_snapshot_export_options_v1(client):
    """Test case for get_vapp_snapshot_export_options_v1

    Get exportable network configurations
    """
    params = [('export_mode', 'export_mode_example'),
                    ('target_vapp_id', 'target_vapp_id_example'),
                    ('target_org_vdc_id', 'target_org_vdc_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/vapp/snapshot/{snapshot_id}/export/options'.format(snapshot_id='snapshot_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vapp_snapshot_instant_recovery_options_v1(client):
    """Test case for get_vapp_snapshot_instant_recovery_options_v1

    Get Instant Recovery information
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/vapp/snapshot/{snapshot_id}/instant_recover/options'.format(snapshot_id='snapshot_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vapp_snapshot_v1(client):
    """Test case for get_vapp_snapshot_v1

    Get vApp snapshot details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/vapp/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vapp_template_snapshot_export_options(client):
    """Test case for get_vapp_template_snapshot_export_options

    Get Export information for a vApp template snapshot
    """
    params = [('catalog_id', 'catalog_id_example'),
                    ('name', 'name_example'),
                    ('org_vdc_id', 'org_vdc_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/vapp/template/snapshot/{snapshot_id}/export/options'.format(snapshot_id='snapshot_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vcd_vapp_v1(client):
    """Test case for get_vcd_vapp_v1

    Get details of a specific vApp
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/vapp/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_vapp_snapshot_v1(client):
    """Test case for query_vapp_snapshot_v1

    Get list of snapshots of vApp
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/vapp/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_vcd_vapps_v1(client):
    """Test case for query_vcd_vapps_v1

    Get summary for vApps
    """
    params = [('sort_by', 'sort_by_example'),
                    ('sort_order', asc),
                    ('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example'),
                    ('is_relic', True),
                    ('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('include_backup_task_info', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/vapp',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_vapp_v1(client):
    """Test case for search_vapp_v1

    Search for a file in a vApp
    """
    params = [('path', 'path_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/vapp/{id}/search'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_vcd_vapp_v1(client):
    """Test case for update_vcd_vapp_v1

    Update vApp
    """
    body = {"isPaused":True,"vcdVmMoidsToExcludeFromSnapshot":["vcdVmMoidsToExcludeFromSnapshot","vcdVmMoidsToExcludeFromSnapshot"],"configuredSlaDomainId":"configuredSlaDomainId","isBestEffortSynchronizationEnabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/vcd/vapp/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vcd_missed_snapshots_v1(client):
    """Test case for vcd_missed_snapshots_v1

    Get details about missed snapshots for a vApp
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vcd/vapp/{id}/missed_snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

