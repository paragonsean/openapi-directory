# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset import Asset
from openapi_server.models.asset_signature import AssetSignature
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_create_site_asset(client):
    """Test case for create_site_asset

    
    """
    params = [('name', 'name_example'),
                    ('size', 56),
                    ('content_type', 'content_type_example'),
                    ('visibility', 'visibility_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{site_id}/assets'.format(site_id='site_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_site_asset(client):
    """Test case for delete_site_asset

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/sites/{site_id}/assets/{asset_id}'.format(site_id='site_id_example', asset_id='asset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_site_asset_info(client):
    """Test case for get_site_asset_info

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/assets/{asset_id}'.format(site_id='site_id_example', asset_id='asset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_site_assets(client):
    """Test case for list_site_assets

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/assets'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_site_asset(client):
    """Test case for update_site_asset

    
    """
    params = [('state', 'state_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sites/{site_id}/assets/{asset_id}'.format(site_id='site_id_example', asset_id='asset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

