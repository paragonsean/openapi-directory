# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_asset(client):
    """Test case for get_asset

    Asset Detail
    """
    params = [('aliases', True)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/asset/{asset_id}'.format(asset_id='asset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset_contributors(client):
    """Test case for get_asset_contributors

    Asset Contributors
    """
    params = [('aliases', True)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/asset/{asset_id}/contributor'.format(asset_id='asset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_assets(client):
    """Test case for list_assets

    Asset Collection
    """
    params = [('updatedAfter', '2015-05-05T00:00:00.000Z'),
                    ('limit', 100),
                    ('aliases', True)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/asset',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

