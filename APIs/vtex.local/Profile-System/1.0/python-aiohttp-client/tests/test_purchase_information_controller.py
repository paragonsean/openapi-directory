# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_create_purchase_information(client):
    """Test case for create_purchase_information

    Create purchase information
    """
    body = None
    params = [('alternativeKey', 'email')]
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
        path='/api/storage/profile-system/profiles/{profile_id}/purchase-info'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_purchase_information(client):
    """Test case for delete_purchase_information

    Delete purchase information
    """
    params = [('alternativeKey', 'email')]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/storage/profile-system/profiles/{profile_id}/purchase-info'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_purchase_information(client):
    """Test case for get_purchase_information

    Get purchase information
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
        path='/api/storage/profile-system/profiles/{profile_id}/purchase-info'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_unmasked_purchase_information(client):
    """Test case for get_unmasked_purchase_information

    Get unmasked purchase information
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
        path='/api/storage/profile-system/profiles/{profile_id}/purchase-info/unmask'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_purchase_information(client):
    """Test case for update_purchase_information

    Update purchase information
    """
    body = None
    params = [('alternativeKey', 'email')]
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
        path='/api/storage/profile-system/profiles/{profile_id}/purchase-info'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

