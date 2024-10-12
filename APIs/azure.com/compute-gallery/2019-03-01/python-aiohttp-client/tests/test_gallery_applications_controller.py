# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.gallery_application import GalleryApplication
from openapi_server.models.gallery_application_list import GalleryApplicationList


pytestmark = pytest.mark.asyncio

async def test_gallery_applications_create_or_update(client):
    """Test case for gallery_applications_create_or_update

    
    """
    gallery_application = {"properties":{"releaseNoteUri":"releaseNoteUri","description":"description","eula":"eula","supportedOSType":"Windows","endOfLifeDate":"2000-01-23T04:56:07.000+00:00","privacyStatementUri":"privacyStatementUri"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/applications/{gallery_application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example', gallery_application_name='gallery_application_name_example'),
        headers=headers,
        json=gallery_application,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_applications_delete(client):
    """Test case for gallery_applications_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/applications/{gallery_application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example', gallery_application_name='gallery_application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_applications_get(client):
    """Test case for gallery_applications_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/applications/{gallery_application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example', gallery_application_name='gallery_application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_applications_list_by_gallery(client):
    """Test case for gallery_applications_list_by_gallery

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/galleries/{gallery_name}/applications'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gallery_name='gallery_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

