# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_pages200_response import GetPages200Response
from openapi_server.models.get_pages200_response_pages_inner import GetPages200ResponsePagesInner


pytestmark = pytest.mark.asyncio

async def test_get_page(client):
    """Test case for get_page

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/pages/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pages(client):
    """Test case for get_pages

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/pages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

