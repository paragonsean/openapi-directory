# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_marketplace_installed_add_on_response import ListMarketplaceInstalledAddOnResponse
from openapi_server.models.preview_marketplace_installed_add_on import PreviewMarketplaceInstalledAddOn


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_marketplace_installed_add_on(client):
    """Test case for create_marketplace_installed_add_on

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'accept_terms_of_service': True,
        'available_add_on_sid': 'available_add_on_sid_example',
        'configuration': None,
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/marketplace/InstalledAddOns',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_marketplace_installed_add_on(client):
    """Test case for delete_marketplace_installed_add_on

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/marketplace/InstalledAddOns/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_marketplace_installed_add_on(client):
    """Test case for fetch_marketplace_installed_add_on

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/InstalledAddOns/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_marketplace_installed_add_on(client):
    """Test case for list_marketplace_installed_add_on

    
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
        path='/marketplace/InstalledAddOns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_marketplace_installed_add_on(client):
    """Test case for update_marketplace_installed_add_on

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'configuration': None,
        'unique_name': 'unique_name_example'
        }
    response = await client.request(
        method='POST',
        path='/marketplace/InstalledAddOns/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

