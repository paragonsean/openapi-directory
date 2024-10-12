# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.get_profile_about_response import GetProfileAboutResponse
from openapi_server.models.get_profile_photo_response import GetProfilePhotoResponse
from openapi_server.models.profile_about import ProfileAbout


pytestmark = pytest.mark.asyncio

async def test_get_profile_about(client):
    """Test case for get_profile_about

    Get-Profile-About
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/settings/profile/about',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile_photo(client):
    """Test case for get_profile_photo

    Get-Profile-Photo
    """
    params = [('format', 'link')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/settings/profile/photo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_profile_about(client):
    """Test case for update_profile_about

    Update-Profile-About
    """
    body = {"text":"<About Profile>"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/settings/profile/about',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_update_profile_photo(client):
    """Test case for update_profile_photo

    Update-Profile-Photo
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/settings/profile/photo',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

