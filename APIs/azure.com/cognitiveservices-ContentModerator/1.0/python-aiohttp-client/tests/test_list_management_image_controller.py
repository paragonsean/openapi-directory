# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.image import Image
from openapi_server.models.image_ids import ImageIds


pytestmark = pytest.mark.asyncio

async def test_list_management_image_add_image(client):
    """Test case for list_management_image_add_image

    
    """
    params = [('tag', 56),
                    ('label', 'label_example')]
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/lists/v1.0/imagelists/{list_id}/images'.format(list_id='list_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_management_image_delete_all_images(client):
    """Test case for list_management_image_delete_all_images

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/contentmoderator/lists/v1.0/imagelists/{list_id}/images'.format(list_id='list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_management_image_delete_image(client):
    """Test case for list_management_image_delete_image

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/contentmoderator/lists/v1.0/imagelists/{list_id}/images/{image_id}'.format(list_id='list_id_example', image_id='image_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_management_image_get_all_image_ids(client):
    """Test case for list_management_image_get_all_image_ids

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/contentmoderator/lists/v1.0/imagelists/{list_id}/images'.format(list_id='list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

