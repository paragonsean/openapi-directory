# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_delete_global_attribute(client):
    """Test case for delete_global_attribute

    Delete specific global attribute
    """
    headers = { 
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/attributes/{attributekey}'.format(attributekey='attributekey_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_global_attributes(client):
    """Test case for delete_global_attributes

    Delete all global attributes
    """
    headers = { 
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/attributes/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_server_privileged_attribute(client):
    """Test case for delete_server_privileged_attribute

    Delete specific privileged attribute of a specific server
    """
    headers = { 
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/servers/{serverid}/privilegedattributes/{attributekey}'.format(serverid='serverid_example', attributekey='attributekey_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_server_privileged_attributes(client):
    """Test case for delete_server_privileged_attributes

    Delete all privileged attributes of a specific server
    """
    headers = { 
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/servers/{serverid}/privilegedattributes'.format(serverid='serverid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_global_attributes(client):
    """Test case for get_global_attributes

    Get all global attributes
    """
    headers = { 
        'Accept': 'text/plain',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/attributes/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_server_privileged_attributes(client):
    """Test case for get_server_privileged_attributes

    Get all privileged attributes of a specific server
    """
    headers = { 
        'Accept': 'text/plain',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/privilegedattributes'.format(serverid='serverid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_set_global_attributes(client):
    """Test case for set_global_attributes

    Set all global attributes
    """
    attributes = None
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/attributes/',
        headers=headers,
        json=attributes,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_set_server_privileged_attributes(client):
    """Test case for set_server_privileged_attributes

    Set all privileged attributes of a specific server
    """
    attributes = None
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/privilegedattributes'.format(serverid='serverid_example'),
        headers=headers,
        json=attributes,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_global_attributes(client):
    """Test case for update_global_attributes

    Update specified global attributes
    """
    attributes = None
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/attributes/',
        headers=headers,
        json=attributes,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_server_privileged_attributes(client):
    """Test case for update_server_privileged_attributes

    Update privileged specified attributes of a specific server
    """
    attributes = None
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/servers/{serverid}/privilegedattributes'.format(serverid='serverid_example'),
        headers=headers,
        json=attributes,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

