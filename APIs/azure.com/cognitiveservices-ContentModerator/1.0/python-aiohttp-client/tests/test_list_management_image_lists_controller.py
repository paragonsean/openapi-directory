# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.image_list import ImageList
from openapi_server.models.list_management_image_lists_create_request import ListManagementImageListsCreateRequest
from openapi_server.models.refresh_index import RefreshIndex


pytestmark = pytest.mark.asyncio

async def test_list_management_image_lists_create(client):
    """Test case for list_management_image_lists_create

    
    """
    body = openapi_server.ListManagementImageListsCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/lists/v1.0/imagelists',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_management_image_lists_delete(client):
    """Test case for list_management_image_lists_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/contentmoderator/lists/v1.0/imagelists/{list_id}'.format(list_id='list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_management_image_lists_get_all_image_lists(client):
    """Test case for list_management_image_lists_get_all_image_lists

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/contentmoderator/lists/v1.0/imagelists',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_management_image_lists_get_details(client):
    """Test case for list_management_image_lists_get_details

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/contentmoderator/lists/v1.0/imagelists/{list_id}'.format(list_id='list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_management_image_lists_refresh_index(client):
    """Test case for list_management_image_lists_refresh_index

    
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/contentmoderator/lists/v1.0/imagelists/{list_id}/RefreshIndex'.format(list_id='list_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_management_image_lists_update(client):
    """Test case for list_management_image_lists_update

    
    """
    body = openapi_server.ListManagementImageListsCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/contentmoderator/lists/v1.0/imagelists/{list_id}'.format(list_id='list_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

