# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_show_public_keys(client):
    """Test case for show_public_keys

    Shows all public keys for a resource.
    """
    headers = { 
        'Accept': 'text/plain',
        'x_request_id': 'test-id',
        'Authorization': 'BasicZm9vOmJhcg==',
        
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/public_keys/{account}/{kind}/{identifier}'.format(account='account_example', kind='user', identifier='admin'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

