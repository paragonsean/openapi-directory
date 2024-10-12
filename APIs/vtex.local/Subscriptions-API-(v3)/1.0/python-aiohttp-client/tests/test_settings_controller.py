# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.settings import Settings


pytestmark = pytest.mark.asyncio

async def test_edit_settings(client):
    """Test case for edit_settings

    Edit Subscriptions settings
    """
    body = openapi_server.Settings()
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
        path='/api/rns/settings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_settings(client):
    """Test case for get_settings

    Get Subscription Settings
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
        path='/api/rns/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

