# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attach_disk_properties import AttachDiskProperties
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.detach_disk_properties import DetachDiskProperties
from openapi_server.models.disk import Disk
from openapi_server.models.disk_fragment import DiskFragment
from openapi_server.models.disk_list import DiskList


pytestmark = pytest.mark.asyncio

async def test_disks_attach(client):
    """Test case for disks_attach

    
    """
    attach_disk_properties = {"leasedByLabVmId":"leasedByLabVmId"}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/disks/{name}/attach'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        json=attach_disk_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_create_or_update(client):
    """Test case for disks_create_or_update

    
    """
    disk = {"properties":{"managedDiskId":"managedDiskId","leasedByLabVmId":"leasedByLabVmId","createdDate":"2000-01-23T04:56:07.000+00:00","hostCaching":"hostCaching","diskBlobName":"diskBlobName","diskSizeGiB":0,"diskType":"Standard","provisioningState":"provisioningState","diskUri":"diskUri","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/disks/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        json=disk,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_delete(client):
    """Test case for disks_delete

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/disks/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_detach(client):
    """Test case for disks_detach

    
    """
    detach_disk_properties = {"leasedByLabVmId":"leasedByLabVmId"}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/disks/{name}/detach'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        json=detach_disk_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_get(client):
    """Test case for disks_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/disks/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_list(client):
    """Test case for disks_list

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/disks'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disks_update(client):
    """Test case for disks_update

    
    """
    disk = {"properties":{"managedDiskId":"managedDiskId","leasedByLabVmId":"leasedByLabVmId","hostCaching":"hostCaching","diskBlobName":"diskBlobName","diskSizeGiB":0,"diskType":"Standard","diskUri":"diskUri"}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/disks/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        json=disk,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

