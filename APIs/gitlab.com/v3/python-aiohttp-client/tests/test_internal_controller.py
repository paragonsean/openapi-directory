# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_v3_internal_broadcast_message(client):
    """Test case for get_v3_internal_broadcast_message

    
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/internal/broadcast_message',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_internal_check(client):
    """Test case for get_v3_internal_check

    
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/internal/check',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_internal_discover(client):
    """Test case for get_v3_internal_discover

    
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/internal/discover',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_internal_merge_request_urls(client):
    """Test case for get_v3_internal_merge_request_urls

    
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/internal/merge_request_urls',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_internal_allowed(client):
    """Test case for post_v3_internal_allowed

    
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/internal/allowed',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_internal_lfs_authenticate(client):
    """Test case for post_v3_internal_lfs_authenticate

    
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/internal/lfs_authenticate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_internal_two_factor_recovery_codes(client):
    """Test case for post_v3_internal_two_factor_recovery_codes

    
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/internal/two_factor_recovery_codes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

