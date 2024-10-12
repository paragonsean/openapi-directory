# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_uri import AccessUri
from openapi_server.models.grant_access_data import GrantAccessData
from openapi_server.models.operation_status_response import OperationStatusResponse
from openapi_server.models.snapshot import Snapshot
from openapi_server.models.snapshot_list import SnapshotList
from openapi_server.models.snapshot_update import SnapshotUpdate


pytestmark = pytest.mark.asyncio

async def test_snapshots_create_or_update(client):
    """Test case for snapshots_create_or_update

    
    """
    snapshot = {"managedBy":"managedBy","sku":{"tier":"Standard","name":"Standard_LRS"},"properties":{"creationData":{"storageAccountId":"storageAccountId","sourceUri":"sourceUri","imageReference":{"lun":0,"id":"id"},"createOption":"Empty","sourceResourceId":"sourceResourceId"},"osType":"Windows","timeCreated":"2000-01-23T04:56:07.000+00:00","provisioningState":"provisioningState","diskSizeGB":6,"encryptionSettings":{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/snapshots/{snapshot_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', snapshot_name='snapshot_name_example'),
        headers=headers,
        json=snapshot,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshots_delete(client):
    """Test case for snapshots_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/snapshots/{snapshot_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', snapshot_name='snapshot_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshots_get(client):
    """Test case for snapshots_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/snapshots/{snapshot_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', snapshot_name='snapshot_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshots_grant_access(client):
    """Test case for snapshots_grant_access

    
    """
    grant_access_data = {"access":"None","durationInSeconds":0}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/snapshots/{snapshot_name}/beginGetAccess'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', snapshot_name='snapshot_name_example'),
        headers=headers,
        json=grant_access_data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshots_list(client):
    """Test case for snapshots_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/snapshots'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshots_list_by_resource_group(client):
    """Test case for snapshots_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/snapshots'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshots_revoke_access(client):
    """Test case for snapshots_revoke_access

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/snapshots/{snapshot_name}/endGetAccess'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', snapshot_name='snapshot_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_snapshots_update(client):
    """Test case for snapshots_update

    
    """
    snapshot = {"properties":{"osType":"Windows","diskSizeGB":0,"encryptionSettings":{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/snapshots/{snapshot_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', snapshot_name='snapshot_name_example'),
        headers=headers,
        json=snapshot,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

