# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hooks_get200_response import HooksGet200Response
from openapi_server.models.hooks_post200_response import HooksPOST200Response


pytestmark = pytest.mark.asyncio

async def test_hooks_get(client):
    """Test case for hooks_get

    
    """
    params = [('action', 'action_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/hooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hooks_post(client):
    """Test case for hooks_post

    
    """
    params = [('action', 'action_example'),
                    ('id', 56),
                    ('target_url', 'target_url_example'),
                    ('event_type', 'event_type_example'),
                    ('request_method', POST)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/hooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

