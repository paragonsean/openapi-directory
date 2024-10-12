# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.listing_extra_attributes import ListingExtraAttributes
from openapi_server.models.listing_media import ListingMedia
from openapi_server.models.rv_listing import RVListing
from openapi_server.models.rv_search_response import RVSearchResponse
from openapi_server.models.search_auto_complete_response import SearchAutoCompleteResponse
from openapi_server.models.ukrv_search_response import UKRVSearchResponse


pytestmark = pytest.mark.asyncio

async def test_listing_rv_id_extra_get(client):
    """Test case for listing_rv_id_extra_get

    Long text RV Listings attributes for Listing with the given id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/rv/{id}/extra'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_rv_id_get(client):
    """Test case for listing_rv_id_get

    RV listing by id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/rv/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_rv_id_media_get(client):
    """Test case for listing_rv_id_media_get

    Listing media by id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/rv/{id}/media'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_rv_uk_id_extra_get(client):
    """Test case for listing_rv_uk_id_extra_get

    Long text RV Listings attributes for Listing with the given id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/rv/uk/{id}/extra'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_rv_uk_id_get(client):
    """Test case for listing_rv_uk_id_get

    RV listing by id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/rv/uk/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_rv_uk_id_media_get(client):
    """Test case for listing_rv_uk_id_media_get

    Listing media by id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/rv/uk/{id}/media'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_rv_active_get(client):
    """Test case for search_rv_active_get

    Gets active RV listings for the given search criteria
    """
    params = [('api_key', 'api_key_example'),
                    ('price_range', 'price_range_example'),
                    ('miles_range', 'miles_range_example'),
                    ('msrp_range', 'msrp_range_example'),
                    ('year_range', 'year_range_example'),
                    ('search_text', 'search_text_example'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('model_o', 'model_o_example'),
                    ('vin', 'vin_example'),
                    ('inventory_type', 'inventory_type_example'),
                    ('stock_no', 'stock_no_example'),
                    ('source', 'source_example'),
                    ('dealer_name', 'dealer_name_example'),
                    ('dealer_id', 'dealer_id_example'),
                    ('exterior_color', 'exterior_color_example'),
                    ('interior_color', 'interior_color_example'),
                    ('engine', 'engine_example'),
                    ('fuel_type', 'fuel_type_example'),
                    ('transmission', 'transmission_example'),
                    ('class', '_class_example'),
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
                    ('first_seen_days', 'first_seen_days_example'),
                    ('slideouts', 'slideouts_example'),
                    ('length_range', 'length_range_example'),
                    ('length', 'length_example'),
                    ('base_exterior_color', 'base_exterior_color_example'),
                    ('base_interior_color', 'base_interior_color_example'),
                    ('seating_capacity', 'seating_capacity_example'),
                    ('fresh_water_capacity', 'fresh_water_capacity_example'),
                    ('sleeps', 'sleeps_example'),
                    ('cylinders', 'cylinders_example'),
                    ('number_of_awnings', 'number_of_awnings_example'),
                    ('doors', 'doors_example'),
                    ('gvwr', 'gvwr_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/rv/active',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_rv_auto_complete_get(client):
    """Test case for search_rv_auto_complete_get

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
        path='/v2/search/rv/auto-complete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_rv_uk_active_get(client):
    """Test case for search_rv_uk_active_get

    Gets active RV listings for the given search criteria
    """
    params = [('api_key', 'api_key_example'),
                    ('price_range', 'price_range_example'),
                    ('miles_range', 'miles_range_example'),
                    ('msrp_range', 'msrp_range_example'),
                    ('year_range', 'year_range_example'),
                    ('search_text', 'search_text_example'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('vin', 'vin_example'),
                    ('source', 'source_example'),
                    ('dealer_name', 'dealer_name_example'),
                    ('dealer_id', 'dealer_id_example'),
                    ('exterior_color', 'exterior_color_example'),
                    ('interior_color', 'interior_color_example'),
                    ('engine_size', 'engine_size_example'),
                    ('fuel_type', 'fuel_type_example'),
                    ('category', 'category_example'),
                    ('state', 'state_example'),
                    ('city', 'city_example'),
                    ('county', 'county_example'),
                    ('postal_code', 'postal_code_example'),
                    ('zip', 'zip_example'),
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
                    ('first_seen_days', 'first_seen_days_example'),
                    ('base_exterior_color', 'base_exterior_color_example'),
                    ('base_interior_color', 'base_interior_color_example'),
                    ('seating_capacity', 'seating_capacity_example'),
                    ('cylinders', 'cylinders_example'),
                    ('doors', 'doors_example'),
                    ('mtplm', 'mtplm_example'),
                    ('sub_category', 'sub_category_example'),
                    ('availability_status', 'availability_status_example'),
                    ('berths', 'berths_example'),
                    ('inventory_type', 'inventory_type_example'),
                    ('width_range', 'width_range_example'),
                    ('exterior_length_range', 'exterior_length_range_example'),
                    ('interior_length_range', 'interior_length_range_example'),
                    ('drive_type', 'drive_type_example'),
                    ('steering', 'steering_example'),
                    ('chassis', 'chassis_example'),
                    ('transmission', 'transmission_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/rv/uk/active',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

