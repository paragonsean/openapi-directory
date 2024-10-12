# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.snapshot import Snapshot
from openapi_server.models.snapshot_patch import SnapshotPatch
from openapi_server.models.snapshots_list import SnapshotsList


pytestmark = pytest.mark.asyncio

async def test_snapshots_create(client):
    """Test case for snapshots_create

    Create a snapshot
    """
    body = openapi_server.Snapshot()
    params = [('api-version', '2019-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}/volumes/{volume_name}/snapshots/{snapshot_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example', volume_name='volume_name_example', snapshot_name='snapshot_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshots_delete(client):
    """Test case for snapshots_delete

    Delete a snapshot
    """
    params = [('api-version', '2019-06-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}/volumes/{volume_name}/snapshots/{snapshot_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example', volume_name='volume_name_example', snapshot_name='snapshot_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshots_get(client):
    """Test case for snapshots_get

    Describe a snapshot
    """
    params = [('api-version', '2019-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}/volumes/{volume_name}/snapshots/{snapshot_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example', volume_name='volume_name_example', snapshot_name='snapshot_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshots_list(client):
    """Test case for snapshots_list

    Describe all snapshots
    """
    params = [('api-version', '2019-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}/volumes/{volume_name}/snapshots'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example', volume_name='volume_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshots_update(client):
    """Test case for snapshots_update

    Update a snapshot
    """
    body = openapi_server.SnapshotPatch()
    params = [('api-version', '2019-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.NetApp/netAppAccounts/{account_name}/capacityPools/{pool_name}/volumes/{volume_name}/snapshots/{snapshot_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', account_name='account_name_example', pool_name='pool_name_example', volume_name='volume_name_example', snapshot_name='snapshot_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

