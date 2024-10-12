# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.gallery_image import GalleryImage
from openapi_server.models.gallery_image_list import GalleryImageList
from openapi_server.models.gallery_image_update import GalleryImageUpdate


pytestmark = pytest.mark.asyncio

async def test_gallery_images_create_or_update(client):
    """Test case for gallery_images_create_or_update

    
    """
    gallery_image = {"properties":{"identifier":{"offer":"offer","publisher":"publisher","sku":"sku"},"description":"description","hyperVGeneration":"V1","eula":"eula","provisioningState":"Creating","disallowed":{"diskTypes":["diskTypes","diskTypes"]},"endOfLifeDate":"2000-01-23T04:56:07.000+00:00","privacyStatementUri":"privacyStatementUri","recommended":{"memory":{"min":6,"max":0},"vCPUs":{"min":6,"max":0}},"osState":"Generalized","osType":"Windows","purchasePlan":{"product":"product","name":"name","publisher":"publisher"},"releaseNoteUri":"releaseNoteUri"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/images/{gallery_image_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example', gallery_image_name='gallery_image_name_example'),
        headers=headers,
        json=gallery_image,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_images_delete(client):
    """Test case for gallery_images_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/images/{gallery_image_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example', gallery_image_name='gallery_image_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_images_get(client):
    """Test case for gallery_images_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/images/{gallery_image_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example', gallery_image_name='gallery_image_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_images_list_by_gallery(client):
    """Test case for gallery_images_list_by_gallery

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/images'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_images_update(client):
    """Test case for gallery_images_update

    
    """
    gallery_image = {"properties":{"identifier":{"offer":"offer","publisher":"publisher","sku":"sku"},"description":"description","hyperVGeneration":"V1","eula":"eula","provisioningState":"Creating","disallowed":{"diskTypes":["diskTypes","diskTypes"]},"endOfLifeDate":"2000-01-23T04:56:07.000+00:00","privacyStatementUri":"privacyStatementUri","recommended":{"memory":{"min":6,"max":0},"vCPUs":{"min":6,"max":0}},"osState":"Generalized","osType":"Windows","purchasePlan":{"product":"product","name":"name","publisher":"publisher"},"releaseNoteUri":"releaseNoteUri"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/images/{gallery_image_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example', gallery_image_name='gallery_image_name_example'),
        headers=headers,
        json=gallery_image,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

