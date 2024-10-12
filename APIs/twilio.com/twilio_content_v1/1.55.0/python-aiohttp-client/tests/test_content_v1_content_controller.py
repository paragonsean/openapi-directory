# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.content_v1_content import ContentV1Content
from openapi_server.models.list_content_response import ListContentResponse


pytestmark = pytest.mark.asyncio

async def test_delete_content(client):
    """Test case for delete_content

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Content/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_content(client):
    """Test case for fetch_content

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Content/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_content(client):
    """Test case for list_content

    
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
        path='/v1/Content',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

