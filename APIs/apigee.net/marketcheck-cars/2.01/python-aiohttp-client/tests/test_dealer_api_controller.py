# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dealer import Dealer
from openapi_server.models.dealers_response import DealersResponse
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_dealer_car_uk_id_get(client):
    """Test case for dealer_car_uk_id_get

    Dealer by id
    """
    params = [('api_key', 'api_key_example'),
                    ('provider', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/dealer/car/uk/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dealer_heavy_equipment_id_get(client):
    """Test case for dealer_heavy_equipment_id_get

    Dealer by id
    """
    params = [('api_key', 'api_key_example'),
                    ('provider', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/dealer/heavy-equipment/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dealer_motorcycle_id_get(client):
    """Test case for dealer_motorcycle_id_get

    Dealer by id
    """
    params = [('api_key', 'api_key_example'),
                    ('provider', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/dealer/motorcycle/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dealer_rv_id_get(client):
    """Test case for dealer_rv_id_get

    Dealer by id
    """
    params = [('api_key', 'api_key_example'),
                    ('provider', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/dealer/rv/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dealer_search(client):
    """Test case for dealer_search

    Find car dealers around
    """
    params = [('api_key', 'api_key_example'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('rows', 10),
                    ('start', 0),
                    ('country', 'country_example'),
                    ('dealer_type', 'dealer_type_example'),
                    ('city', 'city_example'),
                    ('state', 'state_example'),
                    ('listing_count_range', 'listing_count_range_example'),
                    ('inventory_url', 'inventory_url_example'),
                    ('zip', 'zip_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('provider', False),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/dealers/car',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dealers_car_uk_get(client):
    """Test case for dealers_car_uk_get

    Find car dealers around
    """
    params = [('api_key', 'api_key_example'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('rows', 10),
                    ('start', 0),
                    ('country', 'country_example'),
                    ('dealer_type', 'dealer_type_example'),
                    ('city', 'city_example'),
                    ('county', 'county_example'),
                    ('listing_count_range', 'listing_count_range_example'),
                    ('inventory_url', 'inventory_url_example'),
                    ('postal_code', 'postal_code_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('provider', False),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/dealers/car/uk',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dealers_heavy_equipment_get(client):
    """Test case for dealers_heavy_equipment_get

    Find car dealers around
    """
    params = [('api_key', 'api_key_example'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('rows', 10),
                    ('start', 0),
                    ('country', 'country_example'),
                    ('dealer_type', 'dealer_type_example'),
                    ('city', 'city_example'),
                    ('state', 'state_example'),
                    ('listing_count_range', 'listing_count_range_example'),
                    ('inventory_url', 'inventory_url_example'),
                    ('zip', 'zip_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('provider', False),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/dealers/heavy-equipment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dealers_motorcycle_get(client):
    """Test case for dealers_motorcycle_get

    Find car dealers around
    """
    params = [('api_key', 'api_key_example'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('rows', 10),
                    ('start', 0),
                    ('country', 'country_example'),
                    ('dealer_type', 'dealer_type_example'),
                    ('city', 'city_example'),
                    ('state', 'state_example'),
                    ('listing_count_range', 'listing_count_range_example'),
                    ('inventory_url', 'inventory_url_example'),
                    ('zip', 'zip_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('provider', False),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/dealers/motorcycle',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dealers_rv_get(client):
    """Test case for dealers_rv_get

    Find car dealers around
    """
    params = [('api_key', 'api_key_example'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('rows', 10),
                    ('start', 0),
                    ('country', 'country_example'),
                    ('dealer_type', 'dealer_type_example'),
                    ('city', 'city_example'),
                    ('state', 'state_example'),
                    ('listing_count_range', 'listing_count_range_example'),
                    ('inventory_url', 'inventory_url_example'),
                    ('zip', 'zip_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('provider', False),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/dealers/rv',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dealer(client):
    """Test case for get_dealer

    Dealer by id
    """
    params = [('api_key', 'api_key_example'),
                    ('provider', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/dealer/car/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

