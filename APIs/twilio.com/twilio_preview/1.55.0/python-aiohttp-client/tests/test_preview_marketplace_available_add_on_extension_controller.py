# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_marketplace_available_add_on_extension_response import ListMarketplaceAvailableAddOnExtensionResponse
from openapi_server.models.preview_marketplace_available_add_on_available_add_on_extension import PreviewMarketplaceAvailableAddOnAvailableAddOnExtension


pytestmark = pytest.mark.asyncio

async def test_fetch_marketplace_available_add_on_extension(client):
    """Test case for fetch_marketplace_available_add_on_extension

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/AvailableAddOns/{available_add_on_sid}/Extensions/{sid}'.format(available_add_on_sid='available_add_on_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_marketplace_available_add_on_extension(client):
    """Test case for list_marketplace_available_add_on_extension

    
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
        path='/marketplace/AvailableAddOns/{available_add_on_sid}/Extensions'.format(available_add_on_sid='available_add_on_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

