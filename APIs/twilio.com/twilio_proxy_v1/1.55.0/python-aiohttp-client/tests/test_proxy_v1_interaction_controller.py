# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_interaction_response import ListInteractionResponse
from openapi_server.models.proxy_v1_service_session_interaction import ProxyV1ServiceSessionInteraction


pytestmark = pytest.mark.asyncio

async def test_delete_interaction(client):
    """Test case for delete_interaction

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Services/{service_sid}/Sessions/{session_sid}/Interactions/{sid}'.format(service_sid='service_sid_example', session_sid='session_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_interaction(client):
    """Test case for fetch_interaction

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Sessions/{session_sid}/Interactions/{sid}'.format(service_sid='service_sid_example', session_sid='session_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_interaction(client):
    """Test case for list_interaction

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Sessions/{session_sid}/Interactions'.format(service_sid='service_sid_example', session_sid='session_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

