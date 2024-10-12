# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.gallery_image import GalleryImage
from openapi_server.models.gallery_image_fragment import GalleryImageFragment
from openapi_server.models.response_with_continuation_gallery_image import ResponseWithContinuationGalleryImage


pytestmark = pytest.mark.asyncio

async def test_gallery_images_create_or_update(client):
    """Test case for gallery_images_create_or_update

    
    """
    gallery_image = {"properties":{"createdDate":"2000-01-23T04:56:07.000+00:00","isPlanAuthorized":True,"author":"author","isEnabled":True,"icon":"icon","isOverride":True,"description":"description","planId":"planId","provisioningState":"provisioningState","imageReference":{"offer":"offer","osType":"osType","publisher":"publisher","sku":"sku","version":"version"},"latestOperationResult":{"operationUrl":"operationUrl","errorMessage":"errorMessage","errorCode":"errorCode","requestUri":"requestUri","httpMethod":"httpMethod","status":"status"},"uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/galleryimages/{gallery_image_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', gallery_image_name='gallery_image_name_example'),
        headers=headers,
        json=gallery_image,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_images_delete(client):
    """Test case for gallery_images_delete

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/galleryimages/{gallery_image_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', gallery_image_name='gallery_image_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_images_get(client):
    """Test case for gallery_images_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/galleryimages/{gallery_image_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', gallery_image_name='gallery_image_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_images_list(client):
    """Test case for gallery_images_list

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/galleryimages'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_images_update(client):
    """Test case for gallery_images_update

    
    """
    gallery_image = {"properties":{"isPlanAuthorized":True,"isEnabled":True,"isOverride":True,"provisioningState":"provisioningState","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/galleryimages/{gallery_image_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', gallery_image_name='gallery_image_name_example'),
        headers=headers,
        json=gallery_image,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

