# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hook_configuration import HookConfiguration
from openapi_server.models.hook_configuration_request import HookConfigurationRequest


pytestmark = pytest.mark.asyncio

async def test_delete_hook_configuration(client):
    """Test case for delete_hook_configuration

    Delete hook configuration
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/orders/hook/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hook_configuration(client):
    """Test case for get_hook_configuration

    Get hook configuration
    """
    params = [('clientEmail', 'customer@mail.com'),
                    ('page', '10'),
                    ('per_page', '15')]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/orders/hook/config',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hook_configuration(client):
    """Test case for hook_configuration

    Create or update hook configuration
    """
    body = {"filter":{"status":["order-completed","handling","ready-for-handling","waiting-ffmt-authorization","cancel"],"type":"FromWorkflow"},"hook":{"headers":{"key":"value"},"url":"https://endpoint.example/path"}}
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
        path='/api/orders/hook/config',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

