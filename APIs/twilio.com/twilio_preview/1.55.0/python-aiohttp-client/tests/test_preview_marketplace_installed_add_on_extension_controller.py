# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_marketplace_installed_add_on_extension_response import ListMarketplaceInstalledAddOnExtensionResponse
from openapi_server.models.preview_marketplace_installed_add_on_installed_add_on_extension import PreviewMarketplaceInstalledAddOnInstalledAddOnExtension


pytestmark = pytest.mark.asyncio

async def test_fetch_marketplace_installed_add_on_extension(client):
    """Test case for fetch_marketplace_installed_add_on_extension

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/InstalledAddOns/{installed_add_on_sid}/Extensions/{sid}'.format(installed_add_on_sid='installed_add_on_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_marketplace_installed_add_on_extension(client):
    """Test case for list_marketplace_installed_add_on_extension

    
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
        path='/marketplace/InstalledAddOns/{installed_add_on_sid}/Extensions'.format(installed_add_on_sid='installed_add_on_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_marketplace_installed_add_on_extension(client):
    """Test case for update_marketplace_installed_add_on_extension

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'enabled': True
        }
    response = await client.request(
        method='POST',
        path='/marketplace/InstalledAddOns/{installed_add_on_sid}/Extensions/{sid}'.format(installed_add_on_sid='installed_add_on_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

