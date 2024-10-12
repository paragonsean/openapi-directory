# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.gallery_image_version import GalleryImageVersion
from openapi_server.models.gallery_image_version_list import GalleryImageVersionList


pytestmark = pytest.mark.asyncio

async def test_gallery_image_versions_create_or_update(client):
    """Test case for gallery_image_versions_create_or_update

    
    """
    gallery_image_version = {"properties":{"publishingProfile":{"source":{"managedImage":{"id":"id"}}},"storageProfile":{"osDiskImage":{"hostCaching":"None","sizeInGB":6},"dataDiskImages":[{"lun":0},{"lun":0}]},"replicationStatus":{"summary":[{"progress":0,"details":"details","state":"Unknown","region":"region"},{"progress":0,"details":"details","state":"Unknown","region":"region"}],"aggregatedState":"Unknown"},"provisioningState":"Creating"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/images/{gallery_image_name}/versions/{gallery_image_version_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example', gallery_image_name='gallery_image_name_example', gallery_image_version_name='gallery_image_version_name_example'),
        headers=headers,
        json=gallery_image_version,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_image_versions_delete(client):
    """Test case for gallery_image_versions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/images/{gallery_image_name}/versions/{gallery_image_version_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example', gallery_image_name='gallery_image_name_example', gallery_image_version_name='gallery_image_version_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_image_versions_get(client):
    """Test case for gallery_image_versions_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/images/{gallery_image_name}/versions/{gallery_image_version_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example', gallery_image_name='gallery_image_name_example', gallery_image_version_name='gallery_image_version_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_image_versions_list_by_gallery_image(client):
    """Test case for gallery_image_versions_list_by_gallery_image

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/images/{gallery_image_name}/versions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example', gallery_image_name='gallery_image_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

