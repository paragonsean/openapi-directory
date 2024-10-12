# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset_render_response import AssetRenderResponse
from openapi_server.models.asset_response import AssetResponse


pytestmark = pytest.mark.asyncio

async def test_delete_asset(client):
    """Test case for delete_asset

    Delete Asset
    """
    headers = { 
        'DeveloperKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/assets/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset(client):
    """Test case for get_asset

    Get Asset
    """
    headers = { 
        'Accept': 'application/json',
        'DeveloperKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/assets/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset_by_render_id(client):
    """Test case for get_asset_by_render_id

    Get Asset by Render ID
    """
    headers = { 
        'Accept': 'application/json',
        'DeveloperKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/assets/render/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

