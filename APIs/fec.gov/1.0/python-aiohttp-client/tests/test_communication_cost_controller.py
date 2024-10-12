# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cc_totals_by_candidate_page import CCTotalsByCandidatePage
from openapi_server.models.communication_cost_by_candidate_page import CommunicationCostByCandidatePage
from openapi_server.models.communication_cost_page import CommunicationCostPage


pytestmark = pytest.mark.asyncio

async def test_communication_costs_aggregates_get(client):
    """Test case for communication_costs_aggregates_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('support_oppose_indicator', 'support_oppose_indicator_example'),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('sort_nulls_last', False),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/communication_costs/aggregates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_communication_costs_by_candidate_get(client):
    """Test case for communication_costs_by_candidate_get

    
    """
    params = [('district', 'district_example'),
                    ('api_key', 'DEMO_KEY'),
                    ('support_oppose', 'support_oppose_example'),
                    ('election_full', True),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('state', 'state_example'),
                    ('sort_nulls_last', False),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('office', 'office_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/communication_costs/by_candidate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_communication_costs_get(client):
    """Test case for communication_costs_get

    
    """
    params = [('min_date', '2013-10-20'),
                    ('support_oppose_indicator', ['support_oppose_indicator_example']),
                    ('max_image_number', 'max_image_number_example'),
                    ('min_image_number', 'min_image_number_example'),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('min_amount', 'min_amount_example'),
                    ('per_page', 20),
                    ('candidate_id', ['candidate_id_example']),
                    ('line_number', 'line_number_example'),
                    ('sort', 'sort_example'),
                    ('api_key', 'DEMO_KEY'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('image_number', ['image_number_example']),
                    ('max_date', '2013-10-20'),
                    ('max_amount', 'max_amount_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/communication_costs/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_communication_costs_totals_by_candidate_get(client):
    """Test case for communication_costs_totals_by_candidate_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('cycle', [56]),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/communication_costs/totals/by_candidate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

