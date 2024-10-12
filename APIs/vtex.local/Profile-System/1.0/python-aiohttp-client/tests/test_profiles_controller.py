# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.profile import Profile
from openapi_server.models.update_client_profile_request import UpdateClientProfileRequest


pytestmark = pytest.mark.asyncio

async def test_create_client_profile(client):
    """Test case for create_client_profile

    Create client profile
    """
    body = openapi_server.Profile()
    params = [('ttl', 365)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/storage/profile-system/profiles',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_client_profile(client):
    """Test case for delete_client_profile

    Delete client profile
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/storage/profile-system/profiles/{profile_id}'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile(client):
    """Test case for get_profile

    Get profile
    """
    params = [('alternativeKey', 'email')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/storage/profile-system/profiles/{profile_id}'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile_by_version(client):
    """Test case for get_profile_by_version

    Get profile by version
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/storage/profile-system/profiles/{profile_id}/versions/{profile_version_id}'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771', profile_version_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_unmasked_profile(client):
    """Test case for get_unmasked_profile

    Get unmasked profile
    """
    params = [('reason', 'data-validation'),
                    ('alternativeKey', 'email')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/storage/profile-system/profiles/{profile_id}/unmask'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_unmasked_profile_by_version(client):
    """Test case for get_unmasked_profile_by_version

    Get unmasked profile by version
    """
    params = [('reason', 'data-validation')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/storage/profile-system/profiles/{profile_id}/versions/{profile_version_id}/unmask'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771', profile_version_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_client_profile(client):
    """Test case for update_client_profile

    Updates client profile
    """
    body = openapi_server.UpdateClientProfileRequest()
    params = [('alternativeKey', 'email'),
                    ('ttl', 365)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/storage/profile-system/profiles/{profile_id}'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

