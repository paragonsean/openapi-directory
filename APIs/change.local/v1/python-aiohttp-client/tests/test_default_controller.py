# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_v1_donations_carbon_calculate_get(client):
    """Test case for api_v1_donations_carbon_calculate_get

    Calculate shipping carbon offset
    """
    params = [('origin_address', 60148),
                    ('destination_address', 94133),
                    ('distance_mi', 3.4),
                    ('weight_lb', 3.5),
                    ('transportation_method', 'air')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/donations/carbon_calculate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_donations_carbon_stats_get(client):
    """Test case for api_v1_donations_carbon_stats_get

    Retrieve carbon offset stats
    """
    params = [('id', d_NuYL6M2C1kjecXpWzKVODw7W)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/donations/carbon_stats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_donations_create_post(client):
    """Test case for api_v1_donations_create_post

    Create a donation
    """
    params = [('amount', '500'),
                    ('nonprofit_id', 'n_IfEoPCaPqVsFAUI5xl0CBUOx'),
                    ('funding_source', 'customer'),
                    ('zip_code', '94104')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/donations/create',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_donations_crypto_calculate_get(client):
    """Test case for api_v1_donations_crypto_calculate_get

    Calculate crypto carbon offset
    """
    params = [('count', 2),
                    ('currency', 'eth')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/donations/crypto_calculate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_donations_index_get(client):
    """Test case for api_v1_donations_index_get

    List your donations
    """
    params = [('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/donations/index',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_donations_show_get(client):
    """Test case for api_v1_donations_show_get

    Retrieve a donation
    """
    params = [('id', 'd_NuYL6M2C1kjecXpWzKVODw7W')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/donations/show',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_nonprofits_list_get(client):
    """Test case for api_v1_nonprofits_list_get

    Search a nonprofit
    """
    params = [('name', 'Some Nonprofit'),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/nonprofits/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_nonprofits_show_get(client):
    """Test case for api_v1_nonprofits_show_get

    Show a nonprofit
    """
    params = [('id', 'n_IfEoPCaPqVsFAUI5xl0CBUOx')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/nonprofits/show',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

