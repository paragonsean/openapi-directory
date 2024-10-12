# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.custom_image import CustomImage
from openapi_server.models.custom_image_fragment import CustomImageFragment
from openapi_server.models.custom_image_list import CustomImageList


pytestmark = pytest.mark.asyncio

async def test_custom_images_create_or_update(client):
    """Test case for custom_images_create_or_update

    
    """
    custom_image = {"properties":{"isPlanAuthorized":True,"vhd":{"imageName":"imageName","osType":"Windows","sysPrep":True},"managedSnapshotId":"managedSnapshotId","author":"author","managedImageId":"managedImageId","vm":{"windowsOsInfo":{"windowsOsState":"NonSysprepped"},"linuxOsInfo":{"linuxOsState":"NonDeprovisioned"},"sourceVmId":"sourceVmId"},"description":"description","customImagePlan":{"offer":"offer","publisher":"publisher","id":"id"},"provisioningState":"provisioningState","creationDate":"2000-01-23T04:56:07.000+00:00","dataDiskStorageInfo":[{"lun":"lun","storageType":"Standard"},{"lun":"lun","storageType":"Standard"}],"uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/customimages/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=custom_image,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_images_delete(client):
    """Test case for custom_images_delete

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/customimages/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_images_get(client):
    """Test case for custom_images_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/customimages/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_images_list(client):
    """Test case for custom_images_list

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/customimages'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_images_update(client):
    """Test case for custom_images_update

    
    """
    custom_image = {"properties":{"isPlanAuthorized":True,"vhd":{"imageName":"imageName","osType":"Windows","sysPrep":True},"managedSnapshotId":"managedSnapshotId","author":"author","managedImageId":"managedImageId","vm":{"windowsOsInfo":{"windowsOsState":"NonSysprepped"},"linuxOsInfo":{"linuxOsState":"NonDeprovisioned"},"sourceVmId":"sourceVmId"},"description":"description","customImagePlan":{"offer":"offer","publisher":"publisher","id":"id"},"dataDiskStorageInfo":[{"lun":"lun","storageType":"Standard"},{"lun":"lun","storageType":"Standard"}]}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/customimages/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=custom_image,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

