# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address import Address
from openapi_server.models.update_client_address_request import UpdateClientAddressRequest


pytestmark = pytest.mark.asyncio

async def test_create_client_address(client):
    """Test case for create_client_address

    Create client address
    """
    body = openapi_server.Address()
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
        path='/api/storage/profile-system/profiles/{profile_id}/addresses'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_address(client):
    """Test case for delete_address

    Delete address
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
        path='/api/storage/profile-system/profiles/{profile_id}/addresses/{address_id}'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771', address_id='bf82180e-cf9e-4089-9af6-ae1518555992'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_address(client):
    """Test case for get_address

    Get address
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
        path='/api/storage/profile-system/profiles/{profile_id}/addresses/{address_id}'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771', address_id='bf82180e-cf9e-4089-9af6-ae1518555992'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_address_by_version(client):
    """Test case for get_address_by_version

    Get address by version
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
        path='/api/storage/profile-system/profiles/{profile_id}/addresses/{address_id}/versions/{address_version_id}'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771', address_id='bf82180e-cf9e-4089-9af6-ae1518555992', address_version_id='86dfae79-1d23-43f2-a643-2fc8f1839461'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_client_addresses(client):
    """Test case for get_client_addresses

    Get client addresses
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
        path='/api/storage/profile-system/profiles/{profile_id}/addresses'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_unmasked_address(client):
    """Test case for get_unmasked_address

    Get unmasked address
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
        path='/api/storage/profile-system/profiles/{profile_id}/addresses/{address_id}/unmask'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771', address_id='bf82180e-cf9e-4089-9af6-ae1518555992'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_unmasked_address_by_version(client):
    """Test case for get_unmasked_address_by_version

    Get unmasked address by version
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
        path='/api/storage/profile-system/profiles/{profile_id}/addresses/{address_id}/versions/{address_version_id}/unmask'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771', address_id='bf82180e-cf9e-4089-9af6-ae1518555992', address_version_id='86dfae79-1d23-43f2-a643-2fc8f1839461'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_unmasked_client_addresses(client):
    """Test case for get_unmasked_client_addresses

    Get unmasked client addresses
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
        path='/api/storage/profile-system/profiles/{profile_id}/addresses/unmask'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_client_address(client):
    """Test case for update_client_address

    Update client address
    """
    body = openapi_server.UpdateClientAddressRequest()
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
        path='/api/storage/profile-system/profiles/{profile_id}/addresses/{address_id}'.format(profile_id='70caf394-8534-447e-a0ca-1803c669c771', address_id='bf82180e-cf9e-4089-9af6-ae1518555992'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

