# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.presidential_by_candidate_page import PresidentialByCandidatePage
from openapi_server.models.presidential_by_size_page import PresidentialBySizePage
from openapi_server.models.presidential_by_state_page import PresidentialByStatePage
from openapi_server.models.presidential_coverage_page import PresidentialCoveragePage
from openapi_server.models.presidential_summary_page import PresidentialSummaryPage


pytestmark = pytest.mark.asyncio

async def test_presidential_contributions_by_candidate_get(client):
    """Test case for presidential_contributions_by_candidate_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('election_year', [56]),
                    ('contributor_state', ['contributor_state_example']),
                    ('sort', '-net_receipts')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/presidential/contributions/by_candidate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_presidential_contributions_by_size_get(client):
    """Test case for presidential_contributions_by_size_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('size', [56]),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('election_year', [56]),
                    ('sort', 'size')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/presidential/contributions/by_size/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_presidential_contributions_by_state_get(client):
    """Test case for presidential_contributions_by_state_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('election_year', [56]),
                    ('sort', '-contribution_receipt_amount')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/presidential/contributions/by_state/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_presidential_coverage_end_date_get(client):
    """Test case for presidential_coverage_end_date_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('election_year', [56]),
                    ('sort', 'candidate_id')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/presidential/coverage_end_date/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_presidential_financial_summary_get(client):
    """Test case for presidential_financial_summary_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('election_year', [56]),
                    ('sort', '-net_receipts')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/presidential/financial_summary/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

