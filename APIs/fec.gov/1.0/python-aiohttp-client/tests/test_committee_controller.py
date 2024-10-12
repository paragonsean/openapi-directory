# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.committee_detail_page import CommitteeDetailPage
from openapi_server.models.committee_history_profile_page import CommitteeHistoryProfilePage
from openapi_server.models.committee_page import CommitteePage


pytestmark = pytest.mark.asyncio

async def test_candidate_candidate_id_committees_get(client):
    """Test case for candidate_candidate_id_committees_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('committee_type', ['committee_type_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('year', [56]),
                    ('sort_nulls_last', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('filing_frequency', ['filing_frequency_example']),
                    ('organization_type', ['organization_type_example']),
                    ('designation', ['designation_example']),
                    ('sort', 'name')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidate/{candidate_id}/committees'.format(candidate_id='candidate_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_candidate_candidate_id_committees_history_cycle_get(client):
    """Test case for candidate_candidate_id_committees_history_cycle_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('designation', ['designation_example']),
                    ('sort', '-cycle')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidate/{candidate_id}/committees/history/{cycle}'.format(cycle=56, candidate_id='candidate_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_candidate_candidate_id_committees_history_get(client):
    """Test case for candidate_candidate_id_committees_history_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('designation', ['designation_example']),
                    ('sort', '-cycle')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/candidate/{candidate_id}/committees/history'.format(candidate_id='candidate_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_committee_committee_id_get(client):
    """Test case for committee_committee_id_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('committee_type', ['committee_type_example']),
                    ('cycle', [56]),
                    ('sort_null_only', False),
                    ('page', 1),
                    ('year', [56]),
                    ('sort_nulls_last', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('filing_frequency', ['filing_frequency_example']),
                    ('organization_type', ['organization_type_example']),
                    ('designation', ['designation_example']),
                    ('sort', 'name')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/committee/{committee_id}'.format(committee_id='committee_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_committee_committee_id_history_cycle_get(client):
    """Test case for committee_committee_id_history_cycle_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('designation', ['designation_example']),
                    ('sort', '-cycle')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/committee/{committee_id}/history/{cycle}'.format(committee_id='committee_id_example', cycle=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_committee_committee_id_history_get(client):
    """Test case for committee_committee_id_history_get

    
    """
    params = [('api_key', 'DEMO_KEY'),
                    ('election_full', True),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('per_page', 20),
                    ('designation', ['designation_example']),
                    ('sort', '-cycle')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/committee/{committee_id}/history'.format(committee_id='committee_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_committees_get(client):
    """Test case for committees_get

    
    """
    params = [('treasurer_name', ['treasurer_name_example']),
                    ('q', ['q_example']),
                    ('min_first_file_date', '2013-10-20'),
                    ('cycle', [56]),
                    ('sponsor_candidate_id', ['sponsor_candidate_id_example']),
                    ('sort_null_only', False),
                    ('sort_hide_null', False),
                    ('candidate_id', ['candidate_id_example']),
                    ('per_page', 20),
                    ('filing_frequency', ['filing_frequency_example']),
                    ('sort', 'name'),
                    ('max_first_file_date', '2013-10-20'),
                    ('min_first_f1_date', '2013-10-20'),
                    ('api_key', 'DEMO_KEY'),
                    ('min_last_f1_date', '2013-10-20'),
                    ('committee_type', ['committee_type_example']),
                    ('party', ['party_example']),
                    ('sort_nulls_last', False),
                    ('page', 1),
                    ('year', [56]),
                    ('committee_id', ['committee_id_example']),
                    ('state', ['state_example']),
                    ('max_last_f1_date', '2013-10-20'),
                    ('max_first_f1_date', '2013-10-20'),
                    ('designation', ['designation_example']),
                    ('organization_type', ['organization_type_example'])]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyHeaderAuth': 'special-key',
        'ApiKeyQueryAuth': 'special-key',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/committees/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

