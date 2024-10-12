# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_references_event_cost_types0_get(client):
    """Test case for references_event_cost_types0_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/references/event_cost_types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_references_event_custom_fields0_get(client):
    """Test case for references_event_custom_fields0_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/references/event_custom_fields',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_references_event_participation_types0_get(client):
    """Test case for references_event_participation_types0_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/references/event_participation_types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_references_event_tags0_get(client):
    """Test case for references_event_tags0_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/references/event_tags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_references_users_and_resources0_get(client):
    """Test case for references_users_and_resources0_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/references/users_and_resources',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

