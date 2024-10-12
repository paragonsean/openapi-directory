# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_contacts_get(client):
    """Test case for contacts_get

    View all contacts under your account
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/contacts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

