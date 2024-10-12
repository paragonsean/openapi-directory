# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.candidate_detail_page import CandidateDetailPage
from openapi_server.models.candidate_history_page import CandidateHistoryPage
from openapi_server.models.candidate_history_total_page import CandidateHistoryTotalPage
from openapi_server.models.candidate_page import CandidatePage
from openapi_server.models.candidate_total_aggregate_page import CandidateTotalAggregatePage
from openapi_server.models.committee_totals_page import CommitteeTotalsPage
from openapi_server.models.total_by_office_by_party_page import TotalByOfficeByPartyPage
from openapi_server.models.total_by_office_page import TotalByOfficePage


pytestmark = pytest.mark.asyncio

async def test_candidate_candidate_id_get(client):
    """Test case for candidate_candidate_id_get

    
    """
    params = [('incumbent_challenge', ['incumbent_challenge_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('federal_funds_flag', True),
                    ('sort_hide_null', False),
                    ('name', ['name_example']),
                    ('per_page', 20),
                    ('election_year', [56]),
                    ('office', ['office_example']),
                    ('sort', 'name'),
                    ('candidate_status', ['candidate_status_example']),
                    ('district', ['district_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('has_raised_funds', True),
                    ('party', ['party_example']),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('state', ['state_example']),
                    ('year', 'year_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidate/{candidate_id}'.format(candidate_id='candidate_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_candidate_candidate_id_history_cycle_get(client):
    """Test case for candidate_candidate_id_history_cycle_get

    
    """
    params = [('page', 1),
                    ('api_key', 'DEMO_KEY'),
                    ('sort_hide_null', False),
                    ('election_full', True),
                    ('per_page', 20),
                    ('sort_null_only', False),
                    ('sort', '-two_year_period'),
                    ('sort_nulls_last', False)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidate/{candidate_id}/history/{cycle}'.format(cycle=56, candidate_id='candidate_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_candidate_candidate_id_history_get(client):
    """Test case for candidate_candidate_id_history_get

    
    """
    params = [('page', 1),
                    ('api_key', 'DEMO_KEY'),
                    ('sort_hide_null', False),
                    ('election_full', True),
                    ('per_page', 20),
                    ('sort_null_only', False),
                    ('sort', '-two_year_period'),
                    ('sort_nulls_last', False)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidate/{candidate_id}/history'.format(candidate_id='candidate_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_candidate_candidate_id_totals_get(client):
    """Test case for candidate_candidate_id_totals_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('cycle', [56]),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('sort', '-cycle')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidate/{candidate_id}/totals'.format(candidate_id='candidate_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_candidates_get(client):
    """Test case for candidates_get

    
    """
    params = [('incumbent_challenge', ['incumbent_challenge_example']),
                    ('min_first_file_date', '2013-10-20'),
                    ('q', ['q_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('federal_funds_flag', True),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('name', ['name_example']),
                    ('per_page', 20),
                    ('election_year', [56]),
                    ('office', ['office_example']),
                    ('sort', 'name'),
                    ('candidate_status', ['candidate_status_example']),
                    ('max_first_file_date', '2013-10-20'),
                    ('district', ['district_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('has_raised_funds', True),
                    ('party', ['party_example']),
                    ('sort_nulls_last', False),
                    ('is_active_candidate', True),
                    ('page', 1),
                    ('state', ['state_example']),
                    ('year', 'year_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_candidates_search_get(client):
    """Test case for candidates_search_get

    
    """
    params = [('incumbent_challenge', ['incumbent_challenge_example']),
                    ('min_first_file_date', '2013-10-20'),
                    ('q', ['q_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('federal_funds_flag', True),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('name', ['name_example']),
                    ('per_page', 20),
                    ('election_year', [56]),
                    ('office', ['office_example']),
                    ('sort', 'name'),
                    ('candidate_status', ['candidate_status_example']),
                    ('max_first_file_date', '2013-10-20'),
                    ('district', ['district_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('has_raised_funds', True),
                    ('party', ['party_example']),
                    ('sort_nulls_last', False),
                    ('is_active_candidate', True),
                    ('page', 1),
                    ('state', ['state_example']),
                    ('year', 'year_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidates/search/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_candidates_totals_aggregates_get(client):
    """Test case for candidates_totals_aggregates_get

    
    """
    params = [('max_election_cycle', 56),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('election_year', [56]),
                    ('office', 'office_example'),
                    ('sort', ["-election_year"]),
                    ('min_election_cycle', 56),
                    ('district', ['district_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('party', 'party_example'),
                    ('is_active_candidate', True),
                    ('page', 1),
                    ('state', ['state_example']),
                    ('sort_nulls_last', False),
                    ('aggregate_by', 'aggregate_by_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidates/totals/aggregates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_candidates_totals_by_office_by_party_get(client):
    """Test case for candidates_totals_by_office_by_party_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('is_active_candidate', True),
                    ('sort_nulls_last', False),
                    ('election_year', [56]),
                    ('sort_hide_null', False),
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
        path='/v1/candidates/totals/by_office/by_party/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_candidates_totals_by_office_get(client):
    """Test case for candidates_totals_by_office_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('max_election_cycle', 56),
                    ('election_full', True),
                    ('is_active_candidate', True),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_nulls_last', False),
                    ('election_year', [56]),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('office', 'office_example'),
                    ('sort', 'sort_example'),
                    ('min_election_cycle', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidates/totals/by_office/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_candidates_totals_get(client):
    """Test case for candidates_totals_get

    
    """
    params = [('max_disbursements', 'max_disbursements_example'),
                    ('q', ['q_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('max_cash_on_hand_end_period', 'max_cash_on_hand_end_period_example'),
                    ('max_debts_owed_by_committee', 'max_debts_owed_by_committee_example'),
                    ('min_disbursements', 'min_disbursements_example'),
                    ('federal_funds_flag', True),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('election_year', [56]),
                    ('office', ['office_example']),
                    ('sort', 'sort_example'),
                    ('district', ['district_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('min_debts_owed_by_committee', 'min_debts_owed_by_committee_example'),
                    ('max_receipts', 'max_receipts_example'),
                    ('has_raised_funds', True),
                    ('party', ['party_example']),
                    ('sort_nulls_last', False),
                    ('is_active_candidate', True),
                    ('page', 1),
                    ('state', ['state_example']),
                    ('min_cash_on_hand_end_period', 'min_cash_on_hand_end_period_example'),
                    ('min_receipts', 'min_receipts_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidates/totals/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_committee_committee_id_candidates_get(client):
    """Test case for committee_committee_id_candidates_get

    
    """
    params = [('incumbent_challenge', ['incumbent_challenge_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('federal_funds_flag', True),
                    ('sort_hide_null', False),
                    ('name', ['name_example']),
                    ('per_page', 20),
                    ('election_year', [56]),
                    ('office', ['office_example']),
                    ('sort', 'name'),
                    ('candidate_status', ['candidate_status_example']),
                    ('district', ['district_example']),
                    ('api_key', 'DEMO_KEY'),
                    ('has_raised_funds', True),
                    ('party', ['party_example']),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('state', ['state_example']),
                    ('year', 'year_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/committee/{committee_id}/candidates'.format(committee_id='committee_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_committee_committee_id_candidates_history_cycle_get(client):
    """Test case for committee_committee_id_candidates_history_cycle_get

    
    """
    params = [('page', 1),
                    ('api_key', 'DEMO_KEY'),
                    ('sort_hide_null', False),
                    ('election_full', True),
                    ('per_page', 20),
                    ('sort_null_only', False),
                    ('sort', '-two_year_period'),
                    ('sort_nulls_last', False)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/committee/{committee_id}/candidates/history/{cycle}'.format(committee_id='committee_id_example', cycle=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_committee_committee_id_candidates_history_get(client):
    """Test case for committee_committee_id_candidates_history_get

    
    """
    params = [('page', 1),
                    ('api_key', 'DEMO_KEY'),
                    ('sort_hide_null', False),
                    ('election_full', True),
                    ('per_page', 20),
                    ('sort_null_only', False),
                    ('sort', '-two_year_period'),
                    ('sort_nulls_last', False)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/committee/{committee_id}/candidates/history'.format(committee_id='committee_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

