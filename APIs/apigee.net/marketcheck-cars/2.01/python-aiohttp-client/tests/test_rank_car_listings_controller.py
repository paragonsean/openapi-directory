# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.car_rank_request import CarRankRequest
from openapi_server.models.car_rank_response import CarRankResponse
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_rank_car(client):
    """Test case for rank_car

    Compute relative rank for car listings.
    """
    body = {"listing_ids":["listing_ids","listing_ids"],"ranking_criteria":[{"carfax_1_owner":0.8008281904610115,"dom":1.4658129805029452,"is_certified":2.3021358869347655,"price":9.301444243932576,"dom_active":5.637376656633329,"dom_180":5.962133916683182,"carfax_clean_title":6.027456183070403,"miles":7.061401241503109},{"carfax_1_owner":0.8008281904610115,"dom":1.4658129805029452,"is_certified":2.3021358869347655,"price":9.301444243932576,"dom_active":5.637376656633329,"dom_180":5.962133916683182,"carfax_clean_title":6.027456183070403,"miles":7.061401241503109}]}
    params = [('api_key', 'api_key_example'),
                    ('append_api_key', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/search/car/active/rank/listings',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_and_rank_car(client):
    """Test case for search_and_rank_car

    Compute relative rank for car listings.
    """
    body = {"listing_ids":["listing_ids","listing_ids"],"ranking_criteria":[{"carfax_1_owner":0.8008281904610115,"dom":1.4658129805029452,"is_certified":2.3021358869347655,"price":9.301444243932576,"dom_active":5.637376656633329,"dom_180":5.962133916683182,"carfax_clean_title":6.027456183070403,"miles":7.061401241503109},{"carfax_1_owner":0.8008281904610115,"dom":1.4658129805029452,"is_certified":2.3021358869347655,"price":9.301444243932576,"dom_active":5.637376656633329,"dom_180":5.962133916683182,"carfax_clean_title":6.027456183070403,"miles":7.061401241503109}]}
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
                    ('miles_range', '1-'),
                    ('price_range', '1-'),
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
                    ('inventory_type', 'inventory_type_example'),
                    ('page', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/search/car/active/rank',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

