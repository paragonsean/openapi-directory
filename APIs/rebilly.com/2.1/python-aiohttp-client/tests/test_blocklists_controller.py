# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.blocklist import Blocklist
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError


pytestmark = pytest.mark.asyncio

async def test_delete_blocklist(client):
    """Test case for delete_blocklist

    Delete a blocklist
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/blocklists/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_blocklist(client):
    """Test case for get_blocklist

    Retrieve a blocklist
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/blocklists/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_blocklist_collection(client):
    """Test case for get_blocklist_collection

    Retrieve a list of blocklists
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('sort', ['sort_example']),
                    ('filter', 'filter_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/blocklists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_blocklist(client):
    """Test case for post_blocklist

    Create a blocklist
    """
    body = {"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"expirationTime":"2000-01-23T04:56:07.000+00:00","createdTime":"","id":"","type":"payment-card","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/blocklists',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_blocklist(client):
    """Test case for put_blocklist

    Create a blocklist with predefined ID
    """
    body = {"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"expirationTime":"2000-01-23T04:56:07.000+00:00","createdTime":"","id":"","type":"payment-card","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/blocklists/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

