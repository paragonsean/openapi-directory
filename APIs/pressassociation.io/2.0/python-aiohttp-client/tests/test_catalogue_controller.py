# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_catalogue(client):
    """Test case for get_catalogue

    Catalogue Detail
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/catalogue/{catalogue_id}'.format(catalogue_id='catalogue_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_catalogue_asset(client):
    """Test case for get_catalogue_asset

    Catalogue Asset Collection
    """
    params = [('title', 'title_example'),
                    ('start', '2015-05-05T00:00:00'),
                    ('end', '2015-05-06T00:00:00'),
                    ('updatedAfter', '2015-05-06T00:00:00'),
                    ('limit', 500),
                    ('aliases', True)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/catalogue/{catalogue_id}/asset'.format(catalogue_id='catalogue_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_catalogue_asset_detail(client):
    """Test case for get_catalogue_asset_detail

    Catalogue Asset Detail
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/catalogue/{catalogue_id}/asset/{asset_id}'.format(catalogue_id='catalogue_id_example', asset_id='asset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_catalogues(client):
    """Test case for list_catalogues

    Catalogue Collection
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/catalogue',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

