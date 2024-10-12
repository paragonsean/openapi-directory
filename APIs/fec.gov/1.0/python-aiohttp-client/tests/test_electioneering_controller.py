# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ec_totals_by_candidate_page import ECTotalsByCandidatePage
from openapi_server.models.electioneering_by_candidate_page import ElectioneeringByCandidatePage
from openapi_server.models.electioneering_page import ElectioneeringPage


pytestmark = pytest.mark.asyncio

async def test_electioneering_aggregates_get(client):
    """Test case for electioneering_aggregates_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('cycle', [56]),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
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
        path='/v1/electioneering/aggregates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_electioneering_by_candidate_get(client):
    """Test case for electioneering_by_candidate_get

    
    """
    params = [('district', 'district_example'),
                    ('api_key', 'DEMO_KEY'),
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
        path='/v1/electioneering/by_candidate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_electioneering_get(client):
    """Test case for electioneering_get

    
    """
    params = [('min_date', '2013-10-20'),
                    ('api_key', 'DEMO_KEY'),
                    ('description', 'description_example'),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('committee_id', ['committee_id_example']),
                    ('report_year', [56]),
                    ('last_index', 56),
                    ('sort_nulls_last', False),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('min_amount', 'min_amount_example'),
                    ('max_date', '2013-10-20'),
                    ('max_amount', 'max_amount_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/electioneering/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_electioneering_totals_by_candidate_get(client):
    """Test case for electioneering_totals_by_candidate_get

    
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
        path='/v1/electioneering/totals/by_candidate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

