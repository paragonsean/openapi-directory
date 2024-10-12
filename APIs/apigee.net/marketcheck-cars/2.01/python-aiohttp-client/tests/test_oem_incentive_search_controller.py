# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.search_response import SearchResponse


pytestmark = pytest.mark.asyncio

async def test_oem_search(client):
    """Test case for oem_search

    Gets oem incentive listings for the given search criteria
    """
    params = [('api_key', 'api_key_example'),
                    ('offer_type', 'offer_type_example'),
                    ('year', 'year_example'),
                    ('make', 'make_example'),
                    ('model', 'model_example'),
                    ('trim', 'trim_example'),
                    ('msrp', 'msrp_example'),
                    ('apr', 'apr_example'),
                    ('monthly', 'monthly_example'),
                    ('monthly_per_thousand', 'monthly_per_thousand_example'),
                    ('down_payment', 'down_payment_example'),
                    ('due_at_signing', 'due_at_signing_example'),
                    ('security_deposit', 'security_deposit_example'),
                    ('disposition_fee', 'disposition_fee_example'),
                    ('acquisition_fee', 'acquisition_fee_example'),
                    ('duration', 'duration_example'),
                    ('dealer_contribution', 'dealer_contribution_example'),
                    ('mileage_charge', 'mileage_charge_example'),
                    ('mileage_charge_limit', 'mileage_charge_limit_example'),
                    ('cashback_amount', 'cashback_amount_example'),
                    ('cashback_target_group', 'cashback_target_group_example'),
                    ('lease_end_purchase_option', 'lease_end_purchase_option_example'),
                    ('net_capitalised_cost', 'net_capitalised_cost_example'),
                    ('gross_capitalised_cost', 'gross_capitalised_cost_example'),
                    ('total_monthly_payment', 'total_monthly_payment_example'),
                    ('zip', 'zip_example'),
                    ('city', 'city_example'),
                    ('state', 'state_example'),
                    ('country', US),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 56),
                    ('search_text', 'search_text_example'),
                    ('last_seen_range', 'last_seen_range_example'),
                    ('first_seen_range', 'first_seen_range_example'),
                    ('sort_by', 'sort_by_example'),
                    ('sort_order', 'sort_order_example'),
                    ('rows', 10),
                    ('start', 0),
                    ('facets', 'facets_example'),
                    ('range_facets', 'range_facets_example'),
                    ('facet_sort', count),
                    ('stats', 'stats_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/search/car/incentive/oem',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

