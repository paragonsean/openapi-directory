# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_reactions_post(client):
    """Test case for api_reactions_post

    create reaction
    """
    params = [('category', 'category_example'),
                    ('reactable_id', 56),
                    ('reactable_type', 'reactable_type_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/api/reactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_reactions_toggle_post(client):
    """Test case for api_reactions_toggle_post

    toggle reaction
    """
    params = [('category', 'category_example'),
                    ('reactable_id', 56),
                    ('reactable_type', 'reactable_type_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/api/reactions/toggle',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

