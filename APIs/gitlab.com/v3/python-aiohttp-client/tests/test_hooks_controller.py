# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hook import Hook
from openapi_server.models.post_v3_hooks_request import PostV3HooksRequest


pytestmark = pytest.mark.asyncio

async def test_delete_v3_hooks_id(client):
    """Test case for delete_v3_hooks_id

    Delete a hook
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/hooks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_hooks(client):
    """Test case for get_v3_hooks

    Get the list of system hooks
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/hooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_hooks_id(client):
    """Test case for get_v3_hooks_id

    Test a hook
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/hooks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_hooks(client):
    """Test case for post_v3_hooks

    Create a new system hook
    """
    body = openapi_server.PostV3HooksRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/hooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

