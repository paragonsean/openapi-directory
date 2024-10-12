# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_suggestionbyversion(client):
    """Test case for get_suggestionbyversion

    Get Version by ID
    """
    params = [('accountName', 'apiexamples')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/suggestions/{seller_id}/{sellerskuid}/versions/{version}'.format(seller_id='seller123', sellerskuid='1234', version='09072021142808277'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_versions(client):
    """Test case for get_versions

    Get all Versions
    """
    params = [('accountName', 'apiexamples')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/suggestions/{seller_id}/{sellerskuid}/versions'.format(seller_id='seller123', sellerskuid='1234'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

