# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.volume_group_detail import VolumeGroupDetail
from openapi_server.models.volume_group_force_full_request import VolumeGroupForceFullRequest
from openapi_server.models.volume_group_force_full_response import VolumeGroupForceFullResponse
from openapi_server.models.volume_group_mount_summary import VolumeGroupMountSummary
from openapi_server.models.volume_group_mount_summary_list_response import VolumeGroupMountSummaryListResponse
from openapi_server.models.volume_group_on_demand_snapshot_config import VolumeGroupOnDemandSnapshotConfig
from openapi_server.models.volume_group_patch import VolumeGroupPatch
from openapi_server.models.volume_group_snapshot_detail import VolumeGroupSnapshotDetail
from openapi_server.models.volume_group_snapshot_summary import VolumeGroupSnapshotSummary
from openapi_server.models.volume_group_snapshot_summary_list_response import VolumeGroupSnapshotSummaryListResponse
from openapi_server.models.volume_group_summary_list_response import VolumeGroupSummaryListResponse


pytestmark = pytest.mark.asyncio

async def test_create_on_demand_volume_group_backup(client):
    """Test case for create_on_demand_volume_group_backup

    Create on-demand snapshot for the Volume Group
    """
    body = {"slaId":"slaId","volumeIdsIncludedInSnapshot":["volumeIdsIncludedInSnapshot","volumeIdsIncludedInSnapshot"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/volume_group/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_volume_group(client):
    """Test case for get_volume_group

    Get Volume Group details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/volume_group/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_volume_group_force_full_spec(client):
    """Test case for get_volume_group_force_full_spec

    Retrieve the configuration for forcing a full snapshot
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/volume_group/{id}/request/force_full_snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_volume_group_snapshot(client):
    """Test case for get_volume_group_snapshot

    Get Volume Group snapshot details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/volume_group/snapshot/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_volume_group_snapshot_mount(client):
    """Test case for get_volume_group_snapshot_mount

    Get summary information for a mount
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/volume_group/snapshot/mount/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_volume_group(client):
    """Test case for patch_volume_group

    Update Volume Group properties
    """
    body = {"isPaused":True,"forceFull":True,"volumeIdsIncludedInSnapshots":["volumeIdsIncludedInSnapshots","volumeIdsIncludedInSnapshots"],"configuredSlaDomainId":"configuredSlaDomainId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/volume_group/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_volume_group(client):
    """Test case for query_volume_group

    Get list of Volume Groups
    """
    params = [('effective_sla_domain_id', 'effective_sla_domain_id_example'),
                    ('primary_cluster_id', 'primary_cluster_id_example'),
                    ('limit', 56),
                    ('offset', 56),
                    ('is_relic', True),
                    ('name', 'name_example'),
                    ('sla_assignment', 'sla_assignment_example'),
                    ('sort_by', name),
                    ('sort_order', asc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/volume_group',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_volume_group_latest_snapshot(client):
    """Test case for query_volume_group_latest_snapshot

    Get the latest snapshot of the Volume Group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/volume_group/{id}/latest_snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_volume_group_snapshot(client):
    """Test case for query_volume_group_snapshot

    Get list of snapshots of the Volume Group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/volume_group/{id}/snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_volume_group_snapshot_mount(client):
    """Test case for query_volume_group_snapshot_mount

    Get summary information for all mounts
    """
    params = [('source_volume_group_id', 'source_volume_group_id_example'),
                    ('source_host_name', 'source_host_name_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', asc),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/volume_group/snapshot/mount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_volume_group_force_full_snapshot(client):
    """Test case for request_volume_group_force_full_snapshot

    Request a full snapshot on the next backup job of a Volume Group
    """
    body = {"volumeInfos":[{"shouldDedupe":True,"volumeId":"volumeId"},{"shouldDedupe":True,"volumeId":"volumeId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/volume_group/{id}/request/force_full_snapshot'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

