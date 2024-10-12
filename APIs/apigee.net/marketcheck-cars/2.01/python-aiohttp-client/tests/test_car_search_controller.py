# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.listing import Listing
from openapi_server.models.listing_extra_attributes import ListingExtraAttributes
from openapi_server.models.listing_media import ListingMedia
from openapi_server.models.search_auto_complete_response import SearchAutoCompleteResponse
from openapi_server.models.search_response import SearchResponse
from openapi_server.models.uk_search_response import UKSearchResponse


pytestmark = pytest.mark.asyncio

async def test_auto_complete(client):
    """Test case for auto_complete

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
                    ('body_subtype', 'body_subtype_example'),
                    ('vehicle_type', 'vehicle_type_example'),
                    ('transmission', 'transmission_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('fuel_type', 'fuel_type_example'),
                    ('exterior_color', 'exterior_color_example'),
                    ('interior_color', 'interior_color_example'),
                    ('engine', 'engine_example'),
                    ('engine_size', 'engine_size_example'),
                    ('engine_block', 'engine_block_example'),
                    ('state', 'state_example'),
                    ('city', 'city_example'),
                    ('source', 'source_example'),
                    ('dealer_id', 'dealer_id_example'),
                    ('country', US),
                    ('car_type', 'car_type_example'),
                    ('include_non_vin_listings', false),
                    ('ignore_case', True),
                    ('term_counts', False),
                    ('sort_by', index),
                    ('seller_type', 'seller_type_example'),
                    ('radius', 56),
                    ('zip', 'zip_example'),
                    ('inventory_count_range', 'inventory_count_range_example'),
                    ('exclude_dealer_ids', 'exclude_dealer_ids_example'),
                    ('exclude_sources', 'exclude_sources_example'),
                    ('in_transit', 'in_transit_example'),
                    ('facet_min_count', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/car/auto-complete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_car_dealer_inventory_active_get(client):
    """Test case for car_dealer_inventory_active_get

    Get dealers active inventory
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('zip', 'zip_example'),
                    ('include_lease', True),
                    ('include_finance', True),
                    ('lease_term', 'lease_term_example'),
                    ('lease_down_payment', 'lease_down_payment_example'),
                    ('lease_emp', 'lease_emp_example'),
                    ('finance_loan_term', 'finance_loan_term_example'),
                    ('finance_loan_apr', 'finance_loan_apr_example'),
                    ('finance_emp', 'finance_emp_example'),
                    ('finance_down_payment', 'finance_down_payment_example'),
                    ('finance_down_payment_per', 'finance_down_payment_per_example'),
                    ('car_type', 'car_type_example'),
                    ('carfax_1_owner', 'carfax_1_owner_example'),
                    ('carfax_clean_title', 'carfax_clean_title_example'),
                    ('year_range', 'year_range_example'),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('dealer_id', 'dealer_id_example'),
                    ('vin', 'vin_example'),
                    ('source', 'source_example'),
                    ('body_type', 'body_type_example'),
                    ('body_subtype', 'body_subtype_example'),
                    ('vehicle_type', 'vehicle_type_example'),
                    ('vins', 'vins_example'),
                    ('taxonomy_vins', 'taxonomy_vins_example'),
                    ('mm', 'mm_example'),
                    ('ymm', 'ymm_example'),
                    ('ymmt', 'ymmt_example'),
                    ('match', 'match_example'),
                    ('cylinders', 'cylinders_example'),
                    ('transmission', 'transmission_example'),
                    ('doors', 'doors_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('exterior_color', 'exterior_color_example'),
                    ('interior_color', 'interior_color_example'),
                    ('base_exterior_color', 'base_exterior_color_example'),
                    ('base_interior_color', 'base_interior_color_example'),
                    ('engine', 'engine_example'),
                    ('engine_size', 'engine_size_example'),
                    ('engine_aspiration', 'engine_aspiration_example'),
                    ('engine_block', 'engine_block_example'),
                    ('highway_mpg_range', 'highway_mpg_range_example'),
                    ('city_mpg_range', 'city_mpg_range_example'),
                    ('miles_range', 'miles_range_example'),
                    ('price_range', 'price_range_example'),
                    ('msrp_range', 'msrp_range_example'),
                    ('dom_range', 'dom_range_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('rows', 10),
                    ('start', 0),
                    ('include_non_vin_listings', False),
                    ('msa_code', 'msa_code_example'),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example'),
                    ('facet_sort', count),
                    ('stats', 'stats_example'),
                    ('country', US),
                    ('plot', True),
                    ('nodedup', True),
                    ('dedup', True),
                    ('owned', True),
                    ('state', 'state_example'),
                    ('city', 'city_example'),
                    ('dealer_name', 'dealer_name_example'),
                    ('dealership_group_name', 'dealership_group_name_example'),
                    ('trim_o', 'trim_o_example'),
                    ('trim_r', 'trim_r_example'),
                    ('dom_active_range', 'dom_active_range_example'),
                    ('dom_180_range', 'dom_180_range_example'),
                    ('exclude_certified', True),
                    ('fuel_type', 'fuel_type_example'),
                    ('dealer_type', 'dealer_type_example'),
                    ('photo_links', True),
                    ('photo_links_cached', True),
                    ('stock_no', 'stock_no_example'),
                    ('last_seen_range', 'last_seen_range_example'),
                    ('first_seen_range', 'first_seen_range_example'),
                    ('first_seen_at_source_range', 'first_seen_at_source_range_example'),
                    ('first_seen_at_mc_range', 'first_seen_at_mc_range_example'),
                    ('last_seen_days', 'last_seen_days_example'),
                    ('first_seen_days', 'first_seen_days_example'),
                    ('first_seen_at_source_days', 'first_seen_at_source_days_example'),
                    ('first_seen_at_mc_days', 'first_seen_at_mc_days_example'),
                    ('include_relevant_links', False),
                    ('inventory_count_range', 'inventory_count_range_example'),
                    ('in_transit', 'in_transit_example'),
                    ('seating_capacity', 'seating_capacity_example'),
                    ('engine_size_range', 'engine_size_range_example'),
                    ('powertrain_type', 'powertrain_type_example'),
                    ('min_photo_links', 'min_photo_links_example'),
                    ('min_photo_links_cached', 'min_photo_links_cached_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/car/dealer/inventory/active',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_listing(client):
    """Test case for get_listing

    Listing by id
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True),
                    ('include_relevant_links', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/car/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_car_auction_id_extra_get(client):
    """Test case for listing_car_auction_id_extra_get

    Long text Listings attributes for Listing with the given id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/car/auction/{id}/extra'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_car_auction_id_get(client):
    """Test case for listing_car_auction_id_get

    Listing by id
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True),
                    ('include_relevant_links', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/car/auction/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_car_auction_id_media_get(client):
    """Test case for listing_car_auction_id_media_get

    Listing media by id
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/car/auction/{id}/media'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_car_fsbo_id_extra_get(client):
    """Test case for listing_car_fsbo_id_extra_get

    Long text Listings attributes for Listing with the given id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/car/fsbo/{id}/extra'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_car_fsbo_id_get(client):
    """Test case for listing_car_fsbo_id_get

    Listing by id
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True),
                    ('include_relevant_links', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/car/fsbo/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_car_fsbo_id_media_get(client):
    """Test case for listing_car_fsbo_id_media_get

    Listing media by id
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/car/fsbo/{id}/media'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_car_id_extra_get(client):
    """Test case for listing_car_id_extra_get

    Long text Listings attributes for Listing with the given id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/car/{id}/extra'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_car_id_media_get(client):
    """Test case for listing_car_id_media_get

    Listing media by id
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/car/{id}/media'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_car_uk_id_extra_get(client):
    """Test case for listing_car_uk_id_extra_get

    Long text Listings attributes for Listing with the given id
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/car/uk/{id}/extra'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_car_uk_id_get(client):
    """Test case for listing_car_uk_id_get

    Listing by id
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/car/uk/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listing_car_uk_id_media_get(client):
    """Test case for listing_car_uk_id_media_get

    Listing media by id
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/listing/car/uk/{id}/media'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Gets active car listings in UK for the given search criteria
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', False),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('postal_code', 'postal_code_example'),
                    ('zip', 'zip_example'),
                    ('car_type', 'car_type_example'),
                    ('year', 'year_example'),
                    ('year_range', 'year_range_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('variant', 'variant_example'),
                    ('trim', 'trim_example'),
                    ('body_type', 'body_type_example'),
                    ('ymmt', 'ymmt_example'),
                    ('transmission', 'transmission_example'),
                    ('doors', 'doors_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('exterior_color', 'exterior_color_example'),
                    ('interior_color', 'interior_color_example'),
                    ('engine', 'engine_example'),
                    ('miles_range', 'miles_range_example'),
                    ('price_range', 'price_range_example'),
                    ('msrp_range', 'msrp_range_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('rows', 10),
                    ('start', 0),
                    ('msa_code', 'msa_code_example'),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example'),
                    ('facet_sort', count),
                    ('stats', 'stats_example'),
                    ('country', uk),
                    ('plot', True),
                    ('nodedup', True),
                    ('dedup', True),
                    ('county', 'county_example'),
                    ('state', 'state_example'),
                    ('city', 'city_example'),
                    ('fuel_type', 'fuel_type_example'),
                    ('stock_no', 'stock_no_example'),
                    ('dom_range', 'dom_range_example'),
                    ('dom_active_range', 'dom_active_range_example'),
                    ('dom_180_range', 'dom_180_range_example'),
                    ('last_seen_range', 'last_seen_range_example'),
                    ('first_seen_range', 'first_seen_range_example'),
                    ('first_seen_at_source_range', 'first_seen_at_source_range_example'),
                    ('first_seen_at_mc_range', 'first_seen_at_mc_range_example'),
                    ('last_seen_days', 'last_seen_days_example'),
                    ('first_seen_days', 'first_seen_days_example'),
                    ('first_seen_at_source_days', 'first_seen_at_source_days_example'),
                    ('first_seen_at_mc_days', 'first_seen_at_mc_days_example'),
                    ('co2_emissions', 'co2_emissions_example'),
                    ('insurance_group', 'insurance_group_example'),
                    ('vehicle_registration_mark', 'vehicle_registration_mark_example'),
                    ('vehicle_registration_date_range', 'vehicle_registration_date_range_example'),
                    ('num_owners', 'num_owners_example'),
                    ('inventory_count_range', 'inventory_count_range_example'),
                    ('source', 'source_example'),
                    ('dealer_id', 'dealer_id_example'),
                    ('exclude_sources', 'exclude_sources_example'),
                    ('exclude_dealer_ids', 'exclude_dealer_ids_example'),
                    ('in_transit', 'in_transit_example'),
                    ('include_non_vin_listings', False),
                    ('cylinders', 'cylinders_example'),
                    ('photo_links', True),
                    ('photo_links_cached', True),
                    ('base_exterior_color', 'base_exterior_color_example'),
                    ('base_interior_color', 'base_interior_color_example'),
                    ('write_off_category', 'write_off_category_example'),
                    ('exclude_write_off_category', 'exclude_write_off_category_example'),
                    ('fca_status', 'fca_status_example'),
                    ('seating_capacity', 'seating_capacity_example'),
                    ('vrm', 'vrm_example'),
                    ('powertrain_type', 'powertrain_type_example'),
                    ('client_filters', True),
                    ('boost', True),
                    ('car_location_seller_name', 'car_location_seller_name_example'),
                    ('car_location_street', 'car_location_street_example'),
                    ('car_location_city', 'car_location_city_example'),
                    ('car_location_county', 'car_location_county_example'),
                    ('car_location_zip', 'car_location_zip_example'),
                    ('car_location_latitude', 3.4),
                    ('car_location_longitude', 3.4),
                    ('price_change', 'price_change_example'),
                    ('price_change_range', 'price_change_range_example'),
                    ('active_inventory_date_range', 'active_inventory_date_range_example'),
                    ('engine_size', 'engine_size_example'),
                    ('engine_size_range', 'engine_size_range_example'),
                    ('uvc_id', 'uvc_id_example'),
                    ('highway_mpg_range', 'highway_mpg_range_example'),
                    ('city_mpg_range', 'city_mpg_range_example'),
                    ('combined_mpg_range', 'combined_mpg_range_example'),
                    ('owned', True),
                    ('min_photo_links', 'min_photo_links_example'),
                    ('min_photo_links_cached', 'min_photo_links_cached_example'),
                    ('match', 'match_example'),
                    ('ulez_compliant', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/car/uk/active',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_car_active_get(client):
    """Test case for search_car_active_get

    Gets active car listings for the given search criteria
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('zip', 'zip_example'),
                    ('include_lease', True),
                    ('include_finance', True),
                    ('lease_term', 'lease_term_example'),
                    ('lease_down_payment', 'lease_down_payment_example'),
                    ('lease_emp', 'lease_emp_example'),
                    ('finance_loan_term', 'finance_loan_term_example'),
                    ('finance_loan_apr', 'finance_loan_apr_example'),
                    ('finance_emp', 'finance_emp_example'),
                    ('finance_down_payment', 'finance_down_payment_example'),
                    ('finance_down_payment_per', 'finance_down_payment_per_example'),
                    ('car_type', 'car_type_example'),
                    ('carfax_1_owner', 'carfax_1_owner_example'),
                    ('carfax_clean_title', 'carfax_clean_title_example'),
                    ('year_range', 'year_range_example'),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('vin', 'vin_example'),
                    ('body_type', 'body_type_example'),
                    ('body_subtype', 'body_subtype_example'),
                    ('vehicle_type', 'vehicle_type_example'),
                    ('vins', 'vins_example'),
                    ('taxonomy_vins', 'taxonomy_vins_example'),
                    ('mm', 'mm_example'),
                    ('ymm', 'ymm_example'),
                    ('ymmt', 'ymmt_example'),
                    ('match', 'match_example'),
                    ('cylinders', 'cylinders_example'),
                    ('transmission', 'transmission_example'),
                    ('doors', 'doors_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('exterior_color', 'exterior_color_example'),
                    ('interior_color', 'interior_color_example'),
                    ('base_exterior_color', 'base_exterior_color_example'),
                    ('base_interior_color', 'base_interior_color_example'),
                    ('engine', 'engine_example'),
                    ('engine_size', 'engine_size_example'),
                    ('engine_aspiration', 'engine_aspiration_example'),
                    ('engine_block', 'engine_block_example'),
                    ('highway_mpg_range', 'highway_mpg_range_example'),
                    ('city_mpg_range', 'city_mpg_range_example'),
                    ('miles_range', 'miles_range_example'),
                    ('price_range', 'price_range_example'),
                    ('msrp_range', 'msrp_range_example'),
                    ('dom_range', 'dom_range_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('rows', 10),
                    ('start', 0),
                    ('include_non_vin_listings', False),
                    ('msa_code', 'msa_code_example'),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example'),
                    ('facet_sort', count),
                    ('stats', 'stats_example'),
                    ('country', US),
                    ('plot', True),
                    ('nodedup', True),
                    ('dedup', True),
                    ('owned', True),
                    ('source', 'source_example'),
                    ('state', 'state_example'),
                    ('city', 'city_example'),
                    ('trim_o', 'trim_o_example'),
                    ('trim_r', 'trim_r_example'),
                    ('dom_active_range', 'dom_active_range_example'),
                    ('dom_180_range', 'dom_180_range_example'),
                    ('exclude_certified', True),
                    ('fuel_type', 'fuel_type_example'),
                    ('dealer_type', 'dealer_type_example'),
                    ('photo_links', True),
                    ('photo_links_cached', True),
                    ('stock_no', 'stock_no_example'),
                    ('last_seen_range', 'last_seen_range_example'),
                    ('first_seen_range', 'first_seen_range_example'),
                    ('first_seen_at_source_range', 'first_seen_at_source_range_example'),
                    ('first_seen_at_mc_range', 'first_seen_at_mc_range_example'),
                    ('last_seen_days', 'last_seen_days_example'),
                    ('first_seen_days', 'first_seen_days_example'),
                    ('first_seen_at_source_days', 'first_seen_at_source_days_example'),
                    ('first_seen_at_mc_days', 'first_seen_at_mc_days_example'),
                    ('include_relevant_links', False),
                    ('inventory_count_range', 'inventory_count_range_example'),
                    ('dealer_id', 'dealer_id_example'),
                    ('exclude_dealer_ids', 'exclude_dealer_ids_example'),
                    ('exclude_sources', 'exclude_sources_example'),
                    ('in_transit', 'in_transit_example'),
                    ('seating_capacity', 'seating_capacity_example'),
                    ('powertrain_type', 'powertrain_type_example'),
                    ('price_change', 'price_change_example'),
                    ('price_change_range', 'price_change_range_example'),
                    ('active_inventory_date_range', 'active_inventory_date_range_example'),
                    ('engine_size_range', 'engine_size_range_example'),
                    ('high_value_features', 'high_value_features_example'),
                    ('min_photo_links', 'min_photo_links_example'),
                    ('min_photo_links_cached', 'min_photo_links_cached_example'),
                    ('client_filters', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/car/active',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_car_auction_active_get(client):
    """Test case for search_car_auction_active_get

    Gets active auction car listings for the given search criteria
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('zip', 'zip_example'),
                    ('include_lease', True),
                    ('include_finance', True),
                    ('lease_term', 'lease_term_example'),
                    ('lease_down_payment', 'lease_down_payment_example'),
                    ('lease_emp', 'lease_emp_example'),
                    ('finance_loan_term', 'finance_loan_term_example'),
                    ('finance_loan_apr', 'finance_loan_apr_example'),
                    ('finance_emp', 'finance_emp_example'),
                    ('finance_down_payment', 'finance_down_payment_example'),
                    ('finance_down_payment_per', 'finance_down_payment_per_example'),
                    ('car_type', 'car_type_example'),
                    ('carfax_1_owner', 'carfax_1_owner_example'),
                    ('carfax_clean_title', 'carfax_clean_title_example'),
                    ('year_range', 'year_range_example'),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('vin', 'vin_example'),
                    ('body_type', 'body_type_example'),
                    ('body_subtype', 'body_subtype_example'),
                    ('vehicle_type', 'vehicle_type_example'),
                    ('vins', 'vins_example'),
                    ('taxonomy_vins', 'taxonomy_vins_example'),
                    ('mm', 'mm_example'),
                    ('ymm', 'ymm_example'),
                    ('ymmt', 'ymmt_example'),
                    ('match', 'match_example'),
                    ('cylinders', 'cylinders_example'),
                    ('transmission', 'transmission_example'),
                    ('doors', 'doors_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('exterior_color', 'exterior_color_example'),
                    ('interior_color', 'interior_color_example'),
                    ('base_exterior_color', 'base_exterior_color_example'),
                    ('base_interior_color', 'base_interior_color_example'),
                    ('engine', 'engine_example'),
                    ('engine_size', 'engine_size_example'),
                    ('engine_aspiration', 'engine_aspiration_example'),
                    ('engine_block', 'engine_block_example'),
                    ('highway_mpg_range', 'highway_mpg_range_example'),
                    ('city_mpg_range', 'city_mpg_range_example'),
                    ('miles_range', 'miles_range_example'),
                    ('price_range', 'price_range_example'),
                    ('msrp_range', 'msrp_range_example'),
                    ('dom_range', 'dom_range_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('rows', 10),
                    ('start', 0),
                    ('include_non_vin_listings', False),
                    ('msa_code', 'msa_code_example'),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example'),
                    ('facet_sort', count),
                    ('stats', 'stats_example'),
                    ('country', US),
                    ('plot', True),
                    ('nodedup', True),
                    ('dedup', True),
                    ('owned', True),
                    ('state', 'state_example'),
                    ('city', 'city_example'),
                    ('source', 'source_example'),
                    ('dealer_id', 'dealer_id_example'),
                    ('trim_o', 'trim_o_example'),
                    ('trim_r', 'trim_r_example'),
                    ('dom_active_range', 'dom_active_range_example'),
                    ('dom_180_range', 'dom_180_range_example'),
                    ('exclude_certified', True),
                    ('fuel_type', 'fuel_type_example'),
                    ('dealer_type', 'dealer_type_example'),
                    ('photo_links', True),
                    ('photo_links_cached', True),
                    ('stock_no', 'stock_no_example'),
                    ('last_seen_range', 'last_seen_range_example'),
                    ('first_seen_range', 'first_seen_range_example'),
                    ('first_seen_at_source_range', 'first_seen_at_source_range_example'),
                    ('first_seen_at_mc_range', 'first_seen_at_mc_range_example'),
                    ('last_seen_days', 'last_seen_days_example'),
                    ('first_seen_days', 'first_seen_days_example'),
                    ('first_seen_at_source_days', 'first_seen_at_source_days_example'),
                    ('first_seen_at_mc_days', 'first_seen_at_mc_days_example'),
                    ('include_relevant_links', False),
                    ('inventory_count_range', 'inventory_count_range_example'),
                    ('exclude_dealer_ids', 'exclude_dealer_ids_example'),
                    ('exclude_sources', 'exclude_sources_example'),
                    ('in_transit', 'in_transit_example'),
                    ('title_type', 'title_type_example'),
                    ('seating_capacity', 'seating_capacity_example'),
                    ('engine_size_range', 'engine_size_range_example'),
                    ('min_photo_links', 'min_photo_links_example'),
                    ('min_photo_links_cached', 'min_photo_links_cached_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/car/auction/active',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_car_fsbo_active_get(client):
    """Test case for search_car_fsbo_active_get

    Gets active private party car listings for the given search criteria
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('zip', 'zip_example'),
                    ('include_lease', True),
                    ('include_finance', True),
                    ('lease_term', 'lease_term_example'),
                    ('lease_down_payment', 'lease_down_payment_example'),
                    ('lease_emp', 'lease_emp_example'),
                    ('finance_loan_term', 'finance_loan_term_example'),
                    ('finance_loan_apr', 'finance_loan_apr_example'),
                    ('finance_emp', 'finance_emp_example'),
                    ('finance_down_payment', 'finance_down_payment_example'),
                    ('finance_down_payment_per', 'finance_down_payment_per_example'),
                    ('car_type', 'car_type_example'),
                    ('carfax_1_owner', 'carfax_1_owner_example'),
                    ('carfax_clean_title', 'carfax_clean_title_example'),
                    ('year_range', 'year_range_example'),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('vin', 'vin_example'),
                    ('body_type', 'body_type_example'),
                    ('body_subtype', 'body_subtype_example'),
                    ('vehicle_type', 'vehicle_type_example'),
                    ('vins', 'vins_example'),
                    ('taxonomy_vins', 'taxonomy_vins_example'),
                    ('mm', 'mm_example'),
                    ('ymm', 'ymm_example'),
                    ('ymmt', 'ymmt_example'),
                    ('match', 'match_example'),
                    ('cylinders', 'cylinders_example'),
                    ('transmission', 'transmission_example'),
                    ('doors', 'doors_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('exterior_color', 'exterior_color_example'),
                    ('interior_color', 'interior_color_example'),
                    ('base_exterior_color', 'base_exterior_color_example'),
                    ('base_interior_color', 'base_interior_color_example'),
                    ('engine', 'engine_example'),
                    ('engine_size', 'engine_size_example'),
                    ('engine_aspiration', 'engine_aspiration_example'),
                    ('engine_block', 'engine_block_example'),
                    ('highway_mpg_range', 'highway_mpg_range_example'),
                    ('city_mpg_range', 'city_mpg_range_example'),
                    ('miles_range', 'miles_range_example'),
                    ('price_range', 'price_range_example'),
                    ('msrp_range', 'msrp_range_example'),
                    ('dom_range', 'dom_range_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('rows', 10),
                    ('start', 0),
                    ('include_non_vin_listings', False),
                    ('msa_code', 'msa_code_example'),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example'),
                    ('facet_sort', count),
                    ('stats', 'stats_example'),
                    ('country', US),
                    ('plot', True),
                    ('nodedup', True),
                    ('dedup', True),
                    ('owned', True),
                    ('state', 'state_example'),
                    ('city', 'city_example'),
                    ('source', 'source_example'),
                    ('dealer_id', 'dealer_id_example'),
                    ('trim_o', 'trim_o_example'),
                    ('trim_r', 'trim_r_example'),
                    ('dom_active_range', 'dom_active_range_example'),
                    ('dom_180_range', 'dom_180_range_example'),
                    ('exclude_certified', True),
                    ('fuel_type', 'fuel_type_example'),
                    ('dealer_type', 'dealer_type_example'),
                    ('photo_links', True),
                    ('photo_links_cached', True),
                    ('stock_no', 'stock_no_example'),
                    ('last_seen_range', 'last_seen_range_example'),
                    ('first_seen_range', 'first_seen_range_example'),
                    ('first_seen_at_source_range', 'first_seen_at_source_range_example'),
                    ('first_seen_at_mc_range', 'first_seen_at_mc_range_example'),
                    ('last_seen_days', 'last_seen_days_example'),
                    ('first_seen_days', 'first_seen_days_example'),
                    ('first_seen_at_source_days', 'first_seen_at_source_days_example'),
                    ('first_seen_at_mc_days', 'first_seen_at_mc_days_example'),
                    ('include_relevant_links', False),
                    ('inventory_count_range', 'inventory_count_range_example'),
                    ('exclude_dealer_ids', 'exclude_dealer_ids_example'),
                    ('exclude_sources', 'exclude_sources_example'),
                    ('exclude_dealer_listings', True),
                    ('in_transit', 'in_transit_example'),
                    ('seating_capacity', 'seating_capacity_example'),
                    ('engine_size_range', 'engine_size_range_example'),
                    ('min_photo_links', 'min_photo_links_example'),
                    ('min_photo_links_cached', 'min_photo_links_cached_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/car/fsbo/active',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_car_recents_get(client):
    """Test case for search_car_recents_get

    Gets Recent car listings for the given search criteria
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('zip', 'zip_example'),
                    ('include_lease', True),
                    ('include_finance', True),
                    ('lease_term', 'lease_term_example'),
                    ('lease_down_payment', 'lease_down_payment_example'),
                    ('lease_emp', 'lease_emp_example'),
                    ('finance_loan_term', 'finance_loan_term_example'),
                    ('finance_loan_apr', 'finance_loan_apr_example'),
                    ('finance_emp', 'finance_emp_example'),
                    ('finance_down_payment', 'finance_down_payment_example'),
                    ('finance_down_payment_per', 'finance_down_payment_per_example'),
                    ('car_type', 'car_type_example'),
                    ('carfax_1_owner', 'carfax_1_owner_example'),
                    ('carfax_clean_title', 'carfax_clean_title_example'),
                    ('year_range', 'year_range_example'),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('dealer_id', 'dealer_id_example'),
                    ('vin', 'vin_example'),
                    ('source', 'source_example'),
                    ('body_type', 'body_type_example'),
                    ('body_subtype', 'body_subtype_example'),
                    ('vehicle_type', 'vehicle_type_example'),
                    ('vins', 'vins_example'),
                    ('taxonomy_vins', 'taxonomy_vins_example'),
                    ('ymmt', 'ymmt_example'),
                    ('match', 'match_example'),
                    ('cylinders', 'cylinders_example'),
                    ('transmission', 'transmission_example'),
                    ('doors', 'doors_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('exterior_color', 'exterior_color_example'),
                    ('interior_color', 'interior_color_example'),
                    ('base_exterior_color', 'base_exterior_color_example'),
                    ('base_interior_color', 'base_interior_color_example'),
                    ('engine', 'engine_example'),
                    ('engine_size', 'engine_size_example'),
                    ('engine_aspiration', 'engine_aspiration_example'),
                    ('engine_block', 'engine_block_example'),
                    ('highway_mpg_range', 'highway_mpg_range_example'),
                    ('city_mpg_range', 'city_mpg_range_example'),
                    ('miles_range', 'miles_range_example'),
                    ('price_range', 'price_range_example'),
                    ('msrp_range', 'msrp_range_example'),
                    ('dom_range', 'dom_range_example'),
                    ('last_seen_range', 'last_seen_range_example'),
                    ('first_seen_range', 'first_seen_range_example'),
                    ('first_seen_at_source_range', 'first_seen_at_source_range_example'),
                    ('first_seen_at_mc_range', 'first_seen_at_mc_range_example'),
                    ('last_seen_days', 'last_seen_days_example'),
                    ('first_seen_days', 'first_seen_days_example'),
                    ('first_seen_at_source_days', 'first_seen_at_source_days_example'),
                    ('first_seen_at_mc_days', 'first_seen_at_mc_days_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('rows', 10),
                    ('start', 0),
                    ('include_non_vin_listings', False),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example'),
                    ('facet_sort', count),
                    ('stats', 'stats_example'),
                    ('country', US),
                    ('plot', True),
                    ('nodedup', True),
                    ('dedup', True),
                    ('owned', True),
                    ('state', 'state_example'),
                    ('city', 'city_example'),
                    ('msa_code', 'msa_code_example'),
                    ('dealer_name', 'dealer_name_example'),
                    ('dealership_group_name', 'dealership_group_name_example'),
                    ('trim_o', 'trim_o_example'),
                    ('trim_r', 'trim_r_example'),
                    ('dom_active_range', 'dom_active_range_example'),
                    ('dom_180_range', 'dom_180_range_example'),
                    ('exclude_certified', True),
                    ('fuel_type', 'fuel_type_example'),
                    ('dealer_type', 'dealer_type_example'),
                    ('photo_links', True),
                    ('photo_links_cached', True),
                    ('stock_no', 'stock_no_example'),
                    ('sold', True),
                    ('include_relevant_links', False),
                    ('expired', 'expired_example'),
                    ('exclude_dealer_ids', 'exclude_dealer_ids_example'),
                    ('exclude_sources', 'exclude_sources_example'),
                    ('in_transit', 'in_transit_example'),
                    ('seating_capacity', 'seating_capacity_example'),
                    ('active_inventory_date_range', 'active_inventory_date_range_example'),
                    ('engine_size_range', 'engine_size_range_example'),
                    ('price_change_range', 'price_change_range_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/car/recents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_car_uk_recents_get(client):
    """Test case for search_car_uk_recents_get

    Gets Recent UK car listings for the given search criteria
    """
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('zip', 'zip_example'),
                    ('include_lease', True),
                    ('include_finance', True),
                    ('lease_term', 'lease_term_example'),
                    ('lease_down_payment', 'lease_down_payment_example'),
                    ('lease_emp', 'lease_emp_example'),
                    ('finance_loan_term', 'finance_loan_term_example'),
                    ('finance_loan_apr', 'finance_loan_apr_example'),
                    ('finance_emp', 'finance_emp_example'),
                    ('finance_down_payment', 'finance_down_payment_example'),
                    ('finance_down_payment_per', 'finance_down_payment_per_example'),
                    ('car_type', 'car_type_example'),
                    ('carfax_1_owner', 'carfax_1_owner_example'),
                    ('carfax_clean_title', 'carfax_clean_title_example'),
                    ('year_range', 'year_range_example'),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('dealer_id', 'dealer_id_example'),
                    ('source', 'source_example'),
                    ('body_type', 'body_type_example'),
                    ('body_subtype', 'body_subtype_example'),
                    ('vehicle_type', 'vehicle_type_example'),
                    ('ymmt', 'ymmt_example'),
                    ('match', 'match_example'),
                    ('cylinders', 'cylinders_example'),
                    ('transmission', 'transmission_example'),
                    ('doors', 'doors_example'),
                    ('drivetrain', 'drivetrain_example'),
                    ('exterior_color', 'exterior_color_example'),
                    ('interior_color', 'interior_color_example'),
                    ('base_exterior_color', 'base_exterior_color_example'),
                    ('base_interior_color', 'base_interior_color_example'),
                    ('engine', 'engine_example'),
                    ('engine_size', 'engine_size_example'),
                    ('engine_aspiration', 'engine_aspiration_example'),
                    ('engine_block', 'engine_block_example'),
                    ('highway_mpg_range', 'highway_mpg_range_example'),
                    ('city_mpg_range', 'city_mpg_range_example'),
                    ('combined_mpg_range', 'combined_mpg_range_example'),
                    ('miles_range', 'miles_range_example'),
                    ('price_range', 'price_range_example'),
                    ('msrp_range', 'msrp_range_example'),
                    ('dom_range', 'dom_range_example'),
                    ('last_seen_range', 'last_seen_range_example'),
                    ('first_seen_range', 'first_seen_range_example'),
                    ('first_seen_at_source_range', 'first_seen_at_source_range_example'),
                    ('first_seen_at_mc_range', 'first_seen_at_mc_range_example'),
                    ('last_seen_days', 'last_seen_days_example'),
                    ('first_seen_days', 'first_seen_days_example'),
                    ('first_seen_at_source_days', 'first_seen_at_source_days_example'),
                    ('first_seen_at_mc_days', 'first_seen_at_mc_days_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('rows', 10),
                    ('start', 0),
                    ('include_non_vin_listings', False),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example'),
                    ('facet_sort', count),
                    ('stats', 'stats_example'),
                    ('country', uk),
                    ('plot', True),
                    ('nodedup', True),
                    ('dedup', True),
                    ('owned', True),
                    ('state', 'state_example'),
                    ('city', 'city_example'),
                    ('msa_code', 'msa_code_example'),
                    ('dealer_name', 'dealer_name_example'),
                    ('dealership_group_name', 'dealership_group_name_example'),
                    ('trim_o', 'trim_o_example'),
                    ('trim_r', 'trim_r_example'),
                    ('dom_active_range', 'dom_active_range_example'),
                    ('dom_180_range', 'dom_180_range_example'),
                    ('exclude_certified', True),
                    ('fuel_type', 'fuel_type_example'),
                    ('dealer_type', 'dealer_type_example'),
                    ('photo_links', True),
                    ('photo_links_cached', True),
                    ('stock_no', 'stock_no_example'),
                    ('sold', True),
                    ('include_relevant_links', False),
                    ('expired', 'expired_example'),
                    ('exclude_dealer_ids', 'exclude_dealer_ids_example'),
                    ('exclude_sources', 'exclude_sources_example'),
                    ('in_transit', 'in_transit_example'),
                    ('seating_capacity', 'seating_capacity_example'),
                    ('insurance_group', 'insurance_group_example'),
                    ('vrm', 'vrm_example'),
                    ('num_owners', 'num_owners_example'),
                    ('variant', 'variant_example'),
                    ('postal_code', 'postal_code_example'),
                    ('write_off_category', 'write_off_category_example'),
                    ('fca_status', 'fca_status_example'),
                    ('active_inventory_date_range', 'active_inventory_date_range_example'),
                    ('engine_size_range', 'engine_size_range_example'),
                    ('price_change_range', 'price_change_range_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/car/uk/recents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

