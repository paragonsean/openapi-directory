# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_prefix_collection(client):
    """Test case for get_prefix_collection

    Returns list of prefixes
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/identifier/prefixes/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_prefix_contract(client):
    """Test case for get_prefix_contract

    Returns contracted URI
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/identifier/prefixes/contract/{uri}'.format(uri='uri_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_prefix_expand(client):
    """Test case for get_prefix_expand

    Returns expanded URI
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/identifier/prefixes/expand/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

