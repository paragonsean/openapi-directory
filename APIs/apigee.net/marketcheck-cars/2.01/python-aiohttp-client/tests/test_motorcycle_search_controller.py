# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.listing_extra_attributes import ListingExtraAttributes
from openapi_server.models.listing_media import ListingMedia
from openapi_server.models.motorcycle_listing import MotorcycleListing
from openapi_server.models.motorcycle_search_response import MotorcycleSearchResponse
from openapi_server.models.search_auto_complete_response import SearchAutoCompleteResponse


pytestmark = pytest.mark.asyncio

async def test_listing_motorcycle_id_extra_get(client):
    """Test case for listing_motorcycle_id_extra_get

    Long text Motorcycle Listings attributes for Listing with the given id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/motorcycle/{id}/extra'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_motorcycle_id_get(client):
    """Test case for listing_motorcycle_id_get

    Motorcycle listing by id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/motorcycle/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_motorcycle_id_media_get(client):
    """Test case for listing_motorcycle_id_media_get

    Motorcycle listing media by id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/motorcycle/{id}/media'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_motorcycle_active_get(client):
    """Test case for search_motorcycle_active_get

    Gets active motorcycle listings for the given search criteria
    """
    params = [('api_key', 'api_key_example'),
                    ('price_range', 'price_range_example'),
                    ('miles_range', 'miles_range_example'),
                    ('msrp_range', 'msrp_range_example'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('search_text', 'search_text_example'),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('vin', 'vin_example'),
                    ('taxonomy_vin', 'taxonomy_vin_example'),
                    ('inventory_type', 'inventory_type_example'),
                    ('stock_no', 'stock_no_example'),
                    ('source', 'source_example'),
                    ('dealer_id', 'dealer_id_example'),
                    ('color', 'color_example'),
                    ('body_type', 'body_type_example'),
                    ('vehicle_type', 'vehicle_type_example'),
                    ('cylinders', 'cylinders_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('engine', 'engine_example'),
                    ('fuel_type', 'fuel_type_example'),
                    ('transmission', 'transmission_example'),
                    ('state', 'state_example'),
                    ('city', 'city_example'),
                    ('zip', 'zip_example'),
                    ('msa_code', 'msa_code_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('rows', 10),
                    ('start', 0),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example'),
                    ('facet_sort', count),
                    ('stats', 'stats_example'),
                    ('last_seen_range', 'last_seen_range_example'),
                    ('first_seen_range', 'first_seen_range_example'),
                    ('last_seen_days', 'last_seen_days_example'),
                    ('first_seen_days', 'first_seen_days_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/motorcycle/active',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_motorcycle_auto_complete_get(client):
    """Test case for search_motorcycle_auto_complete_get

    API for auto-completion of inputs
    """
    params = [('api_key', 'api_key_example'),
                    ('field', '_field_example'),
                    ('input', 'input_example'),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('body_type', 'body_type_example'),
                    ('vehicle_type', 'vehicle_type_example'),
                    ('transmission', 'transmission_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('fuel_type', 'fuel_type_example'),
                    ('color', 'color_example'),
                    ('engine', 'engine_example'),
                    ('state', 'state_example'),
                    ('city', 'city_example'),
                    ('inventory_type', 'inventory_type_example'),
                    ('ignore_case', True),
                    ('term_counts', False),
                    ('sort_by', index),
                    ('seller_type', 'seller_type_example'),
                    ('radius', 56),
                    ('zip', 'zip_example'),
                    ('facet_min_count', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/motorcycle/auto-complete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

