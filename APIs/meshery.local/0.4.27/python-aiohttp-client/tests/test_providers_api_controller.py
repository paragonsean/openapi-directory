# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.provider_properties import ProviderProperties


pytestmark = pytest.mark.asyncio

async def test_id_choice_provider(client):
    """Test case for id_choice_provider

    Handle GET request for the choice of provider
    """
    params = [('provider', 'provider_example')]
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/provider',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_provider_capabilities(client):
    """Test case for id_get_provider_capabilities

    Handle GET requests for Provider
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/provider/capabilities',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_providers_list(client):
    """Test case for id_get_providers_list

    Handle GET request for list of providers
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/providers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_provider(client):
    """Test case for id_provider

    Handle GET request to provider UI
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/provider',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_react_components(client):
    """Test case for id_react_components

    Handle GET request for React Components
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/provider/extension',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

