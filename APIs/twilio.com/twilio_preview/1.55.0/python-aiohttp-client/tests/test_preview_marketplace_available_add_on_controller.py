# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_marketplace_available_add_on_response import ListMarketplaceAvailableAddOnResponse
from openapi_server.models.preview_marketplace_available_add_on import PreviewMarketplaceAvailableAddOn


pytestmark = pytest.mark.asyncio

async def test_fetch_marketplace_available_add_on(client):
    """Test case for fetch_marketplace_available_add_on

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/AvailableAddOns/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_marketplace_available_add_on(client):
    """Test case for list_marketplace_available_add_on

    
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
        path='/marketplace/AvailableAddOns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

