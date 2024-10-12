# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_uri import AccessUri
from openapi_server.models.disk import Disk
from openapi_server.models.disk_list import DiskList
from openapi_server.models.disk_update import DiskUpdate
from openapi_server.models.grant_access_data import GrantAccessData
from openapi_server.models.operation_status_response import OperationStatusResponse


pytestmark = pytest.mark.asyncio

async def test_disks_create_or_update(client):
    """Test case for disks_create_or_update

    
    """
    disk = {"properties":{"accountType":"Standard_LRS","creationData":{"storageAccountId":"storageAccountId","sourceUri":"sourceUri","imageReference":{"lun":0,"id":"id"},"createOption":"Empty","sourceResourceId":"sourceResourceId"},"osType":"Windows","timeCreated":"2000-01-23T04:56:07.000+00:00","provisioningState":"provisioningState","ownerId":"ownerId","diskSizeGB":6,"encryptionSettings":{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/disks/{disk_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', disk_name='disk_name_example'),
        headers=headers,
        json=disk,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_delete(client):
    """Test case for disks_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/disks/{disk_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', disk_name='disk_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_get(client):
    """Test case for disks_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/disks/{disk_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', disk_name='disk_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_grant_access(client):
    """Test case for disks_grant_access

    
    """
    grant_access_data = {"access":"None","durationInSeconds":0}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/disks/{disk_name}/beginGetAccess'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', disk_name='disk_name_example'),
        headers=headers,
        json=grant_access_data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_list(client):
    """Test case for disks_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/disks'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_list_by_resource_group(client):
    """Test case for disks_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/disks'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_revoke_access(client):
    """Test case for disks_revoke_access

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/disks/{disk_name}/endGetAccess'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', disk_name='disk_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_update(client):
    """Test case for disks_update

    
    """
    disk = {"properties":{"accountType":"Standard_LRS","creationData":{"storageAccountId":"storageAccountId","sourceUri":"sourceUri","imageReference":{"lun":0,"id":"id"},"createOption":"Empty","sourceResourceId":"sourceResourceId"},"osType":"Windows","diskSizeGB":0,"encryptionSettings":{"diskEncryptionKey":{"secretUrl":"secretUrl","sourceVault":{"id":"id"}},"enabled":True,"keyEncryptionKey":{"sourceVault":{"id":"id"},"keyUrl":"keyUrl"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/disks/{disk_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', disk_name='disk_name_example'),
        headers=headers,
        json=disk,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

